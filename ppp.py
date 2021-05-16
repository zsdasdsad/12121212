from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget()

l1 = QLabel("От:")
l2 = QLabel("До:")
l3 = QLabel("Список результатов:")

ag = QPushButton("Сгенерировать")
clearbut = QPushButton("Очистить список")
tb2 = QLineEdit()
tb3 = QLineEdit()
fin = QListWidget()
def avc():
    a = int( tb2.text())
    b = int( tb3.text())
    if a<b:
        rr = randint(a,b)
        rr = str(rr)
        fin.addItem(rr)
    else:
        fin.addItem("Неверный диапазон чисел.")

def clear():
    fin.clear()

clearbut.clicked.connect(clear)
ag.clicked.connect(avc)
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()
hline4 = QHBoxLayout()
hline5 = QHBoxLayout()

winline = QVBoxLayout()

hline2.addWidget(l1)
hline2.addWidget(tb2)
hline2.addWidget(l2)
hline2.addWidget(tb3)
hline3.addWidget(ag)
hline4.addWidget(l3)
hline4.addWidget(fin)
hline5.addWidget(clearbut)

winline.addLayout(hline2)
winline.addLayout(hline3)
winline.addLayout(hline4)
winline.addLayout(hline5)


win.setLayout(winline)

win.show()
app.exec_()