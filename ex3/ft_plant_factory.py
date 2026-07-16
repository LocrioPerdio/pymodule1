#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int, speed: str) -> None:
        self.name: str = name
        self.height: float = round(height, 1)
        self.age: int = age
        self.speed: str = speed
        self.growth: float = 0

    def show(self) -> None:
        print(f"Created: {self.name.capitalize()}: ", end="")
        print(f"{self.height}cm, ", end="")
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


def ft_plant_factory() -> None:
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
