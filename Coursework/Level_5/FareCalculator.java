import java.util.Scanner;

class Taxi {
    double baseFare = 200;
    double costPerKm = 50;
    
    double calculateFare(double distance) {
        return baseFare + (distance * costPerKm);
    }
}

public class FareCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Taxi taxi = new Taxi();
        
        System.out.print("Enter distance (km): ");
        double distance = sc.nextDouble();
        
        double totalFare = taxi.calculateFare(distance);
        
        System.out.println("\nBase Fare: 200 KES");
        System.out.println("Distance: " + distance + " km");
        System.out.println("Cost per km: 50 KES");
        System.out.println("Total Fare: " + totalFare + " KES");
        
        sc.close();
    }
}
