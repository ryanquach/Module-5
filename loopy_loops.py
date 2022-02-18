if __name__ == "__main__":
    
    #create a tuple named pokemon
    pokemon = (
        "pikachu",
        "charmander",
        "bulbasaur"
    )
    #prints the first index
    print(pokemon[1])

    #unpack values of pokemon into new variables
    starter1, starter2, starter3 = pokemon
    print(starter1)
    print(starter2)
    print(starter3)

    #tuple of my name
    my_name = tuple("Ryan")
    print(my_name)

    #check for "i" in my name
    print(f"'i' is in my_name: {'i' in my_name}")

    #for loop printing out integers 2 through 10
    for i in range(2, 11):
        print(i)

    #while loop printing out integer s 2 through 10
    i = 2
    while i < 11:
        print(i)
        i += 1

    #for loop that iterates over string and prints each character
    simple_string = "This is a simple string"
    for letters in simple_string:
        print(letters)

    #iterate over nested for loop and print each word 3 times
    simple_set = ("this", "is", "a", "simple", "set")
    for i in simple_set:
        for j in range(1,4):
            print(f"{j}:{i}")






