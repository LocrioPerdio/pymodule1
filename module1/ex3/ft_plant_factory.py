class Plant:
    def __init__(self, name, height, age, speed):
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.speed: str = speed
        self.growth: float = 0
    
    
    def show(self):
        name = self.name.capitalize()
        height = round(self.height, 1)
        print(f"Created: {name}: ", end="")
        print(f"{height}cm, ", end="")
        print(f"{self.age} days old")
    

    def grow(self):
        if self.speed == "slow":
                self.height +=0.8
                self.growth += 0.8
        elif self.speed == "medium":
                self.height +=1.3
                self.growth += 1.3
        elif self.speed == "fast":
                self.height +=2.0
                self.growth += 2.0       


def ft_plant_factory():
    rose = Plant("rose", 25.0, 30, "slow")
    oak = Plant("oak", 200.0, 365, "slow")
    cactus = Plant("cactus", 5.0, 90, "medium")
    sunflower = Plant("sunflower", 80.0, 45, "fast")
    fern = Plant("fern", 15.0, 120, "fast")
    print("=== Plant Factory Output ===")
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
    
    
if __name__ == "__main__":
    ft_plant_factory()