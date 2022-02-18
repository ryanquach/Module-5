if __name__ == "__main__":

    #prompt user for floating point values until stop is entered
        my_list = []
        input_value = 0
        while input_value != "stop":
            my_list.append(float(input_value))
            input_value = input("Please Enter Floating Point Value:").lower()
        my_list.pop(0)
    
        if len(my_list) > 0:
            print(f"Your Final List is {my_list}")
            average_list = sum(my_list) / len(my_list)
            print(f"The average of the list is {average_list}")
            print(f"The minimum of the list is {min(my_list)}")
            print(f"The maximum of the list is {max(my_list)}")

        print("Finished, Quitting...")
