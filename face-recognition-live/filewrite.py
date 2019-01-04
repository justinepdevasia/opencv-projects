import os
j=1

while(True):

	if not os.path.exists('user-info/'+str(j)+'.txt'):
	   		break
	else:
			j=j+1


print(j)

os.system("espeak your--name--is--not--in--the--data")
os.system("espeak hi---whats--your---name")
print("write your name")
name=raw_input()
file=open("user-info/"+str(j)+".txt","w")
file.write(name)
file.close()
os.system("espeak let----me--take--your--photos--for--future")
os.system("espeak please---pose---for--the--photo")
os.system("python splitvdeo.py")
os.system("espeak thankyou---yourr--photos--have--been--taken")
