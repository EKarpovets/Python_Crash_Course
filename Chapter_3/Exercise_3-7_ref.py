guests = ["Mishka", "Belyash", "Medvedenka", "Mishutka", "Mr. Putin"]

def print_invitation(guests):
    for i in range(0, len(guests)):
        print("You are invited to my party, " + guests[i] + "!")
print_invitation(guests)

not_guest = "Mr. Putin"
print(not_guest + " can't come to the party.")
guests.remove(not_guest)
guests.append("Medvedunchik")
print_invitation(guests)

print("Hey, bears! I found a bigger dinner table! Let's invite someone else!")
guests.insert(0, "Medveditsa")
guests.insert(3, "Belyanochka")
guests.append("Medvedunchik2")
print_invitation(guests)
print("I'm sorry, bears! But the bigger dinner table will not be here in time...")

def remove_guests(guests, i):
    while len(guests) > i:
        popped_guest = guests.pop()
        print("I'm sorry, but you are no longer invited to the party, " + popped_guest)
remove_guests(guests, 2)

print_invitation(guests)

for i in range(0, len(guests)):
    del guests[0]
print(guests)