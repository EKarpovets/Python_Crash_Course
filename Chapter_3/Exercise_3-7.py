guests = ["Mishka", "Belyash", "Medvedenka", "Mishutka", "Mr. Putin"]
for i in range(0, len(guests)):
    print("You are invited to my party, " + guests[i] + "!")
not_guest = "Mr. Putin"
print(not_guest + " can't come to the party.")
guests.remove(not_guest)
guests.append("Medvedunchik")
for i in range(0, len(guests)):
    print("You are invited to my party, " + guests[i] + "!")
print("Hey, bears! I found a bigger dinner table! Let's invite someone else!")
guests.insert(0, "Medveditsa")
guests.insert(3, "Belyanochka")
guests.append("Medvedunchik2")
for i in range(0, len(guests)):
    print("You are invited to my party, " + guests[i] + "!")
print("I'm sorry, bears! But the bigger dinner table will not be here in time...")
while len(guests) > 2:
    popped_guest = guests.pop()
    print("I'm sorry, but you are no longer invited to the party, " + popped_guest)
for i in range(0, len(guests)):
    print("You are invited to my party, " + guests[i] + "!")
for i in range(0, len(guests)):
    del guests[0]
print(guests)