import pickle
def isunique(empno):
    # Get the Records from File
    records = []  # Outer List for Holding records
    with open("empproject.data", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # display the records
    res=True
    for record in records:
        if(record[0]==empno):
            res=False
    return res

def addemployee():
    with open("empproject.data","ab") as fp:
        while(True):
            try:
                print("-"*50)
                empno=int(input("Enter Employee Number: "))
                #save lst data into the file by using dump()
                if(isunique(empno)):
                    lst = []  # create an empty list
                    empname = input("Enter Employee Name: ")
                    empsal = float(input("Enter Employee Salary: "))
                    empcname = input("Enter Employee Comp Name: ")
                    print("-" * 50)
                    lst.append(empno)
                    lst.append(empname)
                    lst.append(empsal)
                    lst.append(empcname)
                    pickle.dump(lst,fp)
                    print("\tEmployee Data saved as Record in File")
                else:
                    print("\tEmployee Number {} is already Exist".format(empno))
                print("-" * 50)
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for Emp, Salary")
            else:
                break
