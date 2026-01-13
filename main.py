import random


class Monster:
    def __init__(self, name, max_health, attack, speed, type_):
        self.name = name
        self.__max_health = max_health
        self.__health = max_health
        self.__attack = attack
        self.__speed = speed
        self.__type = type_
        self.__level = 1

    def take_damage(self, amount):
        self.__health -= amount

    def is_alive(self):
        return self.__health > 0

    def attack(self, target):
        damage = random.randint(self.__attack - 2, self.__attack + 2)
        target.take_damage(damage)
        return damage

    def get_health(self):
        return self.__health

    def get_max_health(self):
        return self.__max_health

    def get_speed(self):
        return self.__speed


def alive_monsters(team):
    return [m for m in team if m.is_alive()]


def battle(team_a, team_b):
    print("Battle begins!")

    round_num = 1
    while alive_monsters(team_a) and alive_monsters(team_b):
        print(f"\n-- Round {round_num} --")

        # build turn order: all alive monsters from both teams
        turn_order = alive_monsters(team_a) + alive_monsters(team_b)
        turn_order.sort(key=lambda m: m.get_speed(), reverse=True)

        for actor in turn_order:
            # actor might have died earlier this round
            if not actor.is_alive():
                continue

            # stop if one team is wiped mid-round
            if not alive_monsters(team_a) or not alive_monsters(team_b):
                break

            # decide target: pick first alive from opposing team
            if actor in team_a:
                target_team = team_b
            else:
                target_team = team_a

            target = alive_monsters(target_team)[0]

            damage = actor.attack(target)
            print(f"{actor.name} hits {target.name} for {damage} damage!")

            if not target.is_alive():
                print(f"{target.name} is defeated!")

        round_num += 1

    # winner
    if alive_monsters(team_a) and not alive_monsters(team_b):
        print("\nTeam A wins!")
        return "A"
    elif alive_monsters(team_b) and not alive_monsters(team_a):
        print("\nTeam B wins!")
        return "B"
    else:
        print("\nBoth teams are down! It's a draw.")
        return "draw"


def make_monster(kind):
    if kind == "slime":
        return Monster("Slime", 30, 5, 3, "earth")
    elif kind == "bat":
        return Monster("Bat", 20, 8, 9, "air")
    elif kind == "goblin":
        return Monster("Goblin", 25, 9, 7, "earth")
    elif kind == "orc":
        return Monster("Orc", 40, 10, 4, "earth")
    elif kind == "skeleton":
        return Monster("Skeleton", 28, 12, 6, "dark")
    elif kind == "stone_golem":
        return Monster("Stone Golem", 60, 7, 1, "earth")
    elif kind == "fire_imp":
        return Monster("Fire Imp", 18, 13, 11, "fire")
    elif kind == "wraith":
        return Monster("Wraith", 26, 14, 10, "dark")
    elif kind == "ogre":
        return Monster("Ogre", 70, 15, 3, "earth")
    else:
        raise ValueError(f"Unknown enemy type: {kind}")


def main():
    pass


if __name__ == '__main__':
    main()
