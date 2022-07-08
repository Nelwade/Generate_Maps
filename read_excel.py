from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import pandas as pd
import numpy as np
import time

df = pd.read_excel('accidents_database.xlsx')


def locator(address):
    geolocator = Nominatim(user_agent="myApp", timeout=10)
    location = geolocator.geocode(address)
    try:
        return location.latitude, location.longitude
    except AttributeError:
        return np.nan, np.nan
    except TimeoutError:
        time.sleep(1)
        locator(address)

df['LATITUDE'], df['LONGITUDE'] = zip(*df['LOCATION'].apply(locator))
df.to_excel('new_database.xlsx')
# print(df)