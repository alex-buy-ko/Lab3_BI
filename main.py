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

CURRENT_KPI = KPI_3
#####################################################
#####################################################
app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800,800)

win = pg.GraphicsWindow(title="OSMP BI SYSTEM")
win.resize(1200,300)
win.setWindowTitle('FuryFuturama: BI')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)
#####################################################
#####################################################

# hbox = QtGui.QVBoxLayout()  

# hbox.setStretch(0,0)
button1 = QtGui.QPushButton(KPI_1)
button1.setToolTip('Эта кнопка нужна чтобы посчитать "Абсолютный прирост"!')
############################### Кнопки меняют CURRENT_KPI #################
button2 = QtGui.QPushButton(KPI_2)
button2.setToolTip('Эта кнопка нужна чтобы посчитать "Темп прироста"!')
button3 = QtGui.QPushButton(KPI_3)
button3.setToolTip('Эта кнопка нужна чтобы посчитать "Темп наращения"!')
# proxy1= QtGui.QGraphicsProxyWidget()
# proxy2= QtGui.QGraphicsProxyWidget()
# proxy3= QtGui.QGraphicsProxyWidget()

# proxy1.resize(100,100)
# proxy1.setWidget(button1)
# proxy2.setWidget(button2)
# proxy3.setWidget(button3)

# pp1 = win.addLayout(row=0, col=0)

# pp1.addItem(proxy1,1,1)
# pp1.addItem(proxy2,2,1)
# pp1.addItem(proxy3,3,1)

low_plot = win.addPlot(title="Низший класс")
low_plot.showGrid(x=True, y=True)
low_plot.setLabel('bottom', "Время", units='Месяцы')
low_plot.setLabel('left', CURRENT_KPI, units='kpi')
low_plot.enableAutoRange('xy')

mid_plot = win.addPlot(title="Средний класс")
mid_plot.showGrid(x=True, y=True)
mid_plot.setLabel('bottom', "Время", units='Месяцы')
mid_plot.setLabel('left', CURRENT_KPI, units='kpi')
mid_plot.enableAutoRange('xy')

high_plot = win.addPlot(title="Люксовый класс")
high_plot.showGrid(x=True, y=True)
high_plot.setLabel('bottom', "Время", units='Месяцы')
high_plot.setLabel('left', CURRENT_KPI, units='kpi')
high_plot.enableAutoRange('xy')

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


#####################################################
#####################################################



y1 = calc_kpi3(low_cat)
y2 = calc_kpi3(mid_cat)
y3 = calc_kpi3(high_cat)

low_plot.plot(x, y1,pen='w')
mid_plot.plot(x, y2,pen='y')
high_plot.plot(x, y3,pen='g')




## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
