import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui import Ui_Dialog  # Import your UI class
import google.generativeai as ai

# PUT API KEY HERE!!
API_KEY = ''
ai.configure(api_key=API_KEY)


model = ai.GenerativeModel("gemini-2.0-flash-lite")
chat = model.start_chat()

class ChatBotDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  
        self.ui.setupUi(self)  

       
        self.ui.pushButton.clicked.connect(self.send_message_to_chatbot)

    def send_message_to_chatbot(self):
        
        user_message = self.ui.textEdit.toPlainText()
        response = chat.send_message(f'Tell me a very short story about {user_message}')
        self.ui.textBrowser.setPlainText(f'{response.text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ChatBotDialog()
    dialog.show()
    sys.exit(app.exec_())
