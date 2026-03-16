# March Madness Weighted Coinflip
import random
import os
from termcolor import colored

os.system("color")

south = [
    "Auburn",
    "Alabama St./Saint Francis",
    "Louisville",
    "Creighton",
    "Michigan",
    "UC San Diego",
    "Texas A&M",
    "Yale",
    "Ole Miss",
    "San Diego St./UNC",
    "Iowa State",
    "Lipscomb",
    "Marquette",
    "New Mexico",
    "Michigan State",
    "Bryant",
]
west = [
    "Florida",
    "Norfolk State",
    "UConn",
    "Oklahoma",
    "Memphis",
    "Colorado State",
    "Maryland",
    "Grand Canyon",
    "Missouri",
    "Drake",
    "Texas Tech",
    "UNC Wilmington",
    "Kansas",
    "Arkansas",
    "Saint John's",
    "Omaha",
]
east = [
    "Duke",
    "American/Mount St. Mary's",
    "Mississippi State",
    "Baylor",
    "Oregon",
    "Liberty",
    "Arizona",
    "Akron",
    "BYU",
    "VCU",
    "Wisconsin",
    "Montana",
    "Saint Mary's",
    "Vanderbilt",
    "Alabama",
    "Robert Morris",
]
midwest = [
    "Houston",
    "SIU Edwardsville",
    "Gonzaga",
    "Georgia",
    "Clemson",
    "McNeese",
    "Purdue",
    "High Point",
    "Illinois",
    "Texas/Xavier",
    "Kentucky",
    "Troy",
    "UCLA",
    "Utah State",
    "Tennessee",
    "Wofford",
]

seed_order = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]

regions = [south, west, east, midwest]
for region in regions:
    for index, team in enumerate(region):
        region[index] = f"{team} ({seed_order[index]})"

counter = 1

noise = float(input("How much noisy randomness would you like to add? (0-100): "))
regular = 100 - noise

def get_winning_percentage(name):
    while True:
        try:
            return float(input(f"{name} Predicted Win Percentage: "))
        except:
            print("Invalid. Try again")



def compete(region):
    global counter

    while len(region) > 1:
        winners = []
        for name_1, name_2 in zip(region[::2], region[1::2]):
            print(f"Matchup {counter}: {name_1} vs. {name_2}")
            counter += 1

            team_1 = get_winning_percentage(name_1)
            team_2 = get_winning_percentage(name_2)

            sum = team_1 + team_2

            team_1_chance = (team_1 / sum) * 100
            team_2_chance = (team_2 / sum) * 100

            print(f"{name_1} Chance to win: {round(team_1_chance, 2)}%")
            print(f"{name_2} Chance to win: {round(team_2_chance, 2)}%")

            noise_flip = random.random() * 100
            flip = random.random() * 100

            if noise_flip < noise:
                print(colored("RANDOM ACTIVATED", "cyan"))
                winner = name_1 if flip < 50 else name_2

            else:
                winner = name_1 if flip < team_1_chance else name_2

            print(
                colored(f"Result: {round(flip, 2)} \nWinner: {winner}", "light_magenta")
            )
            winners.append(winner)

        region = winners

    return region[0]


final_four = []

for region in regions:
    winner = compete(region)
    final_four.append(winner)

champion = compete(final_four)
print(f"Your final champion is {champion}!")
input("Finished!")
