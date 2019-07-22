import re

def textParse(bigString):
    listofTokens = re.split('r\W',bigString)
    return [tok.lower() for tok in listofTokens if len(tok)>2]