# Design Pattern: Observer Pattern : Weather Station
# Develop a Weather Station that notifies all registered display devices
# whenever the temperature changes Using Observer Pattern.

# Subject
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register(self, observer):
        self._observers.append(observer)

    def set_temperature(self, temp):
        print(f"\nWeatherStation: Setting temperature to {temp}°C")
        self._temperature = temp
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

# Observer
class DisplayDevice:
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name} Display: Temperature changed to {temperature}°C")

# --- Verification ---
station = WeatherStation()

# Create display devices
phone_app = DisplayDevice("Phone App")
living_room_screen = DisplayDevice("Living Room Screen")

# Register devices to the weather station
station.register(phone_app)
station.register(living_room_screen)

# Change the temperature (this will automatically notify the devices)
station.set_temperature(25)
station.set_temperature(28)