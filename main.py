# VVV222

# -*- coding: utf-8 -*-
# import initExample ## Add path to library (just for examples; you do not need this)


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from PyQt4 import Qt
#####################################################
#####################################################
KPI_1 = 'Абсолютный прирост'
KPI_2 = 'Темп прироста'
KPI_3 = 'Темп наращения'

CURRENT_KPI = KPI_1
#####################################################
#####################################################
app = QtGui.QApplication([])
# mw = QtGui.QMainWindow()
# mw.resize(800,800)

win = pg.GraphicsWindow(title="OSMP BI SYSTEM")
win.resize(1600,700)
win.setWindowTitle('FuryFuturama: BI')
win.move(150,150)
# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)
#####################################################
#####################################################


low_plot = win.addPlot(title="Низший класс")
mid_plot = win.addPlot(title="Средний класс")
high_plot = win.addPlot(title="Люксовый класс")

for plot_name in [low_plot, mid_plot, high_plot]:
    plot_name.showGrid(x=True, y=True)
    plot_name.setLabel('bottom', "Время", units='Месяцы')

    plot_name.enableAutoRange('xy')
    
#####################################################
#####################################################
##############    TODO BUTTONS      #################
#####################################################
#####################################################
def buttonClicked(kpi_prm):
    ## что-то типа clean()
    low_plot.clear()
    mid_plot.clear()
    high_plot.clear()
    CURRENT_KPI = kpi_prm
    if kpi_prm == KPI_1:
        y1 = calc_kpi1(low_cat)
        y2 = calc_kpi1(mid_cat)
        y3 = calc_kpi1(high_cat)

    elif kpi_prm == KPI_2:
        y1 = calc_kpi2(low_cat)
        y2 = calc_kpi2(mid_cat)
        y3 = calc_kpi2(high_cat)

    elif kpi_prm == KPI_3:
        y1 = calc_kpi3(low_cat)
        y2 = calc_kpi3(mid_cat)
        y3 = calc_kpi3(high_cat)
    for plot_name in [low_plot, mid_plot, high_plot]:
        plot_name.setLabel('left', CURRENT_KPI, units='kpi')
    print("Print: " + CURRENT_KPI)
    low_plot.plot(x, y1,pen='w')
    mid_plot.plot(x, y2,pen='y')
    high_plot.plot(x, y3,pen='g')

    
# win.nextRow()
# win.nextCol()
button1 = QtGui.QPushButton(KPI_1)
button1.setToolTip("""Абсолютный прирост - Абсолютный прирост необходим для расчета темпа прироста. \nОпределяется в разностном сопоставлении двух уровней ряда динамики в единицах измерения исходной информации.""")
button1.clicked.connect(lambda : buttonClicked(KPI_1))
button2 = QtGui.QPushButton(KPI_2)
button2.setToolTip("""Темп прироста, % - Темпы прироста характеризуют абсолютный прирост в относительных величинах. \nТемп прироста (в %) показывает, на сколько процентов изменился сравниваемый уровень с уровнем, принятым за базу сравнения.""")
button2.clicked.connect(lambda : buttonClicked(KPI_2))
button3 = QtGui.QPushButton(KPI_3)
button3.setToolTip("""Темп наращения, % - Важным статистическим показателем динамики социально-экономических процессов является темп наращивания, \nкоторый в условиях интенсификации экономики измеряет наращивание во времени экономического потенциала.""")
button3.clicked.connect(lambda : buttonClicked(KPI_3))

button1.setFont(QtGui.QFont('Verdana', 8))
button2.setFont(QtGui.QFont('Verdana', 8))
button3.setFont(QtGui.QFont('Verdana', 8))
my_btn_style = """
    QPushButton:hover { background-color: rgb(102, 51, 153); }
    QPushButton:!hover { background-color: rgb(204 153 102); }
    QPushButton:pressed { background-color: rgb(153, 153, 255); }
"""

button1.setStyleSheet(my_btn_style)
button2.setStyleSheet(my_btn_style)
button3.setStyleSheet(my_btn_style)

hbox = QtGui.QHBoxLayout()  

# hbox.setStretch(0,0)

proxy1= QtGui.QGraphicsProxyWidget()
proxy2= QtGui.QGraphicsProxyWidget()
proxy3= QtGui.QGraphicsProxyWidget()

proxy1.resize(100,100)
proxy1.setWidget(button1)
proxy2.setWidget(button2)
proxy3.setWidget(button3)

pp1 = win.addLayout(row=4, col=1)

pp1.addItem(proxy1,1,0)
pp1.addItem(proxy2,2,0)
pp1.addItem(proxy3,3,0)


#####################################################
#####################################################
################# ВЫЧИСЛЯЮЩИЙ КЛАСС #################
#####################################################
#####################################################
import pandas as pd
import matplotlib.pyplot as plt
try:
    fixed_df = pd.read_csv('data\\BuisnesData.csv', sep=';',index_col='Mounth')
    # Y
    low_cat = [int(fixed_df['Low'][i]) for i in range(len(fixed_df['Low']))]
    mid_cat = [int(fixed_df['Middle'][i]) for i in range(len(fixed_df['Middle']))]
    high_cat = [int(fixed_df['High'][i]) for i in range(len(fixed_df['High']))]
    # X
    mnth = [i for i in fixed_df.index]
except:
    print("Введён некорректный формат данных")
#     lbl = pg.GraphicsWindow(title="ERROR")
#     lbl.setFixedSize(100, 100)
#     lbl.setWindowTitle('Сообщение об ошибке!')

    lbl1 = QtGui.QLabel('Введены некорректные данные')
    
#     lbl.setOpenExternalLinks(True)
    lbl1.resize(450,150)
    lbl1.move(800, 600)
    lbl1.setText("<h2>Введены некорректные данные.</h2> \nПопробуйте закрыть программу и <p>загрузить <b>корректные</b> данные.</p>")
    lbl1.show()
    
def calc_kpi1(y):
    dy = []
    dy.append(0)
    for i in range(1,len(y)):
        dy.append(y[i] - y[i-1])
    return dy

def calc_kpi2(y):
    dy = calc_kpi1(y)
    d_dy = []
    d_dy.append(0)
    
    for i in range(1,len(y)):

        if y[i-1] != 0:
            d_dy.append(round(dy[i]/y[i-1]*100,2))
        else:
            d_dy.append(0)
    return d_dy


def calc_kpi3(y):
    dy = calc_kpi1(y)
    up_dy = []
    up_dy.append(0)
    for i in range(1,len(y)):
        if y[0] != 0:
            up_dy.append(round(dy[i]/y[0]*100,2))
        else:
            up_dy.append(0)
    return up_dy
x = [i for i in range(1,13)] 

###################################
###################################


# y1 = calc_kpi3(low_cat)
# y2 = calc_kpi3(mid_cat)
# y3 = calc_kpi3(high_cat)

# low_plot.plot(x, y1,pen='w')
# mid_plot.plot(x, y2,pen='y')
# high_plot.plot(x, y3,pen='g')




## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()