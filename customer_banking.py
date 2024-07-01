# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your initial saving account balance? '))
    savings_interest = float(input('What is the APR for the saving account? '))
    savings_balance_maturity = int(input('What is the length of months for your savings account? '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_balance_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('These are the details of the savings account.')
    print("The balance is: $", format(updated_savings_balance, ',.2f'))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("Interest Rate is: ", format(savings_interest,',.2f'),"%")
    # Call the create_cd_account function and pass the variables from the user.
    cd_account_balance = float(input('What is your initial saving account balance? '))
    cd_account_interest = float(input('What is the APR for the saving account? '))
    cd_account_balance_maturity = int(input('What is the length of months for your savings account? '))
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    updated_cd_balance, interest_earned = create_cd_account(cd_account_balance, cd_account_interest, cd_account_balance_maturity)
    print('Here are the details of the CD account.')
    print("The balance is: $",format (updated_cd_balance, ',.2f'))
    print("Interest Rate is:", format(cd_account_interest, ',.2f'),'%')
    print("Length of CD is: ", format (cd_account_balance_maturity))

if __name__ == "__main__":
    # Call the main function.
     print(f"Thanks for visiting,!")
     main()