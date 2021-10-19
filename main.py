from flask import Flask, flash, render_template, request
from app.calculator_form import *
from app.calculator import *
import os

"""
This is the main file that runs the backend logic of the whole application
"""
SECRET_KEY = os.urandom(32)

ev_calculator_app = Flask(__name__)
ev_calculator_app.config['SECRET_KEY'] = SECRET_KEY


@ev_calculator_app.route('/', methods=['GET', 'POST'])
def operation_result():
    # request.form looks for:
    # html tags with matching "name="

    calculator_form = Calculator_Form(request.form)

    # validation of the form
    if request.method == "POST" and calculator_form.validate():
        # if valid, create calculator to calculate the time and cost
        calculator = Calculator()

        # extract information from the form
        battery_capacity = request.form['BatteryPackCapacity']
        initial_charge = request.form['InitialCharge']
        final_charge = request.form['FinalCharge']
        start_date = request.form['StartDate']
        start_time = request.form['StartTime']
        charger_configuration = request.form['ChargerConfiguration']
        postcode = request.form['PostCode']
        location = request.form['Location']

        # find the charger configuration
        power = calculator.get_charger_configuration(charger_configuration)

        # find the charging duration
        charging_duration = calculator.time_calculation(initial_charge, final_charge, battery_capacity, power)

        # calculates the charging cost using different methods under different conditions
        cost = calculator.cost_calculation(start_date, start_time, initial_charge, final_charge, battery_capacity, charger_configuration)
        cost_without_hourly_weather = calculator.cost_cal_without_hourly_weather(start_date, postcode, start_time, charging_duration, charger_configuration, initial_charge, final_charge, location)
        cost_with_hourly_weather = calculator.cost_cal_with_hourly_weather(start_date, postcode, start_time, charging_duration, charger_configuration, initial_charge, final_charge, location)

        # values of variables can be sent to the template for rendering the webpage that users will see
        return render_template('calculator.html', calculation_success=True, form=calculator_form, charging_time=charging_duration, cost1=cost, cost2=cost_without_hourly_weather, cost3=cost_with_hourly_weather)

    else:
        flash_errors(calculator_form)
        return render_template('calculator.html', calculation_success=False, form=calculator_form)


# method to display all errors
def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


if __name__ == '__main__':
    ev_calculator_app.run()
