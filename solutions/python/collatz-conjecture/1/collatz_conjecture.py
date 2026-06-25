def steps(number):
    if number > 0:
        steps = 0
        while (number > 1):
            #print (number)
            #print ("steps: ",steps)
            if isEven(number):
                number = number // 2
                steps = steps + 1
                #print("Dividing by 2")
                #print(number)
            else:
                number = (number * 3) + 1
                steps = steps + 1
                #print("other shit")
                #print(number)
        return steps
    raise ValueError("Only positive integers are allowed")
def isEven(number):
    if number % 2 == 0:
        return True
    return False