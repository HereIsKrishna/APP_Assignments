# Design Pattern: Factory Pattern : Fruit Factory
# Create a FruitFactory that returns Apple, Mango, or Orange objects Using Factory Pattern.
# Each fruit class should display its name.

# Product classes
class Apple:
    def display(self):
        return "I am an Apple!"

class Mango:
    def display(self):
        return "I am a Mango!"

class Orange:
    def display(self):
        return "I am an Orange!"

# Factory class
class FruitFactory:
    @staticmethod
    def get_fruit(fruit_type):
        if fruit_type.lower() == "apple":
            return Apple()
        elif fruit_type.lower() == "mango":
            return Mango()
        elif fruit_type.lower() == "orange":
            return Orange()
        else:
            return None

# --- Verification ---
factory = FruitFactory()

fruit1 = factory.get_fruit("apple")
fruit2 = factory.get_fruit("mango")
fruit3 = factory.get_fruit("orange")

print(fruit1.display())
print(fruit2.display())
print(fruit3.display())