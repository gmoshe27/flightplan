#!/usr/bin/python3
from settings import Settings
from commute import Commute

if __name__ == "__main__":
    settings = Settings("commute_config.ini")
    settings.read_config()

    commute = Commute(settings)

    print ("getting morning commute...")
    commute.morning_commute()
    print ("getting evening commute...")
    commute.evening_commute()
