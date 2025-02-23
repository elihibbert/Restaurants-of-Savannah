#This is the file that will allow the user to add restaurants to the "to try" or the "visited" spreadsheets.

#Import libraries
import csv
import pandas as pd
from additional_functions_restaurant import remove_name


def add_new(): #Option 1 from main menu
    '''
    This function is executed when the user wants to add a new restaurant to try.
    Data will be written to the to_try.csv file
    Values written will be name, type of food, and description.
    User will be re-prompted if name is left blank. Type of food and description may be left blank.
    This file has no inputs or returns
    '''

    #Welcome the user
    print()
    print("Trying a new restaurant is exciting! Please add the name of the restaurant, type of food, and a short description of the restaurant you want to try.")
    print()

    #Get restaurant information from the user
    #Name - while loop used to prevent a blank name
    while True:
        name = input("Name: ").lower().strip()
        if not name:
            print("The name of the restaurant cannot be blank. Please enter a valid name.")
            continue
        else:
            break

    #Type of food
    food_type = input("Type of food: ").lower().strip()

    #Description
    description = input("Description: ").lower().strip()
    


    #Check if this restaurant is already on the list
    to_try_dataframe = pd.read_csv("to_try.csv")
    result = to_try_dataframe["name"].eq(name).any()

    #If the name is not found, append information to to_try.csv
    if not result:
        with open("to_try.csv", "a", newline="\n") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "food_type", "description"])
            writer.writerow({"name": name, "food_type": food_type, "description": description})

    #If the name is found, do not append
    else:
        print("This restaurant is already in the list of restaurants to try!")

    





def add_review(): #Option 2 from main menu
    '''
    This function is executed when the user wants to review a restaurant after trying it.
    Data will be written to the visited.csv file
    Values written will be name, type of food, rating, and description.
    The user will be re-prompted if name or rating is left blank or if the rating is invalid (must be an int between 1 and 10).
    The type of food and description may be left blank.
    This file has no inputs or returns
    When a restaurant is reviewed, if it is present in the to_try list, it will be deleted from that list.
    '''
    #Welcome the user
    print()
    print("You tried a new restaurant? That's exciting! Please enter the name, type of food, rating, and a short description.")
    print()

    #Ask the user for input
    #Name
    while True:
        name = input("Name: ").lower().strip()
        if not name:
            print("The name of the restaurant cannot be blank. Please enter valid name.")
            continue
        else:
            break

    #Type of food
    food_type = input("Type of food: ").lower().strip()

    #Rating
    while True:
        try:
            rating = int(input("Rating from 1 to 10: "))
        except ValueError:
            print("The rating of the restaurant must be a NUMBER from 1 to 10.")
            continue
        else:
            if not rating:
                print("A rating of the restaurant is required.")
                continue
            elif rating < 1 or 10 < rating:
                print("Invalid rating")
                continue
            else:
                break

    #Description
    description = input("Description: ").lower().strip()
    
    

    #Check if the restaurant has already been reviewed
    visited_dataframe = pd.read_csv("visited.csv")
    result = visited_dataframe["name"].eq(name).any()

    #If the name is not found, append information to visited.csv
    if not result:
        with open("visited.csv", "a", newline="\n") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "food_type", "rating", "description"])
            writer.writerow({"name": name, "food_type": food_type, "rating": rating, "description": description})
    
    #If the name is found, do not append
    else:
        print("This restaurant is already in the list of rated restaurants!")


    #Remove the restaurant from the to_try list if the restaurant is found in that list. Import function from other file.
    remove_name(name)
    



