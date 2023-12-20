

def solver1():
    f = open("input2.txt", "r")
    sum=0
    for elem in f.readline().split(","):
        current=0
        for char in elem:
            ascii=ord(char)
            current += ascii
            current = current*17
            current = current % 256
        sum += current
    print(sum)

def computeHash(elem):
    current=0
    for char in elem:
        ascii = ord(char)
        current += ascii
        current = current*17
        current = current % 256
    return current

def solver2():
    boxes_label = {}
    boxes_focal = {}
    for a in range (0,256):
        boxes_label[a]=[]
        boxes_focal[a]=[]
    f = open("input1.txt", "r")
    for elem in f.readline().split(","):
        isEqualSign = len(elem) != len(elem.split("=")[0])
        # =======
        if isEqualSign:
            label = elem.split("=")[0]
            box = computeHash(label)
            focal = elem.split("=")[1]
            if label in boxes_label[box]:
                index = boxes_label[box].index(label)
                boxes_focal[box][index] = focal
            else:
                boxes_focal[box].append(focal)
                boxes_label[box].append(label)
        # -------
        else:
            label = elem.split("-")[0]
            box = computeHash(label)
            if label in boxes_label[box]:
                index = boxes_label[box].index(label)
                boxes_label[box].pop(index)
                boxes_focal[box].pop(index)
        
    sum_focusing_power = 0
    for box in boxes_focal:
        slot  = 1
        for lens in boxes_focal[box]:
            focusing_power = (int(box)+1) * int(slot) * int(lens)
            slot += 1
            sum_focusing_power += focusing_power
    print(sum_focusing_power)
                
             
    

if __name__ == "__main__":
	solver2()