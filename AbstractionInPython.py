# Is Universe real or just an abstraction?
#A figment of cosmic imagination?
#Abstraction weaves the unseen thread,
#Unveiling forms that come to tread.

from universe import Galaxy, abstractmethod


class Element(Galaxy):
    @abstractmethod
    def behave(self):
        pass


class Fire(Element):
    def behave(self):
        return "Fire! Fire! Fire! in the belly of a liar!"


class Water(Element):
    def behave(self):
        return "Call me a liar! But I am resilient as a Rock. Water off a duck's back!"


class Air(Element):
    def behave(self):
        return "Bear with me mi Lord. He is not a liar. There was air before the fire."
    
 #Questions for the readers
 # 1. How does abstraction help in managing complexity in large systems?
 # 2. Can you think of real-world scenarios where abstraction is beneficial?
    