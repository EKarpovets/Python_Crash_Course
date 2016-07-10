def count_words(filename):
    """Count the number of words 'the' in a file."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        number_of_the = contents.lower().count('the')
        print(number_of_the)

filenames = ['true_manliness.txt', 'wide_awake.txt', 'an_essay_on_the_effects_of_opium.txt']
for filename in filenames:
    count_words(filename)