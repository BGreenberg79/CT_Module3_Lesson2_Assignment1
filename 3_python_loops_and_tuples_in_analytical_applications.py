#Task 1 Stock Market Data Analysis

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def average_closing_price(stock_data_list, chosen_symbol, *dates_selected):
    closing_price_list = []
    # for stock_tuple in stock_data_list:
    #   if chosen_symbol not in stock_tuple[0]:
    #       print("Please select a stock symbol in the database.")
    #   for date in dates_selected:
    #       if date not in stock_tuple[1]:
    #           print("Please select dates that are in the stock database") 
    '''Trying to check for stocks or dates not in the database did not work using "not in" sytax so used try except block instead'''
    try:
        for stock_tuple in stock_data_list:
            if stock_tuple[0] == chosen_symbol and stock_tuple[1] in dates_selected:
                closing_price_list.append(stock_tuple[2])
        price_avergae = sum(closing_price_list) / len(closing_price_list)
        return price_avergae
    except (UnboundLocalError, ZeroDivisionError):
        print("Error: Please ensure stock and dates selected are in database")

select_date_list = []
class AverageError(Exception):
    '''Raised when improper user input is used for our function and no average returns'''
    pass

while True:
    choose_symbol = input("What stock symbol would you like to find the average closing price for: ").upper()
    while True:
        choose_date = input("What dates would you like to look up for the average (YYYY-MM-DD): ")
        select_date_list.append(choose_date)
        more_date = input("Would you like to add more dates to average (Y/N): ")
        if more_date.upper() == "N":
            break
        else:
            continue
    average_price = average_closing_price(stock_data, choose_symbol, *select_date_list)
    if average_price == None:
        raise AverageError("Improper stock or dates choosen, please try again.")
    elif average_price != None:
        print(f"The average closing price for {choose_symbol} over the chosen time period is {str(average_price)}")
    more_lookup = input("Would you like to find another average (Y/N): ")
    if more_lookup.upper() == "N":
        break
    else:
        continue

'''
The main function of avergae_closing_price works by passing through the arguments of the list we are pulling information from, the stock we are choosing to find an average price for, and the dates we are averaging
As I mentioned earlier I used a try, except blockt to catch any invalid input for stocks or dates not in the database.
After looping through each tuple in the list of tuples, that is our database, the fuction is checking for a match for the chosen stock in the first index location of each tuple and any matching days in the first index location from our list of dates selected.
Then for any matches we add it to a localized list of closing prices and use the division of the sum by the len fucntions of that list to return an average
I then use two nested while loops for the user to be able to input their chosen stock to average and to include as many days as they would like to choose. 
Inside the outer while loop I run the function I defined with the user inputs taken and then I either raise a custom exception again if the function is run with invalid inputs or user an f-string to  print the result.
I then ask if the user would like to find an additional average before breaking the outer while loop.
'''