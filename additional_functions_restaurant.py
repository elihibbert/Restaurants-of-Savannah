import pandas as pd

def remove_name(desired_name):
    '''
    This function will help remove a restaurant from the to_try.csv file if necessary.
    When a new restaurant is added to the visited.csv file, it is checked if that restaurant is already written on the to_try.csv file.
    If it is found, it is removed.
    The input for this function is the name of the restaurant to check and remove. No outputs are returned.
    This function is called under option 2 from the main menu
    '''
    #Use Pandas package to build the data frame that will be searched from the to_try.csv file.
    to_try_dataframe = pd.read_csv("to_try.csv")

    #Index the data frame to find the desired restaurant name. If it does not exist, this will remain blank and nothing will delete.
    index_number = to_try_dataframe.index[to_try_dataframe.name == desired_name]

    #Delete the name's row (if found)
    to_try_dataframe = to_try_dataframe.drop(index_number)


    #Use pandas to re-write the file to_try.csv
    to_try_dataframe.to_csv("to_try.csv", index=False)


