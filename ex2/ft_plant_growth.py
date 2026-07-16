#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int, speed: str) -> None:
        self.name: str = name
        self.height: float = round(height, 1)
        self.age: int = age
        self.speed: str = speed
        self.growth: float = 0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self.height, 1)}cm, ", end="")
        print(f"{self.age} days old")

    def grow(self) -> None:
        if self.speed == "slow":
            self.height += 0.8
            self.growth += 0.8
        elif self.speed == "medium":
            self.height += 1.3
            self.growth += 1.3
        elif self.speed == "fast":
            self.height += 2.1
            self.growth += 2.1


def ft_plant_growth() -> None:
    plant = Plant("rose", 25.0, 30, "slow")
    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, 8):
        print("=== Day ", day, " ===")
        plant.age += 1
        plant.grow()
        plant.show()
    print(f"Growth this week: {plant.growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
