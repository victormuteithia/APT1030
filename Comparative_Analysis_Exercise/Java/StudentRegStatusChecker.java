// Student Registration Status Checker in Java
import java.util.Scanner;

public class StudentRegStatusChecker {
    public static void main(String[] args) {
        Scanner student = new Scanner(System.in);
        System.out.print("Enter you name: ");
        String stu_name = student.nextLine();
        System.out.print("Enter no. of units registered: ");
        int units = student.nextInt();

        String status = (units > 7) ? "Overload - Approval Required." : "Registration Accepted.";
        
        System.out.println("---------------------------------------");
        System.out.println("Student Name: " + stu_name);
        System.out.println("Units Registered: " + units);
        System.out.println("Status: " + status);
        System.out.println("---------------------------------------");

        student.close();
        
    }
}