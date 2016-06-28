magicians = ['alice', 'robert', 'jim', 'maria', 'jane']
copy_magicians = magicians[:]

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for i in range(0, len(magicians)):
        magicians[i] = "the Great " + magicians[i].title()

make_great(copy_magicians)
show_magicians(magicians)
show_magicians(copy_magicians)
