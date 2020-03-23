
import requests
import json
from utils import(__)

class _Score():
    def __init__(self, ticker):
        self.ticker = ticker

    def data(self):
        url = 'https://finance.yahoo.com/quote/%s'% (self.ticker)+'/financials'
                    
        html = requests.get(url=url).text
        json_ = html.split('root.App.main =')[1].split(
            '(this)')[0].split(';\n}')[0].strip()
        df = json.loads(json_)[
            'context']['dispatcher']['stores']['QuoteSummaryStore']

        X = " "
        
        for idx, item in enumerate(json.dumps(df).split('{"raw": ')):
            if "fmt" in item:
                p = item.split(', "fmt":', maxsplit=1)
                X += p[0] + p[1].split('}', maxsplit=1)[1]
            else:
                X += item  
        df = json.loads(X)
        
        
        cf  = __(df['cashflowStatementHistory']['cashflowStatements'])
        bs  = __(df['balanceSheetHistory']['balanceSheetStatements'])
        ics = __(df['incomeStatementHistory']['incomeStatementHistory'])
        
        cap = (df['summaryDetail']['marketCap'])

        return cf, bs, ics, cap

    def Altman_Z_ScoreBase(self, cf, bs, ics, mkt_cap):
        
        Z1	= (bs.loc['TOTAL CURRENT ASSETS'] -\
          bs.loc['TOTAL CURRENT LIABILITIES'])/ bs.loc['TOTAL ASSETS']

        Z2 =	bs.loc['RETAINED EARNINGS'] / bs.loc['TOTAL ASSETS']
        try:
            Z3 = (ics.loc['INCOME BEFORE TAX'] - ics.loc[
            'INTEREST EXPENSE'])/bs.loc['TOTAL ASSETS'] 
        except TypeError:
            Z3 = ics.loc['EBIT']/bs.loc['TOTAL ASSETS']
    
        Z4   =	mkt_cap	/	bs.loc['TOTAL LIAB']

        Z5	= ics.loc['TOTAL REVENUE']	/ bs.loc['TOTAL ASSETS']
        ZZ	=	1.2	*	Z1	+	1.4	*	Z2	+	3.3	*	Z3	+\
            	0.6	*	Z4	+	1.0	*	Z5

        return ZZ

if __name__ == "__main__":
    pass