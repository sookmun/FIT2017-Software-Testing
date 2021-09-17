import requests
from decimal import Decimal
from flask import Flask, flash
from flask import render_template
from flask import request
from datetime import datetime, timedelta
from self import self
import holidays
import datetime


class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self):
        self.peak_start = datetime.time(6, 0, 0)
        self.peak_end = datetime.time(18, 0, 0)


    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state, final_state, capacity, is_peak, is_holiday,start_date,start_time):
        if is_peak(start_time):
            base_price = 100
        else:
            base_price = 50

        if is_holiday(start_date):
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = (final_state - initial_state) / 100 * capacity * base_price / 100 * surcharge_factor
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, power):
        time = (final_state - initial_state) / 100 * capacity / power
        return time


    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def is_holiday(self, start_date):
        aus_holidays = holidays.AUS()
        if start_date in aus_holidays:
            return True
        return False

    def is_peak(self, start_time):
        current = start_time.split(':')
        current = datetime.datetime(int(current[0]), int(current[1]), 0)
        return self.peak_start <= current <= self.peak_end


    def peak_period(self, start_time,time):
        pass

    # def get_duration(self, start_time, charging_duration):
    def find_endtime(self):
        start_str = "10:00"
        charging_duration = "30"

        # convert the charging session
        hours = int(charging_duration) // 60

        # Get additional minutes with modulus
        minutes = int(charging_duration) % 60

        # Create time as a string
        start_time = datetime.strptime(start_str, '%H:%M')
        charging_session_str = "{}:{}".format(hours, minutes)
        charging_session_final = datetime.strptime(charging_session_str, '%H:%M')
        time_zero = datetime.strptime('00:00', '%H:%M')
        end_time = start_time - time_zero + charging_session_final
        print(end_time)
        hr1 = start_time.hour
        hr2 = end_time.hour
        Calculator.left = Calculator.left + hr2 - hr1
        return Calculator.left

    # to be acquired through API
    def get_sun_hour(self, sun_hour):
        pass

    # to be acquired through API
    # def get_solar_energy_duration(self, start_time):
    def get_solar_energy_duration(self):
        # assume charging session from 5am -  8am
        # start time 5am til 8am
        start_time = "16:00"
        charging_session = "180"
        data = Calculator.get_weather(self)
        # sunset = data["sunset"]
        # sunrise = data["sunrise"]
        sunrise = "7:30"
        sunset = "18:00"
        sunset_time = datetime.strptime(sunset, '%H:%M')
        sunrise_time = datetime.strptime(sunrise, '%H:%M')
        start_time = datetime.strptime(start_time, '%H:%M')

        # convert the charging session
        hours = int(charging_session) // 60

        # Get additional minutes with modulus
        minutes = int(charging_session) % 60

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

        return str(duration)

    # to be acquired through API
    # def get_day_light_length(self, start_time):
    def get_day_light_length(self):

        # data = Calculator.get_weather(self)
        # sunset = data["sunset"]
        # sunrise = data["sunrise"]
        sunrise = "05:44"
        sunset = "19:05"

        sunset_time = datetime.strptime(sunset, '%H:%M')
        sunrise_time = datetime.strptime(sunrise, '%H:%M')
        # dl = sunset - sunrise
        daylight_len = sunset_time - sunrise_time
        str_day_len = str(daylight_len)
        temp = str_day_len.split(":")
        minutes = int(temp[1])/60
        total = int(temp[0]) + minutes
        return total

    # to be acquired through API
    def get_solar_insolation(self):
        """ same sun hour on the same day"""
        data = Calculator.get_weather(self)
        solar_insolation = data["sunHours"]
        return solar_insolation

    # to be acquired through API
    # def get_cloud_cover(self):
    def get_cloud_cover(self, start_time):
        """ need to retrieve hourly cloud value"""
        # need start time
        # input 10:00
        # start_time = "10:00"
        # start_time = request.form['StartTime']
        time = start_time.split(":")
        data = Calculator.get_weather(self)
        cloud_cover = data["hourlyWeatherHistory"][int(time[0])]["cloudCoverPct"]
        return cloud_cover

    def calculate_solar_energy(self):
        # hourly solar energy
        # AG1: si*du/dl*50*0.20 for the amount of days
        # ALG2 :si*1/dl*(1-cc/100)*50*0.20

        si = Calculator.get_solar_insolation(self)
        dl = Calculator.get_day_light_length(self)
        total = 0

        for i in range(Calculator.left):
            start_time = "10:00"
            temp = start_time.split(":")
            hr_num = int(temp[0]) + i
            cc = Calculator.get_cloud_cover(self, str(hr_num))
            cal = (si*1) / dl * (1 - cc / 100) * 50 * 0.20
            total += cal
        return total



    def get_weather(self):
        """get information from weather api  through the postcode """
        # url = 'http://118.138.246.158/api/v1/location?'
        # postcode1 = request.form['PostCode']
        # params = {"postcode": postcode1}
        # res = requests.get(url, params=params)
        # return res
        temp = requests.get("http://118.138.246.158/api/v1/location?postcode=3800")
        data = temp.json()
        a = data[0]["id"]

        # Calculator.check_date(self)
        b = "2021-09-12"
        weather_url = 'http://118.138.246.158/api/v1/weather?location={ID}&date={date}'.format(ID=a, date=b)

        weather = requests.get(weather_url)
        data = weather.json()
        return data

    def check_date(self):
        """ check for reference date"""
        # date = request.form['StartDate']
        # input: DD/MM/YYYY
        date = "2021-09-12"
        current_date = datetime.today().strftime('%d/%m/%Y')
        current = current_date.split("/")
        current_year = int(current[2])

        input = date.split("/")
        input_year = int(input[2])
        # check for future year
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

        input.reverse()
        final_date = "-".join(input)
        return final_date


if __name__ == "__main__":
    time = "10:00"
    get = Calculator.calculate_solar_energy(self)
    print(get)



