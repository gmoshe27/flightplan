# flightplan
A script to help figure out commute times between work and home. Built using python 3.4.

# Setup
You'll need to get an api key from google to use their [distance matrix api](https://developers.google.com/maps/documentation/distance-matrix/).
Once you get the api key, enter the public key into the `commute_config.ini`. Also enter your home address and work address into the config file.

# Usage
Run the flightplan application, `python flight_plan.py` and you will get two files, `to_work.csv` and `from_work.csv`. Each file will have
details about the trip time using the [best guess](https://developers.google.com/maps/documentation/distance-matrix/intro#traffic-model) model
to return the duration in traffic for each commute's starting time. Right now the commute times are hard coded as starting at 6:30am in the morning until
10am and returning from 4pm in the afternoon until 10pm, M-F. Travel duration is calculated in 10 minute increments of the starting time.

# TODO
* The date of the query is hardcoded
* the start/end times for the to and from work locations are hardcoded
* the output is in csv, but should be output to a database
* it would be cool to have this setup as a service that emails the flight plan to you about 20 minutes in advance

