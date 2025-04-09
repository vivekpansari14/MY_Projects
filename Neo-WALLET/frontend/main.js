const card_number = localStorage.getItem("card_number");
const output = document.getElementById("output");

function post(endpoint, data) {
  return fetch(`http://localhost:8080/${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  }).then(res => res.json());
}

function checkBalance() {
  post("balance_enquiry", { card_number }).then(data => show(data));
}

function depositMoney() {
  const amount = prompt("Enter deposit amount:");
  if (amount) post("deposit", { card_number, amount }).then(data => show(data));
}

function withdrawMoney() {
  const amount = prompt("Enter amount to withdraw:");
  if (amount) post("withdraw", { card_number, amount }).then(data => show(data));
}

function quickCash() {
  post("quickcash", { card_number }).then(data => show(data));
}

function getMiniStatement() {
  post("ministatement", { card_number }).then(data => show(data));
}

function transferMoney() {
  const receiver_account_no = document.getElementById("receiver").value;
  const amount = document.getElementById("transfer_amt").value;
  if (receiver_account_no && amount)
    post("transfer", { card_number, receiver_account_no, amount }).then(data => show(data));
}

function show(data) {
  output.innerText = JSON.stringify(data, null, 2);
}
