import java.util.Scanner;

public class DroughtAdvisory {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter rainfall amount (mm): ");
        double rainfall = sc.nextDouble();
        
        System.out.print("Enter temperature (°C): ");
        double temperature = sc.nextDouble();
        
        String advisory;
        
        if (rainfall < 200) {
            advisory = "Irrigation Required";
        } else if (temperature > 30) {
            advisory = "Monitor Soil";
        } else {
            advisory = "Normal Conditions";
        }
        
        System.out.println("Advisory: " + advisory);
        sc.close();
    }
}
