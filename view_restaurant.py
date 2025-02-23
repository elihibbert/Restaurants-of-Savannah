#This is the file that will allow the user to view the restaurant data with various methods.

#Import libraries
import pandas as pd



def view_new(): #Option 3 from Main Menu
    '''
    This function will allow the user to view all the restaurants of the list of restaurants to try.
    The user will have the option to view all the restaurants on the list, search for a specific restaurant,
        or filter by a specific food type.
    Data handling and viewing will be done using the pandas package.
    This function has no inputs or outputs.
    '''
    #Use a while true loop to allow for re-prompting of options if incorrect syntax is used.
    while True:

        #Ask what the user wants to do
        print()
        print()
        print("******** How would you like to proceed to view the restaurants on your list to try? ********")
        print()
        print("Option 1 - View all")
        print("Option 2 - Search for a specific restaurant")
        print("Option 3 - Filter by a specific type of food")
        print()
        user_input = input("Your choice: ").lower().strip()

        #Use Pandas package to build the data frame that will be used in each option
        to_try_dataframe = pd.read_csv("to_try.csv")
        
        


        #Option 1 - View all
        if user_input == "option 1":
            
            #Print all data
            print(to_try_dataframe.to_markdown())
            break



        #Option 2 - Search for a specific restaurant
        elif user_input == "option 2": 
            print()
            name_desired = str(input("Restaurant name: ")).lower().strip() #What is the name of the restaurant they are looking for?
            print()

            #Find the restaurant using the Pandas package
            your_restaurant = to_try_dataframe[to_try_dataframe.name == name_desired]

            #Print the desired restaurant
            print(your_restaurant.to_markdown())
            break



        #Option 3 - Filter by a specific type of food
        elif user_input == "option 3":
            print()
            filter = str(input("Type of food: ")).lower().strip()  #What type of food do they want to filter the results by?
            print()

            #Find the restaurants the have the type of food specified
            your_food_type = to_try_dataframe[to_try_dataframe.food_type == filter]

            #Print the desired restaurants
            print(your_food_type.to_markdown())
            break



        #Invalid user input
        else:
            print("Option 1, Option 2, or Option 3 must be selected. Please try again.")
            continue












def view_review(): #Option 4 from main menu
    '''
    This function will be used to view all the rated restaurants in the system.
    The user will have the option to view all, sort by rating, sort by food type, or search for a specific restaurant.
    Data handling and viewing will be done using the pandas package.
    This function has no inputs or outputs.
    '''
    #Use a while true loop to allow for re-prompting of options if incorrect syntax is used.
    while True:

        #Ask what the user wants to do
        print()
        print()
        print("******** How would you like to proceed to view your rated restaurants? ********")
        print()
        print("Option 1 - View all")
        print("Option 2 - Sort restaurants by rating")
        print("Option 3 - Filter by a specific type of food")
        print("Option 4 - Search for a specific restaurant from the list")
        print()
        user_input = input("Your choice: ").lower().strip()

        #Use Pandas package to build the data frame that will be used in each option
        visited_dataframe = pd.read_csv("visited.csv")



        #Option 1 - View all
        if user_input == "option 1":

            #Print all data
            print(visited_dataframe.to_markdown())
            break



        #Option 2 - Sort by restaurant rating
        elif user_input == "option 2":

            #Use pandas to sort the data
            sorted_rating = visited_dataframe.sort_values("rating", ascending=False)

            #Print sorted data
            print(sorted_rating.to_markdown())
            break



        #Option 3 - Filter by a specific food type
        elif user_input == "option 3":
            print()
            filter = str(input("Type of food: ")).lower().strip()  #What do they want to filter the results by?
            print()

            #Find the restaurants the have the type of food specified using the Pandas package
            your_food_type = visited_dataframe[visited_dataframe.food_type == filter]

            #Print the desired restaurants
            print(your_food_type.to_markdown())
            break



        #Option 4 - Search for a specific restaurant from the list
        elif user_input == "option 4":
            print()
            name_desired = str(input("Restaurant name: ")).lower().strip() #What is the name of the restaurant they are looking for?
            print()

            #Find the restaurant using the Pandas package
            your_restaurant = visited_dataframe[visited_dataframe.name == name_desired]

            #Print the desired restaurant
            print(your_restaurant.to_markdown())
            break



        #Incorrect syntax
        else:
            print("Option 1, Option 2, Option 3, or Option 4 must be selected. Please try again.")
            continue








