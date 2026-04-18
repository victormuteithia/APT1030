import java.util.Scanner;

public class AccessControl {
    
    static void checkAccess(String role) throws Exception {
        if (!role.equals("Doctor")) {
            throw new Exception("Access Denied: Only Doctors are allowed.");
        } else {
            System.out.println("Access Granted: Welcome, Doctor!");
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter role: ");
        String emp_role = sc.nextLine();
        
        try {
            checkAccess(emp_role);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        sc.close();
    }
}
