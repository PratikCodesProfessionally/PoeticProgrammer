#As I sat by the evening sun
#thinking about how rough the day had gone
#different colors of emotions had had me done
#sometimes tears fell readily like when you peel an onion
#sometimes serene peace touched me like a baby just born
#sometimes anger flared up like a wild storm
#It was a bizarre evening of emotional polymorphism

class Emotion:
    def express(self):
        raise NotImplementedError("Subclasses just take my different shapes and sizes!" )
    
class Joy(Emotion):
    def express(self):
        return "Joy a lighter bliss that may cloud the rainy abyss."
    
class Anger(Emotion):
    def express(self):
        return "Anger a mightier hiss of a snake's crocketiering that may divide friends and create a riss."
    
class Sadness(Emotion):
    def express(self):
        return "Sadness a deeper miss that may drown the soul in an emotional abyss."
    
# 🌈 Let's witness the emotional polymorphism
emotions = [Joy(), Anger(), Sadness()]
for emotion in emotions:
    print(emotion.express())
# Output:
# Joy a lighter bliss that may cloud the rainy abyss.
# Anger a mightier hiss of a snake's crocketiering that may divide friends and create a riss.
# Sadness a deeper miss that may drown the soul in an emotional abyss

