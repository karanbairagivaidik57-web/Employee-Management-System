import pickle
def searchemployee():
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
    res = False
    empno = int(input("Enter Employee Number to Search the Details: "))
    for index in range(len(records)):
        if (records[index][0] == empno):
            res = True
            break
    # View the Record
    print("-" * 50)
    if (res):
       print("\tEmployee Exist-Valid Employee")
    else:
        print("\tEmployee Does Not Exist-Invalid Employee")
    print("-" * 50)
