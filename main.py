import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_window import Ui_SmsBomberMainWindow
from controllers.app_controller import AppController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SmsBomberMainWindow()
        self.ui.setupUi(self)
        self.controller = AppController(self.ui)

    # Add this method to handle window close
    def closeEvent(self, event):
        self.controller.stop()  # Stop threads safely
        super().closeEvent(event)  # Proceed with close

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())