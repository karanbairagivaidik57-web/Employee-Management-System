#EmployeeView.py<---Module Name
import pickle
def viewemployee():
    #Get the Records from File
    records=[] # Outer List for Holding records
    with open("empproject.data", "rb") as fp:
        while(True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #display the records
    res=False
    empno=int(input("Enter Employee Number to View the Details: "))
    for index in range(len(records)):
        if(records[index][0]==empno):
            recindex=index
            res=True
            break
    #View the Record
    print("-"*50)
    if(res):
        print("\tEmployee Number:{}".format(records[recindex][0]))
        print("\tEmployee Name:{}".format(records[recindex][1]))
        print("\tEmployee Salary:{}".format(records[recindex][2]))
        print("\tEmployee Company Name:{}".format(records[recindex][3]))
    else:
        print("\tEmployee Number {} Does Not Exist ".format(empno))
    print("-" * 50)

def viewallemployee():
    with open("empproject.data","rb") as fp:
       print("------------------------------------------")
       print("\tENO\t\tNAME\tSAL\t\tCOMPNAME")
       print("------------------------------------------")
       while(True):
           try:
               record = pickle.load(fp)
               for val in record:
                   print("\t{}".format(val),end="\t")
               print()
           except EOFError:
               print("------------------------------------------")
               break
