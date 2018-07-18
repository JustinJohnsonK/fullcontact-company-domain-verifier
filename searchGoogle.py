import googlesearch as gs
import pandas as pd

class  searchGoogle:

    def __init__(self, sheet, columns):

        self.sheet = sheet
        self.columns = columns


    def searchgoogle(self, companyName):

        print("Searching Google for ", companyName)
        result = gs.search(companyName, num=1, stop=1, pause=1)
        return(result)  


    def getDomainFromGoogle(self):

        sheet = self.sheet
        company = self.columns[0]
        domain = self.columns[1]

        gener_loop = ([index, row] for index, row in sheet.iterrows() if((row[company] != "nan" or row[company] != "NaN")
        and (row['Verification'] == 'False' or row['Verification'] == 'None')
        and (type(row[company]) == str) 
        and (pd.isnull(row[company]) == False)
        ))

        i = 0
        length = len(sheet)
        
        while(i < length):

            try:
                index_row = next(gener_loop)
                index = index_row[0]
                row = index_row[1]
                companyName = row[company]
                print(companyName)
                result = next(self.searchgoogle(companyName))
                print(result)
                if(pd.isnull(row[domain]) == False):
                    if(row[domain] in  result):
                        sheet['Verification'][index] = 'True'    
                sheet['From_Google'][index] = result
                i += 1
            except:
                print("Searching Completed")
                return