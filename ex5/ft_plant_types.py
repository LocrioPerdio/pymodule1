#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int, speed: str) -> None:
        self.name: str = name
        self.height: float = round(float(height), 1)
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


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, speed: str, color: str) -> None:
        super().__init__(name, height, age, speed)
        self.color = color
        self.bloom = False

    def ask_bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloom = True

    def show_bloom(self) -> None:
        if self.bloom:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def show_flower(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        self.show_bloom()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, speed: str,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, speed)
        self.trunk_diameter = round(float(trunk_diameter), 1)
        self.shade: bool = False

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self.shade = True

    def show_shade(self) -> None:
        if self.shade:
            print(f"Tree {self.name.capitalize()} now produces a shade "
                  f"of {self.height}cm long and {self.trunk_diameter}cm wide.")

    def show_tree(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        self.show_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, speed: str, harvest_season: str) -> None:
        super().__init__(name, height, age, speed)
        self.harvest_season: str = harvest_season.capitalize()
        self.nutritional_value: int = 0

    def let_age(self, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        self.nutritional_value = days
        self.age: int = self.age + days
        for _ in range(self.nutritional_value):
            super().grow()

    def show_vegetable(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    rose = Flower("rose", 15, 10, "medium",  "red")
    oak = Tree("oak", 200, 365, "slow",  5)
    tomato = Vegetable("tomato", 5, 10, "fast", "april")
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
