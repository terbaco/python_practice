with open(r'd:/0Day/pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
print('\n')
all = ''
for line in lines:
    all += line.strip()

birthday = input("Enter your birthday in the form mmddyy: \n")
if birthday in all:
    print("It's at the position " + str(all.index(birthday)-2) + " after \'.\'\n")
else:
    print("No\n")

newfilename = 'c:/temp/new.txt'
lines = []
step = 8
a = 0
astring = ''
while(a<64):
    astring='\n'
    for i in range(a, a + step):
        astring += str(i)
    a+=step
    lines.append(astring)
with open(newfilename, 'a') as file:
    file.writelines(lines)
'''拆分字符串'''
#endswithit = all.split(birthday)
#newfile = 'd:/0Day/pi_endswith_birthday.txt'
#with open(newfile, 'w') as file:
#    file.write(endswithit)

print(all)
print(len(all))
