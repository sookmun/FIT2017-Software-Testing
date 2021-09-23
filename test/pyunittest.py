from app.calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    # you may create more test methods
    # you may add parameters to test methods
    # this is an example
    # def test_cost(self):
    #     self.calculator = Calculator()
    #     self.assertEqual(self.calculator.cost_calculation("", "", "", "", ""), "")

    def test_holiday(self):
        date = "1/1/2020"
        other_date = "3/5/2021"
        self.calculator = Calculator()
        self.assertTrue(self.calculator.is_holiday(date), "Day is not a holiday")

        self.assertFalse(self.calculator.is_holiday(other_date), "Day is a holiday")



    def test_peak(self):
        time = "17:30"
        other_time = "05:00"
        self.calculator = Calculator()
        self.assertTrue(self.calculator.is_peak(time), "Time given is not within peak hours")

        self.assertFalse(self.calculator.is_peak(other_time), "Time given is not within peak hours")


    def test_charger_config(self):
        self.calculator = Calculator()
        self.assertEqual(2, self.calculator.charger_configuration(1),"Wrong power")

        self.assertEqual(3.6, self.calculator.charger_configuration(2), "Wrong power")

        self.assertEqual(7.2, self.calculator.charger_configuration(3), "Wrong power")

        self.assertEqual(11, self.calculator.charger_configuration(4), "Wrong power")

        self.assertEqual(22, self.calculator.charger_configuration(5), "Wrong power")

        self.assertEqual(32, self.calculator.charger_configuration(6), "Wrong power")

        self.assertEqual(90, self.calculator.charger_configuration(7), "Wrong power")

        self.assertEqual(350, self.calculator.charger_configuration(8), "Wrong power")




    # you may create test suite if needed
if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suit)
