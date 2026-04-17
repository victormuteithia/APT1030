import java.util.Scanner;

public class FinancialRecord {
    private String memberName;
    private String memberID;
    private double[] monthlyContributions;
    private double totalSavings;
    
    // Constructor
    public FinancialRecord() {
        monthlyContributions = new double[6];
        totalSavings = 0;
    }
    
    // Method to input member details
    public void inputMemberDetails() {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter Member Name: ");
        memberName = scanner.nextLine();
        
        System.out.print("Enter Member ID: ");
        memberID = scanner.nextLine();
    }
    
    // Method to input 6 months of contributions
    public void inputMonthlyContributions() {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("\nEnter monthly contributions for 6 months:");
        for (int i = 0; i < 6; i++) {
            System.out.print("Month " + (i + 1) + " contribution: ");
            monthlyContributions[i] = scanner.nextDouble();
        }
    }
    
    // Method to calculate total savings
    public void calculateTotalSavings() {
        totalSavings = 0;
        for (int i = 0; i < 6; i++) {
            totalSavings += monthlyContributions[i];
        }
    }
    
    // Method to display member record
    public void displayRecord() {
        System.out.println("\n========== FINANCIAL RECORD ==========");
        System.out.println("Member Name: " + memberName);
        System.out.println("Member ID: " + memberID);
        System.out.println("Total Savings: " + totalSavings);
        System.out.println("=====================================\n");
    }
    
    // Main method
    public static void main(String[] args) {
        FinancialRecord record = new FinancialRecord();
        
        record.inputMemberDetails();
        
        record.inputMonthlyContributions();
        
        record.calculateTotalSavings();
        
        record.displayRecord();
    }
}
