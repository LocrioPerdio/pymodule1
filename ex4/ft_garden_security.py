#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, _height: float, _age:
                 int, speed: str) -> None:
        self.name: str = name
        self.valid: bool = True
        self._height = self.set_height(_height)
        self.set_age(_age)
        self.speed: str = speed
        self.growth: float = 0

    def grow(self) -> None:
        if self.speed == "slow":
            self._height += 0.8
            self.growth += 0.8
        elif self.speed == "medium":
            self._height += 1.3
            self.growth += 1.3
        elif self.speed == "fast":
            self._height += 2.1
            self.growth += 2.1

    def show(self) -> None:
        _height = round(self._height, 1)
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{_height}cm, ", end="")
        print(f"{self._age} days old")

    def show_created(self) -> None:
        print("Plant created: ", end="")
        self.show()
        print()

    def show_current(self) -> None:
        print("Current state: ", end="")
        self._height = round(float(self._height), 1)
        self.show()

    def set_height(self, _height: float) -> float:
        if _height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
            self.valid = False
        else:
            self._height = _height
        return _height

    def set_age(self, _age: int) -> None:
        if _age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            self.valid = False
        else:
            self._age: int = _age

    def get_height(self) -> None:
        print(f"Height updated: {self._height}cm")

    def get_age(self) -> None:
        print(f"Age updated: {self._age} days")


def ft_garden_security() -> None:
    rose = Plant("rose", 15.0, 10, "slow")
    if rose.valid:
        print("=== Garden Security System ===")
        rose.show_created()
        rose.set_height(25)
        rose.get_height()
        rose.set_age(30)
        rose.get_age()
        print()
        rose.set_height(-23)
        rose.set_age(-10)
        print()
        rose.show_current()


if __name__ == "__main__":
    ft_garden_security()
