import unittest
from app.calculator import Calculator
from datetime import datetime
from unittest.mock import patch

"""
This file is used to perform unit testing on the Calculator class 
"""
class TestCalculator(unittest.TestCase):
    """
    This test class test all the functions in calculator.py
    """

    def test_cost_calculation(self):
        """
        Tests the cost_calculation method in the Calculator class
        """
        cal = Calculator()
        self.assertEqual(cal.cost_calculation("25/12/2020", "08:00", "10", "30", "350", "3"), "14.00")
        self.assertEqual(cal.cost_calculation("22/02/2022", "17:30", "15", "20", "100", "2"), "0.75")
        self.assertEqual(cal.cost_calculation("22/02/2022", "05:00", "15", "20", "100", "2"), "0.38")

    def test_cost_cal_without_hourly_weather(self):
        """
        Tests the cost_cal_without_hourly_weather method in the Calculator class
        """
        postcode_data = [
            {"id": "5bea7b46-9809-4189-aafe-160208da94f7", "postcode": "6001", "name": "PERTH", "state": "WA",
             "latitude": "-31.9505269", "longitude": "115.8604572",
             "distanceToNearestWeatherStationMetres": 3672.959393589811,
             "nearestWeatherStation": {"name": "PERTH METRO", "state": "WA", "latitude": "-31.9192",
                                       "longitude": "115.8728"}}]

        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = postcode_data

            cal = Calculator()
            response = cal.get_link_weather("6001")

        mock_get.assert_called()

        weather_data = {"date": "2020-12-25", "sunrise": "05:10:00", "sunset": "19:24:00", "moonrise": "15:04:00",
                        "moonset": "01:48:00", "moonPhase": "Waxing Gibbous", "moonIlluminationPct": 70, "minTempC": 27,
                        "maxTempC": 36, "avgTempC": 33, "sunHours": 8.6, "uvIndex": 8,
                        "location": {"id": "5bea7b46-9809-4189-aafe-160208da94f7", "postcode": "6001", "name": "PERTH",
                                     "state": "WA",
                                     "latitude": "-31.9505269", "longitude": "115.8604572",
                                     "distanceToNearestWeatherStationMetres": 3672.959393589811,
                                     "nearestWeatherStation": {"name": "PERTH METRO", "state": "WA",
                                                               "latitude": "-31.9192",
                                                               "longitude": "115.8728"}}, "hourlyWeatherHistory": [
                {"hour": 0, "tempC": 29, "weatherDesc": "Partly cloudy", "cloudCoverPct": 1, "uvIndex": 1,
                 "windspeedKph": 4, "windDirectionDeg": 122, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 1, "tempC": 29, "weatherDesc": "Partly cloudy", "cloudCoverPct": 1, "uvIndex": 1,
                 "windspeedKph": 4, "windDirectionDeg": 122, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 2, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 2, "uvIndex": 1,
                 "windspeedKph": 4, "windDirectionDeg": 123, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 3, "tempC": 27, "weatherDesc": "Partly cloudy", "cloudCoverPct": 2, "uvIndex": 1,
                 "windspeedKph": 4, "windDirectionDeg": 123, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 4, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 3, "uvIndex": 1,
                 "windspeedKph": 4, "windDirectionDeg": 152, "windDirectionCompass": "SSE", "precipitationMm": 0,
                 "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 5, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 4, "uvIndex": 1,
                 "windspeedKph": 4, "windDirectionDeg": 182, "windDirectionCompass": "S", "precipitationMm": 0,
                 "humidityPct": 22, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 6, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 5, "uvIndex": 7,
                 "windspeedKph": 3, "windDirectionDeg": 211, "windDirectionCompass": "SSW", "precipitationMm": 0,
                 "humidityPct": 22, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 7, "tempC": 30, "weatherDesc": "Partly cloudy", "cloudCoverPct": 8, "uvIndex": 7,
                 "windspeedKph": 4, "windDirectionDeg": 248, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 21, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 8, "tempC": 31, "weatherDesc": "Partly cloudy", "cloudCoverPct": 11, "uvIndex": 8,
                 "windspeedKph": 5, "windDirectionDeg": 286, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 19, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 9, "tempC": 32, "weatherDesc": "Partly cloudy", "cloudCoverPct": 13, "uvIndex": 8,
                 "windspeedKph": 5, "windDirectionDeg": 324, "windDirectionCompass": "NW", "precipitationMm": 0,
                 "humidityPct": 18, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 10, "tempC": 33, "weatherDesc": "Partly cloudy", "cloudCoverPct": 13, "uvIndex": 8,
                 "windspeedKph": 8, "windDirectionDeg": 300, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 17, "visibilityKm": 10, "pressureMb": 1009},
                {"hour": 11, "tempC": 35, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 8,
                 "windspeedKph": 11, "windDirectionDeg": 276, "windDirectionCompass": "W", "precipitationMm": 0,
                 "humidityPct": 16, "visibilityKm": 10, "pressureMb": 1008},
                {"hour": 12, "tempC": 36, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 9,
                 "windspeedKph": 14, "windDirectionDeg": 252, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 16, "visibilityKm": 10, "pressureMb": 1008},
                {"hour": 13, "tempC": 36, "weatherDesc": "Partly cloudy", "cloudCoverPct": 21, "uvIndex": 9,
                 "windspeedKph": 17, "windDirectionDeg": 242, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 17, "visibilityKm": 10, "pressureMb": 1007},
                {"hour": 14, "tempC": 35, "weatherDesc": "Cloudy", "cloudCoverPct": 28, "uvIndex": 8,
                 "windspeedKph": 19,
                 "windDirectionDeg": 232, "windDirectionCompass": "SW", "precipitationMm": 0, "humidityPct": 19,
                 "visibilityKm": 10, "pressureMb": 1007},
                {"hour": 15, "tempC": 35, "weatherDesc": "Cloudy", "cloudCoverPct": 35, "uvIndex": 8,
                 "windspeedKph": 22,
                 "windDirectionDeg": 223, "windDirectionCompass": "SW", "precipitationMm": 0, "humidityPct": 21,
                 "visibilityKm": 10, "pressureMb": 1006},
                {"hour": 16, "tempC": 34, "weatherDesc": "Cloudy", "cloudCoverPct": 42, "uvIndex": 7,
                 "windspeedKph": 21,
                 "windDirectionDeg": 217, "windDirectionCompass": "SW", "precipitationMm": 0, "humidityPct": 24,
                 "visibilityKm": 10, "pressureMb": 1006},
                {"hour": 17, "tempC": 33, "weatherDesc": "Partly cloudy", "cloudCoverPct": 48, "uvIndex": 8,
                 "windspeedKph": 20, "windDirectionDeg": 212, "windDirectionCompass": "SSW", "precipitationMm": 0,
                 "humidityPct": 27, "visibilityKm": 10, "pressureMb": 1006},
                {"hour": 18, "tempC": 32, "weatherDesc": "Partly cloudy", "cloudCoverPct": 54, "uvIndex": 1,
                 "windspeedKph": 19, "windDirectionDeg": 207, "windDirectionCompass": "SSW", "precipitationMm": 0,
                 "humidityPct": 30, "visibilityKm": 10, "pressureMb": 1006},
                {"hour": 19, "tempC": 31, "weatherDesc": "Partly cloudy", "cloudCoverPct": 42, "uvIndex": 1,
                 "windspeedKph": 18, "windDirectionDeg": 196, "windDirectionCompass": "SSW", "precipitationMm": 0,
                 "humidityPct": 34, "visibilityKm": 10, "pressureMb": 1007},
                {"hour": 20, "tempC": 30, "weatherDesc": "Partly cloudy", "cloudCoverPct": 30, "uvIndex": 1,
                 "windspeedKph": 17, "windDirectionDeg": 186, "windDirectionCompass": "S", "precipitationMm": 0,
                 "humidityPct": 37, "visibilityKm": 10, "pressureMb": 1007},
                {"hour": 21, "tempC": 29, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 1,
                 "windspeedKph": 16, "windDirectionDeg": 175, "windDirectionCompass": "S", "precipitationMm": 0,
                 "humidityPct": 40, "visibilityKm": 10, "pressureMb": 1008},
                {"hour": 22, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 28, "uvIndex": 1,
                 "windspeedKph": 16, "windDirectionDeg": 159, "windDirectionCompass": "SSE", "precipitationMm": 0,
                 "humidityPct": 42, "visibilityKm": 10, "pressureMb": 1008},
                {"hour": 23, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 39, "uvIndex": 1,
                 "windspeedKph": 16, "windDirectionDeg": 142, "windDirectionCompass": "SE", "precipitationMm": 0,
                 "humidityPct": 44, "visibilityKm": 10, "pressureMb": 1008}]}
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = weather_data

            cal = Calculator()
            response = cal.get_weather(postcode_data, "2020-12-25", "PERTH")

        mock_get.assert_called()
        self.assertEqual(cal.cost_cal_without_hourly_weather("25/12/2020", "6001", "08:00", "90", "3", "45", "60", "Perth"), "0.34")

    def test_cost_cal_with_hourly_weather(self):
        """
        Tests the cost_cal_with_hourly_weather method in the Calculator class
        """
        postcode_data = [
            {"id": "22d72902-b72f-4ca0-a522-4dbfb77a7b78", "postcode": "7250", "name": "BLACKSTONE HEIGHTS",
             "state": "TAS", "latitude": "-41.46", "longitude": "147.0820001",
             "distanceToNearestWeatherStationMetres": 5607.391317385195,
             "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                       "longitude": "147.1219"}},
            {"id": "6d91c048-7178-4330-b792-30e53a702396", "postcode": "7250", "name": "EAST LAUNCESTON",
             "state": "TAS",
             "latitude": "-41.441944", "longitude": "147.150833",
             "distanceToNearestWeatherStationMetres": 1692.1148509532288,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "15b4a861-e97a-43fa-a0da-9953106b5554", "postcode": "7250", "name": "ELPHIN", "state": "TAS",
             "latitude": "-41.4309", "longitude": "147.155",
             "distanceToNearestWeatherStationMetres": 1608.3052577708138,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "5998b29a-8e3d-4c1e-857c-b5dce80eea6d", "postcode": "7250", "name": "LAUNCESTON", "state": "TAS",
             "latitude": "-41.4332215", "longitude": "147.1440875",
             "distanceToNearestWeatherStationMetres": 2323.920987503416,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "c9ba20ed-01b6-418e-8a61-b5f9ac5c7fe3", "postcode": "7250", "name": "NEWSTEAD", "state": "TAS",
             "latitude": "-41.444444", "longitude": "147.160556",
             "distanceToNearestWeatherStationMetres": 1033.9903037447873,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "ed442b26-492d-45ed-a2e7-2828c7e06d95", "postcode": "7250", "name": "NORWOOD", "state": "TAS",
             "latitude": "-41.457222", "longitude": "147.1725",
             "distanceToNearestWeatherStationMetres": 1223.5586202650989,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "572c0906-0a82-4102-94d2-bccf2ca97a38", "postcode": "7250", "name": "NORWOOD AVENUE PO",
             "state": "TAS",
             "latitude": "-41.4557", "longitude": "147.173",
             "distanceToNearestWeatherStationMetres": 1388.9427115766343,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "ea44f0b3-72ff-439f-b42a-e486ad7be323", "postcode": "7250", "name": "PROSPECT", "state": "TAS",
             "latitude": "-41.483333", "longitude": "147.139722",
             "distanceToNearestWeatherStationMetres": 2787.874138903107,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "6b791b5f-7ab3-4103-a4cc-5e860e935e0f", "postcode": "7250", "name": "PROSPECT VALE", "state": "TAS",
             "latitude": "-41.481", "longitude": "147.126", "distanceToNearestWeatherStationMetres": 3587.589454353829,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "4507ab34-3a2f-4610-8b9d-fcfdfecdca09", "postcode": "7250", "name": "RAVENSWOOD", "state": "TAS",
             "latitude": "-41.418333", "longitude": "147.176111",
             "distanceToNearestWeatherStationMetres": 2362.1755102588863,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "b4242da1-ff68-4ff9-88b6-59ea8baf1324", "postcode": "7250", "name": "RIVERSIDE", "state": "TAS",
             "latitude": "-41.42", "longitude": "147.103", "distanceToNearestWeatherStationMetres": 1577.355141403387,
             "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                       "longitude": "147.1219"}},
            {"id": "d52144b2-74f7-4fbc-9d5d-c8fd068da060", "postcode": "7250", "name": "ST LEONARDS", "state": "TAS",
             "latitude": "-41.4584", "longitude": "147.2008",
             "distanceToNearestWeatherStationMetres": 3160.908069109459,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "c3836b3d-8277-4cb4-9e9d-40adc7967a37", "postcode": "7250", "name": "SUMMERHILL", "state": "TAS",
             "latitude": "-41.4688362", "longitude": "147.1189067",
             "distanceToNearestWeatherStationMetres": 3800.246608736132,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "6bf11a0e-a46a-4dda-8991-92dcc5971c08", "postcode": "7250", "name": "TRAVELLERS REST",
             "state": "TAS",
             "latitude": "-41.494", "longitude": "147.09", "distanceToNearestWeatherStationMetres": 4032.586323471949,
             "nearestWeatherStation": {"name": "HADSPEN", "state": "TAS", "latitude": "-41.5157",
                                       "longitude": "147.0512"}},
            {"id": "d7d86087-771c-4754-92f6-cc4c31edc3d8", "postcode": "7250", "name": "TREVALLYN", "state": "TAS",
             "latitude": "-41.433333", "longitude": "147.116667",
             "distanceToNearestWeatherStationMetres": 1609.541131584532,
             "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                       "longitude": "147.1219"}},
            {"id": "8e688142-401c-4d48-a8a2-14721cb48a73", "postcode": "7250", "name": "WAVERLEY", "state": "TAS",
             "latitude": "-41.433333", "longitude": "147.183333",
             "distanceToNearestWeatherStationMetres": 1231.7292044665246,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "adb3614f-c464-4d9e-b731-ca4b5f5e9726", "postcode": "7250", "name": "WEST LAUNCESTON",
             "state": "TAS",
             "latitude": "-41.451", "longitude": "147.1292", "distanceToNearestWeatherStationMetres": 3396.576148167821,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}}]
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = postcode_data

            cal = Calculator()
            response = cal.get_link_weather("7250")

        mock_get.assert_called()
        weather_data = {"date": "2021-02-22", "sunrise": "05:44:00", "sunset": "19:06:00", "moonrise": "15:43:00",
                        "moonset": "00:01:00", "moonPhase": "Waxing Gibbous", "moonIlluminationPct": 73, "minTempC": 9,
                        "maxTempC": 21,
                        "avgTempC": 17, "sunHours": 5.8, "uvIndex": 5,
                        "location": {"id": "5998b29a-8e3d-4c1e-857c-b5dce80eea6d", "postcode": "7250",
                                     "name": "LAUNCESTON",
                                     "state": "TAS", "latitude": "-41.4332215", "longitude": "147.1440875",
                                     "distanceToNearestWeatherStationMetres": 2323.920987503416,
                                     "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)",
                                                               "state": "TAS",
                                                               "latitude": "-41.4392", "longitude": "147.1708"}},
                        "hourlyWeatherHistory": [
                            {"hour": 0, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 1, "uvIndex": 1,
                             "windspeedKph": 2, "windDirectionDeg": 232, "windDirectionCompass": "SW",
                             "precipitationMm": 0,
                             "humidityPct": 89, "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 19, "tempC": 15, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 1,
                             "windspeedKph": 11, "windDirectionDeg": 237, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 50, "visibilityKm": 10, "pressureMb": 1010},
                            {"hour": 20, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 11, "uvIndex": 1,
                             "windspeedKph": 9, "windDirectionDeg": 227, "windDirectionCompass": "SW",
                             "precipitationMm": 0,
                             "humidityPct": 55, "visibilityKm": 10, "pressureMb": 1011},
                            {"hour": 21, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 9, "uvIndex": 1,
                             "windspeedKph": 7, "windDirectionDeg": 217, "windDirectionCompass": "SW",
                             "precipitationMm": 0,
                             "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1012},
                            {"hour": 22, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 7, "uvIndex": 1,
                             "windspeedKph": 6, "windDirectionDeg": 212, "windDirectionCompass": "SSW",
                             "precipitationMm": 0,
                             "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1012},
                            {"hour": 23, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 5, "uvIndex": 1,
                             "windspeedKph": 4, "windDirectionDeg": 207, "windDirectionCompass": "SSW",
                             "precipitationMm": 0,
                             "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1012},
                            {"hour": 1, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 3, "uvIndex": 1,
                             "windspeedKph": 2, "windDirectionDeg": 258, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 91, "visibilityKm": 8, "pressureMb": 1007},
                            {"hour": 2, "tempC": 11, "weatherDesc": "Clear", "cloudCoverPct": 6, "uvIndex": 1,
                             "windspeedKph": 3,
                             "windDirectionDeg": 284, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 93,
                             "visibilityKm": 6, "pressureMb": 1006},
                            {"hour": 3, "tempC": 9, "weatherDesc": "Clear", "cloudCoverPct": 9, "uvIndex": 1,
                             "windspeedKph": 3,
                             "windDirectionDeg": 310, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 95,
                             "visibilityKm": 5, "pressureMb": 1006},
                            {"hour": 4, "tempC": 10, "weatherDesc": "Clear", "cloudCoverPct": 7, "uvIndex": 1,
                             "windspeedKph": 4,
                             "windDirectionDeg": 314, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 93,
                             "visibilityKm": 6, "pressureMb": 1006},
                            {"hour": 5, "tempC": 10, "weatherDesc": "Mist", "cloudCoverPct": 6, "uvIndex": 1,
                             "windspeedKph": 4,
                             "windDirectionDeg": 319, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 90,
                             "visibilityKm": 6, "pressureMb": 1006},
                            {"hour": 6, "tempC": 10, "weatherDesc": "Mist", "cloudCoverPct": 4, "uvIndex": 3,
                             "windspeedKph": 4,
                             "windDirectionDeg": 324, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 88,
                             "visibilityKm": 7, "pressureMb": 1007},
                            {"hour": 7, "tempC": 12, "weatherDesc": "Mist", "cloudCoverPct": 3, "uvIndex": 3,
                             "windspeedKph": 6,
                             "windDirectionDeg": 313, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 78,
                             "visibilityKm": 8, "pressureMb": 1007},
                            {"hour": 8, "tempC": 14, "weatherDesc": "Sunny", "cloudCoverPct": 1, "uvIndex": 4,
                             "windspeedKph": 7,
                             "windDirectionDeg": 303, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 68,
                             "visibilityKm": 9, "pressureMb": 1007},
                            {"hour": 9, "tempC": 16, "weatherDesc": "Sunny", "cloudCoverPct": 0, "uvIndex": 5,
                             "windspeedKph": 8,
                             "windDirectionDeg": 292, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 58,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 10, "tempC": 18, "weatherDesc": "Sunny", "cloudCoverPct": 6, "uvIndex": 5,
                             "windspeedKph": 10,
                             "windDirectionDeg": 286, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 52,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 11, "tempC": 19, "weatherDesc": "Sunny", "cloudCoverPct": 12, "uvIndex": 5,
                             "windspeedKph": 11,
                             "windDirectionDeg": 281, "windDirectionCompass": "W", "precipitationMm": 0,
                             "humidityPct": 45,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 12, "tempC": 21, "weatherDesc": "Sunny", "cloudCoverPct": 17, "uvIndex": 6,
                             "windspeedKph": 13,
                             "windDirectionDeg": 275, "windDirectionCompass": "W", "precipitationMm": 0,
                             "humidityPct": 39,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 13, "tempC": 20, "weatherDesc": "Sunny", "cloudCoverPct": 19, "uvIndex": 6,
                             "windspeedKph": 14,
                             "windDirectionDeg": 270, "windDirectionCompass": "W", "precipitationMm": 0,
                             "humidityPct": 38,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 14, "tempC": 20, "weatherDesc": "Partly cloudy", "cloudCoverPct": 20, "uvIndex": 5,
                             "windspeedKph": 15, "windDirectionDeg": 264, "windDirectionCompass": "W",
                             "precipitationMm": 0,
                             "humidityPct": 38, "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 15, "tempC": 20, "weatherDesc": "Partly cloudy", "cloudCoverPct": 22, "uvIndex": 5,
                             "windspeedKph": 16, "windDirectionDeg": 259, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 37, "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 16, "tempC": 18, "weatherDesc": "Partly cloudy", "cloudCoverPct": 20, "uvIndex": 5,
                             "windspeedKph": 15, "windDirectionDeg": 255, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 39, "visibilityKm": 10, "pressureMb": 1008},
                            {"hour": 17, "tempC": 17, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 5,
                             "windspeedKph": 14, "windDirectionDeg": 251, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 42, "visibilityKm": 10, "pressureMb": 1008},
                            {"hour": 18, "tempC": 16, "weatherDesc": "Partly cloudy", "cloudCoverPct": 16, "uvIndex": 1,
                             "windspeedKph": 13, "windDirectionDeg": 247, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 44, "visibilityKm": 10, "pressureMb": 1009}]}
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = weather_data

            response = cal.get_weather(postcode_data, "2020-12-25", "Launceston")

        mock_get.assert_called()

        self.assertEqual(cal.cost_cal_with_hourly_weather("2020-12-25", "7250", "17:30", "45", "5", "20", "75", "Launceston",), "19.95")

    def test_get_price(self):
        """
            Tests the get_price method in the Calculator class
        """
        cal1 = Calculator
        cal1.duration = 90
        cal1.start_time = "18:00"
        self.assertEqual(cal1.get_price(self), [0.5, 0.5])

        cal2 = Calculator
        cal2.duration = 45
        cal2.start_time = "05:30"
        self.assertEqual(cal2.get_price(self), [0.5, 1.0])

        cal3 = Calculator
        cal3.duration = 120
        cal3.start_time = "17:45"
        self.assertEqual(cal3.get_price(self), [1.0, 0.5, 0.5])

    def test_time_calculation(self):
        """
            Tests the time_calculation method in the Calculator class
        """
        cal = Calculator()
        self.assertEqual(cal.time_calculation("10", "20", "100", "22"), "{:.2f}".format(27.27))
        self.assertEqual(cal.time_calculation("50", "70", "300", "90"), "{:.2f}".format(40.00))
        self.assertEqual(cal.time_calculation("10", "90", "450", "350"), "{:.2f}".format(61.71))

    def test_is_holiday(self):
        """
            Tests the is_holiday method in the Calculator class
        """
        date = "1/1/2020"
        other_date = "3/5/2021"
        self.calculator = Calculator()
        self.assertTrue(self.calculator.is_holiday(date), "Day is not a holiday")
        self.assertFalse(self.calculator.is_holiday(other_date), "Day is a holiday")

    def test_is_peak(self):
        """
            Tests the is_holiday method in the Calculator class
        """
        time = "17:30"
        other_time = "05:00"
        time = datetime.strptime(time, "%H:%M")
        other_time = datetime.strptime(other_time, "%H:%M")
        self.calculator = Calculator()
        self.assertTrue(self.calculator.is_peak(time), "Time given is not within peak hours")
        self.assertFalse(self.calculator.is_peak(other_time), "Time given is not within peak hours")

    def test_get_charger_configuration(self):
        """
            Tests the get_charger_configuration method in the Calculator class
        """
        self.calculator = Calculator()
        self.assertEqual(2, self.calculator.get_charger_configuration(1), "Wrong power, 2 should be expected")
        self.assertEqual(3.6, self.calculator.get_charger_configuration(2), "Wrong power, 3.6 should be expected")
        self.assertEqual(7.2, self.calculator.get_charger_configuration(3), "Wrong power, 7.2 should be expected")
        self.assertEqual(11, self.calculator.get_charger_configuration(4), "Wrong power, 11 should be expected")
        self.assertEqual(22, self.calculator.get_charger_configuration(5), "Wrong power, 22 should be expected")
        self.assertEqual(36, self.calculator.get_charger_configuration(6), "Wrong power, 36 should be expected")
        self.assertEqual(90, self.calculator.get_charger_configuration(7), "Wrong power, 90 should be expected")
        self.assertEqual(350, self.calculator.get_charger_configuration(8), "Wrong power, 350 should be expected")
        self.assertEqual(350, self.calculator.get_charger_configuration(-1), "Negative Value will not be accepted")

    def test_get_solar_energy_duration(self):
        """
            Tests the get_solar_energy_duration method in the Calculator class
        """
        cal = Calculator()
        weather_data1 = {"date": "2021-08-01", "sunrise": "07:20:00", "sunset": "17:32:00", "moonrise": "00:52:00",
                         "moonset": "11:45:00", "moonPhase": "Last Quarter", "moonIlluminationPct": 40, "minTempC": 9,
                         "maxTempC": 14, "avgTempC": 11, "sunHours": 3.2, "uvIndex": 3,
                         "location": {"id": "ab9f494f-f8a0-4c24-bd2e-2497b99f2258", "postcode": "3800",
                                      "name": "MONASH UNIVERSITY", "state": "VIC", "latitude": "-37.9105599",
                                      "longitude": "145.1362485",
                                      "distanceToNearestWeatherStationMetres": 3771.993796218797,
                                      "nearestWeatherStation": {"name": "OAKLEIGH (METROPOLITAN GOLF CLUB)",
                                                                "state": "VIC", "latitude": "-37.9142",
                                                                "longitude": "145.0935"}}, "hourlyWeatherHistory": [
                {"hour": 0, "tempC": 10, "weatherDesc": "Heavy rain", "cloudCoverPct": 100, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 349, "windDirectionCompass": "N", "precipitationMm": 2.9,
                 "humidityPct": 90, "visibilityKm": 3, "pressureMb": 1007},
                {"hour": 1, "tempC": 10, "weatherDesc": "Heavy rain", "cloudCoverPct": 94, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 342, "windDirectionCompass": "NNW", "precipitationMm": 1.4,
                 "humidityPct": 90, "visibilityKm": 4, "pressureMb": 1008},
                {"hour": 2, "tempC": 10, "weatherDesc": "Light drizzle", "cloudCoverPct": 87, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 336, "windDirectionCompass": "NNW", "precipitationMm": 0.2,
                 "humidityPct": 90, "visibilityKm": 5, "pressureMb": 1008},
                {"hour": 3, "tempC": 10, "weatherDesc": "Light drizzle", "cloudCoverPct": 81, "uvIndex": 1,
                 "windspeedKph": 9, "windDirectionDeg": 329, "windDirectionCompass": "NNW", "precipitationMm": 0.3,
                 "humidityPct": 90, "visibilityKm": 7, "pressureMb": 1008},
                {"hour": 4, "tempC": 9, "weatherDesc": "Light drizzle", "cloudCoverPct": 79, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 325, "windDirectionCompass": "NW", "precipitationMm": 0.2,
                 "humidityPct": 90, "visibilityKm": 8, "pressureMb": 1009},
                {"hour": 5, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 78, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 321, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 91, "visibilityKm": 9, "pressureMb": 1009},
                {"hour": 6, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 76, "uvIndex": 2,
                 "windspeedKph": 10, "windDirectionDeg": 318, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 91, "visibilityKm": 10, "pressureMb": 1010},
                {"hour": 7, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 78, "uvIndex": 2,
                 "windspeedKph": 10, "windDirectionDeg": 312, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 88, "visibilityKm": 10, "pressureMb": 1010},
                {"hour": 8, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 80, "uvIndex": 2,
                 "windspeedKph": 11, "windDirectionDeg": 307, "windDirectionCompass": "NW", "precipitationMm": 0,
                 "humidityPct": 86, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 9, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 82, "uvIndex": 2,
                 "windspeedKph": 11, "windDirectionDeg": 301, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 84, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 10, "tempC": 11, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 67, "uvIndex": 3,
                 "windspeedKph": 11, "windDirectionDeg": 291, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 11, "tempC": 11, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 51, "uvIndex": 3,
                 "windspeedKph": 12, "windDirectionDeg": 281, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 12, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 35, "uvIndex": 3,
                 "windspeedKph": 12, "windDirectionDeg": 271, "windDirectionCompass": "W", "precipitationMm": 0,
                 "humidityPct": 65, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 13, "tempC": 13, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 30, "uvIndex": 3,
                 "windspeedKph": 11, "windDirectionDeg": 263, "windDirectionCompass": "W", "precipitationMm": 0,
                 "humidityPct": 62, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 14, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 24, "uvIndex": 4,
                 "windspeedKph": 11, "windDirectionDeg": 255, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 15, "tempC": 14, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 4,
                 "windspeedKph": 10, "windDirectionDeg": 248, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 56, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 16, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 4,
                 "windspeedKph": 9, "windDirectionDeg": 233, "windDirectionCompass": "SW", "precipitationMm": 0,
                 "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1012},
                {"hour": 17, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 19, "uvIndex": 4,
                 "windspeedKph": 8, "windDirectionDeg": 219, "windDirectionCompass": "SW", "precipitationMm": 0,
                 "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1012},
                {"hour": 18, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 19, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 204, "windDirectionCompass": "SSW", "precipitationMm": 0,
                 "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1013},
                {"hour": 19, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 16, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 158, "windDirectionCompass": "SSE", "precipitationMm": 0,
                 "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1014},
                {"hour": 20, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 13, "uvIndex": 1,
                 "windspeedKph": 5, "windDirectionDeg": 111, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 74, "visibilityKm": 10, "pressureMb": 1014},
                {"hour": 21, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 10, "uvIndex": 1,
                 "windspeedKph": 5, "windDirectionDeg": 64, "windDirectionCompass": "ENE", "precipitationMm": 0,
                 "humidityPct": 77, "visibilityKm": 10, "pressureMb": 1015},
                {"hour": 22, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 8, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 84, "windDirectionCompass": "E", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1015},
                {"hour": 23, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 7, "uvIndex": 1,
                 "windspeedKph": 8, "windDirectionDeg": 104, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1016}]}
        self.assertEqual(cal.get_solar_energy_duration(weather_data1, "05:00", "90"), 0)
        self.assertEqual(cal.get_solar_energy_duration(weather_data1, "07:00", "90"), 70)
        self.assertEqual(cal.get_solar_energy_duration(weather_data1, "09:00", "90"), 90)
        self.assertEqual(cal.get_solar_energy_duration(weather_data1, "17:00", "90"), 32)

    def test_get_daylight_length(self):
        """
            Tests the get_daylight_length method in the Calculator class
        """
        weather_data1 = {"date":"2021-08-01","sunrise":"07:20:00","sunset":"17:32:00","moonrise":"00:52:00","moonset":"11:45:00","moonPhase":"Last Quarter","moonIlluminationPct":40,"minTempC":9,"maxTempC":14,"avgTempC":11,"sunHours":3.2,"uvIndex":3,"location":{"id":"ab9f494f-f8a0-4c24-bd2e-2497b99f2258","postcode":"3800","name":"MONASH UNIVERSITY","state":"VIC","latitude":"-37.9105599","longitude":"145.1362485","distanceToNearestWeatherStationMetres":3771.993796218797,"nearestWeatherStation":{"name":"OAKLEIGH (METROPOLITAN GOLF CLUB)","state":"VIC","latitude":"-37.9142","longitude":"145.0935"}},"hourlyWeatherHistory":[{"hour":0,"tempC":10,"weatherDesc":"Heavy rain","cloudCoverPct":100,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":349,"windDirectionCompass":"N","precipitationMm":2.9,"humidityPct":90,"visibilityKm":3,"pressureMb":1007},{"hour":1,"tempC":10,"weatherDesc":"Heavy rain","cloudCoverPct":94,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":342,"windDirectionCompass":"NNW","precipitationMm":1.4,"humidityPct":90,"visibilityKm":4,"pressureMb":1008},{"hour":2,"tempC":10,"weatherDesc":"Light drizzle","cloudCoverPct":87,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":336,"windDirectionCompass":"NNW","precipitationMm":0.2,"humidityPct":90,"visibilityKm":5,"pressureMb":1008},{"hour":3,"tempC":10,"weatherDesc":"Light drizzle","cloudCoverPct":81,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":329,"windDirectionCompass":"NNW","precipitationMm":0.3,"humidityPct":90,"visibilityKm":7,"pressureMb":1008},{"hour":4,"tempC":9,"weatherDesc":"Light drizzle","cloudCoverPct":79,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":325,"windDirectionCompass":"NW","precipitationMm":0.2,"humidityPct":90,"visibilityKm":8,"pressureMb":1009},{"hour":5,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":78,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":321,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":91,"visibilityKm":9,"pressureMb":1009},{"hour":6,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":76,"uvIndex":2,"windspeedKph":10,"windDirectionDeg":318,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":91,"visibilityKm":10,"pressureMb":1010},{"hour":7,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":78,"uvIndex":2,"windspeedKph":10,"windDirectionDeg":312,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":88,"visibilityKm":10,"pressureMb":1010},{"hour":8,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":80,"uvIndex":2,"windspeedKph":11,"windDirectionDeg":307,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":86,"visibilityKm":10,"pressureMb":1011},{"hour":9,"tempC":10,"weatherDesc":"Patchy rain possible","cloudCoverPct":82,"uvIndex":2,"windspeedKph":11,"windDirectionDeg":301,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":84,"visibilityKm":10,"pressureMb":1011},{"hour":10,"tempC":11,"weatherDesc":"Patchy rain possible","cloudCoverPct":67,"uvIndex":3,"windspeedKph":11,"windDirectionDeg":291,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1011},{"hour":11,"tempC":11,"weatherDesc":"Patchy rain possible","cloudCoverPct":51,"uvIndex":3,"windspeedKph":12,"windDirectionDeg":281,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":71,"visibilityKm":10,"pressureMb":1011},{"hour":12,"tempC":12,"weatherDesc":"Patchy rain possible","cloudCoverPct":35,"uvIndex":3,"windspeedKph":12,"windDirectionDeg":271,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":65,"visibilityKm":10,"pressureMb":1011},{"hour":13,"tempC":13,"weatherDesc":"Patchy rain possible","cloudCoverPct":30,"uvIndex":3,"windspeedKph":11,"windDirectionDeg":263,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":62,"visibilityKm":10,"pressureMb":1011},{"hour":14,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":24,"uvIndex":4,"windspeedKph":11,"windDirectionDeg":255,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":59,"visibilityKm":10,"pressureMb":1011},{"hour":15,"tempC":14,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":4,"windspeedKph":10,"windDirectionDeg":248,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":56,"visibilityKm":10,"pressureMb":1011},{"hour":16,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":4,"windspeedKph":9,"windDirectionDeg":233,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":60,"visibilityKm":10,"pressureMb":1012},{"hour":17,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":19,"uvIndex":4,"windspeedKph":8,"windDirectionDeg":219,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":64,"visibilityKm":10,"pressureMb":1012},{"hour":18,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":19,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":204,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1013},{"hour":19,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":16,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":158,"windDirectionCompass":"SSE","precipitationMm":0,"humidityPct":71,"visibilityKm":10,"pressureMb":1014},{"hour":20,"tempC":10,"weatherDesc":"Partly cloudy","cloudCoverPct":13,"uvIndex":1,"windspeedKph":5,"windDirectionDeg":111,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":74,"visibilityKm":10,"pressureMb":1014},{"hour":21,"tempC":10,"weatherDesc":"Partly cloudy","cloudCoverPct":10,"uvIndex":1,"windspeedKph":5,"windDirectionDeg":64,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":77,"visibilityKm":10,"pressureMb":1015},{"hour":22,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":8,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":84,"windDirectionCompass":"E","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1015},{"hour":23,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":1,"windspeedKph":8,"windDirectionDeg":104,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1016}]}
        weather_data2 = {"date":"2021-08-01","sunrise":"07:20:00","sunset":"17:17:00","moonrise":"00:49:00","moonset":"11:31:00","moonPhase":"Last Quarter","moonIlluminationPct":40,"minTempC":5,"maxTempC":10,"avgTempC":8,"sunHours":2.6,"uvIndex":2,"location":{"id":"22d72902-b72f-4ca0-a522-4dbfb77a7b78","postcode":"7250","name":"BLACKSTONE HEIGHTS","state":"TAS","latitude":"-41.46","longitude":"147.0820001","distanceToNearestWeatherStationMetres":5607.391317385195,"nearestWeatherStation":{"name":"LAUNCESTON (TI TREE BEND)","state":"TAS","latitude":"-41.4194","longitude":"147.1219"}},"hourlyWeatherHistory":[{"hour":0,"tempC":7,"weatherDesc":"Heavy rain","cloudCoverPct":100,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":343,"windDirectionCompass":"NNW","precipitationMm":2.9,"humidityPct":95,"visibilityKm":8,"pressureMb":1002},{"hour":1,"tempC":7,"weatherDesc":"Heavy rain","cloudCoverPct":96,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":337,"windDirectionCompass":"NNW","precipitationMm":1.4,"humidityPct":94,"visibilityKm":9,"pressureMb":1002},{"hour":2,"tempC":6,"weatherDesc":"Light rain shower","cloudCoverPct":92,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":330,"windDirectionCompass":"NNW","precipitationMm":0.2,"humidityPct":94,"visibilityKm":9,"pressureMb":1002},{"hour":3,"tempC":6,"weatherDesc":"Light rain shower","cloudCoverPct":88,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":323,"windDirectionCompass":"NW","precipitationMm":0.2,"humidityPct":94,"visibilityKm":9,"pressureMb":1002},{"hour":4,"tempC":5,"weatherDesc":"Light rain shower","cloudCoverPct":70,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":324,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":94,"visibilityKm":8,"pressureMb":1003},{"hour":5,"tempC":5,"weatherDesc":"Patchy rain possible","cloudCoverPct":52,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":324,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":94,"visibilityKm":6,"pressureMb":1004},{"hour":6,"tempC":5,"weatherDesc":"Patchy rain possible","cloudCoverPct":34,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":324,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":94,"visibilityKm":4,"pressureMb":1004},{"hour":7,"tempC":5,"weatherDesc":"Patchy rain possible","cloudCoverPct":25,"uvIndex":2,"windspeedKph":10,"windDirectionDeg":322,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":92,"visibilityKm":5,"pressureMb":1005},{"hour":8,"tempC":6,"weatherDesc":"Mist","cloudCoverPct":16,"uvIndex":2,"windspeedKph":10,"windDirectionDeg":320,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":89,"visibilityKm":6,"pressureMb":1005},{"hour":9,"tempC":7,"weatherDesc":"Mist","cloudCoverPct":7,"uvIndex":2,"windspeedKph":11,"windDirectionDeg":318,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":87,"visibilityKm":7,"pressureMb":1006},{"hour":10,"tempC":8,"weatherDesc":"Mist","cloudCoverPct":25,"uvIndex":2,"windspeedKph":11,"windDirectionDeg":309,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":81,"visibilityKm":8,"pressureMb":1006},{"hour":11,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":42,"uvIndex":3,"windspeedKph":12,"windDirectionDeg":301,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":75,"visibilityKm":9,"pressureMb":1006},{"hour":12,"tempC":10,"weatherDesc":"Partly cloudy","cloudCoverPct":59,"uvIndex":4,"windspeedKph":13,"windDirectionDeg":292,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1006},{"hour":13,"tempC":10,"weatherDesc":"Partly cloudy","cloudCoverPct":67,"uvIndex":4,"windspeedKph":12,"windDirectionDeg":290,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":66,"visibilityKm":10,"pressureMb":1006},{"hour":14,"tempC":10,"weatherDesc":"Patchy rain possible","cloudCoverPct":75,"uvIndex":3,"windspeedKph":11,"windDirectionDeg":288,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":64,"visibilityKm":10,"pressureMb":1007},{"hour":15,"tempC":10,"weatherDesc":"Patchy rain possible","cloudCoverPct":83,"uvIndex":3,"windspeedKph":11,"windDirectionDeg":286,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":62,"visibilityKm":10,"pressureMb":1007},{"hour":16,"tempC":10,"weatherDesc":"Patchy rain possible","cloudCoverPct":66,"uvIndex":2,"windspeedKph":9,"windDirectionDeg":294,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1008},{"hour":17,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":49,"uvIndex":2,"windspeedKph":8,"windDirectionDeg":303,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":75,"visibilityKm":10,"pressureMb":1009},{"hour":18,"tempC":8,"weatherDesc":"Patchy rain possible","cloudCoverPct":33,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":312,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":81,"visibilityKm":10,"pressureMb":1009},{"hour":19,"tempC":7,"weatherDesc":"Patchy rain possible","cloudCoverPct":25,"uvIndex":1,"windspeedKph":5,"windDirectionDeg":319,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":85,"visibilityKm":10,"pressureMb":1010},{"hour":20,"tempC":7,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":327,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":89,"visibilityKm":10,"pressureMb":1011},{"hour":21,"tempC":6,"weatherDesc":"Partly cloudy","cloudCoverPct":11,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":334,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":93,"visibilityKm":10,"pressureMb":1012},{"hour":22,"tempC":4,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":340,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":93,"visibilityKm":10,"pressureMb":1012},{"hour":23,"tempC":3,"weatherDesc":"Partly cloudy","cloudCoverPct":17,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":346,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":93,"visibilityKm":10,"pressureMb":1013}]}
        weather_data3 = {"date":"2021-08-01","sunrise":"07:06:00","sunset":"17:41:00","moonrise":"00:45:00","moonset":"11:54:00","moonPhase":"Last Quarter","moonIlluminationPct":40,"minTempC":6,"maxTempC":13,"avgTempC":12,"sunHours":2.8,"uvIndex":3,"location":{"id":"5bea7b46-9809-4189-aafe-160208da94f7","postcode":"6001","name":"PERTH","state":"WA","latitude":"-31.9505269","longitude":"115.8604572","distanceToNearestWeatherStationMetres":3672.959393589811,"nearestWeatherStation":{"name":"PERTH METRO","state":"WA","latitude":"-31.9192","longitude":"115.8728"}},"hourlyWeatherHistory":[{"hour":0,"tempC":6,"weatherDesc":"Overcast","cloudCoverPct":76,"uvIndex":1,"windspeedKph":24,"windDirectionDeg":284,"windDirectionCompass":"WNW","precipitationMm":0.4,"humidityPct":80,"visibilityKm":10,"pressureMb":1015},{"hour":1,"tempC":8,"weatherDesc":"Overcast","cloudCoverPct":81,"uvIndex":1,"windspeedKph":27,"windDirectionDeg":281,"windDirectionCompass":"WNW","precipitationMm":0.2,"humidityPct":80,"visibilityKm":10,"pressureMb":1014},{"hour":2,"tempC":10,"weatherDesc":"Moderate or heavy rain shower","cloudCoverPct":87,"uvIndex":1,"windspeedKph":29,"windDirectionDeg":278,"windDirectionCompass":"W","precipitationMm":0.3,"humidityPct":80,"visibilityKm":9,"pressureMb":1013},{"hour":3,"tempC":13,"weatherDesc":"Moderate or heavy rain shower","cloudCoverPct":92,"uvIndex":1,"windspeedKph":31,"windDirectionDeg":276,"windDirectionCompass":"W","precipitationMm":0.4,"humidityPct":80,"visibilityKm":9,"pressureMb":1012},{"hour":4,"tempC":13,"weatherDesc":"Moderate or heavy rain shower","cloudCoverPct":93,"uvIndex":1,"windspeedKph":33,"windDirectionDeg":271,"windDirectionCompass":"W","precipitationMm":0.2,"humidityPct":79,"visibilityKm":9,"pressureMb":1012},{"hour":5,"tempC":13,"weatherDesc":"Overcast","cloudCoverPct":94,"uvIndex":1,"windspeedKph":36,"windDirectionDeg":266,"windDirectionCompass":"W","precipitationMm":0.6,"humidityPct":78,"visibilityKm":8,"pressureMb":1012},{"hour":6,"tempC":13,"weatherDesc":"Overcast","cloudCoverPct":95,"uvIndex":3,"windspeedKph":38,"windDirectionDeg":261,"windDirectionCompass":"W","precipitationMm":0.8,"humidityPct":77,"visibilityKm":8,"pressureMb":1011},{"hour":7,"tempC":12,"weatherDesc":"Overcast","cloudCoverPct":95,"uvIndex":3,"windspeedKph":39,"windDirectionDeg":253,"windDirectionCompass":"WSW","precipitationMm":0.4,"humidityPct":75,"visibilityKm":9,"pressureMb":1012},{"hour":8,"tempC":12,"weatherDesc":"Patchy rain possible","cloudCoverPct":95,"uvIndex":3,"windspeedKph":40,"windDirectionDeg":245,"windDirectionCompass":"WSW","precipitationMm":0.1,"humidityPct":73,"visibilityKm":9,"pressureMb":1012},{"hour":9,"tempC":12,"weatherDesc":"Patchy rain possible","cloudCoverPct":95,"uvIndex":3,"windspeedKph":41,"windDirectionDeg":236,"windDirectionCompass":"WSW","precipitationMm":0.2,"humidityPct":71,"visibilityKm":10,"pressureMb":1013},{"hour":10,"tempC":12,"weatherDesc":"Patchy rain possible","cloudCoverPct":91,"uvIndex":3,"windspeedKph":40,"windDirectionDeg":233,"windDirectionCompass":"SW","precipitationMm":0.1,"humidityPct":68,"visibilityKm":10,"pressureMb":1013},{"hour":11,"tempC":12,"weatherDesc":"Cloudy","cloudCoverPct":88,"uvIndex":3,"windspeedKph":39,"windDirectionDeg":229,"windDirectionCompass":"SW","precipitationMm":0.3,"humidityPct":64,"visibilityKm":9,"pressureMb":1014},{"hour":12,"tempC":12,"weatherDesc":"Cloudy","cloudCoverPct":85,"uvIndex":3,"windspeedKph":37,"windDirectionDeg":225,"windDirectionCompass":"SW","precipitationMm":0.4,"humidityPct":61,"visibilityKm":9,"pressureMb":1015},{"hour":13,"tempC":12,"weatherDesc":"Cloudy","cloudCoverPct":82,"uvIndex":3,"windspeedKph":36,"windDirectionDeg":223,"windDirectionCompass":"SW","precipitationMm":0.2,"humidityPct":60,"visibilityKm":10,"pressureMb":1015},{"hour":14,"tempC":12,"weatherDesc":"Light rain shower","cloudCoverPct":78,"uvIndex":3,"windspeedKph":35,"windDirectionDeg":222,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":59,"visibilityKm":10,"pressureMb":1015},{"hour":15,"tempC":13,"weatherDesc":"Light rain shower","cloudCoverPct":75,"uvIndex":3,"windspeedKph":33,"windDirectionDeg":220,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":59,"visibilityKm":10,"pressureMb":1016},{"hour":16,"tempC":12,"weatherDesc":"Light rain shower","cloudCoverPct":63,"uvIndex":3,"windspeedKph":30,"windDirectionDeg":212,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":59,"visibilityKm":10,"pressureMb":1017},{"hour":17,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":52,"uvIndex":4,"windspeedKph":27,"windDirectionDeg":204,"windDirectionCompass":"SSW","precipitationMm":0.1,"humidityPct":60,"visibilityKm":10,"pressureMb":1018},{"hour":18,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":40,"uvIndex":1,"windspeedKph":23,"windDirectionDeg":197,"windDirectionCompass":"SSW","precipitationMm":0.1,"humidityPct":61,"visibilityKm":10,"pressureMb":1019},{"hour":19,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":32,"uvIndex":1,"windspeedKph":19,"windDirectionDeg":182,"windDirectionCompass":"S","precipitationMm":0,"humidityPct":63,"visibilityKm":10,"pressureMb":1020},{"hour":20,"tempC":10,"weatherDesc":"Partly cloudy","cloudCoverPct":24,"uvIndex":1,"windspeedKph":15,"windDirectionDeg":168,"windDirectionCompass":"SSE","precipitationMm":0,"humidityPct":64,"visibilityKm":10,"pressureMb":1020},{"hour":21,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":17,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":154,"windDirectionCompass":"SSE","precipitationMm":0,"humidityPct":65,"visibilityKm":10,"pressureMb":1021},{"hour":22,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":44,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":160,"windDirectionCompass":"SSE","precipitationMm":0,"humidityPct":67,"visibilityKm":10,"pressureMb":1021},{"hour":23,"tempC":9,"weatherDesc":"Light rain shower","cloudCoverPct":72,"uvIndex":1,"windspeedKph":8,"windDirectionDeg":167,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":69,"visibilityKm":10,"pressureMb":1021}]}
        cal = Calculator()
        self.assertEqual(cal.get_day_light_length(weather_data1), "10.2000")
        self.assertEqual(cal.get_day_light_length(weather_data2), "9.9500")
        self.assertEqual(cal.get_day_light_length(weather_data3), "10.5833")

    def test_get_solar_insolation(self):
        """
        Tests the get_solar_insolation method in the Calculator class
        """
        cal = Calculator()
        weather_data1 = {"date": "2021-08-01", "sunrise": "07:20:00", "sunset": "17:32:00", "moonrise": "00:52:00",
                         "moonset": "11:45:00", "moonPhase": "Last Quarter", "moonIlluminationPct": 40, "minTempC": 9,
                         "maxTempC": 14, "avgTempC": 11, "sunHours": 3.2, "uvIndex": 3,
                         "location": {"id": "ab9f494f-f8a0-4c24-bd2e-2497b99f2258", "postcode": "3800",
                                      "name": "MONASH UNIVERSITY", "state": "VIC", "latitude": "-37.9105599",
                                      "longitude": "145.1362485",
                                      "distanceToNearestWeatherStationMetres": 3771.993796218797,
                                      "nearestWeatherStation": {"name": "OAKLEIGH (METROPOLITAN GOLF CLUB)",
                                                                "state": "VIC", "latitude": "-37.9142",
                                                                "longitude": "145.0935"}}, "hourlyWeatherHistory": [
                {"hour": 0, "tempC": 10, "weatherDesc": "Heavy rain", "cloudCoverPct": 100, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 349, "windDirectionCompass": "N", "precipitationMm": 2.9,
                 "humidityPct": 90, "visibilityKm": 3, "pressureMb": 1007},
                {"hour": 1, "tempC": 10, "weatherDesc": "Heavy rain", "cloudCoverPct": 94, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 342, "windDirectionCompass": "NNW", "precipitationMm": 1.4,
                 "humidityPct": 90, "visibilityKm": 4, "pressureMb": 1008},
                {"hour": 2, "tempC": 10, "weatherDesc": "Light drizzle", "cloudCoverPct": 87, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 336, "windDirectionCompass": "NNW", "precipitationMm": 0.2,
                 "humidityPct": 90, "visibilityKm": 5, "pressureMb": 1008},
                {"hour": 3, "tempC": 10, "weatherDesc": "Light drizzle", "cloudCoverPct": 81, "uvIndex": 1,
                 "windspeedKph": 9, "windDirectionDeg": 329, "windDirectionCompass": "NNW", "precipitationMm": 0.3,
                 "humidityPct": 90, "visibilityKm": 7, "pressureMb": 1008},
                {"hour": 4, "tempC": 9, "weatherDesc": "Light drizzle", "cloudCoverPct": 79, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 325, "windDirectionCompass": "NW", "precipitationMm": 0.2,
                 "humidityPct": 90, "visibilityKm": 8, "pressureMb": 1009},
                {"hour": 5, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 78, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 321, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 91, "visibilityKm": 9, "pressureMb": 1009},
                {"hour": 6, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 76, "uvIndex": 2,
                 "windspeedKph": 10, "windDirectionDeg": 318, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 91, "visibilityKm": 10, "pressureMb": 1010},
                {"hour": 7, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 78, "uvIndex": 2,
                 "windspeedKph": 10, "windDirectionDeg": 312, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 88, "visibilityKm": 10, "pressureMb": 1010},
                {"hour": 8, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 80, "uvIndex": 2,
                 "windspeedKph": 11, "windDirectionDeg": 307, "windDirectionCompass": "NW", "precipitationMm": 0,
                 "humidityPct": 86, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 9, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 82, "uvIndex": 2,
                 "windspeedKph": 11, "windDirectionDeg": 301, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 84, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 10, "tempC": 11, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 67, "uvIndex": 3,
                 "windspeedKph": 11, "windDirectionDeg": 291, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 11, "tempC": 11, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 51, "uvIndex": 3,
                 "windspeedKph": 12, "windDirectionDeg": 281, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 12, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 35, "uvIndex": 3,
                 "windspeedKph": 12, "windDirectionDeg": 271, "windDirectionCompass": "W", "precipitationMm": 0,
                 "humidityPct": 65, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 13, "tempC": 13, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 30, "uvIndex": 3,
                 "windspeedKph": 11, "windDirectionDeg": 263, "windDirectionCompass": "W", "precipitationMm": 0,
                 "humidityPct": 62, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 14, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 24, "uvIndex": 4,
                 "windspeedKph": 11, "windDirectionDeg": 255, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 15, "tempC": 14, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 4,
                 "windspeedKph": 10, "windDirectionDeg": 248, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 56, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 16, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 4,
                 "windspeedKph": 9, "windDirectionDeg": 233, "windDirectionCompass": "SW", "precipitationMm": 0,
                 "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1012},
                {"hour": 17, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 19, "uvIndex": 4,
                 "windspeedKph": 8, "windDirectionDeg": 219, "windDirectionCompass": "SW", "precipitationMm": 0,
                 "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1012},
                {"hour": 18, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 19, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 204, "windDirectionCompass": "SSW", "precipitationMm": 0,
                 "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1013},
                {"hour": 19, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 16, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 158, "windDirectionCompass": "SSE", "precipitationMm": 0,
                 "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1014},
                {"hour": 20, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 13, "uvIndex": 1,
                 "windspeedKph": 5, "windDirectionDeg": 111, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 74, "visibilityKm": 10, "pressureMb": 1014},
                {"hour": 21, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 10, "uvIndex": 1,
                 "windspeedKph": 5, "windDirectionDeg": 64, "windDirectionCompass": "ENE", "precipitationMm": 0,
                 "humidityPct": 77, "visibilityKm": 10, "pressureMb": 1015},
                {"hour": 22, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 8, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 84, "windDirectionCompass": "E", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1015},
                {"hour": 23, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 7, "uvIndex": 1,
                 "windspeedKph": 8, "windDirectionDeg": 104, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1016}]}
        weather_data2 = {"date": "2021-08-01", "sunrise": "07:20:00", "sunset": "17:17:00", "moonrise": "00:49:00",
                         "moonset": "11:31:00", "moonPhase": "Last Quarter", "moonIlluminationPct": 40, "minTempC": 5,
                         "maxTempC": 10, "avgTempC": 8, "sunHours": 2.6, "uvIndex": 2,
                         "location": {"id": "22d72902-b72f-4ca0-a522-4dbfb77a7b78", "postcode": "7250",
                                      "name": "BLACKSTONE HEIGHTS", "state": "TAS", "latitude": "-41.46",
                                      "longitude": "147.0820001",
                                      "distanceToNearestWeatherStationMetres": 5607.391317385195,
                                      "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS",
                                                                "latitude": "-41.4194", "longitude": "147.1219"}},
                         "hourlyWeatherHistory": [
                             {"hour": 0, "tempC": 7, "weatherDesc": "Heavy rain", "cloudCoverPct": 100, "uvIndex": 1,
                              "windspeedKph": 10, "windDirectionDeg": 343, "windDirectionCompass": "NNW",
                              "precipitationMm": 2.9, "humidityPct": 95, "visibilityKm": 8, "pressureMb": 1002},
                             {"hour": 1, "tempC": 7, "weatherDesc": "Heavy rain", "cloudCoverPct": 96, "uvIndex": 1,
                              "windspeedKph": 10, "windDirectionDeg": 337, "windDirectionCompass": "NNW",
                              "precipitationMm": 1.4, "humidityPct": 94, "visibilityKm": 9, "pressureMb": 1002},
                             {"hour": 2, "tempC": 6, "weatherDesc": "Light rain shower", "cloudCoverPct": 92,
                              "uvIndex": 1, "windspeedKph": 10, "windDirectionDeg": 330, "windDirectionCompass": "NNW",
                              "precipitationMm": 0.2, "humidityPct": 94, "visibilityKm": 9, "pressureMb": 1002},
                             {"hour": 3, "tempC": 6, "weatherDesc": "Light rain shower", "cloudCoverPct": 88,
                              "uvIndex": 1, "windspeedKph": 10, "windDirectionDeg": 323, "windDirectionCompass": "NW",
                              "precipitationMm": 0.2, "humidityPct": 94, "visibilityKm": 9, "pressureMb": 1002},
                             {"hour": 4, "tempC": 5, "weatherDesc": "Light rain shower", "cloudCoverPct": 70,
                              "uvIndex": 1, "windspeedKph": 10, "windDirectionDeg": 324, "windDirectionCompass": "NW",
                              "precipitationMm": 0.1, "humidityPct": 94, "visibilityKm": 8, "pressureMb": 1003},
                             {"hour": 5, "tempC": 5, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 52,
                              "uvIndex": 1, "windspeedKph": 9, "windDirectionDeg": 324, "windDirectionCompass": "NW",
                              "precipitationMm": 0.1, "humidityPct": 94, "visibilityKm": 6, "pressureMb": 1004},
                             {"hour": 6, "tempC": 5, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 34,
                              "uvIndex": 1, "windspeedKph": 9, "windDirectionDeg": 324, "windDirectionCompass": "NW",
                              "precipitationMm": 0.1, "humidityPct": 94, "visibilityKm": 4, "pressureMb": 1004},
                             {"hour": 7, "tempC": 5, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 25,
                              "uvIndex": 2, "windspeedKph": 10, "windDirectionDeg": 322, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 92, "visibilityKm": 5, "pressureMb": 1005},
                             {"hour": 8, "tempC": 6, "weatherDesc": "Mist", "cloudCoverPct": 16, "uvIndex": 2,
                              "windspeedKph": 10, "windDirectionDeg": 320, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 89, "visibilityKm": 6, "pressureMb": 1005},
                             {"hour": 9, "tempC": 7, "weatherDesc": "Mist", "cloudCoverPct": 7, "uvIndex": 2,
                              "windspeedKph": 11, "windDirectionDeg": 318, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 87, "visibilityKm": 7, "pressureMb": 1006},
                             {"hour": 10, "tempC": 8, "weatherDesc": "Mist", "cloudCoverPct": 25, "uvIndex": 2,
                              "windspeedKph": 11, "windDirectionDeg": 309, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 81, "visibilityKm": 8, "pressureMb": 1006},
                             {"hour": 11, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 42, "uvIndex": 3,
                              "windspeedKph": 12, "windDirectionDeg": 301, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 75, "visibilityKm": 9, "pressureMb": 1006},
                             {"hour": 12, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 59,
                              "uvIndex": 4, "windspeedKph": 13, "windDirectionDeg": 292, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1006},
                             {"hour": 13, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 67,
                              "uvIndex": 4, "windspeedKph": 12, "windDirectionDeg": 290, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 66, "visibilityKm": 10, "pressureMb": 1006},
                             {"hour": 14, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 75,
                              "uvIndex": 3, "windspeedKph": 11, "windDirectionDeg": 288, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.1, "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1007},
                             {"hour": 15, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 83,
                              "uvIndex": 3, "windspeedKph": 11, "windDirectionDeg": 286, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.1, "humidityPct": 62, "visibilityKm": 10, "pressureMb": 1007},
                             {"hour": 16, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 66,
                              "uvIndex": 2, "windspeedKph": 9, "windDirectionDeg": 294, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1008},
                             {"hour": 17, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 49,
                              "uvIndex": 2, "windspeedKph": 8, "windDirectionDeg": 303, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 75, "visibilityKm": 10, "pressureMb": 1009},
                             {"hour": 18, "tempC": 8, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 33,
                              "uvIndex": 1, "windspeedKph": 6, "windDirectionDeg": 312, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 81, "visibilityKm": 10, "pressureMb": 1009},
                             {"hour": 19, "tempC": 7, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 25,
                              "uvIndex": 1, "windspeedKph": 5, "windDirectionDeg": 319, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 85, "visibilityKm": 10, "pressureMb": 1010},
                             {"hour": 20, "tempC": 7, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 1,
                              "windspeedKph": 4, "windDirectionDeg": 327, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 89, "visibilityKm": 10, "pressureMb": 1011},
                             {"hour": 21, "tempC": 6, "weatherDesc": "Partly cloudy", "cloudCoverPct": 11, "uvIndex": 1,
                              "windspeedKph": 3, "windDirectionDeg": 334, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 93, "visibilityKm": 10, "pressureMb": 1012},
                             {"hour": 22, "tempC": 4, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 1,
                              "windspeedKph": 3, "windDirectionDeg": 340, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 93, "visibilityKm": 10, "pressureMb": 1012},
                             {"hour": 23, "tempC": 3, "weatherDesc": "Partly cloudy", "cloudCoverPct": 17, "uvIndex": 1,
                              "windspeedKph": 3, "windDirectionDeg": 346, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 93, "visibilityKm": 10, "pressureMb": 1013}]}
        weather_data3 = {"date": "2021-08-01", "sunrise": "07:06:00", "sunset": "17:41:00", "moonrise": "00:45:00",
                         "moonset": "11:54:00", "moonPhase": "Last Quarter", "moonIlluminationPct": 40, "minTempC": 6,
                         "maxTempC": 13, "avgTempC": 12, "sunHours": 2.8, "uvIndex": 3,
                         "location": {"id": "5bea7b46-9809-4189-aafe-160208da94f7", "postcode": "6001", "name": "PERTH",
                                      "state": "WA", "latitude": "-31.9505269", "longitude": "115.8604572",
                                      "distanceToNearestWeatherStationMetres": 3672.959393589811,
                                      "nearestWeatherStation": {"name": "PERTH METRO", "state": "WA",
                                                                "latitude": "-31.9192", "longitude": "115.8728"}},
                         "hourlyWeatherHistory": [
                             {"hour": 0, "tempC": 6, "weatherDesc": "Overcast", "cloudCoverPct": 76, "uvIndex": 1,
                              "windspeedKph": 24, "windDirectionDeg": 284, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.4, "humidityPct": 80, "visibilityKm": 10, "pressureMb": 1015},
                             {"hour": 1, "tempC": 8, "weatherDesc": "Overcast", "cloudCoverPct": 81, "uvIndex": 1,
                              "windspeedKph": 27, "windDirectionDeg": 281, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.2, "humidityPct": 80, "visibilityKm": 10, "pressureMb": 1014},
                             {"hour": 2, "tempC": 10, "weatherDesc": "Moderate or heavy rain shower",
                              "cloudCoverPct": 87, "uvIndex": 1, "windspeedKph": 29, "windDirectionDeg": 278,
                              "windDirectionCompass": "W", "precipitationMm": 0.3, "humidityPct": 80, "visibilityKm": 9,
                              "pressureMb": 1013},
                             {"hour": 3, "tempC": 13, "weatherDesc": "Moderate or heavy rain shower",
                              "cloudCoverPct": 92, "uvIndex": 1, "windspeedKph": 31, "windDirectionDeg": 276,
                              "windDirectionCompass": "W", "precipitationMm": 0.4, "humidityPct": 80, "visibilityKm": 9,
                              "pressureMb": 1012},
                             {"hour": 4, "tempC": 13, "weatherDesc": "Moderate or heavy rain shower",
                              "cloudCoverPct": 93, "uvIndex": 1, "windspeedKph": 33, "windDirectionDeg": 271,
                              "windDirectionCompass": "W", "precipitationMm": 0.2, "humidityPct": 79, "visibilityKm": 9,
                              "pressureMb": 1012},
                             {"hour": 5, "tempC": 13, "weatherDesc": "Overcast", "cloudCoverPct": 94, "uvIndex": 1,
                              "windspeedKph": 36, "windDirectionDeg": 266, "windDirectionCompass": "W",
                              "precipitationMm": 0.6, "humidityPct": 78, "visibilityKm": 8, "pressureMb": 1012},
                             {"hour": 6, "tempC": 13, "weatherDesc": "Overcast", "cloudCoverPct": 95, "uvIndex": 3,
                              "windspeedKph": 38, "windDirectionDeg": 261, "windDirectionCompass": "W",
                              "precipitationMm": 0.8, "humidityPct": 77, "visibilityKm": 8, "pressureMb": 1011},
                             {"hour": 7, "tempC": 12, "weatherDesc": "Overcast", "cloudCoverPct": 95, "uvIndex": 3,
                              "windspeedKph": 39, "windDirectionDeg": 253, "windDirectionCompass": "WSW",
                              "precipitationMm": 0.4, "humidityPct": 75, "visibilityKm": 9, "pressureMb": 1012},
                             {"hour": 8, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 95,
                              "uvIndex": 3, "windspeedKph": 40, "windDirectionDeg": 245, "windDirectionCompass": "WSW",
                              "precipitationMm": 0.1, "humidityPct": 73, "visibilityKm": 9, "pressureMb": 1012},
                             {"hour": 9, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 95,
                              "uvIndex": 3, "windspeedKph": 41, "windDirectionDeg": 236, "windDirectionCompass": "WSW",
                              "precipitationMm": 0.2, "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1013},
                             {"hour": 10, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 91,
                              "uvIndex": 3, "windspeedKph": 40, "windDirectionDeg": 233, "windDirectionCompass": "SW",
                              "precipitationMm": 0.1, "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1013},
                             {"hour": 11, "tempC": 12, "weatherDesc": "Cloudy", "cloudCoverPct": 88, "uvIndex": 3,
                              "windspeedKph": 39, "windDirectionDeg": 229, "windDirectionCompass": "SW",
                              "precipitationMm": 0.3, "humidityPct": 64, "visibilityKm": 9, "pressureMb": 1014},
                             {"hour": 12, "tempC": 12, "weatherDesc": "Cloudy", "cloudCoverPct": 85, "uvIndex": 3,
                              "windspeedKph": 37, "windDirectionDeg": 225, "windDirectionCompass": "SW",
                              "precipitationMm": 0.4, "humidityPct": 61, "visibilityKm": 9, "pressureMb": 1015},
                             {"hour": 13, "tempC": 12, "weatherDesc": "Cloudy", "cloudCoverPct": 82, "uvIndex": 3,
                              "windspeedKph": 36, "windDirectionDeg": 223, "windDirectionCompass": "SW",
                              "precipitationMm": 0.2, "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1015},
                             {"hour": 14, "tempC": 12, "weatherDesc": "Light rain shower", "cloudCoverPct": 78,
                              "uvIndex": 3, "windspeedKph": 35, "windDirectionDeg": 222, "windDirectionCompass": "SW",
                              "precipitationMm": 0, "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1015},
                             {"hour": 15, "tempC": 13, "weatherDesc": "Light rain shower", "cloudCoverPct": 75,
                              "uvIndex": 3, "windspeedKph": 33, "windDirectionDeg": 220, "windDirectionCompass": "SW",
                              "precipitationMm": 0, "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1016},
                             {"hour": 16, "tempC": 12, "weatherDesc": "Light rain shower", "cloudCoverPct": 63,
                              "uvIndex": 3, "windspeedKph": 30, "windDirectionDeg": 212, "windDirectionCompass": "SSW",
                              "precipitationMm": 0, "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1017},
                             {"hour": 17, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 52,
                              "uvIndex": 4, "windspeedKph": 27, "windDirectionDeg": 204, "windDirectionCompass": "SSW",
                              "precipitationMm": 0.1, "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1018},
                             {"hour": 18, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 40,
                              "uvIndex": 1, "windspeedKph": 23, "windDirectionDeg": 197, "windDirectionCompass": "SSW",
                              "precipitationMm": 0.1, "humidityPct": 61, "visibilityKm": 10, "pressureMb": 1019},
                             {"hour": 19, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 32,
                              "uvIndex": 1, "windspeedKph": 19, "windDirectionDeg": 182, "windDirectionCompass": "S",
                              "precipitationMm": 0, "humidityPct": 63, "visibilityKm": 10, "pressureMb": 1020},
                             {"hour": 20, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 24,
                              "uvIndex": 1, "windspeedKph": 15, "windDirectionDeg": 168, "windDirectionCompass": "SSE",
                              "precipitationMm": 0, "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1020},
                             {"hour": 21, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 17, "uvIndex": 1,
                              "windspeedKph": 11, "windDirectionDeg": 154, "windDirectionCompass": "SSE",
                              "precipitationMm": 0, "humidityPct": 65, "visibilityKm": 10, "pressureMb": 1021},
                             {"hour": 22, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 44, "uvIndex": 1,
                              "windspeedKph": 9, "windDirectionDeg": 160, "windDirectionCompass": "SSE",
                              "precipitationMm": 0, "humidityPct": 67, "visibilityKm": 10, "pressureMb": 1021},
                             {"hour": 23, "tempC": 9, "weatherDesc": "Light rain shower", "cloudCoverPct": 72,
                              "uvIndex": 1, "windspeedKph": 8, "windDirectionDeg": 167, "windDirectionCompass": "SSE",
                              "precipitationMm": 0.1, "humidityPct": 69, "visibilityKm": 10, "pressureMb": 1021}]}
        self.assertEqual(cal.get_solar_insolation(weather_data1), 3.2)
        self.assertEqual(cal.get_solar_insolation(weather_data2), 2.6)
        self.assertEqual(cal.get_solar_insolation(weather_data3), 2.8)

    def test_get_cloud_cover(self):
        """
        Tests the get_cloud_cover method in the Calculator class
        """
        cal = Calculator()
        weather_data1 = {"date": "2021-08-01", "sunrise": "07:20:00", "sunset": "17:32:00", "moonrise": "00:52:00",
                         "moonset": "11:45:00", "moonPhase": "Last Quarter", "moonIlluminationPct": 40, "minTempC": 9,
                         "maxTempC": 14, "avgTempC": 11, "sunHours": 3.2, "uvIndex": 3,
                         "location": {"id": "ab9f494f-f8a0-4c24-bd2e-2497b99f2258", "postcode": "3800",
                                      "name": "MONASH UNIVERSITY", "state": "VIC", "latitude": "-37.9105599",
                                      "longitude": "145.1362485",
                                      "distanceToNearestWeatherStationMetres": 3771.993796218797,
                                      "nearestWeatherStation": {"name": "OAKLEIGH (METROPOLITAN GOLF CLUB)",
                                                                "state": "VIC", "latitude": "-37.9142",
                                                                "longitude": "145.0935"}}, "hourlyWeatherHistory": [
                {"hour": 0, "tempC": 10, "weatherDesc": "Heavy rain", "cloudCoverPct": 100, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 349, "windDirectionCompass": "N", "precipitationMm": 2.9,
                 "humidityPct": 90, "visibilityKm": 3, "pressureMb": 1007},
                {"hour": 1, "tempC": 10, "weatherDesc": "Heavy rain", "cloudCoverPct": 94, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 342, "windDirectionCompass": "NNW", "precipitationMm": 1.4,
                 "humidityPct": 90, "visibilityKm": 4, "pressureMb": 1008},
                {"hour": 2, "tempC": 10, "weatherDesc": "Light drizzle", "cloudCoverPct": 87, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 336, "windDirectionCompass": "NNW", "precipitationMm": 0.2,
                 "humidityPct": 90, "visibilityKm": 5, "pressureMb": 1008},
                {"hour": 3, "tempC": 10, "weatherDesc": "Light drizzle", "cloudCoverPct": 81, "uvIndex": 1,
                 "windspeedKph": 9, "windDirectionDeg": 329, "windDirectionCompass": "NNW", "precipitationMm": 0.3,
                 "humidityPct": 90, "visibilityKm": 7, "pressureMb": 1008},
                {"hour": 4, "tempC": 9, "weatherDesc": "Light drizzle", "cloudCoverPct": 79, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 325, "windDirectionCompass": "NW", "precipitationMm": 0.2,
                 "humidityPct": 90, "visibilityKm": 8, "pressureMb": 1009},
                {"hour": 5, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 78, "uvIndex": 1,
                 "windspeedKph": 10, "windDirectionDeg": 321, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 91, "visibilityKm": 9, "pressureMb": 1009},
                {"hour": 6, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 76, "uvIndex": 2,
                 "windspeedKph": 10, "windDirectionDeg": 318, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 91, "visibilityKm": 10, "pressureMb": 1010},
                {"hour": 7, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 78, "uvIndex": 2,
                 "windspeedKph": 10, "windDirectionDeg": 312, "windDirectionCompass": "NW", "precipitationMm": 0.1,
                 "humidityPct": 88, "visibilityKm": 10, "pressureMb": 1010},
                {"hour": 8, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 80, "uvIndex": 2,
                 "windspeedKph": 11, "windDirectionDeg": 307, "windDirectionCompass": "NW", "precipitationMm": 0,
                 "humidityPct": 86, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 9, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 82, "uvIndex": 2,
                 "windspeedKph": 11, "windDirectionDeg": 301, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 84, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 10, "tempC": 11, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 67, "uvIndex": 3,
                 "windspeedKph": 11, "windDirectionDeg": 291, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 11, "tempC": 11, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 51, "uvIndex": 3,
                 "windspeedKph": 12, "windDirectionDeg": 281, "windDirectionCompass": "WNW", "precipitationMm": 0,
                 "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 12, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 35, "uvIndex": 3,
                 "windspeedKph": 12, "windDirectionDeg": 271, "windDirectionCompass": "W", "precipitationMm": 0,
                 "humidityPct": 65, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 13, "tempC": 13, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 30, "uvIndex": 3,
                 "windspeedKph": 11, "windDirectionDeg": 263, "windDirectionCompass": "W", "precipitationMm": 0,
                 "humidityPct": 62, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 14, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 24, "uvIndex": 4,
                 "windspeedKph": 11, "windDirectionDeg": 255, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 15, "tempC": 14, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 4,
                 "windspeedKph": 10, "windDirectionDeg": 248, "windDirectionCompass": "WSW", "precipitationMm": 0,
                 "humidityPct": 56, "visibilityKm": 10, "pressureMb": 1011},
                {"hour": 16, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 4,
                 "windspeedKph": 9, "windDirectionDeg": 233, "windDirectionCompass": "SW", "precipitationMm": 0,
                 "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1012},
                {"hour": 17, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 19, "uvIndex": 4,
                 "windspeedKph": 8, "windDirectionDeg": 219, "windDirectionCompass": "SW", "precipitationMm": 0,
                 "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1012},
                {"hour": 18, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 19, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 204, "windDirectionCompass": "SSW", "precipitationMm": 0,
                 "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1013},
                {"hour": 19, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 16, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 158, "windDirectionCompass": "SSE", "precipitationMm": 0,
                 "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1014},
                {"hour": 20, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 13, "uvIndex": 1,
                 "windspeedKph": 5, "windDirectionDeg": 111, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 74, "visibilityKm": 10, "pressureMb": 1014},
                {"hour": 21, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 10, "uvIndex": 1,
                 "windspeedKph": 5, "windDirectionDeg": 64, "windDirectionCompass": "ENE", "precipitationMm": 0,
                 "humidityPct": 77, "visibilityKm": 10, "pressureMb": 1015},
                {"hour": 22, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 8, "uvIndex": 1,
                 "windspeedKph": 6, "windDirectionDeg": 84, "windDirectionCompass": "E", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1015},
                {"hour": 23, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 7, "uvIndex": 1,
                 "windspeedKph": 8, "windDirectionDeg": 104, "windDirectionCompass": "ESE", "precipitationMm": 0,
                 "humidityPct": 78, "visibilityKm": 10, "pressureMb": 1016}]}
        weather_data2 = {"date": "2021-08-01", "sunrise": "07:20:00", "sunset": "17:17:00", "moonrise": "00:49:00",
                         "moonset": "11:31:00", "moonPhase": "Last Quarter", "moonIlluminationPct": 40, "minTempC": 5,
                         "maxTempC": 10, "avgTempC": 8, "sunHours": 2.6, "uvIndex": 2,
                         "location": {"id": "22d72902-b72f-4ca0-a522-4dbfb77a7b78", "postcode": "7250",
                                      "name": "BLACKSTONE HEIGHTS", "state": "TAS", "latitude": "-41.46",
                                      "longitude": "147.0820001",
                                      "distanceToNearestWeatherStationMetres": 5607.391317385195,
                                      "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS",
                                                                "latitude": "-41.4194", "longitude": "147.1219"}},
                         "hourlyWeatherHistory": [
                             {"hour": 0, "tempC": 7, "weatherDesc": "Heavy rain", "cloudCoverPct": 100, "uvIndex": 1,
                              "windspeedKph": 10, "windDirectionDeg": 343, "windDirectionCompass": "NNW",
                              "precipitationMm": 2.9, "humidityPct": 95, "visibilityKm": 8, "pressureMb": 1002},
                             {"hour": 1, "tempC": 7, "weatherDesc": "Heavy rain", "cloudCoverPct": 96, "uvIndex": 1,
                              "windspeedKph": 10, "windDirectionDeg": 337, "windDirectionCompass": "NNW",
                              "precipitationMm": 1.4, "humidityPct": 94, "visibilityKm": 9, "pressureMb": 1002},
                             {"hour": 2, "tempC": 6, "weatherDesc": "Light rain shower", "cloudCoverPct": 92,
                              "uvIndex": 1, "windspeedKph": 10, "windDirectionDeg": 330, "windDirectionCompass": "NNW",
                              "precipitationMm": 0.2, "humidityPct": 94, "visibilityKm": 9, "pressureMb": 1002},
                             {"hour": 3, "tempC": 6, "weatherDesc": "Light rain shower", "cloudCoverPct": 88,
                              "uvIndex": 1, "windspeedKph": 10, "windDirectionDeg": 323, "windDirectionCompass": "NW",
                              "precipitationMm": 0.2, "humidityPct": 94, "visibilityKm": 9, "pressureMb": 1002},
                             {"hour": 4, "tempC": 5, "weatherDesc": "Light rain shower", "cloudCoverPct": 70,
                              "uvIndex": 1, "windspeedKph": 10, "windDirectionDeg": 324, "windDirectionCompass": "NW",
                              "precipitationMm": 0.1, "humidityPct": 94, "visibilityKm": 8, "pressureMb": 1003},
                             {"hour": 5, "tempC": 5, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 52,
                              "uvIndex": 1, "windspeedKph": 9, "windDirectionDeg": 324, "windDirectionCompass": "NW",
                              "precipitationMm": 0.1, "humidityPct": 94, "visibilityKm": 6, "pressureMb": 1004},
                             {"hour": 6, "tempC": 5, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 34,
                              "uvIndex": 1, "windspeedKph": 9, "windDirectionDeg": 324, "windDirectionCompass": "NW",
                              "precipitationMm": 0.1, "humidityPct": 94, "visibilityKm": 4, "pressureMb": 1004},
                             {"hour": 7, "tempC": 5, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 25,
                              "uvIndex": 2, "windspeedKph": 10, "windDirectionDeg": 322, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 92, "visibilityKm": 5, "pressureMb": 1005},
                             {"hour": 8, "tempC": 6, "weatherDesc": "Mist", "cloudCoverPct": 16, "uvIndex": 2,
                              "windspeedKph": 10, "windDirectionDeg": 320, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 89, "visibilityKm": 6, "pressureMb": 1005},
                             {"hour": 9, "tempC": 7, "weatherDesc": "Mist", "cloudCoverPct": 7, "uvIndex": 2,
                              "windspeedKph": 11, "windDirectionDeg": 318, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 87, "visibilityKm": 7, "pressureMb": 1006},
                             {"hour": 10, "tempC": 8, "weatherDesc": "Mist", "cloudCoverPct": 25, "uvIndex": 2,
                              "windspeedKph": 11, "windDirectionDeg": 309, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 81, "visibilityKm": 8, "pressureMb": 1006},
                             {"hour": 11, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 42, "uvIndex": 3,
                              "windspeedKph": 12, "windDirectionDeg": 301, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 75, "visibilityKm": 9, "pressureMb": 1006},
                             {"hour": 12, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 59,
                              "uvIndex": 4, "windspeedKph": 13, "windDirectionDeg": 292, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1006},
                             {"hour": 13, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 67,
                              "uvIndex": 4, "windspeedKph": 12, "windDirectionDeg": 290, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 66, "visibilityKm": 10, "pressureMb": 1006},
                             {"hour": 14, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 75,
                              "uvIndex": 3, "windspeedKph": 11, "windDirectionDeg": 288, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.1, "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1007},
                             {"hour": 15, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 83,
                              "uvIndex": 3, "windspeedKph": 11, "windDirectionDeg": 286, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.1, "humidityPct": 62, "visibilityKm": 10, "pressureMb": 1007},
                             {"hour": 16, "tempC": 10, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 66,
                              "uvIndex": 2, "windspeedKph": 9, "windDirectionDeg": 294, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1008},
                             {"hour": 17, "tempC": 9, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 49,
                              "uvIndex": 2, "windspeedKph": 8, "windDirectionDeg": 303, "windDirectionCompass": "WNW",
                              "precipitationMm": 0, "humidityPct": 75, "visibilityKm": 10, "pressureMb": 1009},
                             {"hour": 18, "tempC": 8, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 33,
                              "uvIndex": 1, "windspeedKph": 6, "windDirectionDeg": 312, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 81, "visibilityKm": 10, "pressureMb": 1009},
                             {"hour": 19, "tempC": 7, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 25,
                              "uvIndex": 1, "windspeedKph": 5, "windDirectionDeg": 319, "windDirectionCompass": "NW",
                              "precipitationMm": 0, "humidityPct": 85, "visibilityKm": 10, "pressureMb": 1010},
                             {"hour": 20, "tempC": 7, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 1,
                              "windspeedKph": 4, "windDirectionDeg": 327, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 89, "visibilityKm": 10, "pressureMb": 1011},
                             {"hour": 21, "tempC": 6, "weatherDesc": "Partly cloudy", "cloudCoverPct": 11, "uvIndex": 1,
                              "windspeedKph": 3, "windDirectionDeg": 334, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 93, "visibilityKm": 10, "pressureMb": 1012},
                             {"hour": 22, "tempC": 4, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 1,
                              "windspeedKph": 3, "windDirectionDeg": 340, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 93, "visibilityKm": 10, "pressureMb": 1012},
                             {"hour": 23, "tempC": 3, "weatherDesc": "Partly cloudy", "cloudCoverPct": 17, "uvIndex": 1,
                              "windspeedKph": 3, "windDirectionDeg": 346, "windDirectionCompass": "NNW",
                              "precipitationMm": 0, "humidityPct": 93, "visibilityKm": 10, "pressureMb": 1013}]}
        weather_data3 = {"date": "2021-08-01", "sunrise": "07:06:00", "sunset": "17:41:00", "moonrise": "00:45:00",
                         "moonset": "11:54:00", "moonPhase": "Last Quarter", "moonIlluminationPct": 40, "minTempC": 6,
                         "maxTempC": 13, "avgTempC": 12, "sunHours": 2.8, "uvIndex": 3,
                         "location": {"id": "5bea7b46-9809-4189-aafe-160208da94f7", "postcode": "6001", "name": "PERTH",
                                      "state": "WA", "latitude": "-31.9505269", "longitude": "115.8604572",
                                      "distanceToNearestWeatherStationMetres": 3672.959393589811,
                                      "nearestWeatherStation": {"name": "PERTH METRO", "state": "WA",
                                                                "latitude": "-31.9192", "longitude": "115.8728"}},
                         "hourlyWeatherHistory": [
                             {"hour": 0, "tempC": 6, "weatherDesc": "Overcast", "cloudCoverPct": 76, "uvIndex": 1,
                              "windspeedKph": 24, "windDirectionDeg": 284, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.4, "humidityPct": 80, "visibilityKm": 10, "pressureMb": 1015},
                             {"hour": 1, "tempC": 8, "weatherDesc": "Overcast", "cloudCoverPct": 81, "uvIndex": 1,
                              "windspeedKph": 27, "windDirectionDeg": 281, "windDirectionCompass": "WNW",
                              "precipitationMm": 0.2, "humidityPct": 80, "visibilityKm": 10, "pressureMb": 1014},
                             {"hour": 2, "tempC": 10, "weatherDesc": "Moderate or heavy rain shower",
                              "cloudCoverPct": 87, "uvIndex": 1, "windspeedKph": 29, "windDirectionDeg": 278,
                              "windDirectionCompass": "W", "precipitationMm": 0.3, "humidityPct": 80, "visibilityKm": 9,
                              "pressureMb": 1013},
                             {"hour": 3, "tempC": 13, "weatherDesc": "Moderate or heavy rain shower",
                              "cloudCoverPct": 92, "uvIndex": 1, "windspeedKph": 31, "windDirectionDeg": 276,
                              "windDirectionCompass": "W", "precipitationMm": 0.4, "humidityPct": 80, "visibilityKm": 9,
                              "pressureMb": 1012},
                             {"hour": 4, "tempC": 13, "weatherDesc": "Moderate or heavy rain shower",
                              "cloudCoverPct": 93, "uvIndex": 1, "windspeedKph": 33, "windDirectionDeg": 271,
                              "windDirectionCompass": "W", "precipitationMm": 0.2, "humidityPct": 79, "visibilityKm": 9,
                              "pressureMb": 1012},
                             {"hour": 5, "tempC": 13, "weatherDesc": "Overcast", "cloudCoverPct": 94, "uvIndex": 1,
                              "windspeedKph": 36, "windDirectionDeg": 266, "windDirectionCompass": "W",
                              "precipitationMm": 0.6, "humidityPct": 78, "visibilityKm": 8, "pressureMb": 1012},
                             {"hour": 6, "tempC": 13, "weatherDesc": "Overcast", "cloudCoverPct": 95, "uvIndex": 3,
                              "windspeedKph": 38, "windDirectionDeg": 261, "windDirectionCompass": "W",
                              "precipitationMm": 0.8, "humidityPct": 77, "visibilityKm": 8, "pressureMb": 1011},
                             {"hour": 7, "tempC": 12, "weatherDesc": "Overcast", "cloudCoverPct": 95, "uvIndex": 3,
                              "windspeedKph": 39, "windDirectionDeg": 253, "windDirectionCompass": "WSW",
                              "precipitationMm": 0.4, "humidityPct": 75, "visibilityKm": 9, "pressureMb": 1012},
                             {"hour": 8, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 95,
                              "uvIndex": 3, "windspeedKph": 40, "windDirectionDeg": 245, "windDirectionCompass": "WSW",
                              "precipitationMm": 0.1, "humidityPct": 73, "visibilityKm": 9, "pressureMb": 1012},
                             {"hour": 9, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 95,
                              "uvIndex": 3, "windspeedKph": 41, "windDirectionDeg": 236, "windDirectionCompass": "WSW",
                              "precipitationMm": 0.2, "humidityPct": 71, "visibilityKm": 10, "pressureMb": 1013},
                             {"hour": 10, "tempC": 12, "weatherDesc": "Patchy rain possible", "cloudCoverPct": 91,
                              "uvIndex": 3, "windspeedKph": 40, "windDirectionDeg": 233, "windDirectionCompass": "SW",
                              "precipitationMm": 0.1, "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1013},
                             {"hour": 11, "tempC": 12, "weatherDesc": "Cloudy", "cloudCoverPct": 88, "uvIndex": 3,
                              "windspeedKph": 39, "windDirectionDeg": 229, "windDirectionCompass": "SW",
                              "precipitationMm": 0.3, "humidityPct": 64, "visibilityKm": 9, "pressureMb": 1014},
                             {"hour": 12, "tempC": 12, "weatherDesc": "Cloudy", "cloudCoverPct": 85, "uvIndex": 3,
                              "windspeedKph": 37, "windDirectionDeg": 225, "windDirectionCompass": "SW",
                              "precipitationMm": 0.4, "humidityPct": 61, "visibilityKm": 9, "pressureMb": 1015},
                             {"hour": 13, "tempC": 12, "weatherDesc": "Cloudy", "cloudCoverPct": 82, "uvIndex": 3,
                              "windspeedKph": 36, "windDirectionDeg": 223, "windDirectionCompass": "SW",
                              "precipitationMm": 0.2, "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1015},
                             {"hour": 14, "tempC": 12, "weatherDesc": "Light rain shower", "cloudCoverPct": 78,
                              "uvIndex": 3, "windspeedKph": 35, "windDirectionDeg": 222, "windDirectionCompass": "SW",
                              "precipitationMm": 0, "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1015},
                             {"hour": 15, "tempC": 13, "weatherDesc": "Light rain shower", "cloudCoverPct": 75,
                              "uvIndex": 3, "windspeedKph": 33, "windDirectionDeg": 220, "windDirectionCompass": "SW",
                              "precipitationMm": 0, "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1016},
                             {"hour": 16, "tempC": 12, "weatherDesc": "Light rain shower", "cloudCoverPct": 63,
                              "uvIndex": 3, "windspeedKph": 30, "windDirectionDeg": 212, "windDirectionCompass": "SSW",
                              "precipitationMm": 0, "humidityPct": 59, "visibilityKm": 10, "pressureMb": 1017},
                             {"hour": 17, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 52,
                              "uvIndex": 4, "windspeedKph": 27, "windDirectionDeg": 204, "windDirectionCompass": "SSW",
                              "precipitationMm": 0.1, "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1018},
                             {"hour": 18, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 40,
                              "uvIndex": 1, "windspeedKph": 23, "windDirectionDeg": 197, "windDirectionCompass": "SSW",
                              "precipitationMm": 0.1, "humidityPct": 61, "visibilityKm": 10, "pressureMb": 1019},
                             {"hour": 19, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 32,
                              "uvIndex": 1, "windspeedKph": 19, "windDirectionDeg": 182, "windDirectionCompass": "S",
                              "precipitationMm": 0, "humidityPct": 63, "visibilityKm": 10, "pressureMb": 1020},
                             {"hour": 20, "tempC": 10, "weatherDesc": "Partly cloudy", "cloudCoverPct": 24,
                              "uvIndex": 1, "windspeedKph": 15, "windDirectionDeg": 168, "windDirectionCompass": "SSE",
                              "precipitationMm": 0, "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1020},
                             {"hour": 21, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 17, "uvIndex": 1,
                              "windspeedKph": 11, "windDirectionDeg": 154, "windDirectionCompass": "SSE",
                              "precipitationMm": 0, "humidityPct": 65, "visibilityKm": 10, "pressureMb": 1021},
                             {"hour": 22, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 44, "uvIndex": 1,
                              "windspeedKph": 9, "windDirectionDeg": 160, "windDirectionCompass": "SSE",
                              "precipitationMm": 0, "humidityPct": 67, "visibilityKm": 10, "pressureMb": 1021},
                             {"hour": 23, "tempC": 9, "weatherDesc": "Light rain shower", "cloudCoverPct": 72,
                              "uvIndex": 1, "windspeedKph": 8, "windDirectionDeg": 167, "windDirectionCompass": "SSE",
                              "precipitationMm": 0.1, "humidityPct": 69, "visibilityKm": 10, "pressureMb": 1021}]}
        self.assertEqual(cal.get_cloud_cover(weather_data1, 10), 67)
        self.assertEqual(cal.get_cloud_cover(weather_data2, 12), 59)
        self.assertEqual(cal.get_cloud_cover(weather_data3, 18), 40)

    def test_solar_energy_cal_without_future(self):
        """
        Tests the solar_energy_cal_without_future method in the Calculator class
        """
        postcode_data = [{"id": "5bea7b46-9809-4189-aafe-160208da94f7", "postcode": "6001", "name": "PERTH", "state": "WA",
          "latitude": "-31.9505269", "longitude": "115.8604572",
          "distanceToNearestWeatherStationMetres": 3672.959393589811,
          "nearestWeatherStation": {"name": "PERTH METRO", "state": "WA", "latitude": "-31.9192",
                                    "longitude": "115.8728"}}]

        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = postcode_data

            cal = Calculator()
            response = cal.get_link_weather("6001")

        mock_get.assert_called()

        weather_data = {"date": "2020-12-25", "sunrise": "05:10:00", "sunset": "19:24:00", "moonrise": "15:04:00",
         "moonset": "01:48:00", "moonPhase": "Waxing Gibbous", "moonIlluminationPct": 70, "minTempC": 27,
         "maxTempC": 36, "avgTempC": 33, "sunHours": 8.6, "uvIndex": 8,
         "location": {"id": "5bea7b46-9809-4189-aafe-160208da94f7", "postcode": "6001", "name": "PERTH", "state": "WA",
                      "latitude": "-31.9505269", "longitude": "115.8604572",
                      "distanceToNearestWeatherStationMetres": 3672.959393589811,
                      "nearestWeatherStation": {"name": "PERTH METRO", "state": "WA", "latitude": "-31.9192",
                                                "longitude": "115.8728"}}, "hourlyWeatherHistory": [
            {"hour": 0, "tempC": 29, "weatherDesc": "Partly cloudy", "cloudCoverPct": 1, "uvIndex": 1,
             "windspeedKph": 4, "windDirectionDeg": 122, "windDirectionCompass": "ESE", "precipitationMm": 0,
             "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 1, "tempC": 29, "weatherDesc": "Partly cloudy", "cloudCoverPct": 1, "uvIndex": 1,
             "windspeedKph": 4, "windDirectionDeg": 122, "windDirectionCompass": "ESE", "precipitationMm": 0,
             "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 2, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 2, "uvIndex": 1,
             "windspeedKph": 4, "windDirectionDeg": 123, "windDirectionCompass": "ESE", "precipitationMm": 0,
             "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 3, "tempC": 27, "weatherDesc": "Partly cloudy", "cloudCoverPct": 2, "uvIndex": 1,
             "windspeedKph": 4, "windDirectionDeg": 123, "windDirectionCompass": "ESE", "precipitationMm": 0,
             "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 4, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 3, "uvIndex": 1,
             "windspeedKph": 4, "windDirectionDeg": 152, "windDirectionCompass": "SSE", "precipitationMm": 0,
             "humidityPct": 23, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 5, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 4, "uvIndex": 1,
             "windspeedKph": 4, "windDirectionDeg": 182, "windDirectionCompass": "S", "precipitationMm": 0,
             "humidityPct": 22, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 6, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 5, "uvIndex": 7,
             "windspeedKph": 3, "windDirectionDeg": 211, "windDirectionCompass": "SSW", "precipitationMm": 0,
             "humidityPct": 22, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 7, "tempC": 30, "weatherDesc": "Partly cloudy", "cloudCoverPct": 8, "uvIndex": 7,
             "windspeedKph": 4, "windDirectionDeg": 248, "windDirectionCompass": "WSW", "precipitationMm": 0,
             "humidityPct": 21, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 8, "tempC": 31, "weatherDesc": "Partly cloudy", "cloudCoverPct": 11, "uvIndex": 8,
             "windspeedKph": 5, "windDirectionDeg": 286, "windDirectionCompass": "WNW", "precipitationMm": 0,
             "humidityPct": 19, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 9, "tempC": 32, "weatherDesc": "Partly cloudy", "cloudCoverPct": 13, "uvIndex": 8,
             "windspeedKph": 5, "windDirectionDeg": 324, "windDirectionCompass": "NW", "precipitationMm": 0,
             "humidityPct": 18, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 10, "tempC": 33, "weatherDesc": "Partly cloudy", "cloudCoverPct": 13, "uvIndex": 8,
             "windspeedKph": 8, "windDirectionDeg": 300, "windDirectionCompass": "WNW", "precipitationMm": 0,
             "humidityPct": 17, "visibilityKm": 10, "pressureMb": 1009},
            {"hour": 11, "tempC": 35, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 8,
             "windspeedKph": 11, "windDirectionDeg": 276, "windDirectionCompass": "W", "precipitationMm": 0,
             "humidityPct": 16, "visibilityKm": 10, "pressureMb": 1008},
            {"hour": 12, "tempC": 36, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 9,
             "windspeedKph": 14, "windDirectionDeg": 252, "windDirectionCompass": "WSW", "precipitationMm": 0,
             "humidityPct": 16, "visibilityKm": 10, "pressureMb": 1008},
            {"hour": 13, "tempC": 36, "weatherDesc": "Partly cloudy", "cloudCoverPct": 21, "uvIndex": 9,
             "windspeedKph": 17, "windDirectionDeg": 242, "windDirectionCompass": "WSW", "precipitationMm": 0,
             "humidityPct": 17, "visibilityKm": 10, "pressureMb": 1007},
            {"hour": 14, "tempC": 35, "weatherDesc": "Cloudy", "cloudCoverPct": 28, "uvIndex": 8, "windspeedKph": 19,
             "windDirectionDeg": 232, "windDirectionCompass": "SW", "precipitationMm": 0, "humidityPct": 19,
             "visibilityKm": 10, "pressureMb": 1007},
            {"hour": 15, "tempC": 35, "weatherDesc": "Cloudy", "cloudCoverPct": 35, "uvIndex": 8, "windspeedKph": 22,
             "windDirectionDeg": 223, "windDirectionCompass": "SW", "precipitationMm": 0, "humidityPct": 21,
             "visibilityKm": 10, "pressureMb": 1006},
            {"hour": 16, "tempC": 34, "weatherDesc": "Cloudy", "cloudCoverPct": 42, "uvIndex": 7, "windspeedKph": 21,
             "windDirectionDeg": 217, "windDirectionCompass": "SW", "precipitationMm": 0, "humidityPct": 24,
             "visibilityKm": 10, "pressureMb": 1006},
            {"hour": 17, "tempC": 33, "weatherDesc": "Partly cloudy", "cloudCoverPct": 48, "uvIndex": 8,
             "windspeedKph": 20, "windDirectionDeg": 212, "windDirectionCompass": "SSW", "precipitationMm": 0,
             "humidityPct": 27, "visibilityKm": 10, "pressureMb": 1006},
            {"hour": 18, "tempC": 32, "weatherDesc": "Partly cloudy", "cloudCoverPct": 54, "uvIndex": 1,
             "windspeedKph": 19, "windDirectionDeg": 207, "windDirectionCompass": "SSW", "precipitationMm": 0,
             "humidityPct": 30, "visibilityKm": 10, "pressureMb": 1006},
            {"hour": 19, "tempC": 31, "weatherDesc": "Partly cloudy", "cloudCoverPct": 42, "uvIndex": 1,
             "windspeedKph": 18, "windDirectionDeg": 196, "windDirectionCompass": "SSW", "precipitationMm": 0,
             "humidityPct": 34, "visibilityKm": 10, "pressureMb": 1007},
            {"hour": 20, "tempC": 30, "weatherDesc": "Partly cloudy", "cloudCoverPct": 30, "uvIndex": 1,
             "windspeedKph": 17, "windDirectionDeg": 186, "windDirectionCompass": "S", "precipitationMm": 0,
             "humidityPct": 37, "visibilityKm": 10, "pressureMb": 1007},
            {"hour": 21, "tempC": 29, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 1,
             "windspeedKph": 16, "windDirectionDeg": 175, "windDirectionCompass": "S", "precipitationMm": 0,
             "humidityPct": 40, "visibilityKm": 10, "pressureMb": 1008},
            {"hour": 22, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 28, "uvIndex": 1,
             "windspeedKph": 16, "windDirectionDeg": 159, "windDirectionCompass": "SSE", "precipitationMm": 0,
             "humidityPct": 42, "visibilityKm": 10, "pressureMb": 1008},
            {"hour": 23, "tempC": 28, "weatherDesc": "Partly cloudy", "cloudCoverPct": 39, "uvIndex": 1,
             "windspeedKph": 16, "windDirectionDeg": 142, "windDirectionCompass": "SE", "precipitationMm": 0,
             "humidityPct": 44, "visibilityKm": 10, "pressureMb": 1008}]}
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = weather_data

            cal = Calculator()
            response = cal.get_weather(postcode_data, "2020-12-25", "PERTH")

        mock_get.assert_called()
        self.assertEqual(cal.solar_energy_cal_without_future("2020-12-25", "6001", "08:00", "60", "PERTH"), (['5.6996'], [1.0]))

    def test_get_du(self):
        """
        Tests the get_du method in the Calculator class
        """
        cal1 = Calculator
        cal1.duration = 90
        cal1.start_time = "18:00"
        self.assertEqual(cal1.get_du(self), [1.0, 0.5])

        cal2 = Calculator
        cal2.duration = 45
        cal2. start_time = "05:30"
        self.assertEqual(cal2.get_du(self), [0.5, 0.25])

        cal3 = Calculator
        cal3.duration = 120
        cal3.start_time = "17:45"
        self.assertEqual(cal3.get_du(self), [0.25, 1.0, 0.75])

    def test_solar_energy_with_future(self):
        """
        Tests the solar_energy_with_future method in the Calculator class
        """
        postcode_data = [{"id": "22d72902-b72f-4ca0-a522-4dbfb77a7b78", "postcode": "7250", "name": "BLACKSTONE HEIGHTS",
          "state": "TAS", "latitude": "-41.46", "longitude": "147.0820001",
          "distanceToNearestWeatherStationMetres": 5607.391317385195,
          "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                    "longitude": "147.1219"}},{"id": "6d91c048-7178-4330-b792-30e53a702396", "postcode": "7250", "name": "EAST LAUNCESTON", "state": "TAS",
          "latitude": "-41.441944", "longitude": "147.150833",
          "distanceToNearestWeatherStationMetres": 1692.1148509532288,
          "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS", "latitude": "-41.4392",
                                    "longitude": "147.1708"}},{"id": "15b4a861-e97a-43fa-a0da-9953106b5554", "postcode": "7250", "name": "ELPHIN", "state": "TAS",
          "latitude": "-41.4309", "longitude": "147.155", "distanceToNearestWeatherStationMetres": 1608.3052577708138,
          "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS", "latitude": "-41.4392",
                                    "longitude": "147.1708"}},{"id": "5998b29a-8e3d-4c1e-857c-b5dce80eea6d", "postcode": "7250", "name": "LAUNCESTON", "state": "TAS",
          "latitude": "-41.4332215", "longitude": "147.1440875",
          "distanceToNearestWeatherStationMetres": 2323.920987503416,
          "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS", "latitude": "-41.4392",
                                    "longitude": "147.1708"}},{"id": "c9ba20ed-01b6-418e-8a61-b5f9ac5c7fe3", "postcode": "7250", "name": "NEWSTEAD", "state": "TAS",
          "latitude": "-41.444444", "longitude": "147.160556",
          "distanceToNearestWeatherStationMetres": 1033.9903037447873,
          "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS", "latitude": "-41.4392",
                                    "longitude": "147.1708"}},{"id": "ed442b26-492d-45ed-a2e7-2828c7e06d95", "postcode": "7250", "name": "NORWOOD", "state": "TAS",
          "latitude": "-41.457222", "longitude": "147.1725",
          "distanceToNearestWeatherStationMetres": 1223.5586202650989,
          "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                    "longitude": "147.1644"}},{"id": "572c0906-0a82-4102-94d2-bccf2ca97a38", "postcode": "7250", "name": "NORWOOD AVENUE PO", "state": "TAS",
          "latitude": "-41.4557", "longitude": "147.173", "distanceToNearestWeatherStationMetres": 1388.9427115766343,
          "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                    "longitude": "147.1644"}},{"id": "ea44f0b3-72ff-439f-b42a-e486ad7be323", "postcode": "7250", "name": "PROSPECT", "state": "TAS",
          "latitude": "-41.483333", "longitude": "147.139722",
          "distanceToNearestWeatherStationMetres": 2787.874138903107,
          "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                    "longitude": "147.1644"}},{"id": "6b791b5f-7ab3-4103-a4cc-5e860e935e0f", "postcode": "7250", "name": "PROSPECT VALE", "state": "TAS",
          "latitude": "-41.481", "longitude": "147.126", "distanceToNearestWeatherStationMetres": 3587.589454353829,
          "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                    "longitude": "147.1644"}},{"id": "4507ab34-3a2f-4610-8b9d-fcfdfecdca09", "postcode": "7250", "name": "RAVENSWOOD", "state": "TAS",
          "latitude": "-41.418333", "longitude": "147.176111",
          "distanceToNearestWeatherStationMetres": 2362.1755102588863,
          "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS", "latitude": "-41.4392",
                                    "longitude": "147.1708"}},{"id": "b4242da1-ff68-4ff9-88b6-59ea8baf1324", "postcode": "7250", "name": "RIVERSIDE", "state": "TAS",
          "latitude": "-41.42", "longitude": "147.103", "distanceToNearestWeatherStationMetres": 1577.355141403387,
          "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                    "longitude": "147.1219"}},{"id": "d52144b2-74f7-4fbc-9d5d-c8fd068da060", "postcode": "7250", "name": "ST LEONARDS", "state": "TAS",
          "latitude": "-41.4584", "longitude": "147.2008", "distanceToNearestWeatherStationMetres": 3160.908069109459,
          "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                    "longitude": "147.1644"}},{"id": "c3836b3d-8277-4cb4-9e9d-40adc7967a37", "postcode": "7250", "name": "SUMMERHILL", "state": "TAS",
          "latitude": "-41.4688362", "longitude": "147.1189067",
          "distanceToNearestWeatherStationMetres": 3800.246608736132,
          "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                    "longitude": "147.1644"}},{"id": "6bf11a0e-a46a-4dda-8991-92dcc5971c08", "postcode": "7250", "name": "TRAVELLERS REST", "state": "TAS",
          "latitude": "-41.494", "longitude": "147.09", "distanceToNearestWeatherStationMetres": 4032.586323471949,
          "nearestWeatherStation": {"name": "HADSPEN", "state": "TAS", "latitude": "-41.5157",
                                    "longitude": "147.0512"}},{"id": "d7d86087-771c-4754-92f6-cc4c31edc3d8", "postcode": "7250", "name": "TREVALLYN", "state": "TAS",
          "latitude": "-41.433333", "longitude": "147.116667",
          "distanceToNearestWeatherStationMetres": 1609.541131584532,
          "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                    "longitude": "147.1219"}},{"id": "8e688142-401c-4d48-a8a2-14721cb48a73", "postcode": "7250", "name": "WAVERLEY", "state": "TAS",
          "latitude": "-41.433333", "longitude": "147.183333",
          "distanceToNearestWeatherStationMetres": 1231.7292044665246,
          "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS", "latitude": "-41.4392",
                                    "longitude": "147.1708"}},{"id": "adb3614f-c464-4d9e-b731-ca4b5f5e9726", "postcode": "7250", "name": "WEST LAUNCESTON", "state": "TAS",
          "latitude": "-41.451", "longitude": "147.1292", "distanceToNearestWeatherStationMetres": 3396.576148167821,
          "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                    "longitude": "147.1644"}}]
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = postcode_data

            cal3 = Calculator()
            response = cal3.get_link_weather("7250")

        mock_get.assert_called()
        weather_data = {"date": "2021-02-22", "sunrise": "05:44:00", "sunset": "19:06:00", "moonrise": "15:43:00",
         "moonset": "00:01:00", "moonPhase": "Waxing Gibbous", "moonIlluminationPct": 73, "minTempC": 9, "maxTempC": 21,
         "avgTempC": 17, "sunHours": 5.8, "uvIndex": 5,
         "location": {"id": "5998b29a-8e3d-4c1e-857c-b5dce80eea6d", "postcode": "7250", "name": "LAUNCESTON",
                      "state": "TAS", "latitude": "-41.4332215", "longitude": "147.1440875",
                      "distanceToNearestWeatherStationMetres": 2323.920987503416,
                      "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                                "latitude": "-41.4392", "longitude": "147.1708"}},
         "hourlyWeatherHistory": [
             {"hour": 0, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 1, "uvIndex": 1,
              "windspeedKph": 2, "windDirectionDeg": 232, "windDirectionCompass": "SW", "precipitationMm": 0,
              "humidityPct": 89, "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 19, "tempC": 15, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 1,
              "windspeedKph": 11, "windDirectionDeg": 237, "windDirectionCompass": "WSW", "precipitationMm": 0,
              "humidityPct": 50, "visibilityKm": 10, "pressureMb": 1010},
             {"hour": 20, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 11, "uvIndex": 1,
              "windspeedKph": 9, "windDirectionDeg": 227, "windDirectionCompass": "SW", "precipitationMm": 0,
              "humidityPct": 55, "visibilityKm": 10, "pressureMb": 1011},
             {"hour": 21, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 9, "uvIndex": 1,
              "windspeedKph": 7, "windDirectionDeg": 217, "windDirectionCompass": "SW", "precipitationMm": 0,
              "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1012},
             {"hour": 22, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 7, "uvIndex": 1,
              "windspeedKph": 6, "windDirectionDeg": 212, "windDirectionCompass": "SSW", "precipitationMm": 0,
              "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1012},
             {"hour": 23, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 5, "uvIndex": 1,
              "windspeedKph": 4, "windDirectionDeg": 207, "windDirectionCompass": "SSW", "precipitationMm": 0,
              "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1012},
             {"hour": 1, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 3, "uvIndex": 1,
              "windspeedKph": 2, "windDirectionDeg": 258, "windDirectionCompass": "WSW", "precipitationMm": 0,
              "humidityPct": 91, "visibilityKm": 8, "pressureMb": 1007},
             {"hour": 2, "tempC": 11, "weatherDesc": "Clear", "cloudCoverPct": 6, "uvIndex": 1, "windspeedKph": 3,
              "windDirectionDeg": 284, "windDirectionCompass": "WNW", "precipitationMm": 0, "humidityPct": 93,
              "visibilityKm": 6, "pressureMb": 1006},
             {"hour": 3, "tempC": 9, "weatherDesc": "Clear", "cloudCoverPct": 9, "uvIndex": 1, "windspeedKph": 3,
              "windDirectionDeg": 310, "windDirectionCompass": "NW", "precipitationMm": 0, "humidityPct": 95,
              "visibilityKm": 5, "pressureMb": 1006},
             {"hour": 4, "tempC": 10, "weatherDesc": "Clear", "cloudCoverPct": 7, "uvIndex": 1, "windspeedKph": 4,
              "windDirectionDeg": 314, "windDirectionCompass": "NW", "precipitationMm": 0, "humidityPct": 93,
              "visibilityKm": 6, "pressureMb": 1006},
             {"hour": 5, "tempC": 10, "weatherDesc": "Mist", "cloudCoverPct": 6, "uvIndex": 1, "windspeedKph": 4,
              "windDirectionDeg": 319, "windDirectionCompass": "NW", "precipitationMm": 0, "humidityPct": 90,
              "visibilityKm": 6, "pressureMb": 1006},
             {"hour": 6, "tempC": 10, "weatherDesc": "Mist", "cloudCoverPct": 4, "uvIndex": 3, "windspeedKph": 4,
              "windDirectionDeg": 324, "windDirectionCompass": "NW", "precipitationMm": 0, "humidityPct": 88,
              "visibilityKm": 7, "pressureMb": 1007},
             {"hour": 7, "tempC": 12, "weatherDesc": "Mist", "cloudCoverPct": 3, "uvIndex": 3, "windspeedKph": 6,
              "windDirectionDeg": 313, "windDirectionCompass": "NW", "precipitationMm": 0, "humidityPct": 78,
              "visibilityKm": 8, "pressureMb": 1007},
             {"hour": 8, "tempC": 14, "weatherDesc": "Sunny", "cloudCoverPct": 1, "uvIndex": 4, "windspeedKph": 7,
              "windDirectionDeg": 303, "windDirectionCompass": "WNW", "precipitationMm": 0, "humidityPct": 68,
              "visibilityKm": 9, "pressureMb": 1007},
             {"hour": 9, "tempC": 16, "weatherDesc": "Sunny", "cloudCoverPct": 0, "uvIndex": 5, "windspeedKph": 8,
              "windDirectionDeg": 292, "windDirectionCompass": "WNW", "precipitationMm": 0, "humidityPct": 58,
              "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 10, "tempC": 18, "weatherDesc": "Sunny", "cloudCoverPct": 6, "uvIndex": 5, "windspeedKph": 10,
              "windDirectionDeg": 286, "windDirectionCompass": "WNW", "precipitationMm": 0, "humidityPct": 52,
              "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 11, "tempC": 19, "weatherDesc": "Sunny", "cloudCoverPct": 12, "uvIndex": 5, "windspeedKph": 11,
              "windDirectionDeg": 281, "windDirectionCompass": "W", "precipitationMm": 0, "humidityPct": 45,
              "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 12, "tempC": 21, "weatherDesc": "Sunny", "cloudCoverPct": 17, "uvIndex": 6, "windspeedKph": 13,
              "windDirectionDeg": 275, "windDirectionCompass": "W", "precipitationMm": 0, "humidityPct": 39,
              "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 13, "tempC": 20, "weatherDesc": "Sunny", "cloudCoverPct": 19, "uvIndex": 6, "windspeedKph": 14,
              "windDirectionDeg": 270, "windDirectionCompass": "W", "precipitationMm": 0, "humidityPct": 38,
              "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 14, "tempC": 20, "weatherDesc": "Partly cloudy", "cloudCoverPct": 20, "uvIndex": 5,
              "windspeedKph": 15, "windDirectionDeg": 264, "windDirectionCompass": "W", "precipitationMm": 0,
              "humidityPct": 38, "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 15, "tempC": 20, "weatherDesc": "Partly cloudy", "cloudCoverPct": 22, "uvIndex": 5,
              "windspeedKph": 16, "windDirectionDeg": 259, "windDirectionCompass": "WSW", "precipitationMm": 0,
              "humidityPct": 37, "visibilityKm": 10, "pressureMb": 1007},
             {"hour": 16, "tempC": 18, "weatherDesc": "Partly cloudy", "cloudCoverPct": 20, "uvIndex": 5,
              "windspeedKph": 15, "windDirectionDeg": 255, "windDirectionCompass": "WSW", "precipitationMm": 0,
              "humidityPct": 39, "visibilityKm": 10, "pressureMb": 1008},
             {"hour": 17, "tempC": 17, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 5,
              "windspeedKph": 14, "windDirectionDeg": 251, "windDirectionCompass": "WSW", "precipitationMm": 0,
              "humidityPct": 42, "visibilityKm": 10, "pressureMb": 1008},
             {"hour": 18, "tempC": 16, "weatherDesc": "Partly cloudy", "cloudCoverPct": 16, "uvIndex": 1,
              "windspeedKph": 13, "windDirectionDeg": 247, "windDirectionCompass": "WSW", "precipitationMm": 0,
              "humidityPct": 44, "visibilityKm": 10, "pressureMb": 1009}]}
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = weather_data

            response = cal3.get_weather(postcode_data, "2020-12-25", "Launceston")

        mock_get.assert_called()
        self.assertEqual(cal3.solar_energy_with_future("2020-12-23", "7250", "17:30", "45", "Launceston"), (['1.7772', '0.8034'], [0.5, 0.25]))

    def test_solar_energy_cal_preceeding_years(self):
        """
        Tests the solar_energy_cal_preceeding_years method in the Calculator class
        """
        postcode_data = [
            {"id": "22d72902-b72f-4ca0-a522-4dbfb77a7b78", "postcode": "7250", "name": "BLACKSTONE HEIGHTS",
             "state": "TAS", "latitude": "-41.46", "longitude": "147.0820001",
             "distanceToNearestWeatherStationMetres": 5607.391317385195,
             "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                       "longitude": "147.1219"}},
            {"id": "6d91c048-7178-4330-b792-30e53a702396", "postcode": "7250", "name": "EAST LAUNCESTON",
             "state": "TAS",
             "latitude": "-41.441944", "longitude": "147.150833",
             "distanceToNearestWeatherStationMetres": 1692.1148509532288,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "15b4a861-e97a-43fa-a0da-9953106b5554", "postcode": "7250", "name": "ELPHIN", "state": "TAS",
             "latitude": "-41.4309", "longitude": "147.155",
             "distanceToNearestWeatherStationMetres": 1608.3052577708138,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "5998b29a-8e3d-4c1e-857c-b5dce80eea6d", "postcode": "7250", "name": "LAUNCESTON", "state": "TAS",
             "latitude": "-41.4332215", "longitude": "147.1440875",
             "distanceToNearestWeatherStationMetres": 2323.920987503416,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "c9ba20ed-01b6-418e-8a61-b5f9ac5c7fe3", "postcode": "7250", "name": "NEWSTEAD", "state": "TAS",
             "latitude": "-41.444444", "longitude": "147.160556",
             "distanceToNearestWeatherStationMetres": 1033.9903037447873,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "ed442b26-492d-45ed-a2e7-2828c7e06d95", "postcode": "7250", "name": "NORWOOD", "state": "TAS",
             "latitude": "-41.457222", "longitude": "147.1725",
             "distanceToNearestWeatherStationMetres": 1223.5586202650989,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "572c0906-0a82-4102-94d2-bccf2ca97a38", "postcode": "7250", "name": "NORWOOD AVENUE PO",
             "state": "TAS",
             "latitude": "-41.4557", "longitude": "147.173",
             "distanceToNearestWeatherStationMetres": 1388.9427115766343,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "ea44f0b3-72ff-439f-b42a-e486ad7be323", "postcode": "7250", "name": "PROSPECT", "state": "TAS",
             "latitude": "-41.483333", "longitude": "147.139722",
             "distanceToNearestWeatherStationMetres": 2787.874138903107,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "6b791b5f-7ab3-4103-a4cc-5e860e935e0f", "postcode": "7250", "name": "PROSPECT VALE", "state": "TAS",
             "latitude": "-41.481", "longitude": "147.126", "distanceToNearestWeatherStationMetres": 3587.589454353829,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "4507ab34-3a2f-4610-8b9d-fcfdfecdca09", "postcode": "7250", "name": "RAVENSWOOD", "state": "TAS",
             "latitude": "-41.418333", "longitude": "147.176111",
             "distanceToNearestWeatherStationMetres": 2362.1755102588863,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "b4242da1-ff68-4ff9-88b6-59ea8baf1324", "postcode": "7250", "name": "RIVERSIDE", "state": "TAS",
             "latitude": "-41.42", "longitude": "147.103", "distanceToNearestWeatherStationMetres": 1577.355141403387,
             "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                       "longitude": "147.1219"}},
            {"id": "d52144b2-74f7-4fbc-9d5d-c8fd068da060", "postcode": "7250", "name": "ST LEONARDS", "state": "TAS",
             "latitude": "-41.4584", "longitude": "147.2008",
             "distanceToNearestWeatherStationMetres": 3160.908069109459,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "c3836b3d-8277-4cb4-9e9d-40adc7967a37", "postcode": "7250", "name": "SUMMERHILL", "state": "TAS",
             "latitude": "-41.4688362", "longitude": "147.1189067",
             "distanceToNearestWeatherStationMetres": 3800.246608736132,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}},
            {"id": "6bf11a0e-a46a-4dda-8991-92dcc5971c08", "postcode": "7250", "name": "TRAVELLERS REST",
             "state": "TAS",
             "latitude": "-41.494", "longitude": "147.09", "distanceToNearestWeatherStationMetres": 4032.586323471949,
             "nearestWeatherStation": {"name": "HADSPEN", "state": "TAS", "latitude": "-41.5157",
                                       "longitude": "147.0512"}},
            {"id": "d7d86087-771c-4754-92f6-cc4c31edc3d8", "postcode": "7250", "name": "TREVALLYN", "state": "TAS",
             "latitude": "-41.433333", "longitude": "147.116667",
             "distanceToNearestWeatherStationMetres": 1609.541131584532,
             "nearestWeatherStation": {"name": "LAUNCESTON (TI TREE BEND)", "state": "TAS", "latitude": "-41.4194",
                                       "longitude": "147.1219"}},
            {"id": "8e688142-401c-4d48-a8a2-14721cb48a73", "postcode": "7250", "name": "WAVERLEY", "state": "TAS",
             "latitude": "-41.433333", "longitude": "147.183333",
             "distanceToNearestWeatherStationMetres": 1231.7292044665246,
             "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)", "state": "TAS",
                                       "latitude": "-41.4392",
                                       "longitude": "147.1708"}},
            {"id": "adb3614f-c464-4d9e-b731-ca4b5f5e9726", "postcode": "7250", "name": "WEST LAUNCESTON",
             "state": "TAS",
             "latitude": "-41.451", "longitude": "147.1292", "distanceToNearestWeatherStationMetres": 3396.576148167821,
             "nearestWeatherStation": {"name": "LAUNCESTON (KINGS MEADOWS)", "state": "TAS", "latitude": "-41.4664",
                                       "longitude": "147.1644"}}]
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = postcode_data

            cal2 = Calculator()
            response = cal2.get_link_weather("7250")

        mock_get.assert_called()
        weather_data = {"date": "2021-02-22", "sunrise": "05:44:00", "sunset": "19:06:00", "moonrise": "15:43:00",
                        "moonset": "00:01:00", "moonPhase": "Waxing Gibbous", "moonIlluminationPct": 73, "minTempC": 9,
                        "maxTempC": 21,
                        "avgTempC": 17, "sunHours": 5.8, "uvIndex": 5,
                        "location": {"id": "5998b29a-8e3d-4c1e-857c-b5dce80eea6d", "postcode": "7250",
                                     "name": "LAUNCESTON",
                                     "state": "TAS", "latitude": "-41.4332215", "longitude": "147.1440875",
                                     "distanceToNearestWeatherStationMetres": 2323.920987503416,
                                     "nearestWeatherStation": {"name": "HOBLERS BRIDGE (NORTH ESK RIVER)",
                                                               "state": "TAS",
                                                               "latitude": "-41.4392", "longitude": "147.1708"}},
                        "hourlyWeatherHistory": [
                            {"hour": 0, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 1, "uvIndex": 1,
                             "windspeedKph": 2, "windDirectionDeg": 232, "windDirectionCompass": "SW",
                             "precipitationMm": 0,
                             "humidityPct": 89, "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 19, "tempC": 15, "weatherDesc": "Partly cloudy", "cloudCoverPct": 14, "uvIndex": 1,
                             "windspeedKph": 11, "windDirectionDeg": 237, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 50, "visibilityKm": 10, "pressureMb": 1010},
                            {"hour": 20, "tempC": 13, "weatherDesc": "Partly cloudy", "cloudCoverPct": 11, "uvIndex": 1,
                             "windspeedKph": 9, "windDirectionDeg": 227, "windDirectionCompass": "SW",
                             "precipitationMm": 0,
                             "humidityPct": 55, "visibilityKm": 10, "pressureMb": 1011},
                            {"hour": 21, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 9, "uvIndex": 1,
                             "windspeedKph": 7, "windDirectionDeg": 217, "windDirectionCompass": "SW",
                             "precipitationMm": 0,
                             "humidityPct": 60, "visibilityKm": 10, "pressureMb": 1012},
                            {"hour": 22, "tempC": 11, "weatherDesc": "Partly cloudy", "cloudCoverPct": 7, "uvIndex": 1,
                             "windspeedKph": 6, "windDirectionDeg": 212, "windDirectionCompass": "SSW",
                             "precipitationMm": 0,
                             "humidityPct": 64, "visibilityKm": 10, "pressureMb": 1012},
                            {"hour": 23, "tempC": 9, "weatherDesc": "Partly cloudy", "cloudCoverPct": 5, "uvIndex": 1,
                             "windspeedKph": 4, "windDirectionDeg": 207, "windDirectionCompass": "SSW",
                             "precipitationMm": 0,
                             "humidityPct": 68, "visibilityKm": 10, "pressureMb": 1012},
                            {"hour": 1, "tempC": 12, "weatherDesc": "Partly cloudy", "cloudCoverPct": 3, "uvIndex": 1,
                             "windspeedKph": 2, "windDirectionDeg": 258, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 91, "visibilityKm": 8, "pressureMb": 1007},
                            {"hour": 2, "tempC": 11, "weatherDesc": "Clear", "cloudCoverPct": 6, "uvIndex": 1,
                             "windspeedKph": 3,
                             "windDirectionDeg": 284, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 93,
                             "visibilityKm": 6, "pressureMb": 1006},
                            {"hour": 3, "tempC": 9, "weatherDesc": "Clear", "cloudCoverPct": 9, "uvIndex": 1,
                             "windspeedKph": 3,
                             "windDirectionDeg": 310, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 95,
                             "visibilityKm": 5, "pressureMb": 1006},
                            {"hour": 4, "tempC": 10, "weatherDesc": "Clear", "cloudCoverPct": 7, "uvIndex": 1,
                             "windspeedKph": 4,
                             "windDirectionDeg": 314, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 93,
                             "visibilityKm": 6, "pressureMb": 1006},
                            {"hour": 5, "tempC": 10, "weatherDesc": "Mist", "cloudCoverPct": 6, "uvIndex": 1,
                             "windspeedKph": 4,
                             "windDirectionDeg": 319, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 90,
                             "visibilityKm": 6, "pressureMb": 1006},
                            {"hour": 6, "tempC": 10, "weatherDesc": "Mist", "cloudCoverPct": 4, "uvIndex": 3,
                             "windspeedKph": 4,
                             "windDirectionDeg": 324, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 88,
                             "visibilityKm": 7, "pressureMb": 1007},
                            {"hour": 7, "tempC": 12, "weatherDesc": "Mist", "cloudCoverPct": 3, "uvIndex": 3,
                             "windspeedKph": 6,
                             "windDirectionDeg": 313, "windDirectionCompass": "NW", "precipitationMm": 0,
                             "humidityPct": 78,
                             "visibilityKm": 8, "pressureMb": 1007},
                            {"hour": 8, "tempC": 14, "weatherDesc": "Sunny", "cloudCoverPct": 1, "uvIndex": 4,
                             "windspeedKph": 7,
                             "windDirectionDeg": 303, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 68,
                             "visibilityKm": 9, "pressureMb": 1007},
                            {"hour": 9, "tempC": 16, "weatherDesc": "Sunny", "cloudCoverPct": 0, "uvIndex": 5,
                             "windspeedKph": 8,
                             "windDirectionDeg": 292, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 58,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 10, "tempC": 18, "weatherDesc": "Sunny", "cloudCoverPct": 6, "uvIndex": 5,
                             "windspeedKph": 10,
                             "windDirectionDeg": 286, "windDirectionCompass": "WNW", "precipitationMm": 0,
                             "humidityPct": 52,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 11, "tempC": 19, "weatherDesc": "Sunny", "cloudCoverPct": 12, "uvIndex": 5,
                             "windspeedKph": 11,
                             "windDirectionDeg": 281, "windDirectionCompass": "W", "precipitationMm": 0,
                             "humidityPct": 45,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 12, "tempC": 21, "weatherDesc": "Sunny", "cloudCoverPct": 17, "uvIndex": 6,
                             "windspeedKph": 13,
                             "windDirectionDeg": 275, "windDirectionCompass": "W", "precipitationMm": 0,
                             "humidityPct": 39,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 13, "tempC": 20, "weatherDesc": "Sunny", "cloudCoverPct": 19, "uvIndex": 6,
                             "windspeedKph": 14,
                             "windDirectionDeg": 270, "windDirectionCompass": "W", "precipitationMm": 0,
                             "humidityPct": 38,
                             "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 14, "tempC": 20, "weatherDesc": "Partly cloudy", "cloudCoverPct": 20, "uvIndex": 5,
                             "windspeedKph": 15, "windDirectionDeg": 264, "windDirectionCompass": "W",
                             "precipitationMm": 0,
                             "humidityPct": 38, "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 15, "tempC": 20, "weatherDesc": "Partly cloudy", "cloudCoverPct": 22, "uvIndex": 5,
                             "windspeedKph": 16, "windDirectionDeg": 259, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 37, "visibilityKm": 10, "pressureMb": 1007},
                            {"hour": 16, "tempC": 18, "weatherDesc": "Partly cloudy", "cloudCoverPct": 20, "uvIndex": 5,
                             "windspeedKph": 15, "windDirectionDeg": 255, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 39, "visibilityKm": 10, "pressureMb": 1008},
                            {"hour": 17, "tempC": 17, "weatherDesc": "Partly cloudy", "cloudCoverPct": 18, "uvIndex": 5,
                             "windspeedKph": 14, "windDirectionDeg": 251, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 42, "visibilityKm": 10, "pressureMb": 1008},
                            {"hour": 18, "tempC": 16, "weatherDesc": "Partly cloudy", "cloudCoverPct": 16, "uvIndex": 1,
                             "windspeedKph": 13, "windDirectionDeg": 247, "windDirectionCompass": "WSW",
                             "precipitationMm": 0,
                             "humidityPct": 44, "visibilityKm": 10, "pressureMb": 1009}]}
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = weather_data

            response = cal2.get_weather(postcode_data, "2020-12-25", "Launceston")

        mock_get.assert_called()

        self.assertEqual(cal2.solar_energy_cal_preceeding_years("2020-12-25", "7250", "17:30", "45", "Launceston"),
                         [(['1.7772', '0.8034'], [0.5, 0.25]),
                          (['1.3059', '0.5912'], [0.5, 0.25]),
                          (['0.7673', '0.4011'], [0.5, 0.25])])

    def test_get_link_weather(self):
        """
        Tests the get_link_weather method in the Calculator class
        """
        postcode_data = [{"id":"ab9f494f-f8a0-4c24-bd2e-2497b99f2258","postcode":"3800","name":"MONASH UNIVERSITY","state":"VIC","latitude":"-37.9105599","longitude":"145.1362485","distanceToNearestWeatherStationMetres":3771.993796218797,"nearestWeatherStation":{"name":"OAKLEIGH (METROPOLITAN GOLF CLUB)","state":"VIC","latitude":"-37.9142","longitude":"145.0935"}}]
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = postcode_data

            cal = Calculator()
            response = cal.get_link_weather("3800")

        self.assertEqual(response[0]['id'], "ab9f494f-f8a0-4c24-bd2e-2497b99f2258")
        mock_get.assert_called()

    def test_get_weather(self):
        """
        Tests the get_weather method in the Calculator class
        """
        postcode_data = Calculator.get_link_weather(self, "3800")
        weather_data = {"date":"2021-08-01","sunrise":"07:20:00","sunset":"17:32:00","moonrise":"00:52:00","moonset":"11:45:00","moonPhase":"Last Quarter","moonIlluminationPct":40,"minTempC":9,"maxTempC":14,"avgTempC":11,"sunHours":3.2,"uvIndex":3,"location":{"id":"ab9f494f-f8a0-4c24-bd2e-2497b99f2258","postcode":"3800","name":"MONASH UNIVERSITY","state":"VIC","latitude":"-37.9105599","longitude":"145.1362485","distanceToNearestWeatherStationMetres":3771.993796218797,"nearestWeatherStation":{"name":"OAKLEIGH (METROPOLITAN GOLF CLUB)","state":"VIC","latitude":"-37.9142","longitude":"145.0935"}},"hourlyWeatherHistory":[{"hour":0,"tempC":10,"weatherDesc":"Heavy rain","cloudCoverPct":100,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":349,"windDirectionCompass":"N","precipitationMm":2.9,"humidityPct":90,"visibilityKm":3,"pressureMb":1007},{"hour":1,"tempC":10,"weatherDesc":"Heavy rain","cloudCoverPct":94,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":342,"windDirectionCompass":"NNW","precipitationMm":1.4,"humidityPct":90,"visibilityKm":4,"pressureMb":1008},{"hour":2,"tempC":10,"weatherDesc":"Light drizzle","cloudCoverPct":87,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":336,"windDirectionCompass":"NNW","precipitationMm":0.2,"humidityPct":90,"visibilityKm":5,"pressureMb":1008},{"hour":3,"tempC":10,"weatherDesc":"Light drizzle","cloudCoverPct":81,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":329,"windDirectionCompass":"NNW","precipitationMm":0.3,"humidityPct":90,"visibilityKm":7,"pressureMb":1008},{"hour":4,"tempC":9,"weatherDesc":"Light drizzle","cloudCoverPct":79,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":325,"windDirectionCompass":"NW","precipitationMm":0.2,"humidityPct":90,"visibilityKm":8,"pressureMb":1009},{"hour":5,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":78,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":321,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":91,"visibilityKm":9,"pressureMb":1009},{"hour":6,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":76,"uvIndex":2,"windspeedKph":10,"windDirectionDeg":318,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":91,"visibilityKm":10,"pressureMb":1010},{"hour":7,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":78,"uvIndex":2,"windspeedKph":10,"windDirectionDeg":312,"windDirectionCompass":"NW","precipitationMm":0.1,"humidityPct":88,"visibilityKm":10,"pressureMb":1010},{"hour":8,"tempC":9,"weatherDesc":"Patchy rain possible","cloudCoverPct":80,"uvIndex":2,"windspeedKph":11,"windDirectionDeg":307,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":86,"visibilityKm":10,"pressureMb":1011},{"hour":9,"tempC":10,"weatherDesc":"Patchy rain possible","cloudCoverPct":82,"uvIndex":2,"windspeedKph":11,"windDirectionDeg":301,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":84,"visibilityKm":10,"pressureMb":1011},{"hour":10,"tempC":11,"weatherDesc":"Patchy rain possible","cloudCoverPct":67,"uvIndex":3,"windspeedKph":11,"windDirectionDeg":291,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1011},{"hour":11,"tempC":11,"weatherDesc":"Patchy rain possible","cloudCoverPct":51,"uvIndex":3,"windspeedKph":12,"windDirectionDeg":281,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":71,"visibilityKm":10,"pressureMb":1011},{"hour":12,"tempC":12,"weatherDesc":"Patchy rain possible","cloudCoverPct":35,"uvIndex":3,"windspeedKph":12,"windDirectionDeg":271,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":65,"visibilityKm":10,"pressureMb":1011},{"hour":13,"tempC":13,"weatherDesc":"Patchy rain possible","cloudCoverPct":30,"uvIndex":3,"windspeedKph":11,"windDirectionDeg":263,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":62,"visibilityKm":10,"pressureMb":1011},{"hour":14,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":24,"uvIndex":4,"windspeedKph":11,"windDirectionDeg":255,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":59,"visibilityKm":10,"pressureMb":1011},{"hour":15,"tempC":14,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":4,"windspeedKph":10,"windDirectionDeg":248,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":56,"visibilityKm":10,"pressureMb":1011},{"hour":16,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":4,"windspeedKph":9,"windDirectionDeg":233,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":60,"visibilityKm":10,"pressureMb":1012},{"hour":17,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":19,"uvIndex":4,"windspeedKph":8,"windDirectionDeg":219,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":64,"visibilityKm":10,"pressureMb":1012},{"hour":18,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":19,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":204,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1013},{"hour":19,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":16,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":158,"windDirectionCompass":"SSE","precipitationMm":0,"humidityPct":71,"visibilityKm":10,"pressureMb":1014},{"hour":20,"tempC":10,"weatherDesc":"Partly cloudy","cloudCoverPct":13,"uvIndex":1,"windspeedKph":5,"windDirectionDeg":111,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":74,"visibilityKm":10,"pressureMb":1014},{"hour":21,"tempC":10,"weatherDesc":"Partly cloudy","cloudCoverPct":10,"uvIndex":1,"windspeedKph":5,"windDirectionDeg":64,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":77,"visibilityKm":10,"pressureMb":1015},{"hour":22,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":8,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":84,"windDirectionCompass":"E","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1015},{"hour":23,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":1,"windspeedKph":8,"windDirectionDeg":104,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1016}]}
        with patch('app.calculator.requests.get') as mock_get:
            mock_get.return_value.json.return_value = weather_data

            cal = Calculator()
            response = cal.get_weather(postcode_data, "2021-08-01", "MONASH UNIVERSITY")

        self.assertEqual(response["sunrise"], "07:20:00")
        self.assertEqual(response["sunset"], "17:32:00")
        mock_get.assert_called()

    def test_check_date(self):
        """
        Tests the check_date method in the Calculator class
        """
        cal = Calculator()
        date1 = "2022-08-22"
        date2 = "2030-01-30"
        date3 = "2035-09-20"
        self.assertEqual(cal.check_date(date1), "2021-08-22")
        self.assertEqual(cal.check_date(date2), "2021-01-30")
        self.assertEqual(cal.check_date(date3), "2021-09-20")

    def test_format_date(self):
        """
        Tests the format_date method in the Calculator class
        """
        cal = Calculator()
        date = "2021/08/01"
        date2 = "2021/09/21"
        date3 = "2008/08/13"
        self.assertEqual(cal.format_date(date), "01-08-2021")
        self.assertEqual(cal.format_date(date2), "21-09-2021")
        self.assertEqual(cal.format_date(date3), "13-08-2008")


if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suit)
