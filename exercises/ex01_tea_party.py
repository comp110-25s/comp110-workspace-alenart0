"""Tea Party"""

__author__ = "730571229"


def main_planner(guests: int) -> None:
    """Tea Party Main Planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Number of tea bags per person"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats per tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of treats and tea"""
    return 0.5 * (tea_count) + 0.75 * (treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party ")))
