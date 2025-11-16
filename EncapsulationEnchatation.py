class Garden:
    def __init__(self):
        self._flowers = ["rose", "lily", "tulip"]   # protected
        self.__secret_seed = "moon-bloom"           # private

    def grow(self, new_flower):
        self._flowers.append(new_flower)

    def reveal(self):
        return f"In the depth grows a {self.__secret_seed}."
    
    def whisper_secret(self):
        """A gentle way to sense the secret without exposing it"""
        return f"Something precious sleeps beneath..."


class PoetGardener(Garden):
    def express(self):
        # ✅ Can access _flowers (single underscore - protected by convention)
        visible = "I see " + ", ".join(self._flowers) + " dancing in dewlight."
        
        # ❌ Cannot access __secret_seed directly (double underscore - name mangled)
        # print(self.__secret_seed)  # This would raise AttributeError!
        
        return visible
    
    def sense_the_mystery(self):
        """The poet senses the secret without knowing it directly"""
        # Instead of accessing __secret_seed directly, use the parent's method
        hint = self.whisper_secret()
        full_story = self.reveal()
        return f"{hint}\n{full_story}\nThe poet feels its presence, but cannot name it alone."


# 🌻 Let's watch the magic unfold
rumi = PoetGardener()
rumi.grow("sunflower")

print("=== What the Poet Sees (protected _flowers) ===")
print(rumi.express())

print("\n=== What the Garden Reveals (private __secret_seed via method) ===")
print(rumi.reveal())

print("\n=== How the Poet Senses the Mystery ===")
print(rumi.sense_the_mystery())
