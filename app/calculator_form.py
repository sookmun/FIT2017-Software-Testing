from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, Optional
from datetime import date
from app.calculator import *
import requests


# validation for form inputs
class Calculator_Form(FlaskForm):
    # this variable name needs to match with the input attribute name in the html file
    # you are NOT ALLOWED to change the field type, however, you can add more built-in validators and custom messages
    BatteryPackCapacity = StringField("Battery Pack Capacity", [DataRequired()])
    InitialCharge = StringField("Initial Charge", [DataRequired()])
    FinalCharge = StringField("Final Charge", [DataRequired()])
    StartDate = DateField("Start Date", [DataRequired("Data is missing or format is incorrect")], format='%d/%m/%Y')
    StartTime = TimeField("Start Time", [DataRequired("Data is missing or format is incorrect")], format='%H:%M')
    ChargerConfiguration = StringField("Charger Configuration", [DataRequired()])
    PostCode = StringField("Post Code", [DataRequired()])

    # use validate_ + field_name to activate the flask-wtforms built-in validator
    # this is an example for you
    def validate_BatteryPackCapacity(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")
        try :
            field.data =int(field.data)
            if field.data <=0:
                raise ValueError("Capacity must be more than 0")
        except:
            raise ValueError("Capacity must be a positive integer")


    # validate initial charge here
    def validate_InitialCharge(self, field):
        # another example of how to compare initial charge with final charge
        # you may modify this part of the code
        try :
            field.data =int(field.data)
        except:
            raise ValueError("Final Charge must be a positive integer")

        if field.data > int(self.FinalCharge.data):
            raise ValueError("Initial charge data error")
        elif field.data <= 0:
            raise ValueError("Initial charge must be more than 0")
        elif field.data >= 100:
            raise  ValueError("Initial charge must be less than 100")

    # validate final charge here
    def validate_FinalCharge(self, field):
        try:
            field.data = int(field.data)
        except:
            raise ValueError("Final Charge must be a positive integer")

        if field.data < int(self.InitialCharge.data):
            raise ValueError("Final Charge data error")
        elif field.data <= 0:
            raise ValueError("Final Charge must be more than 0")
        elif field.data >= 100:
            raise ValueError("Final Charge must be less than 100")

    # validate start date here
    def validate_StartDate(self, field):
        today = date.today()
        if field.data>today:
            raise ValueError("Start date should not be future dates")

    # validate start time here
    def validate_StartTime(self, field):
        pass

    # validate charger configuration here
    def validate_ChargerConfiguration(self, field):
        try:
            field.data = int(field.data)
        except:
            raise ValueError("Charger Configuration must be an integer")
        if field.data <= 0 or field.data > 8:
            raise ValueError("Incorect Configuration. Choose a value between 1-8")

    # validate postcode here
    def validate_PostCode(self, field):
        url = " http://118.138.246.158/api/v1/location?postcode=" + field.data
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("This is not a valid postcode")


