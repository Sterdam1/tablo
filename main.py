import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from ui_main import Ui_MainWindow

class VolleyTable(QMainWindow):
    def __init__(self):
        self.buffer = []
        self.final_score = [0,0]
        super(VolleyTable, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_team1.clicked.connect(self.button_team1_clicked)
        self.ui.btn_team2.clicked.connect(self.button_team2_clicked)
        self.ui.btn_reset.clicked.connect(self.button_reset)
        self.ui.btn_undo.clicked.connect(self.button_undo)

    def add_to_history(self):
        self.ui.comboBox.addItem('{0} - {1}'.format(self.ui.btn_team1.text(), self.ui.btn_team2.text()))
        self.buffer.clear()

    def checker(self):
        print(abs(int(self.ui.btn_team1.text()) - int(self.ui.btn_team2.text())))
        return abs(int(self.ui.btn_team1.text()) - int(self.ui.btn_team2.text()))     

    def button_team1_clicked(self):        
        if int(self.ui.btn_team1.text()) >= 25 and self.checker() >= 1 and self.ui.btn_team2.isEnabled() == False:
            self.add_to_history()
            if int(self.ui.btn_team1.text()) > 0:
                self.ui.btn_team1.setText('-1')
            self.ui.btn_team2.setText('0')
            self.ui.btn_team2.setEnabled(True)  
                
        if int(self.ui.btn_team1.text()) >= 24 and self.checker() >= 1:
            self.ui.btn_team1.setText(str(int(self.ui.btn_team1.text()) + 1))
            self.ui.btn_sets1.setText(str(int(self.ui.btn_sets1.text()) + 1))
            self.ui.btn_team2.setEnabled(False)   
        else:
            if self.ui.btn_team1.text() != '-1':
                self.buffer.append('team1')
            self.ui.btn_team1.setText(str(int(self.ui.btn_team1.text()) + 1))

    def button_team2_clicked(self):
        if int(self.ui.btn_team2.text()) >= 25 and self.checker() >= 1 and self.ui.btn_team1.isEnabled() == False:
            self.add_to_history()
            if int(self.ui.btn_team2.text()) > 0:
                self.ui.btn_team2.setText('-1')
            self.ui.btn_team1.setText('0')
            self.ui.btn_team1.setEnabled(True)

        if int(self.ui.btn_team2.text()) >= 24 and self.checker() >= 1:
            self.ui.btn_team2.setText(str(int(self.ui.btn_team2.text())+ 1))
            self.ui.btn_sets2.setText(str(int(self.ui.btn_sets2.text()) + 1))
            self.ui.btn_team1.setEnabled(False)   
        else:
            if self.ui.btn_team2.text() != '-1':
                self.buffer.append('team2')
            self.ui.btn_team2.setText(str(int(self.ui.btn_team2.text()) + 1))

    def button_undo(self):      
        if len(self.buffer) != 0:
            if self.buffer[len(self.buffer) - 1] == 'team1':
                self.ui.btn_team1.setText(str(int(self.ui.btn_team1.text()) - 1))
            if self.buffer[len(self.buffer) - 1] == 'team2':
                self.ui.btn_team2.setText(str(int(self.ui.btn_team2.text()) - 1))
            self.buffer.pop(len(self.buffer) - 1)

    def button_reset(self):
        self.ui.comboBox.clear()
        self.ui.btn_team1.setText('0')
        self.ui.btn_team2.setText('0')
        self.ui.btn_sets1.setText('0')
        self.ui.btn_sets2.setText('0')
        self.buffer.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VolleyTable()
    window.show()

    sys.exit(app.exec())