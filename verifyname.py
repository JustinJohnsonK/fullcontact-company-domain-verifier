class verifyname:


    def __init__(self, company, domain):

        self.companyName = company
        self.domainName = domain


    def verify(self):
    
        companyName = self.companyName
        domain = self.domainName
        
        # conditions
        # 1. check for similar company name and domain
        # 2. check for shortform of company in domain
        # 3. check if company name joined with slash is in domain
        # 4. check if company name with all spaces removed is in domain
        # 5. check if first 4 letters in comapny name is in domain
        
        companyName.replace("&", " ")
        companyName.replace("'", "")
        companyName.replace("-", " ")
        companyName.replace(",", " ")
        companyName = " ".join(companyName.split())
        companyFromDomain = domain.split(".")[0]

        cDotSplit = companyName.split(".")
        cSpaceSplit = companyName.split(" ")
        cSplitSlash = companyName.split("/")
        cCommaSplit = companyName.split(",")

        cSpaceJoin = "".join(cSpaceSplit)
        dDotSplit = (domain.split("."))[0]
        cJoinSlash = "".join(cSplitSlash)

        shortCname = ""

        if(len(cSpaceSplit) > 2):
            for i in companyName.split():
                shortCname += i[0]
        else:
            shortCname = cSpaceJoin

        try:
            cJoinTwoSpace = cSpaceSplit[0] + cSpaceSplit[1]
        except:
            cJoinTwoSpace = "".join(cSpaceSplit)

        conditions = [
            companyName in domain,
            cSpaceJoin in domain, 
            cSpaceJoin[:4] in domain,
            cCommaSplit[0] in domain,
            dDotSplit[0] in companyName,
            cJoinTwoSpace in domain,
            cJoinSlash in domain,
            shortCname in domain
        ]

        if any(conditions):
            return "True"
        else:
            return "False"