import

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