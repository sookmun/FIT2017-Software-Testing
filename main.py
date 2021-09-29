from flask import Flask, flash, render_template, request, jsonify
from flask_wtf import FlaskForm

from app.calculator_form import *
from app.calculator import *
import os

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

        # you may change the logic as your like
        # duration = calculator.get_duration(start_time)

        # is_peak = calculator.is_peak()

        # if is_peak:
        #     peak_period = calculator.peak_period(start_date)
        power = calculator.charger_configuration(charger_configuration)

        charging_duration = calculator.time_calculation(initial_charge, final_charge, battery_capacity, power)

        cost1 = calculator.cost_calculation_alg1_asg1(start_date, start_time, initial_charge, final_charge, battery_capacity, charger_configuration)
        cost2 = calculator.cost_calculation_alg1_asg2(start_date, postcode, start_time, charging_duration, charger_configuration, initial_charge, final_charge, location)
        cost3 = calculator.cost_calculation_alg2_asg2(start_date, postcode, start_time, charging_duration, charger_configuration, initial_charge, final_charge, location)
        # cost = calculator.cost_calculation(initial_charge, final_charge, battery_capacity, is_peak, is_holiday)

        # time = calculator.time_calculation(initial_charge, final_charge, battery_capacity, power)

        # you may change the return statement also
        
        # values of variables can be sent to the template for rendering the webpage that users will see
        # return render_template('calculator.html', calculation_success=True, form=calculator_form)
        return render_template('calculator.html', calculation_success=True, form=calculator_form, charging_time=charging_duration, cost1=cost1, cost2=cost2, cost3=cost3)

    else:
        # battery_capacity = request.form['BatteryPackCapacity']
        # flash(battery_capacity)
        # flash("something went wrong")
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
