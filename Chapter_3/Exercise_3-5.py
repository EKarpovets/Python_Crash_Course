guests = ["Mishka", "Belyash", "Medvedenka", "Mishutka", "Mr. Putin"]
for i in range(0, len(guests)):
    print("You are invited to my party, " + guests[i] + "!")
not_guest = "Mr. Putin"
print(not_guest + " can't come to the party.")
guests.remove(not_guest)
guests.append("Medvedunchik")
for i in range(0, len(guests)):
    print("You are invited to my party, " + guests[i] + "!")