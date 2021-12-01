def main():
    # first, read input file into a list of reported depths
    with open("./input.txt", "r") as in_file:
        depths = [int(num) for num in in_file.readlines()]

    # store total num of depths larger than 1st record
    total = 0
    for i in range(len(depths)):
        if depths[i] > depths[i - 1]:
            total += 1
    print(total)

if __name__ == "__main__":
    main()
