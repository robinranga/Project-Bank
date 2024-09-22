# Creting a class with user inputs
class bank_acc:
    def __init__(self, name, number, PAN, Add):
        from random import randint
        self.name = name
        self.number = number
        self.PAN = PAN
        self.Add = Add

        # MSG for account creation
        print("Hello there...\n"
              "Your account has been successfuly opened")


# Default balance on account creation
bal = 0

# Status of loan
status = None

# Amount of loan taken
loan_am = 0

# Intrest on loan
intrest = None


# Function for creating account give inputs to the init function of class
def create_acc():
    print("********************Welcome to Robinson Bank********************")
    name = input("Enter your name : ")
    num = int(input("Enter your Mobile Number : "))
    add = input("Enter your Address : ")
    pan = input("Enter your PAN Number : ")
    # Assignig a class to a variable
    person = bank_acc(name, num, pan, add)
    # Getting the var "Person" outside the function by retuning it.
    return person


# Function to have choices for showing details or not
# Auto called after account creation
def get_choice():
    choice = input("If you want to check your details type YES or NO : ")
    if choice.lower() == "yes" or choice.lower() == "y":
        show_det() # Function to show details
        menu()  # Funtion to go to menu
    elif choice.lower() == "no" or choice.lower() == "n":
        print("We are redirecting you to Menu....")
        menu() # Funtion to go to menu
    else:
        print("You have typed something else...\n"
            "Try typing again...")
        get_choice() # Funtion to get choices again because of error


# Funtion to show details (Definition)
def show_det():
    # For generating a random account number
    from random import randint
    # Displaying the details..
    print("Here are your account details....\n"
    f"Name : {person.name}\n"
    f"Mobile Number : {person.number}\n"
    f"PAN Number : {person.PAN}\n"
    f"Address : {person.Add}\n"
    f"Account Number : {randint(12345678,99999999)}")





# Funtion to show menu and all choices in it
def menu():
    # Numbering of choices and taking input as a number...
    print("********************You are at Menu********************")
    print("Welcome here you can select from the following to do your tasks...\n"
          "1. Check Balance\n"
          "2. Account Info\n"
          "3. Add Money\n"
          "4. Withdraw Money\n"
          "5. Loan\n"
          "6. Loan Status\n"
          "7. Complaint\n"
          "8. Back")
    
    # Handling the exception if user enters a string instead of a number
    try:
        menu_input = int(input("Enter your choice : "))
    except ValueError:
        print("No type a number only...")
        menu()

    # Adding conditions for diferent choices
    if menu_input == 1 :
        check_bal()
    elif menu_input == 2:
        show_det()
        menu()        
    elif menu_input == 3:
        add()    
    elif menu_input == 4:
        withdraw()    
    elif menu_input == 5:
        loan()   
    elif menu_input == 6:
        loan_status()   
    elif menu_input == 7:
        comp()
    elif menu_input == 8:
        print("Thanks for choosing us..\n"
              "We will be always here to help you....") 
        return   


# Funtion to check your balance
def check_bal():
    print(f"Your current balance is ${bal}")
    menu() # Going back to menu 


# Funtion to add money to your account
def add():
    am_add = int(input("Enter the amount to add in your bank : "))
    global bal
    bal += am_add  
    print(f"{am_add}$ are successfully added to your bank account...")
    menu()


# Funtion to withdraw money from account
def withdraw():
    am_with = int(input("Enter the amount to add in your bank : "))
    global bal
    bal -= am_with
    print(f"{am_with}$ are successfully withdrawen from your bank account...")
    menu()


# To take loans
def loan():
    print("Welcome sir,\n"
          "If you want loan then you must have credit score above 650")
    score = int(input("Enter your credit score : "))
    if score >=650 :
        print("That's nice, You have enough credit score to get loan..")
        print("Here are the terms and conditions --\n"
              "-> You must submit the EMI before due date otherwise you will be fined for that.\n"
              "-> You will have to pay the intrest as well (given below)\n"
              "\n")
        print("The intrest amount for the various years are given below...\n"
              "1. For 5 years -- 6%\n"
              "2. For 4 years -- 5%\n"
              "3. For 3 years -- 4%\n")
        confirm = input("Do you want to take loan (Y/N) : ")
        if confirm.lower() == "yes" or confirm.lower() == "y":
            global loan_am
            am_lon = int(input("Enter the amount of loan that you want to get : "))
            loan_am += am_lon
            global bal
            bal += am_lon
            global status
            status = True
            global intrest
            year = int(input("Choose from the given number (1 to 3) to select the number of the years : "))
            if year == 1:
                intrest = 6
            elif year == 2 :
                intrest = 4
            elif year == 3:
                intrest = 3
            else:
                print("You have typed an incorrect number..\n"
                      "So you have to fill the form again..")
                loan()
            print(f"You have successfuly taken the loan of {loan_am}$\n"
                  "Don't forget to pay the amount on time....")
            menu()

        else:
            print("It's Ok we will be waiting for you next time...")
            menu()

    else:
        print("Sorry, you dont have enough credit score so we cannot give you loan....\n"
              "Try increasing your score...")
        menu()





# To get status of loan and pay amount
def loan_status():
    global intrest , loan_am, status, bal
    if status == True:
        print(f"You have a pending loan amount of {loan_am}$\n"
              "Choose from following....\n")
        print("1. Pay Amount\n"
              "2. Pending Amount with intrest\n"
              "3. Back to Menu")
        loan_status_ch = int(input("Enter your choice : "))
        if loan_status_ch == 1:
            pay_am = int(input("Enter a amount to pay your loan : "))
        
            loan_am -= pay_am
            bal -= pay_am
            print(f"The amount of {pay_am}$ has been sucessfuly paid\n")
            if loan_am == 0:
                print("You have paid all the amount\n"
                      "Now there is no need to worry about it....")
                status = False
                loan_status()

            else:
                print(f"You have left with {loan_am}$ to be paid before the due date")
                loan_status()
        if loan_status_ch == 2:
            print(f"You have left with {loan_am}$ to be paid...")
            print(f"You have an interst of {intrest}%")
            loan_status()
        if loan_status_ch == 3:
            print("You are being redirecting to Menu.....")
            menu()
    else:
        print("You have not taken any loan right now..\n"
              "But you can take on from us.....")
        menu()


# To take complaints
def comp():
    print("Sorry for any inconvinence..\n"
          "If you have any querry, please contact us..\n"
          "We will definitely help you as soon as possible....")
    comp = input("Type your complaint : ")
    print("Thanks sir, for contacing us\n"
          "Your complaint has been sucessfuly reistered"
          "We will be helping you soon...")
    menu()    


def back():
    print(f"Thanks {person.name} for visiting us...\n"
        "We will be always here to help you...")
    



person = create_acc()

get_choice()
