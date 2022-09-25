import random

class Bank: 
 
    def __init__(self, n , accno,amt,transc): 
        self.name = n 
        self.accno = accno 
        self.Amount=amt
        self.trans=transc

    def createAccount(self) :
        self.name=input("Enter name: ")
        self.accno=int(input("Enter account number: "))
        self.Amount=int(input("Enter the money to deposit (Minimum 100): "))
    
    def depositMoney(self,acct) :
        acc=acct
        nam=input("Enter your name: ")
        mon=int(input("Enter the amount of money to deposit: "))
        
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                customers[i].Amount+=mon
                customers[i].trans+=1
                print("Total balance in account is %d\n" %customers[i].Amount)
                break
   
    def withdrawMoney(self,acct):
        nam=input("Enter your name: ")
        acc=acct
        mon=int(input("Enter the amount of money to withdraw: "))
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                if(customers[i].Amount<mon):
                    print("Insufficient balance in account to withdraw\n")
                else:
                    customers[i].Amount-=mon
                    customers[i].trans+=1
                    print("Total balance in account is %d\n" %customers[i].Amount)
                break
    def checkBalance(self,acct):
        nam=input("Enter your name: ")
        acc=acct
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                print("Total balance in account is %d\n" %customers[i].Amount)
                break
    
    def transferMoney(self,acct1,acct2):
        nam1=input("Enter your name: ")
        acc1=acct1
        acc2=acct2
        mon=int(input("Enter the amount of money to Transfer: "))
        for i in range(len(customers)):
            if(customers[i].accno==acc1):
                if(customers[i].Amount<mon):
                    print("Insufficient balance in account to Transfer")
                else:
                    customers[i].Amount-=mon
                    customers[i].trans+=1
                    print("Remaining money in account with account number "+ str(acc1) + " after transfer is "+str(customers[i].Amount))
            
            if(customers[i].accno==acc2):
                customers[i].Amount+=mon
                customers[i].trans+=1
                print("Remaining money in account with account number "+ str(acc2) +" after receiving is "+ str(customers[i].Amount))
    
    def searchDetails(self,acct):
        acc=acct
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                print("The name of the account holder is %s\n " %customers[i].name)
                print("The account number is %d\n" %acc)
                print("The balance in the account is %d\n" %customers[i].Amount)
                print("The total number of transactions in the account is %d\n" %customers[i].trans)
        
customers=[]
option='z'

print("Menu \n a) Account creation\n b) Deposit\n c) Withdraw\n d) Check balance\n e) Transfer amount\n f) Search a particular account detail\n g) exit")

while(option!='g'):
    option=input("Choose an option: ")
    if(option=='a'):
        
        name=input("Enter name: ")
        # accno=int(input("Enter account number: "))
        accno = random.randint(5000,10000)
        print("Your account number is : ",accno)
        Amount=int(input("Enter the money to deposit (Minimum 100): "))
        customers.append(Bank(name,accno,Amount,0))
        
        
    elif(option=='b'):  
        acc=int(input("Enter the account number: "))
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                customers[i].depositMoney(acc)
                break
            
    elif(option=='c'):            
        acc=int(input("Enter the account number: "))
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                customers[i].withdrawMoney(acc)    
                break
    elif(option=='d'):           
        acc=int(input("Enter the account number: "))
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                customers[i].checkBalance(acc)    
                break 
    elif(option=='e'):               
        acc1=int(input("Enter your account number: "))   
        acc2=int(input("Enter account number to transfer: "))
        for i in range(len(customers)):
            if(customers[i].accno==acc1):
                customers[i].transferMoney(acc1,acc2)    
                break 
    elif(option=='f'):  
        acc=int(input("Enter the account number: "))
        for i in range(len(customers)):
            if(customers[i].accno==acc):
                customers[i].searchDetails(acc)
        
        
