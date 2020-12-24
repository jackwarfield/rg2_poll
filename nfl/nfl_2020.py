"""
Game data from https://www.pro-football-reference.com
"""
from glicko2 import *
import random
from datetime import datetime, timezone
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")+'T00:00:00.000Z'

df = pd.read_csv ('teams.csv')
df['rating'] = 1500*np.ones(len(df))
df['rd'] = 600*np.ones(len(df))
df['volatility'] = 0.06*np.ones(len(df))

sched = pd.read_csv ('games2020.csv')
sched = sched.reset_index (drop=True)
s_ind = list(sched.index)

for j in range(51):
    #df['rd'] = 350*np.ones(len(df))
    df['wins'] = np.zeros(len(df))
    df['losses'] = np.zeros(len(df))
    df['ties'] = np.zeros(len(df))
    for i in s_ind:
        id1 = sched.loc[i, 'Winner/tie']
        id2 = sched.loc[i, 'Loser/tie']
        hp = sched.loc[i, 'PtsW']
        ap = sched.loc[i, 'PtsL']
        if hp > ap:
            win = True
            df.loc[df.team == id1, 'wins'] += 1
            df.loc[df.team == id2, 'losses'] += 1
        else:
            win = 'Tie'
            df.loc[df.team == id1, 'ties'] += 1
            df.loc[df.team == id2, 'ties'] += 1
        df = update_ratings (id1,id2,win,df.copy())

ranks = df.sort_values ('rating', ascending=False).reset_index(drop=True)[['team', 'rating', 'wins', 'losses', 'ties']].values

print ('| {:<5} | {:<26} | {:<8} | {:<6} |'.format('Rank', 'Team', 'Record', 'Rating'))
print ('| {:<5} | {:<26} | {:<8} | {:<6} |'.format('---:', '---:', ':---', '---:'))
for i in range(1,len(ranks)+1):
    t,r,w,l,e = ranks[i-1]
    if e == 0:
        rec = str(int(w))+'-'+str(int(l))
    else:
        rec = str(int(w))+'-'+str(int(l))+'-'+str(int(e))
    print ('| {:<5} | {:<26} | {:<8} | {:<6} |'.format(i, t, rec, int(r)))

df.to_csv ('teams_2020_rankings.csv', index=False)
