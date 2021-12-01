def get_depths():
    # read input file into a list of reported depths
    with open("./input.txt", "r") as in_file:
        depths = [int(num) for num in in_file.readlines()]
    return depths

def main():
    depths = get_depths()
    # store total num of depths larger than 1st record
    total1 = len([i for i in range(len(depths)) if depths[i] > depths[i - 1]])
    # store total num of sums greater than 1st 3-depth sum
    total2 = len([i for i in range(len(depths)) if (sum(depths[i:i-3:-1])) > (sum(depths[i-1:i-4:-1]))])
    print(f"Part 1 Answer: {total1}")
    print(f"Part 1 Answer: {total2}")

if __name__ == "__main__":
    main()
