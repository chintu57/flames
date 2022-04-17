from pyfiglet import Figlet



def render(text,style):
    f = Figlet(font=style)
    print('\n'*3)
    print(f.renderText(text))

render('FLAMES','slant')
print('\n'*3)
YEL = '\033[33m'
RED = '\033[31m'
BLUE = '\033[34m'
GREEN = '\033[32m'
MGA = '\033[35m'
print(RED + "DESCRIPTION:")
print (RED + "     THIS IS BASED ON LETTERS OF YOUR NAME DONT TAKE THIS AS SERIOUS. JUST KNOW YOUR RELATION AND ENJOY...:)")
print("\n"*2)
name1 = input(YEL + "ENTER YOUR NAMR ").upper()
name2 = input(YEL + "ENTER GIRL NAME ").upper()

print(GREEN + "        Your name is:    ",name1)
print(GREEN + "        Girl name is:    ",name2)

name1 = name1.replace(" ","")
name2 = name2.replace(" ","")

for i in name1:
    for j in name2:
        if i==j:
            name1 = name1.replace(i,"",1)
            name2 = name2.replace(j,"",1)
            break

#print(name1)
#print(name2)

BRIGHT = '\033[1m'

count= len(name1+name2)
#print("Remaining letters after common letters is....",count)
print("\n"*2)

if count>0:
    list = [ "FRIEND","LOVE","AFFECTION","MARRIAGE","ENEMY","SISTER" ]
    while len(list)>1:
        c = count%len(list)
        s_index = c-1
        if s_index>=0:
            left = list[:s_index]
            right = list[s_index+1:]
            list = right+left
        else:
            list = list[:len(list)-1]
    print(BRIGHT + MGA + "Your Relationship is: ",list)
    print("\n"*2)
    print(BRIGHT + BLUE + "               HOPE YOU LIKE THIS......!")
