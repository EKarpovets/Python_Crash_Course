magicians = ['alice', 'robert', 'jim', 'maria', 'jane']

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

show_magicians(magicians)

def make_great(magicians):
    for i in range(0, len(magicians)-1):
        magicians[i] = "the Great " + magicians[i].title()

make_great(magicians)
print(magicians)
