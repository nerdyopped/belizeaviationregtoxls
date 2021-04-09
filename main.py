import urllib.request
from html_table_parser import HTMLTableParser
import pandas as pd

def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()

xhtml = url_get_contents('https://civilaviation.gov.bz/index.php/bdca-civil-aircraft-register').decode('utf-8')
p = HTMLTableParser()
p.feed(xhtml)
print("\n\nPANDAS DATAFRAME\n")
belizeRep = pd.DataFrame(p.tables[4])
print(belizeRep)
belizeRep.to_excel(r'BeliezeReg.xlsx', index= False)