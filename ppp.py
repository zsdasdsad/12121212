from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget()

l1 = QLabel("От:")
l2 = QLabel("До:")
l3 = QLabel("Результат:")

ag = QPushButton("Сгенерировать")
tb2 = QLineEdit()
tb3 = QLineEdit()
fin = QListWidget()

#hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()
hline4 = QHBoxLayout()

winline = QVBoxLayout()

#hline1.addWidget(ml)

hline2.addWidget(l1)
hline2.addWidget(tb2)
hline2.addWidget(l2)
hline2.addWidget(tb3)
hline3.addWidget(ag)
hline4.addWidget(l3)
hline4.addWidget(fin)

#winline.addLayout(hline1)
winline.addLayout(hline2)
winline.addLayout(hline3)
winline.addLayout(hline4)

win.setLayout(winline)

win.show()
app.exec_()