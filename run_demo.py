from Exercise1 import Dragon, Phoenix, Mermaid, FlyMixin, SwimMixin, CreatureManager

# combine mixins with concrete creatures
class FlyingDragon(Dragon, FlyMixin):
    pass

class FlyingPhoenix(Phoenix, FlyMixin):
    pass

class SwimmingMermaid(Mermaid, SwimMixin):
    pass

mgr = CreatureManager()
mgr.add(FlyingDragon(), FlyingPhoenix(), SwimmingMermaid(), Dragon())  # include a plain Dragon

print("Default reports:")
for line in mgr.report():
    print(line)

print("\nUppercase reports:")
for line in mgr.report(uppercase=True):
    print(line)