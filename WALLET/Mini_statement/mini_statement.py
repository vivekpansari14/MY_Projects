from CONFIG.Config import *
from flask import Flask, jsonify, request
from Function.function import *

app = Flask(__name__)

def account_exists_by_card(card_number):
    cursor.execute("SELECT * FROM wallet WHERE card_number = %s", (card_number,))
    return cursor1.fetchone()

def fetch_transactions(accno):
    cursor.execute("""
        SELECT account_no, amount, transaction_date, transaction_id, transaction_type
        FROM wallet_ledger
        WHERE account_no = %s
        ORDER BY transaction_date DESC
        LIMIT 10
    """, (accno,))
    return cursor1.fetchall()


def mini_statement(data):
    card_number = data['card_number']

    if not card_number:
        return jsonify({"status": "failure", "message": "Card number is required."}), 400

    if not check_otp():
        return jsonify({"Status": "Failure", "Statement": "You entered wrong OTP."})

    if not account_exists_by_card(card_number):
        return jsonify({"status": "failure", "message": "Card number not found."}), 404

    wallet_data = account_exists_by_card(card_number)

    transactions = fetch_transactions(wallet_data[0])

    if not transactions:
        return jsonify({"status": "failure", "message": "No transactions found."}), 404

    formatted_transactions = []
    for transaction in transactions:
        formatted_transactions.append({
            "account_no": transaction[0],
            "amount": transaction[1],
            "transaction_date": transaction[2].strftime('%Y-%m-%d %H:%M:%S'),
            "transaction_id": transaction[3],
            "transaction_type": transaction[4]
        })

    return jsonify({"status": "success", "transactions": formatted_transactions})


if __name__ == '__main__':
    app.run(debug=True)
