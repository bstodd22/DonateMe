def show_homepage():
    print(
        """        === DonateMe Homepage === 
----------------------------------------
| 1.    Login     | 2.    Register     |
----------------------------------------
| 3.    Donate    | 4.  Show Donations |
----------------------------------------
|            5.  Exit                  |
----------------------------------------
"""
    )


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = f"{username} donated ${donation_amt:.2f}"
    print("Thank you for a donation!!")
    return donation_string


def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
