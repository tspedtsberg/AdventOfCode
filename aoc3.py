import re
my_file = open("input3_1.txt", "r")
data = my_file.read()

x = ""
x = re.findall(r"mul\((\d+),(\d+)\)", data)
result = []
for x, y in x:
    result.append((int(x), int(y)))

#print(result)
result2 = []
sum = 0
for x, y in result:
    sum += x * y

print(f"first answer = {sum}")
#print(data)
new_pattern = r"do\(\)(.*?)don't\(\)"
new_match = re.findall(new_pattern, data, re.DOTALL)
begninning = "(who() what())>when()why()'mul(454,153)mul(565,994)(mul(890,533)#mul(875,768)+'-^where()}when()mul(103,598)[mul(401,600)when()from()how()+mul(928,225)why():mul(909,344)when()'?where():(what()mul(972,219)${/ mul(402,908)who()&where()~where()mul(60,961)#]$mul(459,473))})~mul(143,89),select()mul(772,463)mul(742,92)<(]},select()[%^when()"
end = "()$where()%~-~mul(622,257)select()where()*!(mul(764,419)?()*when()}"
combined = " ".join(new_match)
test = begninning + combined + end
#print(test)

string1 = str()
string1 = re.findall(r"mul\((\d+),(\d+)\)", test)
#print(string1)
result1 = []
for x1, y1 in string1:
    result1.append((int(x1), int(y1)))


#print(result)
ans = 0
for x, y in result1:
    ans += x * y

print(ans)
