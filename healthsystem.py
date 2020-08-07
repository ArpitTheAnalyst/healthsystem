# Health management system
## 3 clients - arpit, raman , nishant

import datetime
ts = datetime.datetime.now()
print("Welcome to health management system :>")
print("what would like to do:\n(1)logging\n(2)Retrieving\n")
query = input(">> ")
print("for which client: \n(1)arpit\n(2)raman\n(3)nishant\n")
client = input(">> ")
if query=="1" or query==("logging"):
    print("which activity would you like to log :")
else:
    print("which activity would you like to retrieve :")
print("(1)Exercising\n(2)Diet\n")
activity = input(">> ")
def logging():
    if query == "logging" or query=="1":
        if client.lower() =="arpit" or client == "1":
            if activity.lower()== "exercising" or activity=="1":
                with open("exercising_arpit.txt","at") as f:
                   f.write(str(f"[{ts}]> "))
                   f.write(input("Enter name of the exercise arpit did today : "))
                   f.write("\n")
            else:
                with open("food_arpit.txt", "at") as f:
                   f.write(str(f"[{ts}]> "))
                   f.write(input("Enter what arpit ate: "))
                   f.write("\n")
        elif client.lower()=="raman" or client=="2":
           if activity.lower()=="exercising" or activity=="1":
             with open("exercising_raman.txt", "at") as f:
                 f.write(str(f"[{ts}]> "))
                 f.write(input("Enter name of exercise raman did today : "))
                 f.write("\n")
           else:
                with open("food_raman.txt", "at") as f:
                 f.write(str(f"[{ts}]> "))
                 f.write(input("enter what raman ate today: "))
                 f.write("\n")
        elif client.lower()=="nishant" or client=="3":
            if activity.lower()=="Exercising" or activity=="1":
                with open("exercising_nishant.txt", "wt") as f:
                   f.write(str(f"[{ts}]> "))
                   f.write(input("Enter name of exercise nishant done : "))
                   f.write("\n")
            else:
                with open("food_nishant.txt","wt") as f:
                    f.write(str(ts))
                    f.write(input("Enter what nishant ate: "))
                    f.write("\n")
logging()
def retrieve():
    if query.lower()=="retrieve" or query=="2":
        if client.lower() =="arpit" or client == "1":
            if activity.lower()== "exercising" or activity=="1":
                with open("exercising_arpit.txt") as f:
                    eap=f.read()
                    print(eap)
            else:
                with open("food_arpit") as f:
                    fap= f.read()
                    print(fap)
        elif client.lower=="raman" or client=="2":
            if activity.lower()=="exercising" or activity=="1":
                with open("exercising_raman.txt") as f:
                    erm=f.read()
                    print(erm)
            else:
                with open("food_raman.txt") as f:
                    frn=f.read()
                    print(frn)
        elif client.lower()=="nishant" or client=="3":
            if activity.lower()=="exercising" or activity=="1":
                with open("exercising_nishant.txt") as f:
                    ent=f.read()
                    print(ent)
            else:
                with open("food_nishant.txt") as f:
                    fnt=f.read()
                    print(fnt)
        else:
            print("thanx...but no such client or activitry discovered....try again")

retrieve()











