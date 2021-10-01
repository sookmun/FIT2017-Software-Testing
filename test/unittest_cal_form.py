from app.calculator_form import Calculator_Form
import unittest
import main as app
from wtforms.validators import DataRequired, ValidationError, Optional
from datetime import datetime
class MyTestCase(unittest.TestCase):

    def test_validate_Baterypack(self):
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.BatteryPackCapacity.data = "-1"
            with self.assertRaises(ValueError):
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            with self.assertRaises(ValueError):
                form.BatteryPackCapacity.data = ""
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            with self.assertRaises(ValueError):
                form.BatteryPackCapacity.data = "abc"
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            with self.assertRaises(ValidationError):
                form.BatteryPackCapacity.data = None
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)

    def test_validate_InitialCharge(self):
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.FinalCharge.data="30"
            with self.assertRaises(ValueError):
                form.InitialCharge.data = "abc"
                form.validate_InitialCharge(form.InitialCharge)
            with self.assertRaises(ValueError):
                form.InitialCharge.data = "40"
                form.validate_InitialCharge(form.InitialCharge)
            with self.assertRaises(ValueError):
                form.InitialCharge.data = "-1"
                form.validate_InitialCharge(form.InitialCharge)
            with self.assertRaises(ValueError):
                form.InitialCharge.data = "101"
                form.validate_InitialCharge(form.InitialCharge)

    def test_validate_FinalCharge(self):
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "9"
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "abc"
                form.validate_FinalCharge(form.FinalCharge)
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "2"
                form.validate_FinalCharge(form.FinalCharge)
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "0"
                form.validate_FinalCharge(form.FinalCharge)
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "101"
                form.validate_FinalCharge(form.FinalCharge)
    def test_validate_StartDate(self):
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.StartDate.data= datetime.strptime("31/1/18", '%d/%m/%y').date()
            with self.assertRaises(ValueError):
                form.validate_StartDate(form.StartDate)
            form.StartDate.data = datetime.strptime("1/1/18", '%d/%m/%y').date()
            with self.assertRaises(ValueError):
                form.validate_StartDate(form.StartDate)

    def test_validate_ChargerCongfig(self):
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            with self.assertRaises(ValueError):
                form.ChargerConfiguration.data="abc"
                form.validate_ChargerConfiguration(form.ChargerConfiguration)
            with self.assertRaises(ValueError):
                form.ChargerConfiguration.data="0"
                form.validate_ChargerConfiguration(form.ChargerConfiguration)
            with self.assertRaises(ValueError):
                form.ChargerConfiguration.data="9"
                form.validate_ChargerConfiguration(form.ChargerConfiguration)

    def test_validate_PostCode(self):
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            with self.assertRaises(ValueError):
                form.PostCode.data="36000"
                form.validate_PostCode(form.PostCode)


if __name__ == '__main__':
    unittest.main()

