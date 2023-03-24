# A program designed for One Stop Insurance Co. to enter & calculate new insurance policy information for its customers.
# Created On: March 16/2023.
# Author: Samantha Hynes.

# Imports.
import datetime

# Constants.
f = open('OSICDef.dat', 'r')
POLICY_NUM = int(f.readline().strip())
BASICPREM_RATE = float(f.readline().strip())
ADDCAR_DISC = float(f.readline().strip())
EXTRALIA_RATE = float(f.readline().strip())
GLASSCOVG_RATE = float(f.readline().strip())
LOANCARCOVG_RATE = float(f.readline().strip())
HST_RATE = float(f.readline().strip())
PROCESS_FEE = float(f.readline().strip())
f.close()

# Display the Policy Number at beginning of program.
print()
print(f"Policy #: {POLICY_NUM}")
print()

# Beginning of program.
while True:

    # User inputs.
    CustFirst = input("Enter the customer's first name:                         ").title()
    CustLast = input("Enter the customer's last name:                          ").title()

    print()

    StAdd = input("Enter the customer's Street Address:                     ").title()
    City = input("Enter the customer's city:                               ").title()

    # Validate the province with a list.
    ProvList = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "NV", "NT"]
    while True:
        Prov = input("Enter the customer's province(LL):                       ").upper()

        if not Prov in ProvList:
            print("Invalid province, please reenter.")
        else:
            break

    PostCode = input("Enter the customer's postal code:                        ").upper()
    print()

    while True:
        PhNum = input("Enter the customer's phone number(9999999999):           ")
        if PhNum == "":
            print("Cannot be left blank please reenter.")
        elif len(PhNum) != 10:
            print("Phone number must be 10 digits long, please reenter.")
        elif not PhNum.isdigit():
            print("Phone number must be digits(0-9) only, please reenter.")
        else:
            PhNum = "(" + PhNum[0:3] + ")" + PhNum[3:6] + "-" + PhNum[6:10]
            break

    print()

    # Number of cars insured with calculation.
    while True:
        NumCar = int(input("Enter the number of cars to be insured:                  "))
        if NumCar == 1:
            CarTot = BASICPREM_RATE
            break
        else:
            CarTot = (NumCar - 1) * (BASICPREM_RATE * ADDCAR_DISC) + BASICPREM_RATE
            break

    print()

    # Extra cost coverages.
    while True:
        ExtraLiab = input("Enter Y/N for extra liability coverage up to $1,000,000: ").upper()
        if ExtraLiab == "Y":
            ExtraLiab = EXTRALIA_RATE
            break
        else:
            ExtraLiab = 0
            break

    while True:
        GlassCovg = input("Enter Y/N for glass coverage:                            ").upper()
        if GlassCovg == "Y":
            GlassCovg = GLASSCOVG_RATE
            break
        else:
            GlassCovg = 0
            break

    while True:
        LoanCar = input("Enter Y/N for the loaner car option:                     ").upper()
        if LoanCar == "Y":
            LoanCar = LOANCARCOVG_RATE
            break
        else:
            LoanCar = 0
            break

    print()

    # Calculations.
    ExtraCosts = LoanCar + GlassCovg + ExtraLiab
    TotInsPrem = CarTot + ExtraCosts
    HST = TotInsPrem * HST_RATE
    TotCost = TotInsPrem + HST

    # Invoice date.
    InvDate = datetime.datetime.now()
    InvDateDsp = InvDate.strftime("%Y-%m-%d")

    # Next payment due on the first day of the next month.
    Payment = InvDate + datetime.timedelta(days=32)
    Payment = Payment.replace(day=1)
    PaymentDsp = Payment.strftime("%B %d, %Y")

    # Full or monthly payments.
    while True:
        PayTyp = input("Enter F or M to pay in Full or Monthly payments:         ").upper()
        if PayTyp == "F":
            Status = "Pay in Full:"
            PayTyp = TotCost
            break
        elif PayTyp == "M":
            PayTyp = (TotCost + PROCESS_FEE) / 8
            Status = "Monthly Payments/Month:"
            break
        else:
            break

    # Display the results/receipt.
    print()
    print("                         One Stop")
    print("                    Insurance Company")
    print("---------------------------------------------------------")
    print(f"Policy #: {POLICY_NUM:<4d}                   Invoice Date: {InvDateDsp:>10s}")
    print("---------------------------------------------------------")
    print("Customer:                             Customer Phone:")
    print()
    print(f"    {CustFirst:<10s} {CustLast:<10s}             {PhNum:>10s}")
    print(f"    {StAdd:<15s}")
    print(f"    {City:<15s}, {Prov:2s} {PostCode}")
    print("---------------------------------------------------------")
    print(f"Number of cars to be insured:                          {NumCar:>2d}")
    print("---------                                       ---------")
    CarTotDsp = "${:,.2f}".format(CarTot)
    print(f"Insurance Premium:                              {CarTotDsp:>9s}")
    print("---------                                       ---------")
    ExtraLiabDsp = "${:,.2f}".format(ExtraLiab)
    print(f"Extra Liability(Up to $1,000,000):              {ExtraLiabDsp:>9s}")
    GlassCovgDsp = "${:,.2f}".format(GlassCovg)
    print(f"Glass Coverage:                                 {GlassCovgDsp:>9s}")
    LoanCarDsp = "${:,.2f}".format(LoanCar)
    print(f"Loaner Vehicle:                                 {LoanCarDsp:>9s}")
    print("---------                                       ---------")
    ExtraCostsDsp = "${:,.2f}".format(ExtraCosts)
    print(f"Extra Costs Total:                              {ExtraCostsDsp:>9s}")
    print("---------                                       ---------")
    TotInsPremDsp = "${:,.2f}".format(TotInsPrem)
    print(f"Sub Total:                                      {TotInsPremDsp:>9s}")
    HSTDsp = "${:,.2f}".format(HST)
    print(f"HST:                                            {HSTDsp:>9s}")
    print("---------                                       ---------")
    TotCostDsp = "${:,.2f}".format(TotCost)
    print(f"Total:                                          {TotCostDsp:>9s}")
    print("---------------------------------------------------------")
    PayTypDsp = "${:,.2f}".format(PayTyp)
    print(f"{Status} {PayTypDsp:>9s}")
    print(f"Payment Due: {Payment.date()}")
    print("---------------------------------------------------------")

    # Save the data for the claim to a data file.
    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(InvDateDsp))
    f.write("{}, ".format(CustFirst))
    f.write("{}, ".format(CustLast))
    f.write("{}, ".format(StAdd))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(str(NumCar)))
    f.write("{}, ".format(str(ExtraLiab)))
    f.write("{}, ".format(str(GlassCovg)))
    f.write("{}, ".format(str(LoanCar)))
    f.write("{}, ".format(Prov))
    f.write("{}\n ".format(str(TotCost)))
    f.close()

    print()
    print("Policy information processed and saved.")

    # Increase Policy Number counter.
    POLICY_NUM += 1

    f = open('OSICDef.dat', 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASICPREM_RATE)))
    f.write("{}\n".format(str(ADDCAR_DISC)))
    f.write("{}\n".format(str(EXTRALIA_RATE)))
    f.write("{}\n".format(str(GLASSCOVG_RATE)))
    f.write("{}\n".format(str(LOANCARCOVG_RATE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PROCESS_FEE)))
    f.close()

    More = input("Do you want to enter another insurance policy? (Y/N): ").upper()
    if More != "Y":
        exit()


