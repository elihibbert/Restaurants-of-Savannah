#This is the main file in this project that will prompt a user to see how they want to interact.
#The user can add restaurants "to try" or "to visit" or can view the restaurants within the lists.

#Import important libraries
from add_restaurant import add_new, add_review
from view_restaurant import view_new, view_review



def main():
    '''
    This main function is used to run the entire project.
    This function will act as the directory to ask for and direct the user's requests.
    The function is placed within a while loop to allow for re-prompting if incorrect syntax is used.
    '''
    
    while True:
        #See what the user wants to do
        user_input = main_menu().lower().strip()

        #Filter through the options and re-direct to the correct function
        if user_input == "option 1": #To add a new restaurant to try.
            add_new()
            print("Success! Restaurant to try added to the list.")
            break

        elif user_input == "option 2": #To review a restaurant that was recently tried.
            add_review()
            print("Success! Restaurant review added to the list.")
            break

        elif user_input == "option 3": #To view all the restaurants that want to be tried.
            view_new()
            break

        elif user_input == "option 4": #To view all the restaurants that have been reviewed.
            view_review()
            break

        else: #Incorrect user input
            print("Invalid selection, please try again and select Option 1-4.")
            continue








def main_menu():
    '''
    This function presents a main menu to the user. 
    The user should then select if they want to add a new restaurant to try, review a restaurant after trying it,
        view the list of restaurants to try, or view the list of rated restaurants.
    Input's should be using the syntax "Option N" where N is a number between 1 and 4.
    This function then returns the users selection as a string.
    '''
    print()
    print()
    print("************************MAIN MENU************************")
    print()
    print("Welcome to Savannah Georgia! There are so many great restaurants in town.")
    print()
    print("What would you like to do?")
    print()
    print("Option 1  -  Add a new restaurant to try")
    print("Option 2  -  Review a restaurant after visiting")
    print("Option 3  -  View the list of restaurants to try")
    print("Option 4  -  View the list of rated restaurants")
    print()

    #user input
    return str(input("Your choice: "))







if __name__ == "__main__":
    main()