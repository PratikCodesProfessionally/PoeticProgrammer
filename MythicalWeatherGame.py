#The core of every game is it'S story
#where every actor plays for their glory
#In this world of myths and legends untold
#Each elemental spirit is gory and bold
#They use the weapon of Object-Oriented Programming
#rain, sunlight, storms, mist, thunder, snow are their reconing
#There are Mixes abilities (like “shine”, “freeze”, “roar”) using Mixins
#And Polymorphism to let each of them express their unique spin
#There's a Game class to orchestrate the tale and pin
#the actions of each spirit within
#Let the Mythical Weather Game begin!

from abc import ABC, abstractmethod


class Spirit(ABC):
    @abstractmethod
    def forecast(self):
        pass


class RainSpirit(Spirit):
    def forecast(self):
        return "Rain washes away the ancient sorrows."
        
class SunlightSpirit(Spirit):
    def forecast(self):
        return "Sunlight brings hope to the darkest shadows."

class StormSpirit(Spirit):
    def forecast(self):
        return "Storms clear pathways for new tomorrows."

class MistMixin:
    def Mist(self):
        return "Mist veils the world in gentle hollows."

class FreezeMixin:
    def Freeze(self):
        return "Freeze stills the chaos, but the time passes the test of time and flows."
                       

class RoarMixin:
    def Roar(self):
        return "When down, be like a lion, who roars and bellows."

class ShineMixin:
    def Shine(self):
        return "Shine bright like the sun, let it heal your heart and your feelings gardens and meadows."
    
#Hybrid elemental spirits    
class ThunderSpirit(SunlightSpirit, ShineMixin):
    pass

class SnowSpirit(RainSpirit, MistMixin, RoarMixin, FreezeMixin):
    pass



# Demo moved below after WeatherGame definition to avoid NameError when instantiating before the class exists.
class WeatherGame:
    def __init__(self):
        self.weather = []
        
    def add_weather(self, *weather):
        #Here I accept multiple weathers and add them to the game
        #It's done via *args like in Example1 exactly the same
        self.weather.extend(weather)

    def report(self, **settings):
        #keyword arguments to customize the report
        # like uppercase=True or effects=True to kindly modify and sort
        uppercase = settings.get('uppercase', False)
class WeatherGame:
    def __init__(self):
        self.weather = []
        
    def add_weather(self, *weather):
        #Here I accept multiple weathers and add them to the game
        #It's done via *args like in Example1 exactly the same
        self.weather.extend(weather)

    def report(self, **settings):
        #keyword arguments to customize the report
        # like uppercase=True or effects=True to kindly modify and sort
        uppercase = settings.get('uppercase', False)
        effects = settings.get('effects', False)

        final_report = []

        for weather in self.weather:
            line = weather.forecast()
            if effects:
                effect_lines = []
                if isinstance(weather, MistMixin):
                    effect_lines.append(weather.Mist())
                if isinstance(weather, FreezeMixin):
                    effect_lines.append(weather.Freeze())
                if isinstance(weather, RoarMixin):
                    effect_lines.append(weather.Roar())
                if isinstance(weather, ShineMixin):
                    effect_lines.append(weather.Shine())
                if effect_lines:
                    line += " Additionally, " + " Also, ".join(effect_lines)
            if uppercase:
                line = line.upper()
            final_report.append(line)

        return final_report

if __name__ == "__main__":
    #Return poetic final report
    #Let's do a demo
    #Let's keep a tag or a memo
    rain = RainSpirit()
    sunlight = SunlightSpirit()
    storm = StormSpirit()
    thunder = ThunderSpirit()
    snow = SnowSpirit()
    game = WeatherGame()
    #This line summons five spirits to the stage of grace
    game.add_weather(rain, sunlight, storm, thunder, snow)
    report = game.report(uppercase=False, effects=True)
    for line in report:
        print(line)