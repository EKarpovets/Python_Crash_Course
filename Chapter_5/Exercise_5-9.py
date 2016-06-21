users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello, admin! Would you like to see a status report?")
        else:
            print("Hello, " + user + "! Thank you for logging in again.")
else:
    print('We need to find some users!')