"""
Game data from ncaa.com using R script from Luke Benz 
https://github.com/lbenz730/NCAA_Hoops
"""
from glicko2 import *
import random
from datetime import datetime, timezone
import subprocess
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")+'T00:00:00.000Z'

subprocess.call ("./ncaa_hoops_scraper.R")
sched = pd.read_csv ('NCAA_Hoops_Results.csv')
sched = sched[(sched.teamscore.notna()) & (sched.opponent.notna())]
sched.loc[sched.year.isna(), 'year'] = 2021
sched = sched.reset_index(drop=True)
for i in range(len(sched)):
    m,d,y = sched.loc[i, ['month', 'day', 'year']]
    sched.loc[i, 'date'] = '%i-%i-%i' %(m,d,y) 
sched['date'] = pd.to_datetime(sched.date)
sched = sched.sort_values('date').reset_index(drop=True)

df = pd.read_csv ('teams.csv')
df['rating'] = 1500*np.ones(len(df))
df['rd'] = 600*np.ones(len(df))
df['volatility'] = 0.06*np.ones(len(df))

s_ind = list(sched.index)
for j in range(51):
    #df['rd'] = 350*np.ones(len(df))
    df['wins'] = np.zeros(len(df))
    df['losses'] = np.zeros(len(df))
    for i in s_ind:
        id1 = sched.loc[i, 'team']
        id2 = sched.loc[i, 'opponent']
        try:
            _ = df[df.team == id2].values[0]
        except IndexError:
            df3 = pd.DataFrame ([[id2, 'removethis', 800, 600, 0.06]], columns=['team', 'conference', 'rating', 'rd', 'volatility'])
            df = df.append(df3).reset_index(drop=True)
        hp = sched.loc[i, 'teamscore']
        ap = sched.loc[i, 'oppscore']
        if hp > ap:
            win = True
            df.loc[df.team == id1, 'wins'] += 1
        else:
            win = False
            df.loc[df.team == id1, 'losses'] += 1
        df = update_ratings (id1,id2,win,df.copy())
df = df[df.conference != 'removethis']
df = df.sort_values(by='rating', ascending=False).reset_index(drop=True)
df = df[(df.wins + df.losses) > df.loc[0].wins/2.0]

ranks = df.sort_values ('rating', ascending=False).reset_index(drop=True)[['team', 'conference', 'rating', 'wins', 'losses']].values

print ('| {:<5} | {:<20} | {:<10} | {:<8} | {:<6} |'.format('Rank', 'Team', 'Conference', 'Record', 'Rating'))
print ('| {:<5} | {:<20} | {:<10} | {:<8} | {:<6} |'.format('---:', '---:', '---:', '---:', '---:'))
for i in range(1,25+1):
    t,c,r,w,l = ranks[i-1]
    rec = str(int(w))+'-'+str(int(l))
    print ('| {:<5} | {:<20} | {:<10} | {:<8} | {:<6} |'.format(i, t, c, rec, int(r)))

df.to_csv ('teams_2021_rankings.csv', index=False)
