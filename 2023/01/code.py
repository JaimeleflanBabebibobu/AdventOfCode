
def char_replace(line):
    newline = line
    dict = {"one" : "on1e",
            "two" : "tw2o",
            "three" : "th3ree",
            "four" : "fou4r",
            "five" : "fi5ve",
            "six" : "si6x",
            "seven" : "se7ven",
            "eight" : "ei8ght",
            "nine" : "ni9ne"}
    for key in dict:
        newline = newline.replace(key, dict[key])
    return newline


def solver():
    f = open("input1.txt", "r")
    sum = 0
    for line in f:
        first = ""
        last = ""
        newline = char_replace(line)
        for char in newline:
            if char.isnumeric():
                if first == "":
                    first = char
                last = char
        sum += int(first+last)
    print(sum)

if __name__ == "__main__":
	solver()