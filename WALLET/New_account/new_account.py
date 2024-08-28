from CONFIG.Config import *
from flask import Flask, jsonify, request
import random
from Function.function import *
import datetime

def generate_card_number():
    return ''.join(random.choice('0123456789') for _ in range(16))

def generate_expiry_month():
    return str(random.randint(1, 12)).zfill(2)

def generate_expiry_year():
    current_year = datetime.datetime.now().year
    return str(random.randint(current_year+4, current_year + 10))

def account_exists(act, card_number, aadhar, ph):
    cursor1.execute("SELECT account_no FROM wallet WHERE account_no = %s OR card_number = %s OR aadhar_number = %s OR phone_no = %s", (act, card_number, aadhar, ph))
    return cursor1.fetchall()

def insert_account(act, name, ph, amt, status, aadhar, email, card_number, expiry_month, expiry_year):
    cursor1.execute("INSERT INTO wallet (account_no, name, phone_no, wallet_balance, status, aadhar_number, email, card_number, expiry_month, expiry_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (str(act), str(name), str(ph), str(amt), status, str(aadhar), str(email),str(card_number), str(expiry_month), str(expiry_year)))
    conn.commit()

def newaccno(value):
    print("Function called with value:", value)
    name = value['name']
    ph = value['phone_no']
    amt = value['amount']
    aadhar = value['aadhar_number']
    email = value['email']

    act = random.randint(100000000000000, 9999999999999999)
    card_number = generate_card_number()
    expiry_month = generate_expiry_month()
    expiry_year = generate_expiry_year()
    status = 1

    if acc_formatcheck(str(act), str(card_number), str(expiry_month), str(expiry_year)): 
            if not account_exists(act, card_number, aadhar, ph):
                insert_account(act, name, ph, amt, status, aadhar, email, card_number, expiry_month, expiry_year)
                return jsonify({"status": "success", "message": "Account created Successfully."})
            else:
                for _ in range(5):
                    act = random.randint(100000000000000, 9999999999999999)
                    card_number = generate_card_number()
                    if not account_exists(act, card_number, aadhar, ph):
                        insert_account(act, name, ph, amt, status, aadhar, email, card_number, expiry_month, expiry_year)
                        return jsonify({"status": "success", "message": "Account created Successfully."})
                    else:
                        existing_account = account_exists_by_aadhar_and_ph(aadhar, ph)
                        if existing_account:
                            # Determine which parameter (aadhar or ph) is causing the account to exist
                            existing_aadhar = existing_account[4]
                            existing_ph = existing_account[6]

                            if existing_aadhar == aadhar:
                                return jsonify({"status": "failure", "message": f"Account already exists for Aadhar: {aadhar}"})
                            else:
                                return jsonify({"status": "failure", "message": f"Account already exists for Phone Number: {existing_ph}"})     
                return jsonify({"status": "failure", "message": "Failed to generate a unique account number after multiple attempts."})
    else:
        return jsonify({"status": "failure", "message": "Account number format is not valid."})

