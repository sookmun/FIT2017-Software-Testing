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

    def get_duration(self, start_time):
        pass

    # to be acquired through API
    def get_sun_hour(self, sun_hour):
        pass

    # to be acquired through API
    def get_solar_energy_duration(self, start_time):
        pass

    # to be acquired through API
    def get_day_light_length(self, start_time):
        pass

    # to be acquired through API
    def get_solar_insolation(self, solar_insolation):
        pass

    # to be acquired through API
    def get_cloud_cover(self):
        pass

    def calculate_solar_energy(self):
        pass
