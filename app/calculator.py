import requests
from decimal import Decimal
from flask import Flask, flash
from flask import render_template
from flask import request
from datetime import datetime, timedelta
import holidays


class Calculator():
    # you can choose to initialise variables here, if needed.
    period = 1
    power = 0
    price = 0
    duration = 0
    start_time = "00:00"

    def __init__(self):
        pass

    def cost_calculation_alg1_asg1(self, date, start_time, initial_state, final_state, capacity, charger_config):
        formatted_date = Calculator.format_date(self, date)
        ref_date = Calculator.check_date(self, formatted_date)
        Calculator.charger_configuration(self, charger_config)
        current = datetime.strptime(start_time, "%H:%M")

        if Calculator.is_peak(self, current):
            price = Calculator.price * 2
        else:
            price = Calculator.price

        if Calculator.is_holiday(self, ref_date):
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = (float(final_state) - float(initial_state)) / 100 * float(capacity) * float(price) / 100 * surcharge_factor
        return "{:.2f}".format(cost)

    def cost_calculation_alg1_asg2(self, date, postcode, start_time, charging_duration, charger_configuration, initial_state, final_state):
        total_cost = 0
        formatted_date = Calculator.format_date(self, date)
        ref_date = Calculator.check_date(self, formatted_date)
        Calculator.charger_configuration(self, charger_configuration)
        energy = Calculator.calculate_solar_energy_alg1(self, ref_date, postcode, start_time, charging_duration)
        solar_energy = energy[0]
        du = energy[1]
        price = Calculator.get_price(self)
        for i in range(len(energy)):
            solar = solar_energy[i]
            energy_drawn = Calculator.power * du[i]
            net_energy = energy_drawn - float(solar)
            soc = (int(final_state) - int(initial_state))/100
            if Calculator.is_holiday(self, ref_date):
                surcharge = 1.1
            else:
                surcharge = 1.0

            if net_energy <= 0:
                total_cost += 0
            else:
                total_cost += soc * net_energy * surcharge * price[i]

        return "{:.2f}".format(total_cost)

    def cost_calculation_alg2_asg2(self, date, postcode, start_time, charging_duration, charger_configuration,
                                   initial_state, final_state):
        total_cost = 0
        formatted_date = Calculator.format_date(self, date)
        ref_date = Calculator.check_date(self, formatted_date)
        Calculator.charger_configuration(self, charger_configuration)
        energy = Calculator.cum_calculate_solar_energy_alg2(self, ref_date, postcode, start_time, charging_duration)
        price = Calculator.get_price(self)
        for i in range(len(energy)):
            info = energy[i]
            for j in range(len(info)):
                solar = info[0]
                du = info[1]
                solar_energy = solar[j]
                energy_drawn = Calculator.power * du[j]
                net_energy = energy_drawn - float(solar_energy)
                soc = (int(final_state) - int(initial_state)) / 100
                if Calculator.is_holiday(self, ref_date):
                    surcharge = 1.1
                else:
                    surcharge = 1.0

                if net_energy <= 0:
                    total_cost += 0
                else:
                    total_cost += soc * net_energy * surcharge * price[j]

        return "{:.2f}".format(total_cost)

    def get_price(self):
        price = []
        duration = Calculator.duration
        start_time = Calculator.start_time
        remaining_time = duration
        start_time = datetime.strptime(start_time, '%H:%M')
        while remaining_time > 0:
            if Calculator.is_peak(self, start_time):
                price.append(1.0)
            else:
                price.append(0.5)
            hours = 1
            hours_added = timedelta(hours=hours)
            temp = start_time + hours_added
            next_hr = temp.hour
            next_hr_min = "00"
            temp2 = [str(next_hr), next_hr_min]
            next_hr_str = ":".join(temp2)
            next_hour = datetime.strptime(next_hr_str, '%H:%M')
            time_to_next_hour = abs(next_hour - start_time).total_seconds() / 60.0

            dur = min(time_to_next_hour, remaining_time)
            remaining_time = remaining_time - dur
            start_time = next_hour

        return price

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, power):
        time = ((float(final_state) - float(initial_state)) / 100 * float(capacity) / float(power)) * 60
        time_str = "{:.2f}".format(time)
        return time_str

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def is_holiday(self, start_date):
        date = Calculator.format_date(self, start_date)
        ref_date = Calculator.check_date(self, date)
        aus_holidays = holidays.AUS()
        if ref_date in aus_holidays:
            return True
        return False


    def is_peak(self, start_time):
        peak_start = "06:00"
        peak_end = "18:00"
        given_time = datetime.strptime(start_time, '%H:%M')
        peak_start_time = datetime.strptime(peak_start, '%H:%M')
        peak_end_time = datetime.strptime(peak_end, '%H:%M')
        return peak_start_time <= given_time < peak_end_time


    def charger_configuration(self, charger_config):
        config = int(charger_config)
        if config == 1:
            Calculator.power = 2
            Calculator.price = 5
        elif config == 2:
            Calculator.power = 3.6
            Calculator.price = 7.5
        elif config == 3:
            Calculator.power = 7.2
            Calculator.price = 10
        elif config == 4:
            Calculator.power = 11
            Calculator.price = 12.5
        elif config == 5:
            Calculator.power = 22
            Calculator.price = 15
        elif config == 6:
            Calculator.power = 36
            Calculator.price = 20
        elif config == 7:
            Calculator.power = 90
            Calculator.price = 30
        else:
            Calculator.power = 350
            Calculator.price = 50

        return Calculator.power

    def get_solar_energy_duration(self, data, start_time, charging_duration):
        # data = Calculator.get_weather(self, date, postcode)

        sunset = data["sunset"]
        sunrise = data["sunrise"]
        # sunrise = "06:00:00"
        # sunset = "18:00:00"

        sunset_time = datetime.strptime(sunset, '%H:%M:%S')
        sunrise_time = datetime.strptime(sunrise, '%H:%M:%S')
        start_time = datetime.strptime(start_time, '%H:%M')

        # convert the charging session
        hours = int(float(charging_duration)) // 60

        # Get additional minutes with modulus
        minutes = int(float(charging_duration)) % 60

        # Create time as a string
        charging_session_str = "{}:{}".format(hours, minutes)
        charging_session_final = datetime.strptime(charging_session_str, '%H:%M')
        time_zero = datetime.strptime('00:00', '%H:%M')
        end_time = start_time - time_zero + charging_session_final
        duration = 0

        if start_time > sunset_time or end_time < sunrise_time:
            duration = 0
        # whole session in daylight
        elif sunrise_time < start_time < sunset_time and sunrise_time < end_time < sunset_time:
            duration = (charging_session_final.hour * 60) + charging_session_final.minute

            hour = start_time.hour
            minute = start_time.minute
            temp = [str(hour), str(minute)]
            str_start_time = ":".join(temp)
            Calculator.start_time = str_start_time
        #  start_time before sunrise but end_time before sunset
        elif start_time < sunrise_time and end_time < sunset_time:
            cal = end_time - timedelta(hours=sunrise_time.hour, minutes=sunrise_time.minute,
                                       seconds=sunrise_time.second)
            duration = (cal.hour * 60) + cal.minute
            hour = sunrise_time.hour
            minute = sunrise_time.minute
            temp = [str(hour), str(minute)]
            str_start_time = ":".join(temp)
            Calculator.start_time = str_start_time

        # start_time after sunrise but end_time after sunset
        elif start_time > sunrise_time and end_time > sunset_time:
            cal = sunset_time - timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
            duration = (cal.hour * 60) + cal.minute

            hour = start_time.hour
            minute = start_time.minute
            temp = [str(hour), str(minute)]
            str_start_time = ":".join(temp)
            Calculator.start_time = str_start_time

        Calculator.duration = duration
        return duration

    # to be acquired through API
    def get_day_light_length(self, data):

        sunset = data["sunset"]
        sunrise = data["sunrise"]

        sunset_time = datetime.strptime(sunset, '%H:%M:%S')
        sunrise_time = datetime.strptime(sunrise, '%H:%M:%S')
        daylight_len = sunset_time - sunrise_time
        str_day_len = str(daylight_len)
        temp = str_day_len.split(":")
        minutes = int(temp[1])/60
        dl = int(temp[0]) + minutes
        format_dl = "{:.4f}".format(dl)
        return format_dl

    # to be acquired through API
    def get_solar_insolation(self, data):
        """ same sun hour on the same day"""
        # data = Calculator.get_weather(self, date)
        solar_insolation = data["sunHours"]
        return solar_insolation

    # to be acquired through API
    def get_cloud_cover(self, data, start_time):
        """ need to retrieve hourly cloud value"""
        cloud_cover = data["hourlyWeatherHistory"][int(start_time)]["cloudCoverPct"]
        return cloud_cover

    def calculate_solar_energy_alg1(self, date, postcode, start_time, charging_duration):
        total = 0
        final_total = []
        data = Calculator.get_weather(self, date, postcode)
        si = Calculator.get_solar_insolation(self, data)
        dl = Calculator.get_day_light_length(self, data)
        Calculator.get_solar_energy_duration(self, data, start_time, charging_duration)
        du = Calculator.get_du(self)
        for i in range(len(du)):
            total = float(si) * du[i] / float(dl) * 50 * 0.2
            final_total.append("{:.4f}".format(total))
        return final_total, du

    def get_du(self):
        du = []
        duration = Calculator.duration
        start_time = Calculator.start_time
        remaining_time = duration
        start_time = datetime.strptime(start_time, '%H:%M')
        while remaining_time > 0:
            hours = 1
            hours_added = timedelta(hours=hours)
            temp = start_time + hours_added
            next_hr = temp.hour
            next_hr_min = "00"
            temp2 = [str(next_hr), next_hr_min]
            next_hr_str = ":".join(temp2)
            next_hour = datetime.strptime(next_hr_str, '%H:%M')
            time_to_next_hour = abs(next_hour - start_time).total_seconds() / 60.0

            dur = min(time_to_next_hour, remaining_time)
            duration = dur / 60
            remaining_time = remaining_time - dur
            start_time = next_hour
            du.append(duration)

        return du

    def calculate_solar_energy_alg2(self, date, postcode, start_time, charging_duration):
        total = 0
        final_total = []
        # formatted_date = Calculator.format_date(self, date)
        # ref_date = Calculator.check_date(self, formatted_date)
        data = Calculator.get_weather(self, date, postcode)
        si = Calculator.get_solar_insolation(self, data)
        dl = Calculator.get_day_light_length(self, data)
        Calculator.get_solar_energy_duration(self, data, start_time, charging_duration)
        du = Calculator.get_du(self)

        for i in range(len(du)):
            temp = start_time.split(":")
            hr_num = int(temp[0]) + i
            cc = Calculator.get_cloud_cover(self, data, str(hr_num))
            total = float(si) * du[i] / float(dl) * (1-cc/100) * 50 * 0.2
            final_total.append("{:.4f}".format(total))

        return final_total, du

    def cum_calculate_solar_energy_alg2(self, date, postcode, start_time, charging_duration):
        total = []
        date = Calculator.format_date(self, date)

        for i in range(3):
            ref_date = Calculator.check_date(self, date)
            temp = ref_date.split("-")
            year = int(temp[0]) - i
            temp.insert(0, str(year))
            temp.pop(1)
            ref_date2 = "-".join(temp)
            energy = Calculator.calculate_solar_energy_alg2(self, ref_date2, postcode, start_time, charging_duration)
            total.append(energy)

        return total

    def get_weather(self, date, postcode):
        """get information from weather api  through the postcode """
        url = 'http://118.138.246.158/api/v1/location?postcode={postcode}'.format(postcode=postcode)
        temp = requests.get(url)
        data = temp.json()
        location = data[0]["id"]
        ref_date = Calculator.check_date(self, date)
        weather_url = 'http://118.138.246.158/api/v1/weather?location={ID}&date={date}'.format(ID=location, date=ref_date)

        weather = requests.get(weather_url)
        data = weather.json()
        return data

    def check_date(self, date):
        """ check for reference date"""
        current_date = datetime.today().strftime('%Y-%m-%d')
        current = current_date.split("-")
        current_year = int(current[0])
        input = date.split("-")
        input_year = int(input[0])
        if input_year > current_year:
            input.pop(0)
            input.insert(0, str(current_year))

        # check for future month
        if int(input[2]) > current_year:
            current_month = int(current[1])
            input_month = int(input[1])
            if input_month > current_month:
                input.pop(1)
                input.insert(1, str(current_month))

        # check if the day valid for that new month
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if int(input[2]) > days[int(input[1])]:
            year = int(input[0])
            # leap year condition
            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                if int(input[1]) == 2:
                    input.insert(0, "29")
            else:
                input.insert(0, str(days[int(input[1])]))
                input.pop(1)
        date_time_obj = datetime(int(input[0]), int(input[1]), int(input[2]))
        final_time = date_time_obj.strftime("%Y-%m-%d")
        return final_time

    def format_date(self, date):
        temp = date.split("/")
        temp.reverse()
        final_date = "-".join(temp)
        return final_date

if __name__ == "__main__":
    # date = "25/12/2020"
    # postcode = "6001"
    # time = "08:00"
    # charging_duration = "60"
    #
    # res = Calculator.calculate_solar_energy_alg1(self, date, postcode, time, charging_duration)
    # print(res)
    initial_state = "10"
    final_state = "20"
    capacity = "100"
    power = "50"
    date = "22/02/2022"
    postcode = "7250"
    time = "17:30"
    charging_duration = "45"
    charger_config = "3"
    # res = Calculator.cum_calculate_solar_energy_alg2(self, date, postcode, time, charging_duration)
    res = Calculator.cost_calculation_alg1_asg2(self, date, postcode, time, charging_duration, charger_config, initial_state, final_state)
    print(res)

