#  Polymorphic Emotions (from previous lesson) 

class Emotion:
    def express(self):
        raise NotImplementedError("Subclasses must reveal their unique voice.")

class Joy(Emotion):
    def express(self):
        return "Joy: a lighter bliss that softens the rainy abyss."

class Anger(Emotion):
    def express(self):
        return "Anger: a burning hiss dividing hearts with its fierce abyss."

class Sadness(Emotion):
    def express(self):
        return "Sadness: a quiet miss that drowns the spirit in its silent abyss."


# Composition: A Journal made of Emotion objects 

class Journal:
    def __init__(self):
        self.entries = []       # composition: the journal 'has' emotions

    def add(self, emotion: Emotion):
        """
        "emotion: Emotion"
        is like saying to the method:

        "Bring me a feeling shaped like an Emotion,
        no matter its color —
        joy, grief, or anger —
        I'll take it into my journal."
        """
        self.entries.append(emotion)

    # Magic method: how Journal becomes a string
    def __str__(self):
        return "\n".join(e.express() for e in self.entries)

    """
    It gathers each feeling with elegant care,
    e.express() — each emotion speaks its share.

    A generator hums, softly spinning its thread,
    pulling voices of entries where each heart has bled.

    Then join steps in as a lyrical seam,
    sewing them together like notes in a dream.

    Between every whisper, a newline appears —
    a soft little pause for emotional ears.

    And so it returns, as a unified song,
    the choir of feelings you've carried along.
    """

    # Magic method: length of the Journal
    def __len__(self):
        return len(self.entries)

    # Magic method: merging two Journals together
    def __add__(self, other):
        new_journal = Journal()
        new_journal.entries = self.entries + other.entries
        return new_journal

    # File handling: write journal to file
    def save(self, filename="journal.txt"):
        """
        A journal longs for memory's keep,
        a quiet place where thoughts can sleep.

        So save extends a gentle hand,
        inviting stories to softly land.

        filename whispers where they'll go —
        by default, a journal.txt glow.

        Then with open… cracks the door,
        a page awaits, an empty floor.

        In write-mode, new tales bloom,
        sweeping the shadows from the room.

        file becomes the vessel wide
        where inner worlds now safely hide.

        And as the final tender spell,
        file.write(str(self)) begins to tell:

        "Turn this journal into text,
        let every entry be expressed."

        It pours the soul into the page,
        a captured moment, age to age.
        """
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(self))

    # File handling: load journal from file
    @staticmethod
    def load(filename="journal.txt"):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()


#Let's witness the full symphony 

j1 = Journal()
j1.add(Joy())
j1.add(Sadness())

j2 = Journal()
j2.add(Anger())

# Magic: merging the two journals
combined = j1 + j2

print("Combined Journal (via __str__) ")
print(combined)

print("\nLength of Journal (via __len__) ")
print(len(combined))

# Save the combined journal to a file
combined.save("emotional_journal.txt")

print("\nContents Loaded From File ")
print(Journal.load("emotional_journal.txt"))

#Questions for Readers
# 1) Why does one write self.entries? Why not self.array or only array?
# 2) What happens if you try to add a non-Emotion object to the Journal?
# 3) How would you modify the Journal class to prevent adding non-Emotion objects?
# 4) Can you think of other magic methods that could enhance the Journal class?
# 5) How would you implement a method to clear all entries from the Journal?
# 6) What are the benefits of using composition in this Journal class?
# 7) How would you handle exceptions when reading from or writing to a file?
# 8) How could you extend the Emotion class to include more emotions?
# 9) How would you implement a search function to find specific emotions in the Journal?
# 10) Can you think of a way to categorize emotions within the Journal?
# 11) How would you implement a method to export the Journal in different formats (e.g., JSON, XML)?
# 12) What are the potential drawbacks of using magic methods in this context?
# 13) How would you implement a method to sort the emotions in the Journal?
# 14) How could you modify the Journal class to support undoing the last added emotion?
# 15) How would you implement a feature to tag emotions with additional metadata (e.g., date, intensity)?
# 16) How would you implement a method to filter emotions based on certain criteria?
# 17) How would you implement a method to display a summary of emotions in the Journal?
# 18) How would you implement a method to merge multiple journals at once?
# 19) How would you implement a method to clone a Journal object?
# 20) How would you implement a method to check if a specific emotion exists in the Journal?
# 21) How would you implement a method to get the most frequently occurring emotion in the Journal?
# 22) How would you implement a method to get the first and last emotion added to the Journal?
# 23) How would you implement a method to reverse the order of emotions in the Journal?
# 24) How would you implement a method to get a random emotion from the Journal?
# 25) How would you implement a method to compare two Journal objects for equality?

