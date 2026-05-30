import os
import requests
from datetime import datetime
MY_LAT = 41.157944 # Your latitude
MY_LONG = -8.629105 # Your longitude
dir_path = os.path.dirname(os.path.realpath(__file__)) # get the path of the current file

def is_iss_overhead():
    """
    Get if iss is overhead
    :return: true if iss is overhead, false otherwise
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")  # get request
    response.raise_for_status() # raise an error if the status code is not 200
    data = response.json() # get the data from the response

    iss_latitude = float(data["iss_position"]["latitude"]) # get the latitude and longitude of the ISS
    iss_longitude = float(data["iss_position"]["longitude"]) # get the latitude and longitude of the ISS

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5: # Determines if ISS position is within a proximity threshold
        return True
    else:
        return False
def is_night():
    """
    Get if it is night
    :return: true if it is night, false otherwise
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) # get request
    response.raise_for_status() # raise an error if the status code is not 200
    data = response.json() # get the data from the response

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # get the sunrise time
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) # get the sunset time

    now = datetime.now().hour # get the current time

    if now >= sunset or now <= sunrise: # Determines if it is night
        return True
    else:
        return False

if is_iss_overhead() and is_night(): # Determines if it is night and iss is overhead
    # send email
    print("It is night and iss is overhead")