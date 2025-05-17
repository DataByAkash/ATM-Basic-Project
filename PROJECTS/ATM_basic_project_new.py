# ATM Basic Project
# This is a simple command-line ATM project I built to understand how ATM machines work.
# It includes features like checking balance, deposit, withdrawal, PIN change 

# ----------- Function Definitions -----------

# Function to show account balance after verifying the PIN
def show_account_balance(pin, user_pin, account_balance):
    if user_pin == pin:
        print(f'Your current account balance is: ₹{account_balance}')
    else:
        print('You entered the wrong pin.')

# Function to deposit cash using different denominations
def cash_deposit(account_number, user_account_number, account_balance):
    if user_account_number == account_number:
        # Taking number of notes from user
        notes_of_2000 = int(input(' 2000   X    '))
        notes_of_500 = int(input('  500    X    '))
        notes_of_200 = int(input('  200    X    '))
        notes_of_100 = int(input('  100    X    '))

        # Calculating total deposit amount
        total = (2000 * notes_of_2000) + (500 * notes_of_500) + (200 * notes_of_200) + (100 * notes_of_100)
        print(f'\nCash ₹{total} deposited successfully ')
        print(f'Updated account balance: ₹{account_balance + total}')
    else:
        print('Invalid account number ')

# Function to withdraw cash after verifying PIN
def cash_withdrawal(pin, user_pin, account_balance):
    if user_pin == pin:
        cash = int(input('Enter cash to withdraw: ₹'))
        if cash <= account_balance:
            if cash <= 50000:
                print(f'\nPlease collect your ₹{cash}')
                print(f'Your updated account balance is ₹{account_balance - cash}')
            else:
                print(' You cannot withdraw more than ₹50000 at once.')
        else:
            print(' Insufficient funds.')
    else:
        print(' Invalid PIN.')

# Function to change the ATM PIN
def pin_change(pin, user_pin):
    if user_pin == pin:
        new_pin = input('Enter new PIN: ')
        re_enter_pin = input('Re-enter new PIN: ')
        if new_pin == re_enter_pin:
            pin = new_pin  # This will not persist as it's local, but for now it's okay
            print('PIN changed successfully.')
        else:
            print(' PINs do not match.')
    else:
        print(' You cannot change the PIN.')



# ----------- Main Program Starts Here -----------

# Initial values
pin = '4321'
account_balance = 500000
account_number = '1234567890'

# ATM Interface
print('Welcome to XYZ Bank'.center(50, '-'))

# Showing options
print('\n1. Show Account Balance')
print('2. Cash Deposit')
print('3. Cash Withdrawal')
print('4. PIN Change')


# Taking user option
user_option = input('\nSelect any option (1/2/3/4): ')

# Performing operations based on user's choice
if user_option == '1':
    user_pin = input('Enter PIN: ')
    show_account_balance(pin, user_pin, account_balance)

elif user_option == '2':
    user_account_number = input('Enter account number: ')
    cash_deposit(account_number, user_account_number, account_balance)

elif user_option == '3':
    user_pin = input('Enter PIN: ')
    cash_withdrawal(pin, user_pin, account_balance)

elif user_option == '4':
    user_pin = input('Enter PIN: ')
    pin_change(pin, user_pin)

else:
    print(' Invalid option selected.')
