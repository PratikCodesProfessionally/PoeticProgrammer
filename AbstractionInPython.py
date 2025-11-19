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