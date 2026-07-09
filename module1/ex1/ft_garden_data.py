class Plant:
    def __init__(self, name, height, age):
        self.name: str = name
        self.height: int = height
        self.age: int = age
    
    
    def show(self):
        name = self.name.capitalize()
        print(f"{name}: ", end="")
        print(f"{self.height}cm, ", end="")
        print(f"{self.age} days old")

def ft_garden_data():
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()

if __name__ == "__main__":
    ft_garden_data()
