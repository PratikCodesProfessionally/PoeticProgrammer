# Magic Methods The Secret Language of Python
# Magic methods (dunder methods) let you define how objects behave
# with built-in Python operations like +, -, len(), str(), etc.

#Sometimes in life you have got to use cheat codes
#Not to cheat others or to deceive yourself 
#But to learn to love and to spread love
#Gratitude, Grace, Humility and Humanity
#These are you cheat codes for sanity
#These are built in you, engraved in your heart's rarity




class Poem:
    """A poem that knows how to combine, compare, and display itself"""
    
    def __init__(self, lines):
        # Birth of a poem: lines arrive as string or list
        # We shape them gently into verse that will persist
        if isinstance(lines, str):
            self.lines = [lines]
        else:
            self.lines = lines
    
    def __str__(self):
        # When print() calls, the poem speaks
        # Each line flows like water through the creeks
        return "\n".join(self.lines)
    
    def __repr__(self):
        # A mirror for developers to see
        # How many verses hold the poetry
        return f"Poem({len(self.lines)} lines)"
    
    def __len__(self):
        # Count the stanzas, measure the soul
        # How many lines make up the whole?
        return len(self.lines)
    
    def __add__(self, other):
        # Two poems meet, they join as one
        # Like dawn that merges with the sun
        if isinstance(other, Poem):
            return Poem(self.lines + other.lines)
        return NotImplemented
    
    def __eq__(self, other):
        # Are these verses twins in disguise?
        # We check each word before our eyes
        if isinstance(other, Poem):
            return self.lines == other.lines
        return False
    
    def __getitem__(self, index):
        # Pluck a single line like fruit from trees
        # Or slice a passage with graceful ease
        return self.lines[index]
    
    def __contains__(self, word):
        # Does this word live within these pages?
        # We search through verses, through the ages
        text = " ".join(self.lines).lower()
        return word.lower() in text


class Number:
    """A number that knows how to perform arithmetic operations"""
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Number({self.value})"
    
    def __add__(self, other):
        # Addition: two numbers embrace and grow
        # Their sum becomes a gentle flow
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value + other)
        return NotImplemented
    
    def __sub__(self, other):
        # Subtraction: one steps back, creates space
        # What remains is difference with grace
        if isinstance(other, Number):
            return Number(self.value - other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value - other)
        return NotImplemented
    
    def __mul__(self, other):
        # Multiplication: values dance and multiply
        # Like stars that multiply across the sky
        if isinstance(other, Number):
            return Number(self.value * other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value * other)
        return NotImplemented
    
    def __lt__(self, other):
        # Less than: humble numbers bow their head
        # Acknowledging those greater instead
        if isinstance(other, Number):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        return NotImplemented
    
    def __gt__(self, other):
        # Greater than: numbers stand up tall
        # Rising above when others fall
        if isinstance(other, Number):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > other
        return NotImplemented


# Demonstration


print("=" * 60)
print("Poem Magic Methods")
print("=" * 60)

poem1 = Poem(["The wind whispers", "through ancient trees"])
poem2 = Poem(["carrying secrets", "from distant seas"])

print("Poem 1:")
print(poem1)
print(f"\nLength: {len(poem1)} lines")
print(f"Representation: {repr(poem1)}")

print("\nPoem 2:")
print(poem2)

print("\nCombined (poem1 + poem2):")
combined = poem1 + poem2
print(combined)

print(f"\nFirst line: {combined[0]}")
print(f"Contains 'wind': {'wind' in combined}")
print(f"Contains 'fire': {'fire' in combined}")

print("\n" + "=" * 60)
print("Number Magic Methods")
print("=" * 60)

num1 = Number(10)
num2 = Number(5)

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} > {num2} = {num1 > num2}")
print(f"{num1} < {num2} = {num1 < num2}")


# Poetic Wisdom:
#
# Magic methods wear double underscores,
# like secrets hidden behind closed doors.
#
# They teach your objects how to dance
# with operators at a single glance.
#
# __add__ lets plus signs work their way,
# __str__ gives voice to what they say.
#
# __len__ counts what lies within,
# __eq__ knows where matches begin.
#
# These methods are Python's inner art,
# they give your classes a beating heart.


# What you just learned:
# __init__ initializes an object
# __str__ returns a readable string representation
# __repr__ returns a developer-friendly representation
# __len__ defines behavior for len()
# __add__ defines behavior for +
# __sub__ defines behavior for -
# __mul__ defines behavior for *
# __eq__ defines behavior for ==
# __lt__ and __gt__ define behavior for < and >
# __getitem__ enables indexing with []
# __contains__ enables 'in' operator
