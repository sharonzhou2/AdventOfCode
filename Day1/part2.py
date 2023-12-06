

numbersAsWordsDict = {
    "one" : 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

replaceWords = {
    "oneight": "oneeight",
    "twone": "twoone",
    "threeight": "threeeight",
    "fiveight": "fiveeight",
    "eightwo": "eighttwo",
    "eighthree": "eightthree",
    "nineight": "nineeight"
}


    
def replaceUnevenWords(word):
    newWord = word
    for key in replaceWords:
        if key in word:
            newWord = newWord.replace(key, replaceWords[key])
    return newWord

print(replaceUnevenWords("beightwoone6rqjcqq7sixfourrkghseven"))

def convertToNumbers(word):
    newWord = word
    i = 0
    while i <= (len(word)):
        pointerA = i
        pointerB = pointerA + 1
        while pointerB <= len(word):
            key = newWord[pointerA:pointerB]
            if key in numbersAsWordsDict:
                newWord = newWord[:pointerA] + str(numbersAsWordsDict[key]) + newWord[pointerB:]
                pointerA = pointerB - 1
            else:
                pointerB += 1
            
        i += 1
            
    return newWord

print(convertToNumbers("3twonltnmdqttqmj6fivefivesix"))



def retrieveFirstLastNumber(word):
    pointerA = 0
    pointerB = len(word) - 1


    while pointerA != pointerB:
        if word[pointerA].isdigit() and word[pointerB].isdigit():
            return word[pointerA] + word[pointerB]
        
        if not word[pointerA].isdigit():
            pointerA += 1

        if not word[pointerB].isdigit():
            pointerB -= 1
    
    if pointerA == pointerB:
        if word[pointerA].isdigit():
            return word[pointerA] + word[pointerA]
        
        if word[pointerB].isdigit():
            return word[pointerB] + word[pointerB]


    return ""

def addAllNumbers():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines() 
        for line in lines:
            numbers = convertToNumbers(replaceUnevenWords(line))
        

          
            total += int(retrieveFirstLastNumber(numbers))

    return total

print(addAllNumbers())



