def make_list():
    with open("input.txt") as f:
        lines = f.readlines()
        # loop thru each line, split by a double newline
        # then split each line by a single newline, and convert
        # each line to a list of ints
    return sum([int(calib[0] + calib[-1]) for calib in [[c for c in calib if str.isnumeric(c)] for calib in[list(line) for line in [line.strip() for line in lines]] ]])

def main():
    print(make_list())


if __name__ == '__main__':
    main()
