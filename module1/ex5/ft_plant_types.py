class Plant:
    def __init__(self, name, height, age):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self):
        height = round(float(self.height), 1)
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{height}cm, ", end="")
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
        print("=== Flower")
        super().show()
        print(f"Color: {self.color}")
        self.show_bloom()

def ft_plant_types():
    rose = Flower("rose", 15, 10, "red")
    print("=== Garden Plant Types ===")
    rose.show_flower()
    rose.ask_bloom()
    rose.show_flower()



if __name__ == "__main__":
    ft_plant_types()
    