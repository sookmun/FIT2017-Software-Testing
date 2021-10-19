import unittest
from app.calculator_form import Calculator_Form
import main as app
from wtforms.validators import ValidationError
from datetime import datetime


class TestCalculatorForm(unittest.TestCase):
    """
    This test class test all the functions in calculator_form.py
    """

    def test_validate_Batterypack(self):
        """
        Test the validation function for Battery_Pack_Capacity.
        It checks the boundary testing and also the condition coverage of each if and else statement.
        """
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.BatteryPackCapacity.data = "-1"    # boundary value
            with self.assertRaises(ValueError):     # ensures that any number less than 0 is invalid
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            with self.assertRaises(ValueError):
                form.BatteryPackCapacity.data = ""  # ensures that there is data input
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            with self.assertRaises(ValueError):     # ensures that is not a random string
                form.BatteryPackCapacity.data = "abc"
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            with self.assertRaises(ValidationError):    # ensures that the flaks is working properly
                form.BatteryPackCapacity.data = None
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            form.BatteryPackCapacity.data= "90"  # ensures that a valid input is accepted
            try:
                form.validate_BatteryPackCapacity(form.BatteryPackCapacity)
            except:
                raise ValidationError("This input should be accepted")  # an error will be raised if is not accepted

    def test_validate_InitialCharge(self):
        """
        A test function for validation of Initial charge
        This uses combination of both boundary testing from blackbox and branch coverage from whitebox
        This test ensures that the value must be from 0-100 and is also less tha final charge data
        The test ensures that valid input is accepted
        """
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.FinalCharge.data="30" #setting the final charge
            with self.assertRaises(ValueError):
                form.InitialCharge.data = "abc" #ensuring random string is not accepted
                form.validate_InitialCharge(form.InitialCharge)
            with self.assertRaises(ValueError):
                form.InitialCharge.data = "40" #ensuring it has to be less than final charge
                form.validate_InitialCharge(form.InitialCharge)
            with self.assertRaises(ValueError): #boundary testing
                form.InitialCharge.data = "-1"
                form.validate_InitialCharge(form.InitialCharge)
            with self.assertRaises(ValueError): #boundary testing
                form.InitialCharge.data = "101"
                form.validate_InitialCharge(form.InitialCharge)
            #ensuring valid input is accepted
            try:
                form.InitialCharge.data = "3"
                form.validate_InitialCharge(form.InitialCharge)
            except:
                raise ValidationError("This input should be accepted")
            try:
                form.FinalCharge.data="100"
                form.InitialCharge.data = "99" #boundary testing for valid inputs
                form.validate_InitialCharge(form.InitialCharge)
            except:
                raise ValidationError("This input should be accepted")

    def test_validate_FinalCharge(self):
        """
       A test function for validation of Final charge
       This uses combination of both boundary testing from blackbox and branch coverage from whitebox
       This test ensures that the value must be from 0-100 and is also more than initial charge data
       The test ensures that valid input is accepted
       """
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "9"
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "abc"   # ensuring input is an integer
                form.validate_FinalCharge(form.FinalCharge)
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "2"     # ensuring input must be more than initial charge
                form.validate_FinalCharge(form.FinalCharge)
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "0"     # boundary testing
                form.validate_FinalCharge(form.FinalCharge)
            with self.assertRaises(ValueError):
                form.FinalCharge.data = "101"   # boundary testing
                form.validate_FinalCharge(form.FinalCharge)

            # ensuring all valid input is accepted
            # uses the boundary value of valid inputs
            try:
                form.FinalCharge.data = "100"
                form.validate_FinalCharge(form.FinalCharge)
            except:
                raise ValidationError("This input should be accepted")

            try:
                form.InitialCharge.data = "0"
                form.FinalCharge.data = "1"
                form.validate_FinalCharge(form.FinalCharge)
            except:
                raise ValidationError("This input should be accepted")

    def test_validate_StartDate(self):
        """
        A test function for validation of Start Date
        Only accepts date that is past February 2018 because of the weather API
        It checks the boundary testing and also the condition coverage of each if and else statement.
        """
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            form.StartDate.data = datetime.strptime("31/1/2018", '%d/%m/%Y').date()     # boundary value
            with self.assertRaises(ValueError):
                form.validate_StartDate(form.StartDate)
            form.StartDate.data = datetime.strptime("1/1/2018", '%d/%m/%Y').date()
            with self.assertRaises(ValueError):
                form.validate_StartDate(form.StartDate)
            # ensuring the valid input is accepted
            # uses the boundary date of 1 February 2018
            try:
                form.StartDate.data = datetime.strptime("2/10/2021", '%d/%m/%Y').date()
                form.validate_StartDate(form.StartDate)
            except:
                raise ValidationError("This input should be accepted")
            try:
                form.StartDate.data = datetime.strptime("1/2/2018", '%d/%m/%Y').date()
                form.validate_StartDate(form.StartDate)
            except:
                raise ValidationError("This input should be accepted")

    def test_validate_ChargerCongfig(self):
        """
        A test function for validation of charger configuration
        Only accepts number from 1-8
        It checks the boundary testing and also the condition coverage of each if and else statement.
        """
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            with self.assertRaises(ValueError):
                form.ChargerConfiguration.data = "abc"    # ensuring that the input is an integer
                form.validate_ChargerConfiguration(form.ChargerConfiguration)
            with self.assertRaises(ValueError):
                form.ChargerConfiguration.data = "0"      # boundary value
                form.validate_ChargerConfiguration(form.ChargerConfiguration)
            with self.assertRaises(ValueError):
                form.ChargerConfiguration.data = "9"    # boundary value
                form.validate_ChargerConfiguration(form.ChargerConfiguration)
            # ensuring the valid input is accepted
            # uses the valid boundary value of 1-8
            try:
                form.ChargerConfiguration.data = "8"
                form.validate_ChargerConfiguration(form.ChargerConfiguration)
            except:
                raise ValidationError("This input should be accepted")

            try:
                form.ChargerConfiguration.data = "1"
                form.validate_ChargerConfiguration(form.ChargerConfiguration)
            except:
                raise ValidationError("This input should be accepted")

    def test_validate_PostCode(self):
        """
       A test function for validation of Postcode
       Only accepts valid postcode
       It checks the boundary testing and also the condition coverage of each if and else statement.
       """
        app.ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with app.ev_calculator_app.app_context():
            form = Calculator_Form()
            with self.assertRaises(ValueError):
                form.PostCode.data = "36000"          # raises an error when postcode is invalid
                form.validate_PostCode(form.PostCode)
            with self.assertRaises(ValueError):
                form.PostCode.data = "abc"          # ensuring is not a random string
                form.validate_PostCode(form.PostCode)

            # ensuring valid postcode is accepted
            try:
                form.PostCode.data = "3800"
                form.validate_PostCode(form.PostCode)
            except:
                raise ValidationError("This input should be accepted")


if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorForm)
    unittest.TextTestRunner(verbosity=2).run(suit)

