from PySide6.QtCore import QThread, Signal
from controllers.send_worker import SendWorker
from apis.sms import SMS_PROVIDERS
from apis.call import CALL_PROVIDERS
import threading


class SenderThread(QThread):
    log = Signal(str)
    stat = Signal(object)

    def __init__(self, phone, delay, loop_delay, enable_sms, enable_call):
        super().__init__()
        self.phone = phone
        self.delay = delay
        self.loop_delay = loop_delay
        self.enable_sms = enable_sms
        self.enable_call = enable_call

        self.stop_event = threading.Event()

    def stop(self):
        # ✅ ONLY signal stop
        self.stop_event.set()
        self.log.emit("🛑 Stop requested")

    def run(self):
        apis = []

        if self.enable_sms:
            apis.extend(SMS_PROVIDERS)
        if self.enable_call:
            apis.extend(CALL_PROVIDERS)

        if not apis:
            self.log.emit("⚠ No APIs enabled")
            return

        loop_count = 0

        while not self.stop_event.is_set():
            loop_count += 1
            self.log.emit(f"🔁 Loop {loop_count} started")

            active_workers = []

            for api in apis:
                if self.stop_event.is_set():
                    break
                
                api_instance = api()

                worker = SendWorker(api_instance, self.phone, self.stop_event)

                # ⚠️ IMPORTANT: queued connections only
                worker.signals.log.connect(self.log)
                worker.signals.result.connect(self.stat)

                # Use Python thread with daemon=True
                t = threading.Thread(target=worker.run, daemon=True)
                t.start()
                active_workers.append(t)

                # interruptible delay
                self.stop_event.wait(self.delay)

            # ✅ WAIT for workers with timeout
            for t in active_workers:
                t.join(timeout=30.0)  # 5-second timeout per worker
                if t.is_alive():
                    self.log.emit("⚠️ Worker join timed out—will be killed as daemon on exit")

            if self.stop_event.is_set():
                break

            self.log.emit(f"⏳ Loop Delay {self.loop_delay}")
            self.stop_event.wait(self.loop_delay)

        self.log.emit("✅ Sender thread exited cleanly")