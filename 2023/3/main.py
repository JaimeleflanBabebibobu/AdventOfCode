def isSymbol(character, searchFor=None):
    if searchFor is None:
        result = not(character.isdigit()) and character != "."
    else : 
        result = not(character.isdigit()) and character != "." and character == searchFor
    return result

def isThereSymbolInLocations(locations, matrix, searchFor=None):
    if searchFor is not None:
        for xy in locations:
            if isSymbol(matrix[xy[0]][xy[1]], searchFor):
                return True, (xy[0], xy[1])
        return False, ()
    else:
        for xy in locations:
            if isSymbol(matrix[xy[0]][xy[1]]):
                return True
        return False

def check_around(matrix, line, column, searchFor=None):
    all_locations= [[line-1, column -1], [line-1, column], [line-1, column +1],
                    [line, column -1] ,                    [line, column +1],
                    [line+1, column -1], [line+1, column], [line+1, column +1]]
    if line==0:
        all_locations.remove([line-1, column -1])
        all_locations.remove([line-1, column])
        all_locations.remove([line-1, column +1])
        if column==0:
            all_locations.remove([line, column -1])
            all_locations.remove([line+1, column -1])
        elif column==len(matrix[line])-1:
            all_locations.remove([line, column +1])
            all_locations.remove([line+1, column +1])
    elif line==len(matrix)-1:
        all_locations.remove([line+1, column -1])
        all_locations.remove([line+1, column])
        all_locations.remove([line+1, column +1])
        if column==0:
            all_locations.remove([line-1, column -1])
            all_locations.remove([line, column -1])
        elif column==len(matrix[line])-1:
            all_locations.remove([line-1, column +1])
            all_locations.remove([line, column +1])
    else:
        if column==0:
            all_locations.remove([line+1, column -1])
            all_locations.remove([line-1, column -1])
            all_locations.remove([line, column -1])
        elif column==len(matrix[line])-1:
            all_locations.remove([line-1, column +1])
            all_locations.remove([line, column +1])
            all_locations.remove([line+1, column +1])
    return isThereSymbolInLocations(all_locations, matrix, searchFor)

def check_around_for_gear(matrix, line, column):
    return check_around(matrix, line, column, "*")

def solver():
    list_numbers_with_symbol_around = []
    linenumber = 0
    with open('input.txt', 'r') as f:
        matrix = [[num for num in line if num != "\n"] for line in f]
    for line in matrix:
        currently_reading_int = False
        current_has_symbol_around = False
        current_int = ""
        for column, char in enumerate(line):
            if char.isdigit():
                currently_reading_int = True
                current_int += char
                current_has_symbol_around = current_has_symbol_around or check_around(matrix, linenumber, column)
            else:
                if currently_reading_int == True:
                    currently_reading_int = False
                    if current_has_symbol_around:
                        list_numbers_with_symbol_around.append(int(current_int))
                    current_int=""
                    current_has_symbol_around = False
        if currently_reading_int == True:
            currently_reading_int = False
            if current_has_symbol_around:
                list_numbers_with_symbol_around.append(int(current_int))
            current_int=""
            current_has_symbol_around = False
        linenumber+=1
    finalresult = 0
    for elem in list_numbers_with_symbol_around:
        finalresult += elem 
    print(finalresult)

def solver2():
    dict_gears_what_around = {}
    linenumber = 0
    with open('input.txt', 'r') as f:
        matrix = [[num for num in line if num != "\n"] for line in f]
    for line in matrix:
        currently_reading_int = False
        current_has_symbol_around = False
        current_int = ""
        current_gear_coordinates = ()
        for column, char in enumerate(line):
            if char.isdigit():
                currently_reading_int = True
                current_int += char
                isThereGear, gear_coordinates = check_around_for_gear(matrix, linenumber, column)
                if current_gear_coordinates == ():
                    current_gear_coordinates = gear_coordinates
                current_has_symbol_around = current_has_symbol_around or isThereGear
            else:
                if currently_reading_int == True:
                    currently_reading_int = False
                    if current_has_symbol_around:
                        if current_gear_coordinates in dict_gears_what_around:
                            dict_gears_what_around[current_gear_coordinates].append(int(current_int))
                        else:
                            dict_gears_what_around[current_gear_coordinates]=[int(current_int)]
                    current_int=""
                    current_has_symbol_around = False
                    current_gear_coordinates = ()
        if currently_reading_int == True:
            currently_reading_int = False
            if current_has_symbol_around:
                if current_gear_coordinates in dict_gears_what_around:
                    dict_gears_what_around[current_gear_coordinates].append(int(current_int))
                else:
                    dict_gears_what_around[current_gear_coordinates]=[int(current_int)]
            current_int=""
            current_has_symbol_around = False
            current_gear_coordinates = ()
        linenumber+=1
      
    finalresult = 0
    for key in dict_gears_what_around:
        current_gear_result = 0
        if len(dict_gears_what_around[key])>1:
            for number in dict_gears_what_around[key]:
                if current_gear_result == 0:
                    current_gear_result += number
                else:
                    current_gear_result *= number
        finalresult += current_gear_result
    print(finalresult)

if __name__ == "__main__" :
    solver2()