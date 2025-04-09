from CONFIG.Config import get_connection, close_connection
from flask import Flask, jsonify, request
from Function.function import *


app = Flask(__name__)

conn = get_connection()
cursor = conn.cursor()

def deposit_amount(card_number, amount):
    cursor.execute("UPDATE wallet SET wallet_balance = wallet_balance + %s WHERE card_number = %s", (amount, card_number))
    conn.commit()



def deposit(data):
    card_number = data['card_number']
    amount = data['amount']

    if not card_number or not amount:
        return jsonify({"status": "failure", "message": "Card number and amount are required."}), 400

    try:
        wallet_data = account_exists_by_card(card_number)

        if not wallet_data:
            return jsonify({"status": "failure", "message": "Card number not found."}), 404
        
        # if not check_otp():
        #     return jsonify({"Status": "Failure", "Statement": "You entered wrong otp."})

        current_balance = wallet_data[8]
        print("current balance: ", current_balance)

        deposit_amount(card_number, amount)
        transaction_type = "credit"
        insert_into_ledger(wallet_data, amount, transaction_type)


        wallet_data = account_exists_by_card(card_number)
        current_balance = wallet_data[8]
        print("current balance: ", current_balance)

        result=  {"status": "success", "message": "Transaction successful."}
    
        # Consume all results to avoid "Commands out of sync" error
        cursor.fetchall()

        return jsonify(result)
    finally:
        # Close the cursor and return the connection to the pool
        cursor.close()
        close_connection(conn, cursor)


if __name__ == '__main__':
    app.run(debug=True)
