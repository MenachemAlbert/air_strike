class Mission:
    def __init__(self, target, pilot, aircraft, weather_score):
        self.target = target
        self.pilot = pilot
        self.aircraft = aircraft
        self.weather_score = weather_score
        self.score = self.calculate_mission_score()

