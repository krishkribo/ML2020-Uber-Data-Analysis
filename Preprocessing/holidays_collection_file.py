import holidays
import os
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from tqdm import tqdm
import multiprocessing
from datetime import date
import json


def get_geolocation(geo_locator):
	reverse = RateLimiter(geo_locator.reverse,min_delay_seconds = 1)
	df['address'] = df['location'].progress_apply(reverse)
	df['state'] = [ad.raw['address'].get('state','null') for ad in df['address']]
	df['city'] = [ad.raw['address'].get('city','null') for ad in df['address']]

def get_holiday(date_year,state):
	d = int(date_year.split('/')[1])
	m = int(date_year.split('/')[0])
	y = int(date_year.split('/')[-1])
	res = ""
	date_value = date(y,m,d)
	NY_holiday = holidays.CountryHoliday('US',state=state)

	if len(pd.bdate_range(date_value,date_value)) == 1:
		if date(y,m,d) in NY_holiday:
			res = "holiday"
		else:
			res = "weekday"
	elif len(pd.bdate_range(date_value,date_value)) == 0:
		if (date(y,m,d) in NY_holiday) == True:
			res = "holiday"
		else:
			res = "weekend"
	return res


# uncomment if you are using the geopy lib
tqdm.pandas()

# intialize the geo-coder
geo_locator = Nominatim(user_agent = 'geoapiExercises')
# path handelling
os.chdir(r"/media/krishna/My Directory/University files/2020-2021/1b/Machine Learning/Project/Uber-data-analysis/")
data = os.listdir('Uber-dataset')
data_new = []
for d in data:
	tmp = d.split('.')
	if tmp[-1] == 'csv':
		data_new.append(d)

# add the month and year to the holiday columns
month_year = [d.split("-")[-1].split(".")[0] for d in data_new]
uber_dir = os.getcwd()
os.chdir(r"/media/krishna/My Directory/University files/2020-2021/1b/Machine Learning/Project/Uber-data-analysis/preprocessing")
# load boundaries
with open (r"boundary_coordinates.json") as f:
	boundary_points = json.load(f)
#data_new = [data_new[-1]] # test point
for d in data_new:
	month_year = d.split("-")[-1].split(".")[0]
	df = pd.DataFrame()
	date_year = []
	locations = []
	state = []
	os.chdir(r"/media/krishna/My Directory/University files/2020-2021/1b/Machine Learning/Project/Uber-data-analysis/Uber-dataset")
	os.chdir(d)
	# process the uber data files
	file = pd.read_csv(d)
	for t,La,Lon in tqdm(zip(file['Date/Time'],file['Lat'],file['Lon']), desc ="extracting the date, latitude and longitude from data"):
		date_year.append(t.split(' ')[0])
		locations.append((La,Lon))
	df = pd.DataFrame({'date-year':date_year,
				'location':locations})

	# get the state and city name from the latitude and longitude points use geopy
	# uncomment below lines if you are using geopy
	#get_geolocation(geo_locator)

	# map the state name using the border data points of the hudson river which seperate NewYork and New Jersey
	# uncomment if your are using the custom segmentor
	for loc in tqdm(df['location'], desc ="state seperation for month "+month_year):
		tmp_diff =[np.abs(loc[0]-pts[0])+np.abs(loc[1]-pts[1]) for pts in boundary_points["hudson_borders"]]
		tmp_bound = boundary_points["hudson_borders"][tmp_diff.index(min(tmp_diff))]
		if np.abs(loc[1])<np.abs(tmp_bound[1]):
			state.append("NY")
		else:
			state.append("NJ")
	df['state'] = state

	# get the holidays from the date and year column based on the state
	#df['holiday'] = [get_holiday(date,state) for date,state in tqdm(zip(df['date-year'],df['state']), desc ="Extracting the holidays")]
	df['holiday'] = df.progress_apply(lambda x: get_holiday(x['date-year'],x['state']),axis=1)
	df.to_csv(month_year+"_holiday.csv")
	#print(df)
