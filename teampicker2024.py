# March Madness Weighted Coinflip
import random
import os
from termcolor import colored

os.system("color")

south = [
    "Houston",
    "Longwood",
    "Nebraska",
    "Texas A&M",
    "Wisconsin",
    "James Madison",
    "Duke",
    "Vermont",
    "Texas Tech",
    "NC State",
    "Kentucky",
    "Oakland",
    "Florida",
    "Boise St./Colorado",
    "Marquette",
    "Western Kentucky",
]
east = [
    "UConn",
    "Stetson",
    "Florida Atlantic",
    "Northwestern",
    "San Diego St.",
    "UAB",
    "Auburn",
    "Yale",
    "BYU",
    "Duquesne",
    "Illinois",
    "Morehead St.",
    "Washington St.",
    "Drake",
    "Iowa St.",
    "South Dakota St. ",
]
midwest = [
    "Purdue",
    "MSU/Grambling",
    "Utah St.",
    "TCU",
    "Gonzaga",
    "McNeese",
    "Kansas",
    "Samford",
    "South Carolina",
    "Oregon",
    "Creighton",
    "Akron",
    "Texas",
    "Virginia/Colorado St.",
    "Tennessee",
    "Saint Peter’s",
]
west = [
    "North Carolina",
    "Howard/Wagner",
    "Mississippi St.",
    "Michigan St.",
    "Saint Mary’s",
    "Grand Canyon",
    "Alabama",
    "Charleston",
    "Clemson",
    "New Mexico",
    "Baylor",
    "Colgate",
    "Dayton",
    "Nevada",
    "Arizona",
    "Long Beach St.",
]

seed_order = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]

regions = [east, west, south, midwest]
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
