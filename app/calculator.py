import requests
from decimal import Decimal
import self as self
from flask import Flask, flash
from flask import render_template
from flask import request
from datetime import datetime


class Calculator:
    # you can choose to initialise variables here, if needed.
    def __init__(self):
        pass

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state, final_state, capacity, is_peak, is_holiday):
        if is_peak:
            base_price = 100
        else:
            base_price = 50

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1
        # initial_state = Decimal(initial_state)
        # final_state = Decimal(final_state)
        # capacity = Decimal(capacity)

        cost = (final_state - initial_state) / 100 * capacity * base_price / 100 * surcharge_factor
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, power):
        time = (final_state - initial_state) / 100 * capacity / power
        return time

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def is_holiday(self, start_date):
        pass

    def is_peak(self):
        pass

    def peak_period(self, start_time):
        pass

    def get_duration(self, start_time):
        pass

    # to be acquired through API
    def get_sun_hour(self, sun_hour):
        # si solar insolation (sun hour)
        pass

    # to be acquired through API
    def get_solar_energy_duration(self, start_time):
        pass

    # to be acquired through API
    # def get_day_light_length(self, start_time):
    def get_day_light_length(self):

        data = Calculator.get_weather(self)

        sunset = data["sunset"]
        sunrise = data["sunrise"]

        sunset_time = datetime.strptime(sunset,  '%H:%M:%S')
        sunrise_time = datetime.strptime(sunrise, '%H:%M:%S')
        # dl = sunset - sunrise
        daylight_len = sunset_time - sunrise_time
        str_day_len = str(daylight_len)
        temp = str_day_len.split(":")
        minutes = int(temp[1])/60
        total = int(temp[0]) + minutes
        return total

    # to be acquired through API
    def get_solar_insolation(self):
        # url = "http://118.138.246.158/api/v1/weather?location={location}&date={date}".format(location=location, date=date)
        # temp = requests.get(url)
        temp = requests.get("http://118.138.246.158/api/v1/weather?location=ab9f494f-f8a0-4c24-bd2e-2497b99f2258&date=2021-08-01")
        data = temp.json()
        # print(data)
        solar_insolation = data["sunHours"]
        return solar_insolation

    # to be acquired through API
    def get_cloud_cover(self):
        # need start time
        # input 10:00
        # start_time = "10:00"
        start_time = request.form['StartTime']
        time = start_time.split(":")
        data = Calculator.get_weather(self)
        cloud_cover = data["hourlyWeatherHistory"][int(time[0])]["cloudCoverPct"]
        print(cloud_cover)

    def calculate_solar_energy(self):
        # si*du/dl*50*0.20 for the amount of days
        pass

    def get_weather(self):
        # url = 'http://118.138.246.158/api/v1/location?'
        # postcode1 = request.form['PostCode']
        # params = {"postcode": postcode1}
        # res = requests.get(url, params=params)
        # return res
        res = requests.get("http://118.138.246.158/api/v1/location?postcode=3800")
        data = res.json()
        a = data[0]["id"]
        # print(data)
        # print(a)

        # Calculator.check_date(self)
        b = "2021-09-12"
        weather_url = 'http://118.138.246.158/api/v1/weather?location={ID}&date={date}'.format(ID=a, date=b)

        weather = requests.get(weather_url)
        data = weather.json()
        return data

    def check_date(self):
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
    res = Calculator()
    get = Calculator.get_day_light_length(self)
    print(get)
    # data = "3800"
    # res = Calculator.getApi(self)
    # print(res)
    # date = "20/9/2010"
    # res = Calculator.check_date(self, date)
    # print(res)


