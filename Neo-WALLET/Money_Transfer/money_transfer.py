from flask import Flask, jsonify, request
from Function.function import *
from CONFIG.Config import *

app = Flask(__name__)

def transfer_amount(account_details,receiver_account_no,  amount):
    # Deduct amount from sender's account
    cursor1.execute("UPDATE wallet SET wallet_balance = wallet_balance - %s WHERE account_no = %s", (amount, account_details[0]))
    
    # Add amount to receiver's account
    #cursor1.execute("UPDATE wallet SET wallet_balance = wallet_balance + %s WHERE account_no = %s", (amount, receiver_account_no))

    # Insert transaction into ledger
    transaction_type = "debit"
    insert_into_ledger((account_details[0], account_details[1], receiver_account_no), amount, transaction_type)

    conn.commit()


def money_transfer(data):
    # sender_account_no = data['sender_account_no'] data.get('sender_account_no')
    card_number = data['card_number']
    receiver_account_no = data['receiver_account_no']
    amount = data['amount']

    if not card_number or not receiver_account_no or not amount:
        return jsonify({"status": "failure", "message": "All fields are required."}), 400

    # Check if sender has sufficient balance
    wallet_data = account_exists_by_card(card_number)

    if not wallet_data:
        return jsonify({"status": "failure", "message": "Sender account not found."}), 404
    
    if not check_otp():
        return jsonify({"Status": "Failure", "Statement": "You entered wrong otp."})

    if wallet_data[8] < amount:
        return jsonify({"status": "failure", "message": "Insufficient balance in sender's account."}), 400

    # Perform the transfer
    transfer_amount((wallet_data[0],card_number), receiver_account_no, amount)

    return jsonify({"status": "success", "message": "Amount transferred successfully."})

if __name__ == '__main__':
    app.run(debug=True)
