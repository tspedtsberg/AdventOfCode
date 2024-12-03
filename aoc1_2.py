

my_file = open("input1.1.1.txt", "r")
data = my_file.read()
data_into_list = data.split()
#liste 1 odd numre
list_1 = data_into_list[::2]
list_2 = data_into_list[1::2]
my_file.close() 

#laver alle strenge i listen om til integers
intlist_1 = [int(item) for item in list_1] # venstre
intlist_2 = [int(item) for item in list_2] # højre

def main():
    similarity_score = 0

    for num in intlist_1: # løber numre igennem i liste 1
        count = intlist_2.count(num) #count er antallet af gange num fra liste 1 optræder i liste2
        similarity_score += num * count #Der bliver lagt en sum af count og selve nummeret fra 1 til scoren
    
    
    print(similarity_score)
    
    


    
        

    

    


if __name__ == "__main__":
    main() 



