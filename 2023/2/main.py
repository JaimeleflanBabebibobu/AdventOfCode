
def find_max_in_game_for_colors(list_of_colors, game):
    dict_max_colors={}
    for color in list_of_colors:
        dict_max_colors[color]=0
    subsets = game.split(";")
    for subset in subsets:
        number_per_colors = subset.split(",")
        for color_and_number in number_per_colors:
            number=int([int(s) for s in color_and_number.split() if s.isdigit()][0])
            color=[s for s in color_and_number.split() if not s.isdigit()][0]
            if dict_max_colors[color]<number:
                dict_max_colors[color]=number
    return dict_max_colors

def compute_possible_game(max_color_per_game, blue, green, red):
    sum=0
    for game in max_color_per_game:
        if max_color_per_game[game]['blue']<=blue and max_color_per_game[game]['green']<=green and max_color_per_game[game]['red']<=red:
            sum+=int(game)
    print(sum)

def compute_power(color_dict):
    sum=0
    for game in color_dict:
        color_score = 1
        for color in color_dict[game]:
            color_score *= color_dict[game][color]
        sum+= color_score
    print(sum)


def solver():
    f = open("input.txt", "r")
    max_color_per_game = {}
    for line in f:
        game_number=line.split(":")[0].split(" ")[-1]
        max_color_per_game[game_number]=find_max_in_game_for_colors(["blue", "green", "red"], line.split(":")[-1])
    blue = 14
    green = 13
    red = 12
    compute_possible_game(max_color_per_game, blue, green, red)

def solver2():
    f = open("input.txt", "r")
    min_color_per_game = {}
    for line in f:
        game_number=line.split(":")[0].split(" ")[-1]
        min_color_per_game[game_number]=find_max_in_game_for_colors(["blue", "green", "red"], line.split(":")[-1])
    compute_power(min_color_per_game)

if __name__ == "__main__" :
    solver2()