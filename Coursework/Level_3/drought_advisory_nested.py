def get_rainfall_advisory(rainfall, temperature):
    
    if rainfall < 200:
        return "Irrigation Required"
    else:
        if temperature > 30:
            return "Monitor Soil"
        else:
            return "Normal Conditions"


def main():
    try:
        # Get user input
        rainfall = float(input("Enter rainfall amount (mm): "))
        temperature = float(input("Enter temperature (°C): "))
        
        # Validate inputs
        if rainfall < 0 or temperature < -50:
            print("Error: Please enter valid rainfall (>= 0) and temperature values.")
            return
        
        # Get and display advisory
        advisory = get_rainfall_advisory(rainfall, temperature)
        print(f"\nAdvisory: {advisory}")
        
    except ValueError:
        print("Error: Please enter valid numeric values for rainfall and temperature.")


if __name__ == "__main__":
    main()
