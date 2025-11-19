# Advanced Mixins Practical Magic
# Three powerful, real-world mixins: Logging, Serialization, and Timing
# Written in clean, real-world structure with lyrical twists


import datetime
import json
import time


# 1. LoggingMixin watching your code speak
# It stamps each message with the time
# and whispers who delivered the rhyme.
class LoggingMixin:
    def log(self, message):
        # Get current time in HH:MM:SS format
        now = datetime.datetime.now().strftime("%H:%M:%S")
        # Print: [time] ClassName: message
        print(f"[{now}] {self.__class__.__name__}: {message}")


# 2. SerializationMixin turning objects into JSON
# This mixin takes the heart within,
# turns soul to string, begins again.
class SerializationMixin:
    def to_json(self):
        # self.__dict__ = all attributes of this object
        # json.dumps = convert Python dict to JSON string
        # indent=2 = pretty print with spacing
        # ensure_ascii=False = allow non-ASCII characters (é, ü, नेपाली, etc.)
        return json.dumps(self.__dict__, indent=2, ensure_ascii=False)


# 3. TimingMixin measure how long something takes
# A pulse is taken, soft and slight,
# it measures day, it measures night.
class TimingMixin:
    def time_it(self, func, *args, **kwargs):
        # *args = positional arguments (captured as tuple)
        #   Example: greet("Patrick", "joyful") → args = ("Patrick", "joyful")
        #   Position matters: 1st goes to 1st param, 2nd to 2nd param
        #
        # **kwargs = keyword arguments (captured as dict)
        #   Example: greet(name="Patrick", mood="joyful") → kwargs = {"name": "Patrick", "mood": "joyful"}
        #   Order doesn't matter because names are explicit
        
        # Start the stopwatch
        start = time.time()
        
        # Run the function with all its arguments
        result = func(*args, **kwargs)
        
        # Stop the stopwatch
        end = time.time()
        
        # Return both the result and the duration
        # {end - start:.5f} = format to 5 decimal places
        return result, f"Took {end - start:.5f} seconds"


# Real classes that combine mixins


class Task(LoggingMixin, SerializationMixin):
    """A task that can log and serialize itself"""
    
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    
    def perform(self):
        self.log(f"Starting task '{self.name}'")
        return f"Performing {self.name}..."


class Worker(LoggingMixin, TimingMixin):
    """A worker that can log and time operations"""
    
    def __init__(self, name):
        self.name = name
    
    def do(self, work):
        def inner_task():
            self.log(f"{self.name} is working on: {work}")
            time.sleep(0.3)  # simulate effort
            return f"Completed: {work}"
        
        return self.time_it(inner_task)


# Demonstration


print("=" * 60)
print("Task Example Logging and Serialization")
print("=" * 60)

task = Task("Harvesting sunbeams", difficulty="medium")
print(task.perform())
print("\nSerialized Task:")
print(task.to_json())

print("\n" + "=" * 60)
print("Worker Example Logging and Timing")
print("=" * 60)

worker = Worker("Rumi")
result, duration = worker.do("Weaving moonlight")
print(f"{result}")
print(duration)


# Poetic Wisdom:
#
# Positional arguments
# march in a line,
# left to right,
# in obedient time.
#
# Keyword arguments
# are rebels of sorts—
# they whisper their names
# with elegant reports.
#
# *args gathers wanderers
# who arrive unannounced,
# **kwargs collects
# the named ones pronounced.
#
# Together they enter
# a function's embrace—
# positional dancers,
# keywords full of grace.


# What you just learned:
# Mixins give specific, reusable abilities
# They don't define identity they give skills
# Classes can combine many mixins safely
# You can add logging, saving, timing, formatting, security, etc.
# Mixins keep your code clean and modular
