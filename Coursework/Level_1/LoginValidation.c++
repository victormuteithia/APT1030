#include <iostream>
#include <string>

using namespace std;

int main() {
    // Predefined credentials
    string validUsername = "adminKE";
    string validPassword = "254Secure";
    
    // Declare variables for user input
    string username, password;
    
    // Prompt for username
    cout << "Enter username: ";
    cin >> username;
    
    // Prompt for password
    cout << "Enter password: ";
    cin >> password;
    
    // Validate credentials
    if (username == validUsername && password == validPassword) {
        cout << "\nAccess Granted" << endl;
    } else {
        cout << "\nAccess Denied. Invalid Credentials" << endl;
    }
    
    return 0;
}
