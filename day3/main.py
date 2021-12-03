def get_report():
    with open("./input.txt", "r") as in_file:
        lines = [line.strip() for line in in_file.readlines()]
    return lines


def part1():
    # grab report rows
    report = get_report()
    # to store gamma rate values
    gamma_rate = ""
    epsilon_rate = ""
    # get length of each report line
    rep_length = len(report[0])
    for i in range(rep_length):
        total_0 = 0
        total_1 = 0
        for line in report:
            if line[i] == "0":
                total_0 += 1
            else:
                total_1 += 1
        if total_1 > total_0:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print(f'gamma_rate: {gamma_rate}')
    print(f'epsilon_rate: {epsilon_rate}')
    print(f'power consumption: {gamma_rate * epsilon_rate}')

if __name__ == '__main__':
    part1()