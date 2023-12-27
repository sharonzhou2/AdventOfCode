MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def checkMaxInGame(games, gamesDict):
    gamesArray = games.split(",")


    for game in gamesArray:
        gameWordsList = game.split(" ")
        value = int(gameWordsList[1])
        colour = gameWordsList[2]

        if colour not in gamesDict:
            gamesDict[colour] = value
        else:
            gamesDict[colour] += value
    # print(gamesDict)
    

    return isSatisfyGameColour(gamesDict)



def isSatisfyGameColour(gamesDict):
    for colour in gamesDict:
        value = gamesDict[colour]
        # print(colour, value)
        if colour == "blue":
            if value > MAX_BLUE_CUBES:
                return False
        
        if colour == "green":
            if value > MAX_GREEN_CUBES:
                return False
        
        if colour ==  "red":
            if value > MAX_RED_CUBES:
                return False
    
    return True


# print(isSatisfyGameColour(" 14 green, 8 blue, 9 red"))


def runAllInput():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()

        for line in lines:
            line = line[line.find(":") + 1:]
            subTotal = 0

            line = line.replace("\n", "")
            games = line.split(";")
            gamesDict = {}

            for game in games:
                if checkMaxInGame(game, gamesDict):
                    # print("satisfied")
                    subTotal += 1
                else:
                    subTotal = 0
                    break
            print(subTotal)
            total += subTotal
    return total


print(runAllInput())