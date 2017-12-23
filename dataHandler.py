import pandas as pd
import matplotlib.pyplot as plt


x = [i for i in range(1, 13)]
def dataLoader():
    try:
        fixed_df = pd.read_csv('C:\\Users\\user\\Documents\\Lab3_BI\\data\\BuisnesData.csv', sep=';', index_col='Mounth')
        # Y
        low_cat = [int(fixed_df['Low'][i]) for i in range(len(fixed_df['Low']))]
        mid_cat = [int(fixed_df['Middle'][i]) for i in range(len(fixed_df['Middle']))]
        high_cat = [int(fixed_df['High'][i]) for i in range(len(fixed_df['High']))]
        # X
        mnth = [i for i in fixed_df.index]
        return low_cat, mid_cat, high_cat
    except:
        print("Введён некорректный формат данных")
        #     lbl = pg.GraphicsWindow(title="ERROR")
        #     lbl.setFixedSize(100, 100)
        #     lbl.setWindowTitle('Сообщение об ошибке!')

        lbl1 = QtGui.QLabel('Введены некорректные данные')

        #     lbl.setOpenExternalLinks(True)
        lbl1.resize(450, 150)
        lbl1.move(800, 600)
        lbl1.setText(
            "<h2>Введены некорректные данные.</h2> \nПопробуйте закрыть программу и <p>загрузить <b>корректные</b> данные.</p>")
        lbl1.show()


def calc_kpi1(y):
    dy = []
    dy.append(0)
    for i in range(1, len(y)):
        dy.append(y[i] - y[i - 1])
    return dy


def calc_kpi2(y):
    dy = calc_kpi1(y)
    d_dy = []
    d_dy.append(0)

    for i in range(1, len(y)):

        if y[i - 1] != 0:
            d_dy.append(round(dy[i] / y[i - 1] * 100, 2))
        else:
            d_dy.append(0)
    return d_dy


def calc_kpi3(y):
    dy = calc_kpi1(y)
    up_dy = []
    up_dy.append(0)
    for i in range(1, len(y)):
        if y[0] != 0:
            up_dy.append(round(dy[i] / y[0] * 100, 2))
        else:
            up_dy.append(0)
    return up_dy

