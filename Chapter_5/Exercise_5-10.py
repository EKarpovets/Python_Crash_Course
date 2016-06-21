current_users = ['admin', 'mishutka', 'kusik', 'belyash', 'medvedenka']
new_users = ['MiShUtKa', 'Kuska', 'Admin', 'Medvedunchik', 'Belyashik2015']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("This username already exists. Pick a new one.")
    else:
        print("This username is available.")