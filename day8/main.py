from os import read


def read_input():
    with open('./input.txt','r') as in_file:
        lines = in_file.readlines()

    return [{'in': line.split(' | ')[0].strip(), 'out': line.split(' | ')[1].strip()} for line in lines]

def part1():
    # grab the input
    lines = read_input()
    # map used to store numbers and their # of segments
    len_map = {
        2:1,
        4:4,
        3:7,
        7:8
    }
    total = len([chunk for line in lines for chunk in line['out'].split(' ')  if len(chunk) in len_map.keys()])
    print(total)


if __name__ == '__main__':
    part1()