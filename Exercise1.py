from abc import ABC, abstractmethod

class Creature(ABC):
    @abstractmethod
    def describe(self):
        pass

class Dragon(Creature):
    def describe(self):
        return " 'Fire! Fire! Fire! - burning bright in the belly of a liar!', says the dragon, the fire cannon."

class Phoenix(Creature):
    def describe(self):
        return " 'From ashes of hope I rise, with wings of never giving flame and eyes of infinite skies,' cries the phoenix."    
    
class Mermaid(Creature):
    def describe(self):
        return " 'Sing me a song of the sea, where the waves dance and the heart is free,' hums the mermaid."

#Mixins for additional behaviors
#Mixins should not inherit from Creature
class FlyMixin:
    def fly(self):
        return "soars across the sky!"

class SwimMixin:
    def swim(self):
        return "glides through silent waters..."

#This class should store creatures in a list    
class CreatureManager:    
    def __init__(self):
        # create the list once for the lifetime of the manager
        self.creatures = []

    def add(self, *creatures):
        # Accept multiple creatures and append to the existing list
        self.creatures.extend(creatures)

#Have a method report(**kawargs) that uses keyword arguments for optional settings: 1)uppercase =True/False 2)Inside this method: Call describe() for every creature (polymorphism). If the creature has fly() or swim() methods, call them too. Apply settings from kwargs.
    def report(self, **kwargs):
        uppercase = kwargs.get('uppercase', False)
        reports = []
        
        for creature in self.creatures:
            descriptions = [creature.describe()]
            
            if callable(getattr(creature, 'fly', None)):
                descriptions.append(creature.fly())
            if callable(getattr(creature, 'swim', None)):
                descriptions.append(creature.swim())
                
            full_report = " ".join(descriptions)
            if uppercase:
                full_report = full_report.upper()
                
            reports.append(full_report)
        
        return reports


