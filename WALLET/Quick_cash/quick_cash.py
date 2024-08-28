from CONFIG.Config import *
from flask import Flask, jsonify, request
from Function.function import *

app = Flask(__name__)

# def account_exists_by_card(card_number):
#     cursor1.execute("SELECT * FROM wallet WHERE card_number = %s", (card_number,))
#     return cursor1.fetchone()

def quick_cash(card_number, amount):
    cursor1.execute("UPDATE wallet SET wallet_balance = wallet_balance - %s WHERE card_number = %s", (amount, card_number))
    conn.commit()

# def generate_transaction_id():
#     return ''.join(random.choice('0123456789') for _ in range(11))


# def insert_into_ledger(account_no, amount,transaction_type):
#     transaction_id = generate_transaction_id()
#     transaction_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     if(transaction_type == "debit"):
#         cursor1.execute("INSERT INTO wallet_ledger (senders_account_no,receiver_account_no, amount, transaction_date, transaction_id, transaction_type) VALUES (%s, %s, %s, %s, %s)", 
#                         (str(account_no), "NULL", str(amount), transaction_date, str(transaction_id), str(transaction_type)))
    
#     if(transaction_type=="credit"):
#         cursor1.execute("INSERT INTO wallet_ledger (receiver_account_no, senders_account_no, amount, transaction_date, transaction_id, transaction_type) VALUES (%s, %s, %s, %s, %s)", 
#                     (str(account_no), "NULL", str(amount), transaction_date, str(transaction_id), str(transaction_type)))
    
#     conn.commit()



def quick_cash_func(data):
    card_number = data['card_number']
    amount = 500

    if not card_number:
        return jsonify({"status": "failure", "message": "Card number is  required."}), 400

    wallet_data = account_exists_by_card(card_number)

    if not wallet_data:
        return jsonify({"status": "failure", "message": "Card number not found."}), 404
    
    if not check_otp():
        return jsonify({"Status": "Failure", "Statement": "You entered wrong otp."})

    current_balance = wallet_data[8]
    print("current balance: ", current_balance)

    if current_balance < amount:
        return jsonify({"status": "failure", "message": "Insufficient balance."}), 400

    quick_cash(card_number, amount)
    transaction_type = "debit"

    insert_into_ledger( wallet_data, amount, transaction_type )


    wallet_data = account_exists_by_card(card_number)
    current_balance = wallet_data[8]
    print("current balance: ", current_balance)

    return jsonify({"status": "success", "message": "Transaction successful."})


if __name__ == '__main__':
    app.run(debug=True)
