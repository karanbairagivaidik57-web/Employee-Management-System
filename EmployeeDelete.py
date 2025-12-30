import pickle
def deleteemployee():
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
    empno=int(input("Enter Employee Number to Delete: "))
    for record in records:
        if(record[0]==empno):
            rec=record
            res=True
            break
    #Delete Record
    if(res):
        records.remove(rec)
        with open("empproject.data", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\tEmployee Record Deleted Successfully")
    else:
        print("\tEmployee Number {} Does Not Exist".format(empno))
