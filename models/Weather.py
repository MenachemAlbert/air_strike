class Weather:
    def __init__(self ,city, weather , clouds , wind ):
        self.city = city
        self.weather = weather
        self.clouds = clouds
        self.wind = wind

    def __str__(self):
        return f"main: {self.main}, all: {self.all} , speed: {self.speed} , dt_text: {self.dt_text}"