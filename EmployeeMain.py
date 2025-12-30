from EmpMenu import menu
from EmployeeAdd import addemployee
from EmployeeDelete import deleteemployee
from EmployeeUpdate import updateemployee
from EmployeeSearch import searchemployee
from EmployeeView import viewallemployee,viewemployee
while(True):
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewemployee()
            case 5:
                viewallemployee()
            case 6:
                searchemployee()
            case 7:
                print("\tThx for Using This Project")
                break
            case _:
                print("\tUr Selection of Operation wrong--try again")
    except ValueError:
        print("\tDon't Enter alnums,strs and symbols for Choice:")
