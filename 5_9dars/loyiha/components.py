from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
from database import database
SELECTED_SEAT_NO = -1




class Label(QLabel):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.setStyleSheet("""
            font-size: 36px;
            color: red;
        """)


class Input(QLineEdit):
    def __init__(self, oyna: QWidget):
        super().__init__(oyna)
        self.resize(300, 40)
        self.setStyleSheet("""
            font-size: 24px;
        """)


class ComboBox(QComboBox):
    def __init__(self, oyna: QWidget):
        super().__init__(oyna)
        self.resize(300, 40)
        self.setStyleSheet("""
            font-size: 20px;
        """)


class Button(QPushButton):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setText(text)

        self.resize(150, 50)
        self.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                border-radius: 5px;
                border: 3px solid blue;
                background-color: none;
                color: blue;
            }
                           
            QPushButton:hover {
                border: 3px solid darkblue; 
                background-color: darkblue;
                color: white;
            }
                           
            QPushButton:pressed {           
                border: 3px solid green;
                background-color: green;
                color: white;
            }
        """)


class SeatButton(QPushButton):
    def __init__(self, no: int, oyna: str, x: int, y: int, FIO: str = "F.I.SH"):
        super().__init__(oyna)
        self.no = no
        self.oyna = oyna

        self.setText(str(no))
        self.fioLabel = QLabel(FIO, oyna)
        self.priceLabel = Label("",oyna)
        self.priceLabel.move(70, 460)
        self.fioLabel.setStyleSheet("""
            font-size: 18px;
            color: green;
            font-weight: bold;
        """)

        self.resize(50, 50)
        self.move(x, y)
        self.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                border: 3px solid green;
                color: green;
                background-color: none;
                font-weight: bold;
            }

            QPushButton:hover {
                border: 3px solid darkgreen;
                color: green darkgreen;
            }
        """)

        self.clicked.connect(self.bosildi)


    def bosildi(self):

        self.oyna.clickted_count += 1
        if self.oyna.clickted_count == 1:

            FIO = self.oyna.fioInput.text()
            if FIO == "":
                self.alert("ism kiritishingiz shart!")
            else:
                self.fioLabel.setText(FIO)
                self.fioLabel.setStyleSheet("""
                color: #946c00;
                font-size: 18px;
                font-weight: bold;
                """)
                self.setStyleSheet("""
                border: 3px solid #946c00;              
                color: #946c00;
                font-size: 24px;
                font-weight: bold;
                """)
                global SELECTED_SEAT_NO
                self.priceLabel.adjustSize()

                SELECTED_SEAT_NO = int(self.text())

                price = database.getPrice(SELECTED_SEAT_NO)
                self.priceLabel.setText(f"Narxi: {price} uzs")
                self.priceLabel.adjustSize()

                self.changeComboboxItem(self.no)
            
        else:
            self.alert("Oldin kiritilgan\nma'lumotlarni tozalang")
    def changeComboboxItem(self,no : int):
        self.oyna.placesComboBox.setCurrentText(str(no))
    def alert(self, text : str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(text)
        msgBox.resize(400, 1000)
        msgBox.setStandardButtons(QMessageBox.Ok)
        
        return msgBox.exec()



    def move(self, x: int, y: int):
        super().move(x, y)
        self.fioLabel.move(self.x(), y - 24)


    def band_qilingan(self, FIO: str):              
        self.fioLabel.setText(FIO)
        self.fioLabel.adjustSize()
        self.fioLabel.setStyleSheet("""
            font-size: 18px;
            color: red;
            font-weight: bold;
        """)

        self.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                border: 3px solid red;
                color: red;
                background-color: none;
                font-weight: bold;
            }

            QPushButton:hover {
                border: 3px solid darkred;
                color: red darkred;
            }
        """)

    

def getLastSelectedSeat():
    global SELECTED_SEAT_NO
    return SELECTED_SEAT_NO


