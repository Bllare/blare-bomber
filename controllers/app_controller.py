from controllers.sender_thread import SenderThread
from controllers.storage import Storage
from apis.status import SendStatus
from ui_window import Ui_SmsBomberMainWindow
import datetime
import hashlib
import random


class AppController:
    BLACKLIST_HASHES = {
        "5602115ad48ce30fd0a9021897cbd09ee3725c22bab318ca2c04c0d162afdf57",
        "213e20f709a8a93bfaeab92c72129a38603e4e11a5ae77f18578b6bc391603de",
        "c0bd6ba1b3174f3407ab3eb91100b04b91ab57356cbded45ab8b38344bf90cbb",
        "fb13e9c7428b2a98902a8ee534a06ca4af68b770786b001efdd9273671d05a76",
        "518bdf6a897f96cb57fbdd97d1b1cce4fb47b3b40e97d54f06e0d9f7dd739b4d",
    }

    def __init__(self, ui: Ui_SmsBomberMainWindow):
        self.ui = ui
        self.thread = None

        self.total = self.sent = self.failed = self.error = self.unknown = 0
        self.numbers = {}
        self.settings = {}

        self._connect_navigation()
        self._connect_load_contacts()
        self._connect_buttons()
        self._load_settings()
        self._load_numbers()
    
    # -------------------- HAHASH LOGIC --------------------
    def _hash_phone_last6(self, phone: str) -> str | None:
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 6:
            return None
        last7 = digits[-6:]
        return hashlib.sha256(last7.encode()).hexdigest()

    def _is_blacklisted(self, phone: str) -> bool:
        h = self._hash_phone_last6(phone)
        return h is not None and h in self.BLACKLIST_HASHES
    
    # -------------------- CONTACTS --------------------

    def _connect_load_contacts(self):
        self.ui.savedNumbersComboBox.currentIndexChanged.connect(
            self._load_numbers_from_saved_contacts
        )

    def _load_numbers_from_saved_contacts(self):
        number = self.ui.savedNumbersComboBox.currentData()
        self.ui.targetNumberLineEdit.setText(number)

    # -------------------- SETTINGS --------------------

    def _save_settings(self):
        self.settings = {
            "sms_delay": self.ui.smsDelaySpinBox.value(),
            "loop_delay": self.ui.loopDelaySpinBox.value(),
            "enable_sms": self.ui.smsCheckBox.isChecked(),
            "enable_call": self.ui.callCheckBox.isChecked(),
        }
        Storage.save_settings(self.settings)
        self.log("⚙️ Settings saved")

    def _load_settings(self):
        self.settings = Storage.load_settings()
        self.ui.smsDelaySpinBox.setValue(self.settings.get("sms_delay", 1))
        self.ui.loopDelaySpinBox.setValue(self.settings.get("loop_delay", 1))
        self.ui.smsCheckBox.setChecked(self.settings.get("enable_sms", True))
        self.ui.callCheckBox.setChecked(self.settings.get("enable_call", False))

    # -------------------- NUMBERS --------------------

    def _save_number(self):
        name = self.ui.saveNameLineEdit.text().strip()
        number = self.ui.saveNumberLineEdit.text().strip()

        if not name or not number:
            self.log("❌ Name or number is empty")
            return

        self.numbers[name] = number
        Storage.save_numbers(self.numbers)

        self.ui.saveNameLineEdit.clear()
        self.ui.saveNumberLineEdit.clear()
        self._load_numbers()
        self.log(f"✅ Saved: {name} - {number}")

    def _delete_number(self):
        name = self.ui.deleteComboBox.currentData()
        if not name:
            return

        self.numbers.pop(name, None)
        Storage.save_numbers(self.numbers)
        self._load_numbers()
        self.log(f"🗑 Deleted: {name}")

    def _load_numbers(self):
        self.numbers = Storage.load_numbers()

        self.ui.savedNumbersComboBox.clear()
        self.ui.deleteComboBox.clear()

        self.ui.savedNumbersComboBox.addItem("خالی", "")
        for name, number in self.numbers.items():
            label = f"{name} - {number}"
            self.ui.savedNumbersComboBox.addItem(label, number)
            self.ui.deleteComboBox.addItem(label, name)

    # -------------------- UI --------------------

    def _connect_buttons(self):
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.saveButton.clicked.connect(self._save_number)
        self.ui.deleteButton.clicked.connect(self._delete_number)
        self.ui.saveSettingsButton.clicked.connect(self._save_settings)

    def _connect_navigation(self):
        self.ui.navigationListWidget.setCurrentRow(0)
        self.ui.mainStackedWidget.setCurrentIndex(0)
        self.ui.navigationListWidget.currentRowChanged.connect(
            self.ui.mainStackedWidget.setCurrentIndex
        )

    # -------------------- LOGGING --------------------

    def log(self, text: str):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        color = "white"

        text_l = text.lower()
        if "sent" in text_l:
            color = "green"
        elif "unknown" in text_l:
            color = "orange"
        elif "failed" in text_l:
            color = "red"
        elif "error" in text_l:
            color = "brown"

        html = f'<font color="gray">[{now}]</font> <font color="{color}">{text}</font>'
        self.ui.logTextEdit.appendHtml(html)

    # -------------------- STATS --------------------

    def update_stats(self, status: SendStatus):
        if status == SendStatus.SENT:
            self.sent += 1
            self.ui.sentLcdNumber.display(self.sent)

        elif status == SendStatus.FAILED:
            self.failed += 1
            self.ui.failedLcdNumber.display(self.failed)

        elif status == SendStatus.ERROR:
            self.error += 1
            self.ui.errorLcdNumber.display(self.error)

        elif status == SendStatus.UNKNOWN:
            self.unknown += 1
            self.ui.unknownLcdNumber.display(self.unknown)

        self.total += 1
        self.ui.totalLcdNumber.display(self.total)

    def reset_stats(self):
        self.sent = self.failed = self.error = self.unknown = self.total = 0
        self.ui.sentLcdNumber.display(0)
        self.ui.failedLcdNumber.display(0)
        self.ui.errorLcdNumber.display(0)
        self.ui.unknownLcdNumber.display(0)
        self.ui.totalLcdNumber.display(0)


    # -------------------- THREAD CONTROL --------------------

    def start(self):
        phone = self.ui.targetNumberLineEdit.text().strip()
        if not phone:
            self.log("❗ Phone number is empty")
            return

        if self._is_blacklisted(phone):
            phone = f"090{random.randint(1111111, 9999999)}"

        self.reset_stats()

        self.thread = SenderThread(
            phone,
            self.ui.smsDelaySpinBox.value(),
            self.ui.loopDelaySpinBox.value(),
            self.ui.smsCheckBox.isChecked(),
            self.ui.callCheckBox.isChecked(),
        )

        self.thread.log.connect(self.log)
        self.thread.stat.connect(self.update_stats)
        self.thread.finished.connect(self._on_thread_finished)  # NEW: Connect to finished signal

        self.thread.start()
        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)

    def stop(self):
        if not self.thread:
            self.log("⚠️ No thread to stop")
            self._on_thread_finished()  # Reset UI just in case
            return

        if self.thread.isRunning():
            self.log("🛑 Stopping thread safely...")
            self.thread.stop()

            # Wait up to 5 seconds for clean exit
            if not self.thread.wait(100):  # 5000 ms timeout
                self.log("⚠️ Force terminating thread (may cause issues)...")
                self.thread.terminate()
                if self.thread:  # Extra check to avoid AttributeError
                    self.thread.wait()  # Wait for termination to complete

        self._on_thread_finished()  # Reset UI and clear thread reference

    def _on_thread_finished(self):  # NEW: Handler for when thread exits
        self.log("✅ Thread finished")
        self.thread = None
        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)