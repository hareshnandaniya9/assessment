print()
print("                         WELLCOME TO PYTHON BANK MANAGEMENT SYSTEM")
print()

print("Select Your Role")
print("1.Banker")
print("2.Customer")
print("3.Exit")
print()

while True:
    role=int(input("Select Your Role:"))
    if role == 1:
        print()
        print("                    Wellcome to Banker's App")
        print()
        print("Opration manu")
        print()
        print("1).Add Costomer")
        print("2).View Costomer")
        print("3).Sherch Costomer")
        print("4).view All Costomer")
        print()
        opration=int(input("Which pration yo preform:"))
        print()
        if opration == 1:
            fl=open('costomer.txt','a')
            
            ac_no=int(input("Enter Costomer Account Number:"))
            name=input("Enter Costomer Name:")
            balance=float(input("Enter Opning Balance:"))
            fl.write(f"Account_No:{ac_no}\nName:{name}\nOpning Balance:{balance}\n")
            fl.close()
        elif opration == 2:
            fl=open('costomer.txt','r')
            for i in fl:
                n=1
                print(i)
                n+=1
                print()
            fl.close()
        elif opration == 3:
            print("Which Way To Sarch Costomer")
            print()
            print("1.By Name")
            print("2.By Account Number")
            search=input("Enter Name/Account Number:")
            if search == '1':
                src=input("What Is Costomer Name:")
                fl=open('costomer.txt','r')
                lines=fl.readlines()
                for line in lines:
                    if line.find(search) != -1:
                        print(search, "Data Exists in File")
                        print("Line:",lines.index(line))
                        print("Name:",src)
                        break
                    else:
                        print("Data Not Exists In File:")
            elif search == '2':
                src=int(input("What Is Costomer Acount Number:"))
                fl=open('costomer.txt','r')
                lines=fl.readlines()
                for line in lines:
                    if line.find(search) != 0:
                        print(search, "Data Exists in File")
                        print("Line:",lines.index(line))
                        print("Acount Number:",src)
                        break
                    else:
                        print("Data Not Exists In File:")
        elif opration == 4:
            fl=open('costomer.txt','r')
            print(fl.read())
        else:
            print("Invalid In put")
    elif role == 2:
        print()
        print("                    Wellcome to Costomer's App")
        print()
        print("Opration manu")
        print()
        print("1).Withdwal Amount")
        print("2).Deposite Amount")
        print("3).View balance")
        print()
        opration=int(input("Which pration yo preform:"))
        print()
        if opration == 1:
            fl=open('c_amount.txt','a')
            ac_no=int(input("Enter Costomer Account Number:"))
            name=input("Enter Costomer Name:")
            ta_balance=50000
            print("Your Total Avalible Balnce:",ta_balance)
            withdwal_amount=float(input("Enter Withdwal Ammount:"))
            total_balance=ta_balance-withdwal_amount
            fl.write(f"Acount_Number:{ac_no}\nName:{name}\nTotal_avalible_balance:{ta_balance}\nWithdwal_Amount:{withdwal_amount}\nTotal_Balance:{total_balance}\n")
            fl.close()
        elif opration == 2:
            fl=open('c_diposite.txt','a')
            ac_no=int(input("Enter Costomer Account Number:"))
            name=input("Enter Costomer Name:")
            ta_balance=50000
            print("Your Total  Balnce:",ta_balance)
            diposite_amount=float(input("Enter Diposite Ammount:"))
            total_balance=ta_balance+diposite_amount
            fl.write(f"Acount_Number:{ac_no}\nName:{name}\nTotal_balance:{ta_balance}\nDiposite_Amount:{diposite_amount}\nTotal_Avalible_Balance:{total_balance}\n")
            fl.close()
        elif opration == 3:
            fl=open('c_diposite.txt','r')
            print(fl.readlines()[4])
            fl.close()
        else:
            print("Enter Invalid Input")
    elif role == 3:
        print()
        print("Visit Next Time")
        print()
        print("!!!Thank You!!!")
        break
        nextcal=input("let start again?(yes/no):")
        print()
        if (nextcal=="no"):
            print("Thaks For Using Python Bank Management System App:")
            break


       
        
        
                 
