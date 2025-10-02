import random

def weather_report(city):

    possible_weather = ['cloudy','sunny','raining','very foggy','snowing','thunderstorming']

    weather = random.choice(possible_weather)
    temperature = 0

    if weather == 'sunny':
        temperature = random.randint(25,40)
    
    elif weather == 'snowing':
        temperature = random.randint(-10,2)

    else:
        temperature = random.randint(0,30)

    report = (f"Todays is {weather} in {city} with a temperature of {temperature} degrees celsius, thanks for being here see you tomorrow!")

    return report

city_name = input("Enter a city name: ")
print(weather_report(city_name))