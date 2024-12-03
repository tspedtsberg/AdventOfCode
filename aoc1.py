
my_file = open("input1.1.1.txt", "r")
data = my_file.read()
data_into_list = data.split()
#liste 1 odd numre
list_1 = data_into_list[::2]
list_2 = data_into_list[1::2]
my_file.close() 

#laver alle strenge i listen om til integers
intlist_1 = [int(item) for item in list_1]
intlist_2 = [int(item) for item in list_2]

list_of_locations_to_check = []
#første sted at kigge er: Chief Historian's office
#listen er ikke navne men "location_id"    


def main():
    new_list_1, new_list_2 = sortering(intlist_1, intlist_2)
    
    # Find the differences
    dif_list = find_dif(new_list_1, new_list_2)
    
    # Convert differences to positive values
    positive_list = convert_to_pos(dif_list)
    
    # Sum the positive values
    result_sum = summering(positive_list)
    
    # Print the result
    print(result_sum)
    



def sortering(list_1, list_2):
    new_list_1 = sorted(list_1)
    new_list_2 = sorted(list_2)
    return new_list_1, new_list_2

def find_dif(new_list_1, new_list_2):
    dif_list =  [a - b for a, b in zip(new_list_1, new_list_2)]
    return dif_list

def convert_to_pos(dif_list):
    positive_list = [abs(x) for x in dif_list]
    return positive_list

def summering(positive_list):
    result_sum = sum(positive_list)
    return result_sum

if __name__ == "__main__":
    main()