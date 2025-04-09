from flask import Flask, request, jsonify
from CONFIG.Config import *
from Balance_Enq.balance_enq import checkbalance
from New_account.new_account import newaccno
from Cash_Withdraw.cash_withdraw import withdraw
from Cash_Deposit.cash_deposit import deposit
from Quick_cash.quick_cash import quick_cash_func
from Mini_statement.mini_statement import mini_statement
from Money_Transfer.money_transfer import money_transfer
import re

app = Flask(__name__)

NAME_REGEX = re.compile(r'^[a-zA-Z\s]+$')
PHONE_REGEX = re.compile(r'^\d{10}$')
AADHAR_NUMBER_REGEX = re.compile(r'^\d{12}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
CARD_NUMBER_REGEX = re.compile(r'^\d{16}$')
AMOUNT_REGEX = re.compile(r'^(?:[1-9]\d*(?:\.\d{1,2})?|(?:null|0(?:\.0{1,2})?))$')
ACCOUNT_NO_REGEX = re.compile(r'^\d{16}$')


def validate_data(data, validations):
    errors = {}
    for param, regex in validations.items():
        value = data.get(param, '')
        
        # Convert numbers to string for validation
        if isinstance(value, (int, float)):
            value = str(value)
        
        if not regex.match(value):
            errors[param] = f"Invalid {param.replace('_', ' ')}"
    return errors if errors else None



# Centralized error handler
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({'message': 'Internal server error!', 'error': str(e)}), 500

@app.route('/balance_enquiry', methods=['POST'])
def balance():
    data = request.get_json()  #card_number

    validations = {
    "card_number": CARD_NUMBER_REGEX,}

    validation_errors = validate_data(data, validations)

    if validation_errors:
        return jsonify({"errors": validation_errors}), 400
    
    return checkbalance(data)

@app.route('/new_account', methods=['POST'])
def new_account():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data/ invalid data provided!'}), 400
    
    validations = {
    "name": NAME_REGEX,
    "phone_no": PHONE_REGEX,
    "amount": AMOUNT_REGEX,
    "aadhar_number": AADHAR_NUMBER_REGEX,
    "email": EMAIL_REGEX }

    validation_errors = validate_data(data, validations)

    if validation_errors:
        return jsonify({"errors": validation_errors}), 400

    return newaccno(data)
    # "name": "abhishek baral",
    # "phone_no": "9876564432",
    # "wallet_balance": 5000,
    # "aadhar_number": "627250126765",
    # "email": "angelpriya88@email.com"

@app.route('/withdraw', methods=['POST'])
def cash_withdraw():
    data = request.get_json()

    validations = {
    "card_number": CARD_NUMBER_REGEX,
    "amount": AMOUNT_REGEX
    }

    validation_errors = validate_data(data, validations)

    if validation_errors:
        return jsonify({"errors": validation_errors}), 400
    
    return withdraw(data)
    
    # "card_number":"4621292988410557",
    # "amount": 2999.00


@app.route('/deposit', methods=['POST'])
def cash_deposit():
    data = request.get_json()

    validations = {
    "card_number": CARD_NUMBER_REGEX,
    "amount": AMOUNT_REGEX
    }

    validation_errors = validate_data(data, validations)

    if validation_errors:
        return jsonify({"errors": validation_errors}), 400
    
    return deposit(data)
    # "card_number": "4621292988410557",
    # "amount": 2000

@app.route('/quickcash', methods=['POST'])
def quickcash():
    data = request.get_json()

    validations = {
    "card_number": CARD_NUMBER_REGEX,}

    validation_errors = validate_data(data, validations)

    if validation_errors:
        return jsonify({"errors": validation_errors}), 400

    return quick_cash_func(data)
    # "card_number": "4621292988410557",

@app.route('/ministatement', methods=['POST'])
def Mini_Statement():
    data = request.get_json()

    validations = {
    "card_number": CARD_NUMBER_REGEX,}

    validation_errors = validate_data(data, validations)

    if validation_errors:
        return jsonify({"errors": validation_errors}), 400
    
    return mini_statement(data)
    # "card_number": "4621292988410557",

@app.route('/transfer', methods=['POST'])
def Money_Transfer():
    data = request.get_json()

    validations = {
    "card_number": CARD_NUMBER_REGEX,
    "receiver_account_no": ACCOUNT_NO_REGEX,
    "amount": AMOUNT_REGEX
    }

    validation_errors = validate_data(data, validations)

    if validation_errors:
        return jsonify({"errors": validation_errors}), 400
    
    return money_transfer(data)
    # "card_number": "4621292988410557",
    # "receiver_account_no":"7777753104026925",
    # "amount": 1000.50

#blueprint lib