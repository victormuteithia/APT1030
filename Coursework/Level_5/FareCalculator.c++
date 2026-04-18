#include <iostream>
using namespace std;

double calculateFare(double distance) {
    double baseFare = 200;
    double costPerKm = 50;
    return baseFare + (distance * costPerKm);
}

int main() {
    double distance;
    
    cout << "Enter distance (km): ";
    cin >> distance;
    
    if (distance < 0) {
        cout << "Error: Distance cannot be negative." << endl;
        return 1;
    }
    
    double totalFare = calculateFare(distance);
    
    cout << "\n--- Fare Breakdown ---" << endl;
    cout << "Base Fare: 200 KES" << endl;
    cout << "Distance: " << distance << " km" << endl;
    cout << "Cost per km: 50 KES" << endl;
    cout << "Total Fare: " << totalFare << " KES" << endl;
    
    return 0;
}
