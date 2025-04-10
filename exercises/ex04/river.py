"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        living_fish = [fish for fish in self.fish if fish.age <= 3]
        living_bears = [bear for bear in self.bears if bear.age <= 5]
        self.fish = living_fish
        self.bears = living_bears
        return None

    def remove_fish(self, amount: int):
        for fish in range(min(amount, len(self.fish))):
            del self.fish[0]
        return None

    def bears_eating(self):
        if len(self.fish) >= 5:
            for bear in self.bears:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        not_starving_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = not_starving_bears
        return None

    def repopulate_fish(self):
        fish_pairs_t4 = (len(self.fish) // 2) * 4
        for fish in range(fish_pairs_t4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        bear_pairs = len(self.bears) // 2
        for bear in range(bear_pairs):
            self.bears.append(Bear())
        return None

    def view_river(self):

        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

        return None
