import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui import Ui_Dialog  # Import your generated UI class
import google.generativeai as ai

# Configure the API
API_KEY = ''
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-2.0-flash-lite")
chat = model.start_chat()

class ChatBotDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the generated UI class
        self.ui.setupUi(self)  # Set up the UI in this dialog

        # Connect the button to the chatbot logic
        self.ui.pushButton.clicked.connect(self.send_message_to_chatbot)

    def send_message_to_chatbot(self):
        # Get the user input from the textEdit
        user_message = self.ui.textEdit.toPlainText()

        # Get the chatbot response
        response = chat.send_message(f'Tell me a very short story about {user_message}')
        # Display the response in the label
        self.ui.textBrowser.setPlainText(f'{response.text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ChatBotDialog()
    dialog.show()
    sys.exit(app.exec_())
