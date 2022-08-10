#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
ipl = pd.read_csv('matches.csv')
print(ipl)


# In[2]:


ipl.describe()


# In[3]:


ipl['win_by'] = ipl.iloc[:,11:13].sum(axis=1)
print(ipl.head(5))


# In[4]:


ipl = ipl.drop(columns=['win_by'])
print(ipl)


# In[5]:


ipl = ipl.drop(columns=['umpire3'])
print(ipl)


# In[6]:


ipl.loc[ipl['win_by_runs']!=0,'win_type'] = 'runs'
ipl.loc[ipl['win_by_wickets']!=0,'win_type'] = 'wickets'
ipl['win_by'] = ipl.iloc[:,11:13].sum(axis=1)
print(ipl.head(5))


# In[7]:


ipl = ipl.drop(columns=['win_by_wickets','win_by_runs'])
print(ipl.head(5))


# In[8]:


ipl = ipl.drop(columns = ['venue','season','umpire2'])
print(ipl.head(5))


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
print(ipl.head(5))


# In[10]:


cols = list(ipl.columns.values)
ipl = ipl[cols[0:10] + [cols[-1]] + [cols[-2]] + cols[10:12]]
print(cols)


# In[11]:


print(ipl.head(5))


# 

# In[15]:


ipl1 = ipl.loc[ipl['result']!='normal']
ipl2 = ipl.loc[ipl['dl_applied']!=0]
print(ipl1)
print(ipl2)


# In[16]:


ipl.to_csv('IPL_analysis_ready.csv',index = False)


# In[ ]:


#bookmarked the data here and data cleansing over now

