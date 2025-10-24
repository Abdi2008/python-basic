import requests
import json

def get_weather(api_key, city):
    # This is the base URL for the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # These are the parameters we send with our request
    # 'q' is for the city name
    # 'appid' is for your API key
    # 'units=metric' gets the temperature in Celsius
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' 
    }
    
    try:
        # Send the GET request to the API
        response = requests.get(base_url, params=params)
        
        # Raise an error if the request was unsuccessful (e.g., 404 Not Found)
        response.raise_for_status() 
        
        # Parse the JSON response text into a Python dictionary
        weather_data = response.json()
        
        # --- Displaying the Data ---
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        
        print(f"\n--- Weather in {city} ---")
        print(f"Sky: {main_weather} ({description})")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"Error: City '{city}' not found.")
        elif response.status_code == 401:
            print("Error: Invalid API key. Please check your key.")
        else:
            print(f"An HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"A network error occurred: {err}")
    except KeyError:
        print("Error: Could not parse weather data. The response may be incomplete.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


# --- --- --- --- --- ---
#      RUN THE SCRIPT
# --- --- --- --- --- ---

# ❗ IMPORTANT: Replace this with your own API key
YOUR_API_KEY = "PASTE YOUR API KEY"

if YOUR_API_KEY == "PASTE_YOUR_API_KEY_HERE":
    print("Error: Please replace 'PASTE_YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key.")
else:
    # Get input from the user
    user_city = input("Enter a city name: ")
    if user_city:
        get_weather(YOUR_API_KEY, user_city)
    else:
        print("You must enter a city name.")