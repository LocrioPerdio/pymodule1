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
        print(f"{name}: ", end="")
        print(f"{height}cm, ", end="")
        print(f"{self.age} days old")
    

    def grow(self):
        if self.speed == "slow":
                self.height +=0.8
                self.growth += 0.8
        elif
            self.speed == "medium":
                self.height +=1.3
                self.growth += 1.3
        elif
            self.speed == "fast":
                self.height +=2.0
                self.growth += 2.0       


def ft_plant_growth():
    plant = Plant("rose", 25.0, 30, "slow")
    print("=== Garden Plant Growth ===")
    plant.show()
    for _ in range(1, 8):
        print("=== Day ", _, " ===")
        plant.age += 1
        plant.grow()
        plant.show()
    print(f"Growth this week: {plant.growth}cm")

if __name__ == "__main__":
    ft_plant_growth()