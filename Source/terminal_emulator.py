from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TerminalEmulator(QWidget):
    def __init__(self):
        super(TerminalEmulator, self).__init__()

        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.start('cmd.exe')
        self.terminal = QTextEdit(self)
        self.terminal.setReadOnly(True)
        self.command_line = CommandLineEdit(self)
        self.command_line.returnPressed.connect(self.execute_command)

        layout = QVBoxLayout(self)
        layout.addWidget(self.terminal)
        layout.addWidget(self.command_line)

        self.process.readyRead.connect(self.update_terminal)
        self.process.finished.connect(self.process_finished)

        self.update_prompt()

    def execute_command(self):
        command = self.command_line.text()
        self.command_line.add_to_history(command)
        if command.strip() == 'cls':
            self.terminal.clear()
        else:
            self.terminal.append(command)
            self.process.write((command + '\n').encode())
        self.command_line.clear()

    def update_terminal(self):
        output = self.process.readAll().data().decode(errors='ignore')
        self.terminal.append(output)

    def process_finished(self):
        self.terminal.append("Process finished.")
        self.update_prompt()

    def update_prompt(self):
        self.command_line.setPlaceholderText('>')

class CommandLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(CommandLineEdit, self).__init__(*args, **kwargs)
        self.history = []
        self.history_index = 0

    def add_to_history(self, command):
        self.history.append(command)
        self.history_index = len(self.history)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up and self.history:
            self.history_index = max(0, self.history_index - 1)
            self.setText(self.history[self.history_index])
        elif event.key() == Qt.Key_Down and self.history:
            self.history_index = min(len(self.history) - 1, self.history_index + 1)
            self.setText(self.history[self.history_index])
        else:
            super(CommandLineEdit, self).keyPressEvent(event)
