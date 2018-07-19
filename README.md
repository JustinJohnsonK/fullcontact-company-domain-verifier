# fullcontact-company-domain-verifier

# About:

Compares the given set of "Company Names" with the corresponding "Company Domains" and prints weather its True or False.

Searches Google for additional verification.
 

# Requiremnets:

Tested in python 3.6.5

Install:

1) pip3 install google
2) pip3 install pandas
3) Input .csv file with Company_Names and Company_Domain


# Input File:

(csv format)

File should be in the same folder of the program.

Input file should contain all column with 'Company Names' and another column with 'Company Domain'.


# Output File:

(csv format)

Name format -> inputFileName-result.csv

Will be created in the same location where the program runs.

Contain all the columns in the input file + "Verification" column (+ "From_Google" column).

"Verification" : 

"True" - if the company domain is correct according to the provided rules.

"False" - if the company domain is wrong according to the provided rules.

"None" - if either the company name or the domain is not provided.

"From_Google":(optional column)

Blank - if company domain is already verified to "True" according to the given set of rules.

Domain - Google search the company name and enters the first domain which appears in the search result.
         (Will not always provide the correct result).

Domain will only appear for cases with Verification column = "False" or "None". 

If company name is empty then the "Verification" remain "None"


# Executing:

Start execting from execute.py

In terminal type:   python3 execute.py
