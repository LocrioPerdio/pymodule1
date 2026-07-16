#!/usr/bin/python3
class Plant:
    def __init__(self, name: str, height: float, age: int, speed: str) -> None:
        self.name: str = name
        self.height: float = round(float(height), 1)
        self.age: int = age
        self.speed: str = speed
        self.stats = self.Stats(self)
        self.growth: float = 0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self.height, 1)}cm, ", end="")
        print(f"{self.age} days old")
        self.stats.add_show()

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

    class Stats:
        def __init__(self, plant: 'Plant') -> None:
            self.plant = plant
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0
            self._shade_calls = 0

        def add_grow(self) -> None:
            self.__grow_calls += 1

        def add_shade(self) -> None:
            self._shade_calls += 1

        def add_age(self) -> None:
            self.__age_calls += 1

        def add_show(self) -> None:
            self.__show_calls += 1

        def show_stats(self) -> None:
            print(f"[statistics for {self.plant.name.capitalize()}]")
            print(f"Stats: {self.__grow_calls} grow, {self.__age_calls}"
                  f" age, {self.__show_calls} show")

    @staticmethod
    def check_year_old(age: int) -> None:
        checker: bool = False
        if age > 365:
            checker = True
        print(f"Is {age} days more than a year? -> {checker}")

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0, "")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, speed: str, color: str) -> None:
        super().__init__(name, height, age, speed)
        self.color: str = color
        self.bloom: bool = False

    def grow_and_bloom(self) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.bloom = True
        self.height += 8
        self.stats.add_grow()

    def grow_age_and_bloom(self) -> None:
        print(f"[make {self.name} to grow, age and bloom]")
        self.bloom = True
        self.age += 20
        self.height += 30
        self.stats.add_age()

    def show_bloom(self) -> None:
        if self.bloom:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def show_flower(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        self.show_bloom()


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, speed: str, color: str) -> None:
        super().__init__(name, height, age, speed,  color)
        self.seeds: int = 0

    def seed_grow(self) -> None:
        super().grow_and_bloom()
        self.seeds += 42

    def seed_age(self) -> None:
        super().grow_age_and_bloom()
        self.seeds += 42

    def show_seed(self) -> None:
        super().show_flower()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, speed: str, trunk_diameter: float) -> None:
        super().__init__(name, height, age, speed)
        self.stats = self.TreeStats(self)
        self.trunk_diameter = round(float(trunk_diameter), 1)
        self.shade: bool = False

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self.shade = True
        self.stats.add_shade()

    def show_shade(self) -> None:
        if self.shade:
            print(f"Tree {self.name.capitalize()} now produces a shade of "
                  f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show_tree(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
        self.show_shade()

    class TreeStats(Plant.Stats):
        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self._shade_calls} shade")


def display_statistics(plant: Plant) -> None:
    plant.stats.show_stats()


def ft_plant_analytics() -> None:
    rose = Flower("rose", 15, 10, "medium", "red")
    oak = Tree("oak", 200, 365, "slow", 5)
    sunflower = Seed("sunflower", 80, 45, "slow", "yellow",)
    anonymous = Plant.create_anonymous()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year_old(30)
    Plant.check_year_old(400)
    print()
    print("=== Flower")
    rose.show_flower()
    rose.stats.show_stats()
    rose.grow_and_bloom()
    rose.show_flower()
    display_statistics(rose)
    print()
    print("=== Tree")
    oak.show_tree()
    display_statistics(oak)
    oak.produce_shade()
    oak.show_shade()
    display_statistics(oak)
    print()
    print("=== Seed")
    sunflower.show_seed()
    sunflower.seed_age()
    sunflower.show_seed()
    display_statistics(sunflower)
    print()
    print("=== Anonymous")
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    ft_plant_analytics()
