import random
import json
import yaml

def load_config():
    try:
        with open("config.json", "r") as f:
            config_json = json.load(f)
        with open("config.yml", "r") as f:
            config_yml = yaml.safe_load(f)
        return {**config_json.get("weather", {}), **config_yml.get("weather", {})}
    except Exception as e:
        print("Error loading config:", e)
        return {"city": "Istanbul"}

def simulate_weather(city):
    temperature = random.randint(-5, 35)
    humidity = random.randint(20, 90)
    conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
    condition = random.choice(conditions)

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

if __name__ == "__main__":
    config = load_config()
    city = config.get("city", "Istanbul")
    simulate_weather(city)
