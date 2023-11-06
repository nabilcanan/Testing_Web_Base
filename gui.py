import sys
import threading
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from app import app  # This imports your Flask app


def run_flask():
    app.run()


if __name__ == '__main__':
    # Start Flask in a background thread
    threading.Thread(target=run_flask).start()

    # Start the PyQt application
    app_qt = QApplication(sys.argv)
    web = QWebEngineView()
    web.load(QUrl("http://127.0.0.1:5000"))  # Load the Flask server's address
    web.show()
    sys.exit(app_qt.exec_())
