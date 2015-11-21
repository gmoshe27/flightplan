import requests
from datetime import datetime, timedelta
from pytz import timezone

class Commute(object):
    def __init__(self, settings):
        self.settings = settings

    def get_distance(self, departure_time):
        uri = "https://maps.googleapis.com/maps/api/distancematrix/json"
        params = {
            "origins": self.settings.get_home_address(),
            "destinations": self.settings.get_work_address(),
            "mode": "driving",
            "traffic_model": "best_guess",
            "departure_time": departure_time,
            "key": self.settings.get_api_key() 
        }

        response = requests.get(uri, params=params)
        return response

    def get_posix_datetime(self, date):
        eastern = timezone('US/Eastern')
        epoch = datetime(1970, 1, 1, tzinfo=timezone('UTC'))
        est = eastern.localize(date)
        return int((est - epoch).total_seconds())

    def write_details(self, response, date, csv_file):
        day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        json = response.json()
        details = json["rows"][0]["elements"][0]
        line = "{0}, {1}, {2}, {3}\n".format(
            day_of_week[date.isoweekday()],
            date,
            details["duration_in_traffic"]["text"],
            details["duration_in_traffic"]["value"])

        csv_file.write(line)

    def get_commute(self, start_date, start_hour, end_hour, start_minute, output_file):
        minute = start_minute
        for hour in range(start_hour, end_hour):
            while minute < 60:
                commute_date = start_date.replace(hour=hour, minute=minute)
                flight_time = self.get_posix_datetime(commute_date)

                r = self.get_distance(flight_time)
                self.write_details(r, commute_date, output_file)

                minute += 10

            minute = 0

    def morning_commute(self):
        day_of_week = datetime(2015, 11, 23)
        to_work = open("to_work.csv", "wt")

        #start on Monday and go to Friday
        for day_offset in range(0, 5):
            date = day_of_week + timedelta(day_offset)

            # get the driving distance and best guess for leaving every 10 minutes starting at 6:30am
            self.get_commute(date, 6, 10, 30, to_work)

        to_work.close()

    def evening_commute(self):
        day_of_week = datetime(2015, 11, 23)
        from_work = open("from_work.csv", "wt")

        #start on Monday and go to Friday
        for day_offset in range(0, 5):
            date = day_of_week + timedelta(day_offset)

            # get the driving distance and best guess for leaving every 10 minutes starting at 6:30am
            self.get_commute(date, 4, 10, 0, from_work)

        from_work.close()

    def test_query(self):
        # start on monday and go until Friday
        day_of_week = datetime(2015, 11, 23)
        date = day_of_week.replace(hour=6, minute=30)
        flight_time = get_posix_datetime(date)
        r = get_distance(flight_time)
        json = r.json()
        print(json["rows"][0]["elements"][0]["duration_in_traffic"]["text"])
