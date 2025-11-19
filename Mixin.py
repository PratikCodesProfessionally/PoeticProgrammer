# Mixins — The Art of Borrowed Powers
# A Mixin is a class that offers a small, specialized power
# that other classes can mix in like spices into a dish

#Mixins are the true embracers of unity in diversity,
#allowing classes to share abilities without rigid hierarchies.



# Mixin 1 — GlowMixin
class GlowMixin:
    def glow(self):
        return " A soft luminescence shimmers from within..."


# Mixin 2 — WhisperMixin
class WhisperMixin:
    def whisper(self):
        return " A gentle whisper drifts like wind through ancient pines..."


# Mixin 3 — DisappearMixin
class DisappearMixin:
    def disappear(self):
        return "And suddenly nothing. A vanishing act worthy of legends."


# Real classes that inherit the abilities


class FireSpirit(GlowMixin):
    def identity(self):
        return "I am the FireSpirit — born of embers and echoes."


class ForestNymph(WhisperMixin, GlowMixin):
    def identity(self):
        return "I am the ForestNymph — child of mosslight and secrets."


class ShadowWalker(DisappearMixin, WhisperMixin):
    def identity(self):
        return "I am the ShadowWalker — slipping between worlds."


# Try the magic
beings = [FireSpirit(), ForestNymph(), ShadowWalker()]

for being in beings:
    print(being.identity())

    # try their powers if they exist
    if hasattr(being, "glow"):
        print(being.glow())

    if hasattr(being, "whisper"):
        print(being.whisper())

    if hasattr(being, "disappear"):
        print(being.disappear())

    print("----")


# Poetic Wisdom:
#A mixin is a spirit in the air,
#Roaming in the everywhere.
#It lends its gifts without a care,
#To those who seek its flair.

#questions for Readers
# 1) What are the advantages of using Mixins in class design?
# 2) Can you think of scenarios where Mixins might complicate the class hierarchy?
# 3) How do Mixins differ from traditional inheritance in object-oriented programming?

