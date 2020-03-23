import pandas as pd
from utils import(sector, plotting)
from Altman_Z_Score import _Score
import random
from symbols import (BasicMaterials as BM, 
                              CommunicationServices as CS, 
                              ConsumerCyclical as CC, 
                              ConsumerDefensive as CD, 
                              Energy as Eneg, 
                              FinancialServices as FS, 
                              Healthcare as HC, 
                              Industrials as Ind, 
                              RealEstate as RE, 
                              Technology as Techn, 
                              )

def pre_main_(syms):

    AZS_list = []; MKT_list = []
    for sym in syms:
        main = _Score(sym)
        cf, bs, ics, cap = main.data()
        
        result = main.Altman_Z_ScoreBase(cf, bs, ics, cap).round(2)
        AZS_list.append(result); MKT_list.append(cap)
    
    df=pd.DataFrame(AZS_list, columns = ['Score'], index=syms)
    df['Market Cap'] = pd.DataFrame(MKT_list, 
                   columns = ['Market Cap'], index=syms
                   )['Market Cap'].map('{:,.0f}'.format)
    
    df = df.sort_values(by='Score')
    
    return df

def main_():
    N = 15
    #Sector Basic Materials 
    syms = BM
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    
    #'''
    #Sector Communication Services
    syms = CS
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    
    #Sector Consumer Defensive 
    syms = CD
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
                         
    #Sector Energy 
    syms = Eneg
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    
    #Sector Real Estate
    syms = RE
    sect = sector(syms)
    plotting((pre_main_(syms)), sect)
    
    #Sector Industrials 
    syms = Ind
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    
    
    ######################
    #Sector Consumer Cyclical 
    syms = CC
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    
    #Sector Financial Services 
    syms = FS
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    
    #Sector Health Care 
    syms = HC
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    
    #Sector Technology 
    syms = Techn
    sect = sector(syms)
    syms = random.sample(syms, N)
    plotting((pre_main_(syms)), sect)
    #'''
if __name__ == "__main__":
    main_()
    