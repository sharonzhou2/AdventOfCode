import math

def checkCard():
    with open('input.txt') as f:
        lines = f.readlines()

        total = 0

        for line in lines:
            line = line[line.find(":") + 1:]
            line = line.replace("\n", "")

            games = line.split("|")

            total += checkGames(games)

    return total
              
def checkGames(games):
    winning_numbers = games[0]
    chosen_numbers = games[1]

    winning_numbers = [num.strip() for num in winning_numbers.split(" ") if num] 
    winning_number_dict = {}

    for wn in winning_numbers:
        if wn in winning_number_dict:
            winning_number_dict[wn] += 1
        else:
            winning_number_dict[wn] = 1

    chosen_numbers = [num.strip() for num in chosen_numbers.split(" ") if num]
    subTotal = 0

    for numbers in chosen_numbers:
        if numbers in winning_number_dict:
            subTotal += winning_number_dict[numbers]

    return math.floor(2**(subTotal - 1))

print(checkCard())
