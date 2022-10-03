import pandas as pd
from class_journey import journey
from class_station import station
from datetime import (
    datetime,
    date,
    time)

# Use the read_csv method to make a dataframe from
# the csv file:
cycle_data = pd.read_csv('cyclingtrips_Sep2019.csv')

# Set N equal to total number of cycle trips in cycle_data
N = len(cycle_data)

# Initiate empty dictionary to store each station as an instance of class_station,
# where each unique station_id will be the key for the corresponding station object
station_data = {}

# Initiate empty list to store each cycle trip as an instance of class_journey
journey_data = []


# Loop through every cycle trip in cycle_data
for i in range(N):

    # Check if we have already instantiated the start station as a value in station_data.
    # If not, instantiate the start station as a station object and include as a value in
    # station_data with key equal to the corresponding start_station_id
    start_station_id = cycle_data.iloc[i]['start_station_id']
    if start_station_id in station_data:
        pass
    else:
        start_station_name = cycle_data.iloc[i]['start_station_name']
        start_station_description = cycle_data.iloc[i]['start_station_description']
        start_station_latitude = float(cycle_data.iloc[i]['start_station_latitude'])
        start_station_longitude = float(cycle_data.iloc[i]['start_station_longitude'])

        station_data[start_station_id] = station(start_station_id, start_station_name, start_station_description, start_station_latitude, start_station_longitude)

    start_station = station_data[start_station_id]


    # Check if we have already instantiated the end station as a value in station_data.
    # If not, instantiate the end station as a station object and include as a value in
    # station_data with key equal to the corresponding end_station_id
    end_station_id = cycle_data.iloc[i]['end_station_id']
    if end_station_id in station_data:
        pass
    else:
        end_station_name = cycle_data.iloc[i]['end_station_name']
        end_station_description = cycle_data.iloc[i]['end_station_description']
        end_station_latitude = float(cycle_data.iloc[i]['end_station_latitude'])
        end_station_longitude = float(cycle_data.iloc[i]['end_station_longitude'])

        station_data[end_station_id] = station(end_station_id, end_station_name, end_station_description, end_station_latitude, end_station_longitude)

    end_station = station_data[end_station_id]


    # Extract aware datetime objects (i.e with timezone info) from started_at and ended_at strings.
    started_at_datetime = datetime.fromisoformat(cycle_data.iloc[i]['started_at'])
    journey_start_time = started_at_datetime.timetz()
    journey_start_date = started_at_datetime.date()
    ended_at_datetime = datetime.fromisoformat(cycle_data.iloc[i]['ended_at'])
    journey_end_time = ended_at_datetime.timetz()
    journey_end_date = ended_at_datetime.date()

    # Extract duration in seconds of each journey as an integer.
    journey_duration = int(cycle_data.iloc[i]['duration'])

    # instantiate each cycle trip as a journey object and append to journey_data.
    journey_data.append(journey(start_time = journey_start_time, start_date = journey_start_date, end_time = journey_end_time, end_date = journey_end_date, duration = journey_duration, start_station = start_station, end_station = start_station))
