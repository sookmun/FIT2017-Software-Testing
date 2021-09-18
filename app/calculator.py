import requests
from decimal import Decimal
from flask import Flask, flash
from flask import render_template
from flask import request
from datetime import datetime, timedelta
from self import self
import holidays


class Calculator():
    # you can choose to initialise variables here, if needed.
    period = 1
    power = 0
    price = 0

    def __init__(self):
        pass


    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, alg, initial_state, final_state, capacity, start_date, start_time, charging_duration, postcode, charger_config):
        Calculator.charger_configuration(self, charger_config)
        if Calculator.is_peak(self, start_time):
            Calculator.price = Calculator.price * 2

        if Calculator.is_holiday(self, start_date):
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        charging_cost = Calculator.calculate_charging_cost(self, alg, start_date, start_time, charging_duration, postcode)
        cost = (float(final_state) - float(initial_state)) / 100 * float(capacity) * float(charging_cost) / 100 * surcharge_factor
        return "{:.2f}".format(cost)

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, power):
        time = ((float(final_state) - float(initial_state)) / 100 * int(capacity) / float(power)) * 60
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
        peak_start_time = datetime.strptime(peak_start, '%H:%M')
        peak_end_time = datetime.strptime(peak_end, '%H:%M')
        current = datetime.strptime(start_time, "%H:%M")

        return peak_start_time <= current <= peak_end_time

    def charger_configuration(self, num_str):
        num = int(num_str)
        if num == 1:
            Calculator.power = 2
            Calculator.price = 5
        elif num == 2:
            Calculator.power = 3.6
            Calculator.price = 7.5
        elif num == 3:
            Calculator.power = 7.2
            Calculator.price = 10
        elif num == 4:
            Calculator.power = 11
            Calculator.price = 12.5
        elif num == 5:
            Calculator.power = 22
            Calculator.price = 15
        elif num == 6:
            Calculator.power = 36
            Calculator.price = 20
        elif num == 7:
            Calculator.power = 90
            Calculator.price = 30
        else:
            Calculator.power = 350
            Calculator.price = 50

        return Calculator.power

    def peak_period(self, start_time,time):
        pass

    def get_duration(self, start_time, charging_duration):
        # convert the charging session
        hours = int(float(charging_duration)) // 60

        # Get additional minutes with modulus
        minutes = int(float(charging_duration)) % 60

        # Create time as a string
        start_time = datetime.strptime(start_time, '%H:%M')
        charging_session_str = "{}:{}".format(hours, minutes)
        charging_session_final = datetime.strptime(charging_session_str, '%H:%M')
        time_zero = datetime.strptime('00:00', '%H:%M')
        end_time = start_time - time_zero + charging_session_final
        hr1 = start_time.hour
        hr2 = end_time.hour
        Calculator.period = Calculator.period + hr2 - hr1

    # to be acquired through API
    def get_solar_energy_duration(self, data, start_time, charging_session):
    # def get_solar_energy_duration(self, start_time, charging_session):

        sunset = data["sunset"]
        sunrise = data["sunrise"]
        # sunrise = "06:00:00"
        # sunset = "18:00:00"

        sunset_time = datetime.strptime(sunset, '%H:%M:%S')
        sunrise_time = datetime.strptime(sunrise, '%H:%M:%S')
        start_time = datetime.strptime(start_time, '%H:%M')

        # convert the charging session
        hours = int(float(charging_session)) // 60

        # Get additional minutes with modulus
        minutes = int(float(charging_session)) % 60

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
        #  start_time before sunrise but end_time before sunset
        elif start_time < sunrise_time and end_time < sunset_time:
            cal = end_time - timedelta(hours=sunrise_time.hour, minutes=sunrise_time.minute, seconds=sunrise_time.second)
            duration = (cal.hour * 60) + cal.minute
        # start_time after sunrise but end_time after sunset
        elif start_time > sunrise_time and end_time > sunset_time:
            cal = sunset_time - timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
            duration = (cal.hour * 60) + cal.minute

        return duration

    # to be acquired through API
    # def get_day_light_length(self, start_time):
    def get_day_light_length(self, data):

        sunset = data["sunset"]
        sunrise = data["sunrise"]

        sunset_time = datetime.strptime(sunset, '%H:%M:%S')
        sunrise_time = datetime.strptime(sunrise, '%H:%M:%S')
        daylight_len = sunset_time - sunrise_time
        str_day_len = str(daylight_len)
        temp = str_day_len.split(":")
        minutes = int(temp[1])/60
        total = int(temp[0]) + minutes
        return total

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

    def calculate_solar_energy_alg2(self, data, start_time, charging_duration):
        si = Calculator.get_solar_insolation(self, data)
        dl = Calculator.get_day_light_length(self, data)
        total = 0
        Calculator.get_duration(self, start_time, charging_duration)

        for i in range(Calculator.period):
            temp = start_time.split(":")
            hr_num = int(temp[0]) + i
            cc = Calculator.get_cloud_cover(self, data, str(hr_num))
            cal = (si*1) / dl * (1 - cc / 100) * 50 * 0.20
            total += cal

        return total

    def calculate_solar_energy_alg1(self, date, start_time, charging_duration, postcode):
        date = Calculator.format_date(self, date)
        data = Calculator.get_weather(self, date, postcode)
        si = Calculator.get_solar_insolation(self, data)
        dl = Calculator.get_day_light_length(self, data)
        du = Calculator.get_solar_energy_duration(self, data, start_time, charging_duration)
        res = si * du / dl * 50 * 0.20
        ans = "{:.2f}".format(res)
        return ans

    def cum_calculate_solar_energy(self, date, start_time, charging_duration, postcode):
        total = 0
        date = Calculator.format_date(self, date)

        for i in range(3):
            temp = date.split("-")
            year = int(temp[0]) - i
            temp.insert(0, str(year))
            temp.pop(1)
            ref_date = "-".join(temp)
            data = Calculator.get_weather(self, ref_date, postcode)
            total += Calculator.calculate_solar_energy_alg2(self, data, start_time, charging_duration)

        average = total / 3
        average_str = "{:.2f}".format(average)
        return average_str

    def calculate_charging_cost(self, alg, date, start_time, charging_duration, postcode):
        charging_cost = 0
        energy = 0

        if alg == 1:
            energy = Calculator.calculate_solar_energy_alg1(self, date, start_time, charging_duration, postcode)
        elif alg == 2:
            energy = Calculator.cum_calculate_solar_energy(self, date, start_time, charging_duration, postcode)

        # Calculator.charger_configuration(self, charger_config)
        solar_energy = float(energy)

        if solar_energy >= Calculator.power:
            charging_cost = 0
        else:
            charging_cost = (Calculator.power - solar_energy) * Calculator.price

        final_charging_cost = "{:.2f}".format(charging_cost)
        return final_charging_cost


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
        current_year = int(current[2])
        input = date.split("-")
        input_year = int(input[2])
        if input_year > current_year:
            input.pop(2)
            input.append(str(current_year))

        # check for future month
        if int(input[2]) > current_year:
            current_month = int(current[1])
            input_month = int(input[1])
            if input_month > current_month:
                input.pop(1)
                input.insert(1, str(current_month))

        # check if the day valid for that new month
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if int(input[0]) > days[int(input[1])]:
            year = int(input[2])
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
        final = "-".join(temp)
        return final


if __name__ == "__main__":
    dat = "12/9/2021"
    time = "17:00"

    # res = Calculator.get_solar_energy_duration(self,"10:00", "8.43")
    # print(res)
    # new_date = Calculator.format_date(self, dat)
    # # info = Calculator.get_weather(self, new_date, "3800")
    # # get = Calculator.get_solar_insolation(self, info)
    # # res = Calculator.cum_calculate_solar_energy(self, dat, time, "180", "3800")
    # # res2 = Calculator.calculate_solar_energy_alg1(self, dat, time, 8, "3800")
    # # res = Calculator.charger_configuration(self, "2")
    # res = Calculator.calculate_charging_cost(self, 2,  dat, time, "30", "3800", "7")
    # print(res)
    # print(res)



