import pandas as pd
from verifyname import verifyname as vn
from searchGoogle import searchGoogle as sg

""" 
Requiremnets:
Tested in python 3.6
Install -
1) pip install google
2) pip install pandas

Input File:
csv format
File should be in the same folder of the program

Output File:
csv format
Will be created in the same location where the program runs
Name will be -> inputFileName-result.csv

"""

def verifyCompanyDomain(sheet, column):
    # retirieve company column name and domain column name from list
    company = column[0]
    domain = column[1]

    for index, row in sheet.iterrows():     # iterate rowwise through the sheet
        companyName = row[company]
        domainName = row[domain]
        if(pd.isnull(companyName) == False and pd.isnull(domainName) == False):     # checking weather both company name and domain exists
            if(type(companyName) == str and type(domainName) == str):               # check if company names and domains are strings
                v = vn(companyName.lower(), domainName.lower())
                verify = v.verify()                                                 # verifyName function verifies domain offline
                sheet["Verification"][index] = verify                               # verification result is stored in Verification column of each row


def readFile(FileName, columns):
    """
    Read input file
    Remove duplicates - only similar rows
    Create new column for storing result after verification
    """

    sheet = pd.read_csv(FileName, usecols = columns, nrows = 400)
    sheet_len = len(sheet)
    sheet.drop_duplicates(subset = None, inplace = True)
    print("{} duplicates found in {}".format((sheet_len - len(sheet)), FileName))

    sheet["Verification"] = "None"
    return sheet


def writeIntoFile(sheet, fileName):

    sheet.to_csv(fileName, sep='\t')


def Main():

    try:
        # get inputs from user 
        fileName = input("Enter csv file name...")
        if('.csv' not in fileName):
            fileName = fileName + '.csv'
        
        companyName = input("Enter column name with company name...")
        domainName = input("Enter column name with company domain...")
    except:
        print("Error Inputting File...")
        print("Please Make sure that the file name and column names are correct....")
        return

    # store column names in a list for passing them to other functions
    columns = [companyName, domainName]
    outPutFile = fileName.replace('.csv', '') + '-result.csv'   # output filename will be of the format (inputFileName-result.csv)

    sheet = readFile(fileName, columns)     # read the input file
    verifyCompanyDomain(sheet, columns)     # verify company domain

    print("Sheet = ", sheet)
    print("#"*100)

    option = input("Enter \t1 -> Search the (False and None) results in Google, \n \t2 -> Satisfied with the current output \n \t...")
    if(option == '1'):
        sheet['From_Google'] = " "
        search = sg(sheet, columns)
        search.getDomainFromGoogle()
        print(sheet)
    
    print("Output is in ->", outPutFile)
    writeIntoFile(sheet, outPutFile)


if __name__ == '__main__':
    Main()