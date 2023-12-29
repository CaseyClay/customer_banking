# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('What is the starting balance of the savings account? '))
    savings_interest = float(input('Please enter an interest rate? '))
    savings_maturity = int(input('How many months? '))                   
    # Call the create_savings_account function and pass the variables from the user.
    updated_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'the interest earned on the savings account is ${interest_earned:.2f}')
    print(f'the updated savings account balance is ${updated_balance:.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('what is the starting balance of the cd account? '))
    cd_interest = float(input('please enter an interest rate? '))
    cd_maturity = int(input('how many months? '))
    # Call the create_cd_account function and pass the variables from the user.
    cd_balance_updated, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'the interest earned on the CD account is ${cd_interest_earned:.2f}')
    print(f'the updated CD account balance is ${cd_balance_updated:.2f}')
if __name__ == "__main__":
    # Call the main function.
    main()