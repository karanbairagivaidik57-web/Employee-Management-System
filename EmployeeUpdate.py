import pickle
def updateemployee():
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
    res=False
    empno = int(input("Enter Employee Number for Updating Details:"))
    for index in range(len(records)):
        if(records[index][0]==empno):
            recindex = index
            res=True
            break
    #Updation Process
    if(res):
        empsal=float(input("Enter Employee New Salary:"))
        empcompname=input("Enter Employee New Comp Name:")
        records[recindex][2]=empsal
        records[recindex][3]=empcompname
        #Re-write the Updated Records to the File by Overlapping
        with open("empproject.data", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\tEmployee Record Updated Successfully")
    else:
        print("\tEmployee Number {} Does Not Exist".format(empno))
