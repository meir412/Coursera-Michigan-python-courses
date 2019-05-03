score = input("Enter Score: ")

score = float(score)

if (score > 1.0 or score < 0.0):
    print("error")
elif (score < 0.6):
    print("F")
elif (score < 0.7):
    print("D")
elif (score < 0.8):
    print("C")
elif (score < 0.9):
    print("B")
else :
    print("A")


