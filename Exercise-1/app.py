from flask import Flask
import requests 
app = Flask(__name__)

@app.route('/')
def Hello():
	return 'Hello World!'

@app.route('/weather/<city>')
def Weather(city):
	
	secretWeather = 'bb96320928f968ccb0b8da40d302ab6e'
	weatherURL = 'http://api.openweathermap.org/data/2.5/weather'
	weatherParams = {'q' : city, 'units': 'metric', 'appid': secretWeather}
	weatherResponse = requests.get(url = weatherURL, params = weatherParams)
	temperature = weatherResponse.json()['main']['temp']
	
	if temperature < 0:
		gifKeyWord = 'winter is coming'
	elif temperature >= 0 and temperature <= 20:
		gifKeyWord = 'chilly'
	elif temperature > 20 and temperature <= 30:
		gifKeyWord = 'nice weather'
	else: gifKeyWord = 'sweating'

	secretGiphy = 'PxesQDO150gAhhmoS7DgWFqtR9yHMNw7'
	giphyURL = 'http://api.giphy.com/v1/gifs/translate'
	giphyParams = {'api_key': secretGiphy, 's': gifKeyWord , 'weirdness': 2}
	giphyResponse = requests.get(url = giphyURL, params = giphyParams)
	gifImageURL = giphyResponse.json()['data']['images']['original']['url']
	
	return 'Temperature in ' + city + ' is: ' + str(temperature) + '<br><img src=' + str(gifImageURL) + '>'

if __name__ == "__main__":
	app.run()