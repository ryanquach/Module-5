if __name__ == "__main__":
    
    #create list named food with two elements
    food = ["rice", "beans"]
    print(food)
    
    #append "broccoli" to food
    food.append("broccoli")
    print(food)

    #add strings to food using .extend()
    food.extend(["bread", "pizza"])
    print(food)

    #print first two items in food using slicing notation
    print(food[:2])

    #print last item in food using index notation
    #subtract length by 1 to find last index
    print(len(food) - 1) 
    print(food[4])

    #create list from string using split()
    breakfast_string = "eggs,fruit,orange juice"
    breakfast= breakfast_string.split(',')
    print(breakfast)

    #verify breakfast_list has 3 elements
    breakfast_len = len(breakfast)
    print(f"breakfast is 3 elements long: {breakfast_len == 3}")

    #prompt user for floating point values until stop is entered
    my_list = []
    i = 0
    while i < 1:
        input_value = input("Please enter floating point value or stop:").lower()
        if input_value == "stop":
            print("Loop has stopped")
            print(f"Final list is: {my_list}")
            break
        my_list.append(float(input_value))
        print(f"Current list is: {my_list}")
            
    #so it doesn't produce an error when immediately stopped
    if len(my_list) > 0:
        average_list = sum(my_list) / len(my_list)
        print(f"The average of the list is: {average_list}")
        print(f"The minimum value of the list is: {min(my_list)}")
        print(f"The maximum value of the list is {max(my_list)}")
       
        
