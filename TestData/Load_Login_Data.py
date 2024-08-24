from Utilities.Xlutilities import *

def Load_data(xpath, sheet):
    row = GetRow(xpath, sheet)
    col = GetCol(xpath, sheet)
    l2=[]
    for r in range(2,row+1):
        l1=[]
        for c in range(1,col+1):
            #print(r,c)
            #print(ReadCell(xpath, sheet, r, c))
            l1.append(ReadCell(xpath, sheet, r, c))
        l2.append(tuple(l1))
    return l2


#Load_data("./LoginData.xlsx", "Sheet1")