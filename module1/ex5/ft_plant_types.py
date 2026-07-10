class Plant:
    def __init__(self, name, height, age):
        self.name: str = name
        self.height: int = round(float(height), 1)
        self.age: int = age


    def show(self):
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{self.height}cm, ", end="")
        print(f"{self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = False


    def ask_bloom(self):
        print(f"[asking the {self.name} to bloom]")
        self.bloom = True

    
    def show_bloom(self):
        if self.bloom:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")
    

    def show_flower(self):    
        super().show()
        print(f"Color: {self.color}")
        self.show_bloom()

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = round(float(trunk_diameter), 1)
        self.shade = False


    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        self.shade = True

    
    def show_shade(self):
        if self.shade:
            print(f"Tree {self.name.capitalize()} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")
            

    def show_tree(self):    
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        self.show_shade()

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = 0


    def let_age(self, days):
        print(f"[make {self.name} grow and age for {days} days]")
        self.nutritional_value = days
        self.age = self.age + days
        self.grow()

    
    def grow(self):
        for _ in range(self.nutritional_value):
            self.height += 2.1
        self.height = round(float(self.height), 1)     
            

    def show_vegetable(self):    
        super().show()
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")



def ft_plant_types():
    rose = Flower("rose", 15, 10, "red")
    oak = Tree("oak", 200, 365, 5)
    tomato = Vegetable("tomato", 5, 10, "april") 
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show_flower()
    rose.ask_bloom()
    rose.show_flower()
    print()
    print("=== Tree")
    oak.show_tree()
    oak.produce_shade()
    oak.show_shade()
    print()
    print("=== Vegetable")
    tomato.show_vegetable()
    tomato.let_age(20)
    tomato.show_vegetable()


if __name__ == "__main__":
    ft_plant_types()
    