# SACCO Member Financial Record in Python

def savings_calculator():
    mbr_name = input("Enter your name: ")
    mbr_id = input("Enter your Member ID no.: ")

    first_month_cntb = int(input("Enter your first month contribution: "))
    second_month_cntb = int(input("Enter your second month contribution: "))
    thrid_month_cntb = int(input("Enter your thrid month contribution: "))
    fourth_month_cntb = int(input("Enter your fourth month contribution: "))
    fifth_month_cntb = int(input("Enter your fifth month contribution: "))
    sixth_month_cntb = int(input("Enter your sixth month contribution: "))

    total_savings = first_month_cntb + second_month_cntb + thrid_month_cntb + fourth_month_cntb + fifth_month_cntb + sixth_month_cntb

    print("\n------------------------------")
    print(f"Member name: {mbr_name}")
    print(f"Member ID: {mbr_id}")
    print(f"Total savings for the last 6 months: {total_savings}")
    print("------------------------------\n")


if __name__ == "__main__":
    savings_calculator()


