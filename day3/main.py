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
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print(f"gamma_rate: {gamma_rate}")
    print(f"epsilon_rate: {epsilon_rate}")
    print(f"power consumption: {gamma_rate * epsilon_rate}")


def most_common(arr):
    occ_0 = 0
    occ_1 = 0
    for num in arr:
        if num == '0':
            occ_0 += 1
        else:
            occ_1 += 1
    if occ_0 == occ_1:
        return '-1'
    return '0' if occ_0 > occ_1 else '1'

def least_common(arr):
    occ_0 = 0
    occ_1 = 0
    for num in arr:
        if num == '0':
            occ_0 += 1
        else:
            occ_1 += 1
    if occ_0 == occ_1:
        return '-1'
    return '0' if occ_0 < occ_1 else '1'


def get_o2_rating():
    # this is wild
    # grab report rows
    report = get_report()
    rep_length = len(report[0])
    for i in range(rep_length + 1):
        if len(report) == 1:
            o2_rating = report[0]
            return int(o2_rating,2)
        loop_list = [line[i] for line in report]
        targ_bit = most_common(loop_list)
        if targ_bit != '-1':
            report = [line for line in report if line[i] == targ_bit]
        else:
            report = [line for line in report if line[i] == '1']

def get_co2_rating():
    report = get_report()
    rep_length = len(report[0])
    for i in range(rep_length + 1):
        if len(report) == 1:
            co2_rating = report[0]
            return int(co2_rating,2)
        loop_list = [line[i] for line in report]
        targ_bit = least_common(loop_list)
        if targ_bit != '-1':
            report = [line for line in report if line[i] == targ_bit]
        else:
            report = [line for line in report if line[i] == '0']

def part2():
    print(get_co2_rating() * get_o2_rating())

if __name__ == "__main__":
    part2()
