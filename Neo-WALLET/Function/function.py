from CONFIG.Config import get_connection, close_connection
import random
import re
import datetime

conn = get_connection()
cursor = conn.cursor()

#check if acc exist for the acc number
def acc_in(table_name, value1, accno):
    try:
        query = f"SELECT card_number FROM {table_name} WHERE {value1} = %s"
        cursor.execute(query, (str(accno),))
        dt = cursor.fetchall()
        return 1 if dt else 0
    except Exception as e:
        print(f"Error in acc_in: {e}")
        return 0

#generates unqiue transaction id
def generate_transaction_id():
    return ''.join(random.choice('0123456789') for _ in range(11))

#wallet_ledger data udpate insert function
def insert_into_ledger(wallet_data, amount, transaction_type):
    transaction_id = generate_transaction_id()
    transaction_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    account_no=wallet_data[0]
    card_number=wallet_data[1]

    if(transaction_type == "debit"):
        if wallet_data[2]:
            receiver_account_no= wallet_data[2]
        else:
            receiver_account_no= "SAME"

        cursor.execute("INSERT INTO wallet_ledger (senders_account_no, receiver_account_no, card_number, amount, transaction_date, transaction_id, transaction_type) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                        (str(account_no),receiver_account_no, str(card_number),  str(amount), transaction_date, str(transaction_id), str(transaction_type)))
    
    if(transaction_type=="credit"):
        senders_account_no= "SAME"
        cursor.execute("INSERT INTO wallet_ledger (receiver_account_no, senders_account_no, card_number, amount, transaction_date, transaction_id, transaction_type) VALUES (%s,%s, %s, %s, %s, %s, %s)", 
                    (str(account_no),senders_account_no, str(card_number), str(amount), transaction_date, str(transaction_id), str(transaction_type)))
    
    conn.commit()

#check if acc exist for the card number
def account_exists_by_card(card_number):
    try:
        cursor.execute("SELECT * FROM wallet WHERE card_number = %s", (card_number,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error occurred while fetching account by card number {card_number}: {e}")
        return False

#check aadhar and ph number exist account
def account_exists_by_aadhar_and_ph(aadhar, ph):
    try:
        cursor.execute("SELECT * FROM wallet WHERE aadhar_number = %s OR phone_no= %s", (aadhar, ph))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error occurred while fetching account by Aadhar and phone number: {e}")
        return False

#otp function
def check_otp():
    generated_otp = random.randint(1000, 9999)
    print("otp generated is:", generated_otp)
    entered_otp = get_user_input()
    
    if entered_otp == generated_otp:
        return True
    else:
        return False

def get_user_input():
    while True:
        try:
            user_input = int(input("Enter your OTP: "))
            if len(str(user_input))==4:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid OTP (4-digit number).")


def acc_formatcheck(accno, card_number, month, year):
    #validating acc number
    if not re.match('^[0-9]{0,16}$',accno):
        return 0
    #validating card number
    if not re.match('^[0-9]{16}$', card_number):
        return 0
    
    # Validate expiry_month (should be two-digit number between 01 and 12)
    if not re.match('^(0[1-9]|1[0-2])$', month):
        return 0
    
    # Validate expiry_year (should be a four-digit number)
    if not re.match('^[0-9]{4}$', year):
        return 0
    
    return 1
    
       
def acc_no_check(accno):
    if not re.match('^[0-9]{16}$', accno):
        return 0
    else:
        return 1




