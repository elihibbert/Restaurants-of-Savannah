#This is a unit test that will review and test every individual function used in the restaurants project
#These functions do not have a clear input/outputs so this will be unofficial testing written as comments.
#Each function will have a list of things to test, I will then go out and test and confirm.

#Import all the functions used in the restaurants project to test
'''
from restaurant import main, main_menu
from add_restaurant import add_new, add_review
from view_restaurant import view_new, view_review
from additional_functions_restaurant import remove_name
'''


def test_main():
    #Test invalid inputs - SUCCESSFUL
    '''
    Invalid option --> reprompted if:
        user_input = ["test", "Option 0", "Option 5", "opion 3", "option3", "option three"]
    '''
    #Test valid inputs - SUCCESSFUL
    '''
    Valid and redirected as listed:
    user_input = "OPTION 1"
    #assert add_new()
    user_input = "opTIon 2"
    #assert add_review()
    user_input = "Option 3       "
    #assert view_new()
    user_input = "      Option 4"
    #assert view_review()
    '''

def test_add_new():
    #Test name variable - SUCCESSFUL
    '''
    Invalid --> reprompt if:
        blank, name already exists in the list
    Valid --> entered into the to_try.csv file if:
        integer/float, any string, test a name that exists in the visited list but not the to try list
    '''
    #Test food type and description - SUCCESSFUL
    '''
    Valid --> entered into the to_try.csv file if:
        blank, int/float/str, string includes comma, sting includes '
    Also test: random capitalization is turned to lower, strip method with random spacing
    '''

def test_add_review():
    #Test name variable - SUCCESSFUL
    '''
    Invalid --> reprompt if:
        blank, name already exists in the list (test caps and whitespace on this)
    Valid --> entered into the visited.csv file if:
        integer/float, any string, exists in the to try list but not the visited list,
        exists in the reviewed list but spelled slightly wrong
    '''
    #Test rating variable - SUCCESSFUL
    '''
    Invalid --> reprompt if:
        blank, str value, less than 1, greater than 10
    Valid --> 1-10 integer
    What is the result of a float? --> float is invalid
    '''
    #Test food type and description - SUCCESSFUL
    '''
    Valid --> entered into the visited.csv file if:
        blank, int/float/str, string includes comma, sting includes '
    Also test: random capitalization is turned to lower, strip method with random spacing
    '''

def test_remove_name():
    #Test valid input - SUCCESSFUL
    '''
    If a name is input into the visited list that exists on the to_try list it should be deleted from the to_try list
    Test exact name match. Capitalization differences, spacing differences, different type and descriptions.
    '''
    #Test invalid input - SUCCESSFUL
    '''
    Test a close but different name, test a random unrelated name, test a name with 1 character different, 
        test the case where CTRL+C is used before the enitre input process is completed,
        test a name already in the visited list but not the to try list
    '''

def test_view_new():
    #Test re-prompting for options - SUCCESSFUL
    '''
    Invalid --> reprompt if:
        test, option 4, opin 3, option3, option three
    Valid if:
        OPTION 1, opTIon 2,     option 3      ,
        SPACING DID NOT WORK
    '''
    #Test option 1 - View all - SUCCESSFUL
    '''
    option 1 views the entire table, check against csv file
    '''
    #Test option 2 - search for a specific restaurant - SUCCESSFUL
    '''
    Shows a valid result if:
        valid name input with varying capitalization and whitespace. Test before and after a new restaurant is added.
    Shows an empty response if:
        invalid name, one character off, two names attempted to search for, type of food searched for instead of name, 
        name from reviewed list searched for 
    '''
    #Test option 3 - Filter for specific food type - SUCCESSFUL
    '''
    Shows valid result if:
        Existing type of food searched for (multiple result or just 1 result depending on type), with capitalization,
        with extra whitespace, test the same food type before and after it is input to see difference
    Shows an empty result if:
        food type is not present, if food type is present in other visited list, if food type is spelled wrong,
        if the name of the restaurant is searched for, something from the description is searched for
    What happens if you search for blank? --> blank is returned
    '''

def test_view_review():
    #Test re-prompting for options - SUCCESSFUL
    '''
    Invalid --> reprompt if:
        test, option 5, opin 3, option3, option three
    Valid if:
        OPTION 1, opTIon 2,     option 3  , oPtIoN 4
    '''
    #Test option 1 - View all - SUCCESSFUL
    '''
    option 1 views the entire table, check against csv file
    '''
    #Test option 2 - sort by rating - SUCCESSFUL
    '''
    Check against the csv file that it is accurate and same number of values
    '''
    #Test option 3 - Filter for specific food type - SUCCESSFUL
    '''
    Shows valid result if:
        Existing type of food searched for (multiple result or just 1 result depending on type), with capitalization,
        with extra whitespace, test the same food type before and after it is input to see difference
    Shows an empty result if:
        food type is not present, if food type is present in other to try list, if food type is spelled wrong,
        if the name of the restaurant is searched for, if something from the description is searched for.
    '''
     #Test option 4 - search for a specific restaurant - SUCCESSFUL
    '''
    Shows a valid result if:
        valid name input with varying capitalization and whitespace. Test before and after a new restaurant is added.
    Shows an empty response if:
        invalid name, one character off, two names attempted to search for, type of food searched for instead of name, 
        name from to try list searched for 
    '''
def test_various():
    #Test these random other thoughts
    '''
    Test 
    '''