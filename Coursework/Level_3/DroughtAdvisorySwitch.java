import java.util.Scanner;

public class DroughtAdvisory {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter rainfall amount (mm): ");
        double rainfall = sc.nextDouble();
        
        System.out.print("Enter temperature (°C): ");
        double temperature = sc.nextDouble();
        
        String advisory;
        
        int condition = (rainfall < 200) ? 1 : (temperature > 30) ? 2 : 3;
        
        switch (condition) {
            case 1:
                advisory = "Irrigation Required";
                break;
            case 2:
                advisory = "Monitor Soil";
                break;
            case 3:
                advisory = "Normal Conditions";
                break;
            default:
                advisory = "Unknown";
        }
        
        System.out.println("Advisory: " + advisory);
        sc.close();
    }
}
