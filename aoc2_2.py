#safe = the levels are either all increasing or all decreasing
#any 2 adjacent levels differ by at least 1 and max 3
path = "./AdventOfCode/input_folder/input2_1.txt"

with open("input2_1.txt") as file:
    data = []
    for line in file:
        data.append(line)

list_of_list = [list(map(int, line.split())) for line in data]

#liste til tests
plist = [[69, 68, 70, 65, 63],[3, 6, 8, 11, 14, 17, 19, 20],[26, 28, 27, 29, 34],[69, 68, 67, 65, 63]]

def main():
    result = iterate_thru(list_of_list)
    antal = len(result)
    print(antal)
    

def iterate_thru(plist):
    check1_list = []
    for sublist in plist:
        for i in range(len(sublist)):
            tmp_rapport = sublist[:i] + sublist[i+1:]
            print(f"rapporten som undersøges: {tmp_rapport}")
            if check1(tmp_rapport) == True:
                print(f"{tmp_rapport} passer alle kriterier")
                check1_list.append(tmp_rapport)
                break
            
    return(check1_list)


def check1(tmp_rapport):
    for count, num in enumerate(tmp_rapport[:-1]):
        diff = tmp_rapport[count+1] - num
        x = 0
        if abs(diff) < 1 or abs(diff) > 3:
            print(f"{diff}passer ikke kriterie 1")
            x = 1
            return False
        print(f"{diff} for rapporten: {tmp_rapport}")
        x = 0
    #step 2
    if x == 0:
        print(f"forsætter med {tmp_rapport}")
        new_tp_list = tmp_rapport.copy()
        x = sorted(new_tp_list, reverse = False)
        y = sorted(new_tp_list, reverse = True)
        if tmp_rapport == x or tmp_rapport == y:
            return True
        else:
            False
        

       
if __name__ == "__main__":
    main()            
