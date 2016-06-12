guests = ["Mishka", "Belyash", "Medvedenka", "Mishutka", "Mr. Putin"]

def print_invitation(guests):
    for i in range(0, len(guests)):
        print("You are invited to my party, " + guests[i] + "!")
print_invitation(guests)

print(str(len(guests)) + " guests are invited to my party")
