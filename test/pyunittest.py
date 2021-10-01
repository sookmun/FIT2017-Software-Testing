from app.calculator import Calculator
from app.calculator_form import Calculator_Form
import unittest
from datetime import datetime
import main as app
from wtforms.validators import DataRequired, ValidationError, Optional
from wtforms import StringField, DateField, TimeField
from unittest.mock import Mock

class TestCalculator(unittest.TestCase):
    """
    cost_calculation_alg1_asg1(self, date, start_time, initial_state, final_state, capacity, charger_config)
    cost_calculation_alg1_asg2(self, date, postcode, start_time, charging_duration, charger_configuration, initial_state, final_state, location)
    cost_calculation_alg2_asg2(self, date, postcode, start_time, charging_duration, charger_configuration,initial_state, final_state, location)
    get_price(self)
    time_calculation(self, initial_state, final_state, capacity, power)
    is_holiday(self, start_date)    **DONE**
    is_peak(self, start_time)       **DONE**
    charger_configuration(self, charger_config)  **DONE**
    get_solar_energy_duration(self, data, start_time, charging_duration)
    get_day_light_length(self, data)
    get_solar_insolation(self, data)
    get_cloud_cover(self, data, start_time)
    calculate_solar_energy_alg1(self, date, postcode, start_time, charging_duration, location)
    get_du(self)
    calculate_solar_energy_alg2(self, date, postcode, start_time, charging_duration, location)
    cum_calculate_solar_energy_alg2(self, date, postcode, start_time, charging_duration, location)
    get_weather(self, date, postcode, location)     THIS USES THE API
    check_date(self, date)
    """

    # you may create more test methods
    # you may add parameters to test methods
    # this is an example
    # def test_cost(self):
    #     self.calculator = Calculator()
    #     self.assertEqual(self.calculator.cost_calculation("", "", "", "", ""), "")

    # def test_general(self):
    #     initial_state = "5"
    #     final_state = "70"
    #     capacity = "80"
    #     power = "50"
    #     date = "2022-02-22"
    #     location="launceston"
    #     postcode = "7250"
    #     time = "17:30"
    #     charging_duration = "45"
    #     charger_config = "3"
    #     cal = Calculator()
    #     data = cal.get_weather(date, postcode, location)
    #     self.assertEqual("2021-02-22",cal.check_date(date),"invalid date")
    #     self.assertEqual(5.8,cal.get_solar_insolation(data),"invalid si")
    #     self.assertEqual('13.3667',cal.get_day_light_length(data))
    #     self.assertEqual(18, cal.get_cloud_cover(data, "17"))
    #     self.assertEqual(16, cal.get_cloud_cover(data, "18"))
    #     print(cal.cum_calculate_solar_energy_alg2(date, postcode, time, charging_duration, location))
    #     # dateOne="2020-02-22"
    #     # data = cal.get_weather(dateOne, postcode, location)
    #     #
    #     # self.assertEqual(6.7, cal.get_solar_insolation(data), "invalid si")
    #     # dateTwo= "2019-02-22"
    #
    #     # res = cal.cum_calculate_solar_energy_alg2(date, postcode, time, charging_duration, location)
    #     # print(res)
    def test_exampleOne(self):
        cal=Calculator()
        postcode= "6001"
        date= "2020-12-25"
        start_time="08:00"
        charging_duration = "60"
        location="perth"
        data = cal.get_weather(date, postcode, location)
        self.assertEqual(8.6,cal.get_solar_insolation(data),"invalid si")
        self.assertEqual("14.2333",cal.get_day_light_length(data),"invalid dl")
        ret= cal.calculate_solar_energy_alg1(date,postcode,start_time,charging_duration,location)
        ret=ret[0][0]
        # self.assertEqual("6.0422",ret,"Wrong Calculation")

    def test_exampleTwo(self):
        initial_state = "5"
        final_state = "70"
        capacity = "80"
        power = "50"
        date = "2022-02-22"
        location="launceston"
        postcode = "7250"
        time = "17:30"
        charging_duration = "45"
        charger_config = "3"
        cal = Calculator()
        data = cal.get_weather(date, postcode, location)
        self.assertEqual("2021-02-22",cal.check_date(date))
        self.assertEqual(5.8, cal.get_solar_insolation(data), "invalid si")
        self.assertEqual("13.3667",cal.get_day_light_length(data),"invalid dl")
        f=cal.calculate_solar_energy_alg2(date, postcode, time, "29", location)
        # self.assertEqual("1.7407",f[0][0],"Wrong Calculation")
        d = cal.calculate_solar_energy_alg2(date, postcode, "18:00", "15", location)
        # self.assertEqual("0.9112", d[0][0], "Wrong Calculation")





    def test_holiday(self):
        date = "1/1/2020"
        other_date = "3/5/2021"
        self.calculator = Calculator()
        self.assertTrue(self.calculator.is_holiday(date), "Day is not a holiday")
        self.assertFalse(self.calculator.is_holiday(other_date), "Day is a holiday")

    def test_peak(self):
        time = "17:30"
        other_time = "05:00"
        time = datetime.strptime(time, "%H:%M")
        other_time = datetime.strptime(other_time, "%H:%M")
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
        self.assertEqual(36, self.calculator.charger_configuration(6), "Wrong power")
        self.assertEqual(90, self.calculator.charger_configuration(7), "Wrong power")
        self.assertEqual(350, self.calculator.charger_configuration(8), "Wrong power")



if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suit)
