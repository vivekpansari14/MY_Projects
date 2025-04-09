
# 💳 Neo-WALLET – Secure Wallet Management System

Neo-WALLET is a full-stack wallet management system that allows users to securely manage digital transactions through a RESTful API and an intuitive frontend. It supports account creation, deposits, withdrawals, quick cash, balance checks, transaction statements, and transfers with OTP and JWT-based authentication.

---

## 🚀 Features

- 🔐 OTP verification
- 🏦 Account Creation with Auto-Generated Card & Expiry
- 💰 Deposit & Withdraw Money
- ⚡ Quick Cash (₹500 withdrawal)
- 📊 Balance Enquiry
- 📄 Mini Statement (Last 10 Transactions)
- 🔁 Money Transfer to other accounts
- 🧠 Data validation using regex on server-side
- 🧪 Tested backend with error-handling & DB pooling

---

## 🛠️ Tech Stack

### Backend:
- Python (Flask)
- MySQL
- flask-jwt-extended
- mysql-connector-python
- python-dotenv
- bcrypt

### Frontend:
- HTML5
- CSS3
- Bootstrap 5
- JavaScript (fetch API)

---

## 📁 Project Structure

```
/backend
  ├── CONFIG/
  ├── Balance_Enq/
  ├── Cash_Deposit/
  ├── Cash_Withdraw/
  ├── Quick_cash/
  ├── Mini_statement/
  ├── Money_Transfer/
  ├── New_account/
  └── ROUTER/main.py

/frontend
  ├── index.html
  ├── dashboard.html
  ├── create_account.html
  ├── main.js
  └── styles.css
```

---

## 🧪 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/vivekpansari14/MY_Projects/Neo-WALLET
   cd Neo-WALLET
   ```

2. Create and configure a `.env` file in `/backend/CONFIG/`:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=transaction_wallet
   DB_PORT=3306
   JWT_SECRET_KEY=your_jwt_secret
   ```

3. Run the backend server:
   ```bash
   cd backend
   python main.py
   ```

4. Open `frontend/index.html` in your browser to start.

---

## 📄 License
This project is licensed under the MIT License.
