def make_sandwich(*fillings):
    print("\nMaking a sandwich with:")
    for filling in fillings:
        print("- " + filling)

make_sandwich('tuna', 'onions', 'cucumbers')
make_sandwich('ham')
make_sandwich('ham', 'cheese')