# In[1]:


import pandas as pd
ipl = pd.read_csv('matches.csv')


# In[2]:


ipl.describe()


# In[3]:


ipl['win_by'] = ipl.iloc[:,11:13].sum(axis=1)


# In[4]:


ipl = ipl.drop(columns=['win_by','umpire3'])


# In[6]:


ipl.loc[ipl['win_by_runs']!=0,'win_type'] = 'runs'
ipl.loc[ipl['win_by_wickets']!=0,'win_type'] = 'wickets'
ipl['win_by'] = ipl.iloc[:,11:13].sum(axis=1)


# In[7]:


ipl = ipl.drop(columns=['win_by_wickets','win_by_runs','venue','season','umpire2'])


# In[9]:


ipl.loc[ipl['team1']=='Royal Challengers Bangalore', 'team1'] = 'RCB'
ipl.loc[ipl['team1']=='Rising Pune Supergiant', 'team1'] = 'RPS'
ipl.loc[ipl['team1']=='Kolkata Knight Riders', 'team1'] = 'KKR'
ipl.loc[ipl['team1']=='Kings XI Punjab', 'team1'] = 'KXIP'
ipl.loc[ipl['team1']=='Sunrisers Hyderabad', 'team1'] = 'SRH'
ipl.loc[ipl['team1']=='Delhi Daredevils', 'team1'] = 'DD'
ipl.loc[ipl['team1']=='Gujarat Lions', 'team1'] = 'GL'
ipl.loc[ipl['team1']=='Mumbai Indians', 'team1'] = 'MI'
ipl.loc[ipl['team1']=='Rajasthan Royals', 'team1'] = 'RR'
ipl.loc[ipl['team1']=='Pune Warriors', 'team1'] = 'PWI'
ipl.loc[ipl['team1']=='Deccan Chargers', 'team1'] = 'DC'
ipl.loc[ipl['team1']=='Rising Pune Supergiants', 'team1'] = 'RPS'
ipl.loc[ipl['team1']=='Kochi Tuskers Kerala', 'team1'] = 'KTK'
ipl.loc[ipl['team1']=='Chennai Super Kings', 'team1'] = 'CSK'
ipl.loc[ipl['team2']=='Royal Challengers Bangalore', 'team2'] = 'RCB'
ipl.loc[ipl['team2']=='Rising Pune Supergiant', 'team2'] = 'RPS'
ipl.loc[ipl['team2']=='Kolkata Knight Riders', 'team2'] = 'KKR'
ipl.loc[ipl['team2']=='Kings XI Punjab', 'team2'] = 'KXIP'
ipl.loc[ipl['team2']=='Sunrisers Hyderabad', 'team2'] = 'SRH'
ipl.loc[ipl['team2']=='Delhi Daredevils', 'team2'] = 'DD'
ipl.loc[ipl['team2']=='Gujarat Lions', 'team2'] = 'GL'
ipl.loc[ipl['team2']=='Mumbai Indians', 'team2'] = 'MI'
ipl.loc[ipl['team2']=='Rajasthan Royals', 'team2'] = 'RR'
ipl.loc[ipl['team2']=='Pune Warriors', 'team2'] = 'PWI'
ipl.loc[ipl['team2']=='Deccan Chargers', 'team2'] = 'DC'
ipl.loc[ipl['team2']=='Rising Pune Supergiants', 'team2'] = 'RPS'
ipl.loc[ipl['team2']=='Kochi Tuskers Kerala', 'team2'] = 'KTK'
ipl.loc[ipl['team2']=='Chennai Super Kings', 'team2'] = 'CSK'
ipl.loc[ipl['toss_winner']=='Royal Challengers Bangalore', 'toss_winner'] = 'RCB'
ipl.loc[ipl['toss_winner']=='Rising Pune Supergiant', 'toss_winner'] = 'RPS'
ipl.loc[ipl['toss_winner']=='Kolkata Knight Riders', 'toss_winner'] = 'KKR'
ipl.loc[ipl['toss_winner']=='Kings XI Punjab', 'toss_winner'] = 'KXIP'
ipl.loc[ipl['toss_winner']=='Sunrisers Hyderabad', 'toss_winner'] = 'SRH'
ipl.loc[ipl['toss_winner']=='Delhi Daredevils', 'toss_winner'] = 'DD'
ipl.loc[ipl['toss_winner']=='Gujarat Lions', 'toss_winner'] = 'GL'
ipl.loc[ipl['toss_winner']=='Mumbai Indians', 'toss_winner'] = 'MI'
ipl.loc[ipl['toss_winner']=='Rajasthan Royals', 'toss_winner'] = 'RR'
ipl.loc[ipl['toss_winner']=='Pune Warriors', 'toss_winner'] = 'PWI'
ipl.loc[ipl['toss_winner']=='Deccan Chargers', 'toss_winner'] = 'DC'
ipl.loc[ipl['toss_winner']=='Rising Pune Supergiants', 'toss_winner'] = 'RPS'
ipl.loc[ipl['toss_winner']=='Kochi Tuskers Kerala', 'toss_winner'] = 'KTK'
ipl.loc[ipl['toss_winner']=='Chennai Super Kings', 'toss_winner'] = 'CSK'
ipl.loc[ipl['winner']=='Royal Challengers Bangalore', 'winner'] = 'RCB'
ipl.loc[ipl['winner']=='Rising Pune Supergiant', 'winner'] = 'RPS'
ipl.loc[ipl['winner']=='Kolkata Knight Riders', 'winner'] = 'KKR'
ipl.loc[ipl['winner']=='Kings XI Punjab', 'winner'] = 'KXIP'
ipl.loc[ipl['winner']=='Sunrisers Hyderabad', 'winner'] = 'SRH'
ipl.loc[ipl['winner']=='Delhi Daredevils', 'winner'] = 'DD'
ipl.loc[ipl['winner']=='Gujarat Lions', 'winner'] = 'GL'
ipl.loc[ipl['winner']=='Mumbai Indians', 'winner'] = 'MI'
ipl.loc[ipl['winner']=='Rajasthan Royals', 'winner'] = 'RR'
ipl.loc[ipl['winner']=='Pune Warriors', 'winner'] = 'PWI'
ipl.loc[ipl['winner']=='Deccan Chargers', 'winner'] = 'DC'
ipl.loc[ipl['winner']=='Rising Pune Supergiants', 'winner'] = 'RPS'
ipl.loc[ipl['winner']=='Kochi Tuskers Kerala', 'winner'] = 'KTK'
ipl.loc[ipl['winner']=='Chennai Super Kings', 'winner'] = 'CSK'


# In[10]:


cols = list(ipl.columns.values)
ipl = ipl[cols[0:10] + [cols[-1]] + [cols[-2]] + cols[10:12]]


# In[15]:


ipl1 = ipl.loc[ipl['result']!='normal']
ipl2 = ipl.loc[ipl['dl_applied']!=0]
print(ipl1)
print(ipl2)

# OUTPUT :
#       id       city        date team1 team2 toss_winner toss_decision  \
# 33    34     Rajkot  2017-04-29    GL    MI          GL           bat   
# 125  126  Cape Town  2009-04-23    RR   KKR         KKR         field   
# 189  190    Chennai  2010-03-21  KXIP   CSK         CSK         field   
# 300  301      Delhi  2011-05-21    DD   PWI          DD           bat   
# 387  388  Hyderabad  2013-04-07   RCB   SRH         RCB           bat   
# 400  401  Bangalore  2013-04-16    DD   RCB         RCB         field   
# 475  476  Abu Dhabi  2014-04-29    RR   KKR          RR           bat   
# 535  536  Ahmedabad  2015-04-21    RR  KXIP        KXIP         field   
# 545  546  Bangalore  2015-04-29   RCB    RR          RR         field   
# 570  571  Bangalore  2015-05-17    DD   RCB         RCB         field   

#         result  dl_applied winner  win_by win_type player_of_match  \
# 33         tie           0     MI       0      NaN       KH Pandya   
# 125        tie           0     RR       0      NaN       YK Pathan   
# 189        tie           0   KXIP       0      NaN        J Theron   
# 300  no result           0    NaN       0      NaN             NaN   
# 387        tie           0    SRH       0      NaN       GH Vihari   
# 400        tie           0    RCB       0      NaN         V Kohli   
# 475        tie           0     RR       0      NaN     JP Faulkner   
# 535        tie           0   KXIP       0      NaN        SE Marsh   
# 545  no result           0    NaN       0      NaN             NaN   
# 570  no result           0    NaN       0      NaN             NaN   

#              umpire1  
# 33      AK Chaudhary  
# 125        MR Benson  
# 189      K Hariharan  
# 300        SS Hazare  
# 387     AK Chaudhary  
# 400        M Erasmus  
# 475        Aleem Dar  
# 535        M Erasmus  
# 545        JD Cloete  
# 570  HDPK Dharmasena  
#       id           city        date team1 team2 toss_winner toss_decision  \
# 56    57      Bangalore  2017-05-17   SRH   KKR         KKR         field   
# 99   100          Delhi  2008-05-17    DD  KXIP          DD           bat   
# 102  103        Kolkata  2008-05-18   KKR   CSK         KKR           bat   
# 119  120      Cape Town  2009-04-19  KXIP    DD          DD         field   
# 122  123         Durban  2009-04-21  KXIP   KKR         KKR         field   
# 148  149      Centurion  2009-05-07   CSK  KXIP         CSK           bat   
# 251  252          Kochi  2011-04-18   CSK   KTK         KTK         field   
# 280  281        Kolkata  2011-05-07   CSK   KKR         CSK           bat   
# 290  291      Bangalore  2011-05-14   KKR   RCB         RCB         field   
# 488  489          Delhi  2014-05-10    DD   SRH         SRH         field   
# 536  537  Visakhapatnam  2015-04-22   SRH   KKR         KKR         field   
# 567  568      Hyderabad  2015-05-15   SRH   RCB         SRH           bat   
# 597  598      Hyderabad  2016-04-26   SRH   RPS         RPS         field   
# 620  621        Kolkata  2016-05-14   RPS   KKR         RPS           bat   
# 624  625  Visakhapatnam  2016-05-17    DD   RPS         RPS         field   
# 625  626      Bangalore  2016-05-18   RCB  KXIP        KXIP         field   

#      result  dl_applied winner  win_by win_type   player_of_match  \
# 56   normal           1    KKR       7  wickets   NM Coulter-Nile   
# 99   normal           1   KXIP       6     runs  DPMD Jayawardene   
# 102  normal           1    CSK       3     runs           M Ntini   
# 119  normal           1     DD      10  wickets        DL Vettori   
# 122  normal           1    KKR      11     runs          CH Gayle   
# 148  normal           1    CSK      12     runs         ML Hayden   
# 251  normal           1    KTK       7  wickets       BB McCullum   
# 280  normal           1    KKR      10     runs     Iqbal Abdulla   
# 290  normal           1    RCB       4  wickets          CH Gayle   
# 488  normal           1    SRH       8  wickets          DW Steyn   
# 536  normal           1    SRH      16     runs         DA Warner   
# 567  normal           1    RCB       6  wickets           V Kohli   
# 597  normal           1    RPS      34     runs          AB Dinda   
# 620  normal           1    KKR       8  wickets         YK Pathan   
# 624  normal           1    RPS      19     runs          AB Dinda   
# 625  normal           1    RCB      82     runs           V Kohli   

#                    umpire1  
# 56            AK Chaudhary  
# 99          AV Jayaprakash  
# 102              Asad Rauf  
# 119              MR Benson  
# 122              DJ Harper  
# 148              DJ Harper  
# 251            K Hariharan  
# 280              Asad Rauf  
# 290            RE Koertzen  
# 488           RM Deshpande  
# 536         RK Illingworth  
# 567           AK Chaudhary  
# 597            AY Dandekar  
# 620         A Nand Kishore  
# 624            Nitin Menon  
# 625  KN Ananthapadmanabhan 

# In[16]:


ipl.to_csv('IPL_analysis_ready.csv',index = False)


# bookmarked the data here and data cleansing over now
# You can access both the CSVs in the parent folder of this file. And check how the data has been cleansed using python pandas library.
