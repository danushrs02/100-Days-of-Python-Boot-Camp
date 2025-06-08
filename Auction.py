


logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidders={}
def highest(high):
    highest_val=0
    for i in high:
        if high[i]>highest_val:
            highest_val=high[i]
            winner=i
    print(f"The Winner is {winner} with his bid ${highest_val}")


def tender():
    bidd=input("Bidder's Name:\n")
    price=int(input("Enter the amount\n"))

    bidders[bidd]=price

    left=input("Is any on left ? yes or no").lower()
    if left == "no":

        highest(bidders)
    else:
        print("\n"*100)
        tender()
tender()



