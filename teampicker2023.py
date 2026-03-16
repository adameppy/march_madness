# March Madness Weighted Coinflip
import random
import os
from termcolor import colored

os.system("color")

south = [
    "Alabama",
    "TAMU-CC/SEMO",
    "Maryland",
    "West Virginia",
    "San Diego St.",
    "Charleston",
    "Virginia",
    "Furman",
    "Creighton",
    "NC State",
    "Baylor",
    "UCSB",
    "Missouri",
    "Utah St.",
    "Arizona",
    "Princeton",
]
east = [
    "Purdue",
    "Texas Southern",
    "Memphis",
    "Florida Atlantic",
    "Duke",
    "Oral Roberts",
    "Tennessee",
    "Louisiana",
    "Kentucky",
    "Providence",
    "Kansas St.",
    "Montana St.",
    "Michigan St.",
    "USC",
    "Marquette",
    "Vermont",
]
midwest = [
    "Houston",
    "Northern Ky.",
    "Iowa",
    "Auburn",
    "Miami (FL)",
    "Drake",
    "Indiana",
    "Kent St.",
    "Iowa St.",
    "Mississippi St.",
    "Xavier",
    "Kennesaw St.",
    "Texas A&M",
    "Penn St.",
    "Texas",
    "Colgate",
]
west = [
    "Kansas",
    "Howard",
    "Arkansas",
    "Illinois",
    "Saint Mary's",
    "VCU",
    "UConn",
    "Iona",
    "TCU",
    "Arizona St./Nevada",
    "Gonzaga",
    "Grand Canyon",
    "Northwestern",
    "Boise St.",
    "UCLA",
    "UNC Asheville",
]

seed_order = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]

regions = [south, east, midwest, west]
for region in regions:
    for index, team in enumerate(region):
        region[index] = f"{team} ({seed_order[index]})"

counter = 1

noise = float(input("How much noisy randomness would you like to add? (0-100): "))
regular = 100 - noise


def compete(region):
    global counter

    while len(region) > 1:
        winners = []
        for name_1, name_2 in zip(region[::2], region[1::2]):
            print(f"Matchup {counter}: {name_1} vs. {name_2}")
            counter += 1

            team_1 = float(input(f"{name_1} Predicted Win Percentage: "))
            team_2 = float(input(f"{name_2} Predicted Win Percentage: "))

            sum = team_1 + team_2

            team_1_chance = (team_1 / sum) * 100
            team_2_chance = (team_2 / sum) * 100

            print(f"{name_1} Chance to win: {round(team_1_chance, 2)}%")
            print(f"{name_2} Chance to win: {round(team_2_chance, 2)}%")

            noise_flip = random.random() * 100
            flip = random.random() * 100

            if noise_flip < noise:
                print(colored("RANDOM ACTIVATED", "cyan"))
                winner = name_1 if random.random() < 50 else name_2

            else:
                winner = name_1 if flip < team_1_chance else name_2

            print(colored(f"Result: {round(flip, 2)} \nWinner: {winner}", "light_magenta"))
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