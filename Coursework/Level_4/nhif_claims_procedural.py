def calculate_claim(amount):
    co_payment = amount * 0.10
    return amount - co_payment


def display_patient_info(name, policy_number):
    print(f"Name: {name}")
    print(f"Policy Number: {policy_number}")


name = input("Enter patient name: ")
policy = input("Enter policy number: ")

print("\nPatient Information:")
display_patient_info(name, policy)

try:
    amount = float(input("\nEnter claim amount (KES): "))
    co_payment = amount * 0.10
    final_claim = calculate_claim(amount)
    
    print("\n--- Claim Breakdown ---")
    print(f"Original Amount: KES {amount:.2f}")
    print(f"Co-payment (10%): KES {co_payment:.2f}")
    print(f"Final Claim: KES {final_claim:.2f}")
    
except ValueError:
    print("Error: Please enter a valid amount.")
