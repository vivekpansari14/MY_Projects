from flask import Flask, jsonify
from CONFIG.Config import get_connection, close_connection
from Function.function import *
from mysql.connector import pooling

app = Flask(__name__)

def checkbalance(value):
    card_number = value['card_number']

    conn = get_connection()
    cursor = conn.cursor()

    try:
        wallet_data = account_exists_by_card(card_number)
        
        if not wallet_data:
            return jsonify({"status": "failure", "message": "Card number not found."}), 404

        if acc_in("wallet", "account_no", wallet_data[0]) != 1:
            return jsonify({"Status": "Failure", "Statement": "Account no is not active."})

        # if not check_otp():
        #     return jsonify({"Status": "Failure", "Statement": "You entered wrong otp."})

        cursor.execute("SELECT wallet_balance FROM transaction_wallet.wallet WHERE account_no = %s", (wallet_data[0],))
        data = cursor.fetchone()
        
        if data:
            balance = float(data[0])
            result = {"Status": "Success", "Statement": f"Current Balance is {balance}"}
        else:
            result = {"Status": "Failure", "Statement": "No balance data found for the account."}

        # Consume all results to avoid "Commands out of sync" error
        cursor.fetchall()

        return jsonify(result)
    
    finally:
        # Close the cursor and return the connection to the pool
        cursor.close()
        close_connection(conn, cursor)

if __name__ == '__main__':
    app.run(debug=True)
