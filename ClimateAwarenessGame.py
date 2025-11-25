from abc import ABC, abstractmethod

#Abstract climate role class

class ClimateActor(ABC):
    @abstractmethod
    def act(self):
        """How does an actor's behaviour impact climate change?"""
        pass

#Mixins for positive actions
#Teams for positive tractions    

class RecycleMixin:
    def recycle(self):
        return "gives second life to E-Gadgets and plastics and hence feels happy and fantastic!"
    
class ConserveEnergyMixin:
    def conserve_energy(self):
        return "switches off netflix binges, light plugs and hinges, inteference fringes and smoky thoughts to bring positive changes!"   
    
class PlantTreesMixin:
    def plant_trees(self):
        return "worships the age old trees and the shelter of honey bees, planting the seeds of tomorrow's breeze and feels at ease!"

#Actors with polymorphic behaviour
#contractors who need to act as a climate savior

class Human(ClimateActor):
    def act(self):
        return "The Human stands at the crossroads of climate change, making choices that shape the future of our planet."
    
class IndustrialMachine(ClimateActor):
    def act(self):
        return "As the machine runs, it burns the fossil fuel chunks, ever so thirsty for a game of zero sum, leaving behind a trail of carbon crumbs."

class Government(ClimateActor):
    def act(self):
        return "Left or right, if the policy is not right, nobody can save us against climate change's might."

#Hybrid climate heros
#the silent warriors laying the foundation and silos

class EcoWarrior(Human, RecycleMixin, ConserveEnergyMixin, PlantTreesMixin):
    pass

class GreenFactory(IndustrialMachine, RecycleMixin, ConserveEnergyMixin):
    pass

class ForestNation(Government, PlantTreesMixin):
    pass    

#Game should be managed and orchestrated from a manager
#The duties and responsibilities should be conveyed to every player

class climateGame:
    def __init__(self):
        self.actors = []
        
    def add_actors(self, *actors):
        #Here I accept multiple actors and add them to the game
        #It's done via *args like in Example1 exactly the same
        self.actors.extend(actors)

    def report(self, **settings):
        #keyword arguments to customize the report
        # like uppercase=True or show_actions=True to kindly modify and sort
        uppercase = settings.get('uppercase', False)
        show_actions = settings.get('show_actions', False)

        final_report = []

        for actor in self.actors:
            line = actor.act()
            if show_actions:
                actions = []
                if isinstance(actor, RecycleMixin):
                    actions.append(actor.recycle())
                if isinstance(actor, ConserveEnergyMixin):
                    actions.append(actor.conserve_energy())
                if isinstance(actor, PlantTreesMixin):
                    actions.append(actor.plant_trees())
                if actions:
                    line += " Additionally, " + " Also, ".join(actions)
            if uppercase:
                line = line.upper()
            final_report.append(line)

        return final_report

#Let's do a demo
#Let's keep a tag or a memo

eco = EcoWarrior() 
industry = GreenFactory()
nation= ForestNation()

game = climateGame()
#This line summons three souls to the stage of grace
# namely: eco, industry, and nation, through add_actors' gate, 
#where the game awaits to orchestrate their climate debate,
#joining them in a discussion to determine the planet's fate.
game.add_actors(eco, industry, nation) 


for line in game.report(show_actions=True):
    print(line)
            
        
   


