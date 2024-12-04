#safe = the levels are either all increasing or all decreasing
#any 2 adjacent levels differ by at least 1 and max 3
path = "./AdventOfCode/input_folder/input2_1.txt"

with open("input2_1.txt") as file:
    data = []
    for line in file:
        data.append(line)

list_of_list = [list(map(int, line.split())) for line in data]

plist = [[69, 68, 70, 65, 63],[3, 6, 8, 11, 14, 17, 19, 20],[26, 28, 27, 29, 34],[69, 68, 67, 65, 63]]

def main():
    tp_list = check1(list_of_list)
    result = check2(tp_list)
    antal = len(result)
    print(antal)

    

def check1(list_of_list):
    tmp_safe = []

    for sublist in list_of_list:
        is_safe = True
        for count, num in enumerate(sublist[:-1]):
            diff = sublist[count+1] - num
            if abs(diff) >= 1 and abs(diff) <= 3:
                is_safe = True
            else:
                is_safe = False
                break
        if is_safe == True:
            tmp_safe.append(sublist)
    return tmp_safe

def check2(tp_list):
    final_list = []
    for sublist in tp_list:
        new_tmp_lst = sublist.copy()
        x = sorted(new_tmp_lst, reverse = False)
        y = sorted(new_tmp_lst, reverse = True)
        if sublist == x or sublist == y:
            final_list.append(sublist)
        else:
            print(f"Listen er ikke udelukkende increasing eller decreasing - se listen her: {sublist}")
            
    return final_list
        
    
            
if __name__ == "__main__":
    main()            
