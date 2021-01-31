import requests
import json
import time

api_key = 'Your Google API key1'
api_key1='Your Google APIkey2'
address=input('Enter your full address')

lat=''
lon=''
business_types = [
"accounting",
"airport",
"amusement_park",
"aquarium",
"art_gallery",
"atm",
"bakery",
"bank",
"bar",
"beauty_salon",
"bicycle_store",
"book_store",
"bowling_alley",
"bus_station",
"cafe",
"campground",
"car_dealer",
"car_rental",
"car_repair",
"car_wash",
"casino",
"cemetery",
"church",
"city_hall",
"clothing_store",
"convenience_store",
"courthouse",
"dentist",
"department_store",
"doctor",
"electrician",
"electronics_store",
"embassy",
"fire_station",
"florist",
"funeral_home",
"furniture_store",
"gas_station",
"gym",
"hair_care",
"hardware_store",
"hindu_temple",
"home_goods_store",
"hospital",
"insurance_agency",
"jewelry_store",
"laundry",
"lawyer",
"library",
"liquor_store",
"local_government_office",
"locksmith",
"lodging",
"meal_delivery",
"meal_takeaway",
"mosque",
"movie_rental",
"movie_theater",
"moving_company",
"museum",
"night_club",
"painter",
"park",
"parking",
"pet_store",
"pharmacy",
"physiotherapist",
"plumber",
"police",
"post_office",
"real_estate_agency",
"restaurant",
"roofing_contractor",
"rv_park",
"school",
"shoe_store",
"shopping_mall",
"spa",
"stadium",
"storage",
"store",
"subway_station",
"supermarket",
"synagogue",
"taxi_stand",
"train_station",
"transit_station",
"travel_agency",
"veterinary_care",
"zoo"]

total_results = []

def get_nearby_places(coordinates, business_type, next_page):
	URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinates+'&radius=1000&key='+ api_key +'&type='+business_type+'&pagetoken='+next_page)
	r = requests.get(URL)
	response = r.text
	python_object = json.loads(response)
	results = python_object["results"]
	for result in results:
		place_name = result['name']
		place_id = result['place_id']
		website = get_place_website(place_id)
		print([business_type, place_name, website])
		total_results.append([business_type, place_name, website])
	try:
		next_page_token = python_object["next_page_token"]
	except KeyError:
		#no next page
		return
	time.sleep(1)
	get_nearby_places(coordinates, business_type, next_page_token)

def coordinate(add):
	global lat
	global lon
	params={
		'key':api_key1,
		'address':add
	}
	base_url='https://maps.googleapis.com/maps/api/geocode/json?'
	response=requests.get(base_url,params=params).json()
	response.keys()
	if response['status']=='OK':
		geometry=response['results'][0]['geometry']
		lat =  geometry['location']['lat']
		lon = geometry['location']['lng']

coordinate(address)
def get_place_website(place_id):
	reqURL = ('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place_id+'&key='+api_key)
	r = requests.get(reqURL)
	response = r.text
	python_object = json.loads(response)
	try:
		place_details = python_object["result"]
		if 'website' in place_details:
			return place_details['website']
		else:
			return "no website listed in API"
	except:
		print("err getting place details")


for loop in business_types:
	get_nearby_places('{},{}'.format(lat,lon),'{}'.format(loop),'')
	print(total_results)
