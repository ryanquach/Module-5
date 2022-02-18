if __name__ == "__main__":
    
    #create empty dictionary named pokedex
    pokedex = {}

    #add key, value pairs to pokedex
    pokedex["Venosaur"] = ["Grass", "Poison"]
    pokedex["Charizard"] = ["Fire", "Flying"]
    pokedex["Blastoise"] = ["Water"]
    #prints dictionary line by line
    for key, value in pokedex.items():
        print(key, ":", value)

    #remove Blastoise from dictionary
    del pokedex["Blastoise"]
    for key, value in pokedex.items():
        print(key, ":", value)