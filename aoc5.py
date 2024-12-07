import pathlib
from collections import defaultdict
import functools
# the code doesn't work. its not sorting with the cmp_to_key 

#hente data
rules, content = pathlib.Path("/home/tspedtsberg/AdventOfCode/input_folder/input5test.txt").read_text().strip().split("\n\n")
contenttest = pathlib.Path("/home/tspedtsberg/AdventOfCode/input_folder/input5test.txt").read_text().strip().split("\n")


testrb = {}
#main
def problem1():
    struktureret_content = conv_to_list(content)
    print(struktureret_content)

    ans1, ans2 = sortering(struktureret_content)
    print(f"answer 1 = {ans1}")
    print(f"answer 2 = {ans2}")
    



#strukturering af data:
def conv_to_list(content):
    struktured_list = [] #liste til at holde endelig liste med lister
    for list in content.split("\n"):
            sublist = []
            for num in list.split(","): # spiller listen ved hvert ","
                sublist.append(int(num))# laver num om til int og tilføjer til sublist
            struktured_list.append(sublist)
    return struktured_list

                
#strukturering af rules
def conv(rules):
    rules_tuple = ()
    for rule in rules.split("\n"):
        subtuple = ()
        for x in rule.split("\n"):
            #print(x)
            key, value = x.split("|")
            key_value_tuple = (key, value)
            #print(key_value_tuple)
            subtuple += (key_value_tuple,)
        rules_tuple += subtuple
        #print(rules_tuple)
    rb = defaultdict(set) #en dict men man undgår "keyerror" ved ".add" hvis key ikke allerede eksisterer.
    for first, later in rules_tuple:
        rb[first].add(later)
    #print(rb)
    return(rb)


def create_compare(rb):
    def cmp(a, b):
        for pair in rb:
            #print(a, b)
            if (a, b) == pair:
                print("correct")
                return 1
            else:
                print("uncorrect")
                return -1
        
    return cmp

    

def sortering(content):
    p1 = 0
    p2 = 0
    rb = conv(rules)
    print(rb)
    for list in content:
        print(list)
        y = sorted(list, key=functools.cmp_to_key(create_compare(rb)))
        print(y)
        mid = len(list) // 2
        if y == list:
            #print(sorted(list, key=cmp_to_key(create_compare(rb))))
            p1 += y[mid]
            print(p1) 
        else: 
            x = sorted(list, key=functools.cmp_to_key(create_compare(rb)))
            #print(list.sort(key=cmp_to_key(create_compare(rb))))
            #print("ikke lig liste")
            p2 += x[mid]
            
    return p1, p2
        
            


problem1()