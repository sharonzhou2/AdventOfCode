
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


    return "0"

def addAllNumbers():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines() 
        for line in lines:
            total += int(retrieveFirstLastNumber(line))

    return total

res = addAllNumbers()
print(res)



