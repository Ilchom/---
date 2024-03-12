from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QListWidget, QGroupBox, QButtonGroup, QLineEdit
from texts import *
from ruffer import *
import time

age_res = 0
name_res = ''
puls1 = 0
puls2 = 0
puls3 = 0
text_res = ''

'MODULES-----------------------------------------------------------------------------------------------MODULES'





def next_win1():
    global name_res, age_res
    name_res = str(name.text())
    age_res = age.text()
    win1.hide()
    win2.show()

def next_win2():
    global puls1
    puls1 = int(puls.text())
    win2.hide()
    win3.show()


def next_win3():
    win3.hide()
    win4.show()


def next_win4():
    global puls2, puls3, text_res, win5
    puls2 = int(before_rest.text())
    puls3 = int(after_rest.text())
    text_res = name_res +', '+ str(test(puls1, puls2, puls3, age_res))
    win4.hide()

    win5 = QWidget()
    win5.setWindowTitle('Тест Руфье')

    vl5 = QVBoxLayout()

    info5 = QLabel(text_res)
    next_btn5 = QPushButton('Закрыть')

    vl5.addWidget(info5)
    vl5.addWidget(next_btn5)
    win5.setLayout(vl5)
    next_btn5.clicked.connect(next_win5)

    win5.show()



def next_win5():
    win5.close()


'BEGINING------------------------------------------------------------------------------------------------BEGINING'


app = QApplication([])

'1------------------------------------------------------------------------------------------------1'
win1 = QWidget()
win1.setWindowTitle('Тест Руфье')

vl1 = QVBoxLayout()

start_info = QLabel(start_text)
name = QLineEdit()

age = QLineEdit()

next_btn = QPushButton('Продолжить')
in_age = QLabel('Введите возраст:')
in_name = QLabel('Введите имя:')


vl1.addWidget(start_info)
vl1.addWidget(in_name)
vl1.addWidget(name)
vl1.addWidget(in_age)
vl1.addWidget(age)
vl1.addWidget(next_btn)

win1.setLayout(vl1)
next_btn.clicked.connect(next_win1)

'2------------------------------------------------------------------------------------------------2'
win2 = QWidget()
win2.setWindowTitle('Тест Руфье')


vl2 = QVBoxLayout()
hl2 = QHBoxLayout()

info2 = QLabel(text2)
puls = QLineEdit()
next_btn2 = QPushButton('Продолжить')
res_puls = QLabel('Введите результат:')
timer_btn2 = QPushButton('Таймер')

hl2.addWidget(next_btn2)

vl2.addWidget(info2)
vl2.addWidget(res_puls)
vl2.addWidget(puls)

vl2.addLayout(hl2)

win2.setLayout(vl2)
next_btn2.clicked.connect(next_win2)

'3------------------------------------------------------------------------------------------------3'
win3 = QWidget()
win3.setWindowTitle('Тест Руфье')


vl3 = QVBoxLayout()
hl3 = QHBoxLayout()

info3 = QLabel(text3)
next_btn3 = QPushButton('Сделано')


vl3.addWidget(info3)

hl3.addWidget(next_btn3)


vl3.addLayout(hl3)

win3.setLayout(vl3)
next_btn3.clicked.connect(next_win3)

'4------------------------------------------------------------------------------------------------4'
win4 = QWidget()
win4.setWindowTitle('Тест Руфье')


vl4 = QVBoxLayout()
hl4 = QHBoxLayout()

info4 = QLabel(text4)
before_rest = QLineEdit()
after_rest = QLineEdit()
next_btn4 = QPushButton('Завершить')
in_before = QLabel('Результат до отдыха:')
in_after = QLabel('Результат после отдыха:')


vl4.addWidget(info4)
vl4.addWidget(in_before)
vl4.addWidget(before_rest)
vl4.addWidget(in_after)
vl4.addWidget(after_rest)

hl4.addWidget(next_btn4)

vl4.addLayout(hl4)

win4.setLayout(vl4)
next_btn4.clicked.connect(next_win4)

'5------------------------------------------------------------------------------------------------5'


'END------------------------------------------------------------------------------------------------END'




win1.show()
app.exec()
