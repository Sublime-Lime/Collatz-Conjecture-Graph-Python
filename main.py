import matplotlib.pyplot as plt
userInput = ""
while True:
    if userInput.isnumeric():
        myNum = float(userInput)
        if myNum > 0:
            break
    else:
        userInput = input("Enter number to generate collatz conjecture graph for (>0): ")
y = [myNum]
x = [1]
while True:
    if y[-1] == 1:
        break
    elif y[-1] % 2 == 0:
        y.append(y[-1]/2)
        x.append(x[-1]+1)
    else:
        y.append(y[-1]*3+1)
        x.append(x[-1]+1)
plt.plot(x, y, '-x')
plt.ylabel('Number Value')
plt.xlabel('Number of iterations')
plt.show()
