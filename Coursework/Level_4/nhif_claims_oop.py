class Patient:
    def __init__(self, name, policy_number):
        self.name = name
        self.policy_number = policy_number
    
    def calculate_claim(self, amount):
        co_payment = amount * 0.10
        return amount - co_payment
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Policy Number: {self.policy_number}")


name = input("Enter patient name: ")
policy = input("Enter policy number: ")
patient = Patient(name, policy)

print("\nPatient Information:")
patient.display_info()

try:
    amount = float(input("\nEnter claim amount (KES): "))
    co_payment = amount * 0.10
    final_claim = patient.calculate_claim(amount)
    
    print("\n--- Claim Breakdown ---")
    print(f"Original Amount: KES {amount:.2f}")
    print(f"Co-payment (10%): KES {co_payment:.2f}")
    print(f"Final Claim: KES {final_claim:.2f}")
    
except ValueError:
    print("Error: Please enter a valid amount.")
