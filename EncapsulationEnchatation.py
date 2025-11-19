#Gardens are where the love grows in secret,
#A future predestined red, pink, glossy, scarlet
#But between different shades is a mystery scarred in violet
#Some are guarded by thorns seen, some by unseen bayonets


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
        # Can access _flowers (single underscore - protected by convention)
        visible = "I see " + ", ".join(self._flowers) + " dancing in dewlight."
        
        # Cannot access __secret_seed directly (double underscore - name mangled)
        # print(self.__secret_seed)  # This would raise AttributeError!
        
        return visible
    
    def sense_the_mystery(self):
        """The poet senses the secret without knowing it directly"""
        # Instead of accessing __secret_seed directly, use the parent's method
        hint = self.whisper_secret()
        full_story = self.reveal()
        return f"{hint}\n{full_story}\nThe poet feels its presence, but cannot name it alone."


#  Let's watch the magic unfold
rumi = PoetGardener()
rumi.grow("sunflower")

print("\nWhat the Poet Sees (protected _flowers)")
print(rumi.express())

print("\nWhat the Garden Reveals (private __secret_seed via method)")
print(rumi.reveal())

print("\nHow the Poet Senses the Mystery (indirect access)")
print(rumi.sense_the_mystery())
