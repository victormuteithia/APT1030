import java.util.Scanner;

class Patient {
    String name;
    String policyNumber;
    
    Patient(String name, String policyNumber) {
        this.name = name;
        this.policyNumber = policyNumber;
    }
    
    double calculateClaim(double amount) {
        return amount * 0.90;
    }
}

public class NHIFClaims {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter patient name: ");
        String name = sc.nextLine();
        
        System.out.print("Enter policy number: ");
        String policy = sc.nextLine();
        
        Patient patient = new Patient(name, policy);
        
        System.out.println("\nName: " + patient.name);
        System.out.println("Policy Number: " + patient.policyNumber);
        
        try {
            System.out.print("\nEnter claim amount (KES): ");
            double amount = sc.nextDouble();
            double coPayment = amount * 0.10;
            double finalClaim = patient.calculateClaim(amount);
            
            System.out.println("\nOriginal Amount: KES " + amount);
            System.out.println("Co-payment (10%): KES " + coPayment);
            System.out.println("Final Claim: KES " + finalClaim);
            
        } catch (Exception e) {
            System.out.println("Error: Invalid input");
        }
        sc.close();
    }
}
