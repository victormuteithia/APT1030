// eCitizen Login Validation System in Java

import java.util.Scanner;

import javax.swing.plaf.synth.SynthButtonUI;

public class LoginValidation {
    public static void main(String[] args) {
        Scanner user = new Scanner(System.in);
        System.out.print("Enter your username: ");
        String username = user.nextLine();
        System.out.print("Enter your password: ");
        String password = user.nextLine();

        if (username == "adminKE" && password == "254Secure") {
            System.out.println("\nAccess Granted.");
        } else {
            System.out.println("\nAccess Denied. Invalid Credentials.");
        }

        user.close();
    }
}