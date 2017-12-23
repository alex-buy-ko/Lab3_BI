import unittest
import dataHandler

# проверим ассертами calc_kpi c "0"

class BiLogicTestCase_positive(unittest.TestCase):
    y = [1147, 1490, 1483, 1186, 1020, 1401, 1270, 1227, 1397, 1328, 1447, 916]
    dy = [0, 343, -7, -297, -166, 381, -131, -43, 170, -69, 119, -531]
    d_dy = [0, 29.9, -0.47, -20.03, -14.0, 37.35, -9.35, -3.39, 13.85, -4.94, 8.96, -36.7]
    up_dy = [0, 29.9, -0.61, -25.89, -14.47, 33.22, -11.42, -3.75, 14.82, -6.02, 10.37, -46.29]

    def test_calc_kpi1(self):
        test_dy = dataHandler.calc_kpi1(self.y)
        self.assertEquals(test_dy, self.dy)

    def test_calc_kpi2(self):
        test_d_dy = dataHandler.calc_kpi2(self.y)
        self.assertEquals(test_d_dy, self.d_dy)

    def test_calc_kpi3(self):
        test_up_dy = dataHandler.calc_kpi3(self.y)
        self.assertEquals(test_up_dy, self.up_dy)