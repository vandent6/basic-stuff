

def print_board(size):
    intSize = int(size)
    for i in range(0, intSize):
        print(" ---" * intSize)
        print("|   " * (intSize + 1))
    print(" ---" * intSize)


size = input("What size board do you want to play on? ")

print_board(size)
