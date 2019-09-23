import bs4
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen as uReq
import time
import datetime
import pandas as pd
# from datetime import datetime

# This function retrieves the wave height
def wave_height_finder():
	#list of URLs to scrape from
	my_url = ['https://www.ndbc.noaa.gov/station_page.php?station=44013']

	for url in my_url:
	#initiating python's ability to parse URL
		uClient = uReq(url)
	# this will offload our content in'to a variable
		page_html = uClient.read()
	# closes our client
		uClient.close()
		page_soup = BeautifulSoup(page_html, "html.parser")	
	# Fetching/Defining data to variables
		wave_height = page_soup.find('td', string='Wave Height (WVHT):').find_next_sibling().get_text().strip()
		wave_interval = page_soup.find('td', string='Dominant Wave Period (DPD):').find_next_sibling().get_text().strip()
		wind_direction = page_soup.find('td', string='Wind Direction (WDIR):').find_next_sibling().get_text().strip()
		wind_speed = page_soup.find('td', string='Wind Speed (WSPD):').find_next_sibling().get_text().strip()
		air_temp = page_soup.find('td', string='Air Temperature (ATMP):').find_next_sibling().get_text().strip()
		water_temp = page_soup.find('td', string='Water Temperature (WTMP):').find_next_sibling().get_text().strip()

		#Wind Direction Splicing
		wind_direction_abbreviated = wind_direction[:4]

		#Wind Speed Splicing
		wind_speed_abbreviated = wind_speed.split('.')
		# print(wind_speed_abbreviated)
		wind_speed_sliced = wind_speed_abbreviated[0]
		wind_speed_abbreviated_int = int(wind_speed_sliced)

		# Loading Screens 
		print("\n")
		print("Hacking Weather Sensors...")
		print("\n")
		time.sleep(1)
		print("Retrieving Government Data...")
		print("\n")
		time.sleep(1)
		print("Decrypting Classified Documents...")
		print("\n")
		time.sleep(1)
		print("Initializing Data...")	
		print("\n")
		time.sleep(1)
		print("\n")

		print("-----Current Buoy Data for Boston Harbor:-----")
		time.sleep(1)
		print("\n")

		# Current Time 
		#Grab current date/time (24 hr format, includes seconds)
		current_time_AM_PM = datetime.datetime.now()
		#12-hour format
		current_time_sliced = current_time_AM_PM.strftime('%Y/%m/%d %I:%M%p')
		# separating Date from Time (DD/MM/YYY HH/MM)
		date_today = current_time_sliced.split(' ')
		date_ = date_today[0]
		time_ = date_today[1]
		# Removing first letter if it's '0', so it doesn't read as '08:07pm', etc
		if time_[0]=="0":
			time_ = time_[1:]

		print("Date:", date_)
		print("Current Time:", time_)
		print("Location: Boston Harbor")
		time.sleep(1)
		print("\n")


		# now = datetime.datetime.now()

		# print("Current Date & Time:")
		# print(str(now))
		# time.sleep(1)
		# print("\n")

		# Printing of current conditions
		print("Current Wave Height:", wave_height)
		print("Current Wave Interval:", wave_interval)
		print("Current Wave Direction:", wind_direction)
		print("Current Wind Speed:", wind_speed)
		print("Current Air Temp:", air_temp)
		print("Current Water Temp:", water_temp)
		print("\n")


		# Logic begins for determining if surf conditions are good or not
		# Creating lists of WaveHeights, Wave Intervals, Wind Directions to check against in our logic 
		# for determining good surf conditions
		wave_height_list = ['0.1 ft','0.2 ft','0.3 ft','0.4 ft','0.5 ft','0.6 ft','0.7 ft','0.8 ft','0.9 ft',
								'1.1 ft', '1.2 ft', '1.3 ft', '1.4 ft', '1.5 ft', '1.6 ft', '1.7 ft', '1.8 ft','1.9 ft',
								'2.0 ft','2.3 ft','2.4 ft','2.5 ft','2.6 ft','2.7 ft','2.8 ft','2.9 ft']

		wave_interval_list = ['1 sec', '2 sec', '3 sec', '4 sec', '5 sec', '6 sec', '7 sec']


		wind_direction_list = ["SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

		# Here is the logic used to determine if current conditions are generating good waves
		if wave_height not in wave_height_list and wave_interval not in wave_interval_list and wind_direction in wind_direction_list and wind_speed_abbreviated_int < 17:
			time.sleep(1)
			print("Good Waves Right Now in Boston! Go out ;& Surf!")
		else:
			time.sleep(1)
			print("Summary: Unfortunately, surf conditions in Boston are not good right now.")
			time.sleep(1)
			print("\n")


		# Current Time 
		#Grab current date/time (24 hr format, includes seconds)
		# current_time_AM_PM = datetime.datetime.now()
		# #12-hour format
		# current_time_sliced = current_time_AM_PM.strftime('%Y/%m/%d %I:%M%p')
		# # separating Date from Time (DD/MM/YYY HH/MM)
		# date_today = current_time_sliced.split(' ')
		# date_ = date_today[0]
		# time_ = date_today[1]
		# # Removing first letter if it's '0', so it doesn't read as '08:07pm', etc
		# if time_[0]=="0":
		# 	time_ = time_[1:]

		# print("Date:", date_)
		# print("Current Time:", time_)
		# print(current_time_AM_PM.strftime('%Y/%m/%d %I:%M:%S'))

		wind_speed_abbreviated = wind_speed.split('.')
		wind_speed_sliced = wind_speed_abbreviated[0]


def tide_finder():
	# Using Pandas to parse through the html table found in the URL containing Tide Data
	tide_table = pd.read_html('https://www.tide-forecast.com/locations/Castle-Island-Boston-Harbor-Massachusetts/tides/latest')[0]

	tide_ = tide_table['Tide'].values

	time_date = tide_table['Time (EDT) & Date'].values

	for (t, i) in zip(tide_, time_date):
		time_date_sliced = i.split('(')
		time_ = time_date_sliced[0]
		date_ = time_date_sliced[1]

		#change the variable name so it makes it clear what we're printing :)
		tide_ = t
		print(tide_ + ':', time_)


wave_height_finder()
tide_finder()



## Useful Info:

# The following are the wind_direction values (abbreviated wind directions)
	# need to do the same for wind speed ... ie when does it become too windy?

# West = GOOD
# East = BAD

# NNE = North-Northeast
# NE = Northeast
# ENE = East-Northeast
# E = East
# ESE = East-Southeast
# SE = Southeast
# SSE = South-Southeast
# S = South
# SSW = South-Southwest
# SW = Southwest
# WSW = West-Southwest
# W = West
# WNW = West-Northwest
# NW = Northwest
# NNW = North-Northwest