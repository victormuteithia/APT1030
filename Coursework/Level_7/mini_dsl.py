accounts = {
    "Alice": 5000,
    "Bob": 3000,
    "Charlie": 1500
}


def parse_command(command):
    tokens = command.strip().split()
    
    if tokens[0] == "TRANSFER":
        amount = float(tokens[1])
        sender = tokens[3]
        receiver = tokens[5]
        return {"type": "TRANSFER", "amount": amount, "sender": sender, "receiver": receiver}
    
    elif tokens[0] == "WITHDRAW":
        amount = float(tokens[1])
        account = tokens[3]
        return {"type": "WITHDRAW", "amount": amount, "account": account}
    
    elif tokens[0] == "DEPOSIT":
        amount = float(tokens[1])
        account = tokens[3]
        return {"type": "DEPOSIT", "amount": amount, "account": account}
    
    return None


def execute_transfer(parsed):
    sender = parsed["sender"]
    receiver = parsed["receiver"]
    amount = parsed["amount"]
    
    if sender not in accounts:
        print(f"Error: Sender '{sender}' not found.")
        return
    
    if receiver not in accounts:
        print(f"Error: Receiver '{receiver}' not found.")
        return
    
    if accounts[sender] < amount:
        print(f"Error: Insufficient balance. {sender} has {accounts[sender]} KES, needs {amount} KES.")
        return
    
    accounts[sender] -= amount
    accounts[receiver] += amount
    print(f"Success: {sender} transferred {amount} KES to {receiver}.")
    print(f"  {sender} balance: {accounts[sender]} KES")
    print(f"  {receiver} balance: {accounts[receiver]} KES")


def execute_withdraw(parsed):
    account = parsed["account"]
    amount = parsed["amount"]
    
    if account not in accounts:
        print(f"Error: Account '{account}' not found.")
        return
    
    if accounts[account] < amount:
        print(f"Error: Insufficient balance. {account} has {accounts[account]} KES, needs {amount} KES.")
        return
    
    accounts[account] -= amount
    print(f"Success: {account} withdrew {amount} KES.")
    print(f"  {account} balance: {accounts[account]} KES")


def execute_deposit(parsed):
    account = parsed["account"]
    amount = parsed["amount"]
    
    if account not in accounts:
        print(f"Error: Account '{account}' not found.")
        return
    
    if amount <= 0:
        print(f"Error: Deposit amount must be positive.")
        return
    
    accounts[account] += amount
    print(f"Success: {account} deposited {amount} KES.")
    print(f"  {account} balance: {accounts[account]} KES")


def execute(parsed):
    if parsed["type"] == "TRANSFER":
        execute_transfer(parsed)
    elif parsed["type"] == "WITHDRAW":
        execute_withdraw(parsed)
    elif parsed["type"] == "DEPOSIT":
        execute_deposit(parsed)


print("=== Mobile Money DSL ===\n")

commands = [
    "TRANSFER 1000 FROM Alice TO Bob IF BALANCE >= 1000",
    "WITHDRAW 500 FROM Charlie IF BALANCE >= 500",
    "TRANSFER 10000 FROM Alice TO Bob IF BALANCE >= 10000",
    "WITHDRAW 2000 FROM Bob IF BALANCE >= 2000",
    "DEPOSIT 2000 TO Alice IF BALANCE == TRUE"
]

for cmd in commands:
    print(f"Command: {cmd}")
    parsed = parse_command(cmd)
    if parsed:
        execute(parsed)
    else:
        print("Error: Invalid command.")
    print()
