"""
Game data from https://collegefootballdata.com
"""
from glicko2 import *
import random
from datetime import datetime, timezone
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")+'T00:00:00.000Z'

df = pd.read_csv ('teams.csv')
df['rd'] = 600*np.ones(len(df))

sched = pd.read_csv ('games2020.csv')
sched = sched[sched.home_points.notna()]
sched = sched.sort_values ('start_date', ascending=True)
sched = sched.reset_index (drop=True)
s_ind = list(sched.index)

year = sched.loc[0, 'season']
#df['rd'] = 350*np.ones(len(df))
for i in s_ind:
    id1 = sched.loc[i, 'home_id']
    id2 = sched.loc[i, 'away_id']
    try:
        _ = df[df.id == id1].values[0]
    except IndexError:
        df3 = pd.DataFrame ([[id1, sched.loc[i, 'home_team'], 800, 600, 0.06]], columns=['id', 'school', 'rating', 'rd', 'volatility'])
        df = df.append(df3).reset_index(drop=True)
    try:
        _ = df[df.id == id2].values[0]
    except IndexError:
        df3 = pd.DataFrame ([[id2, sched.loc[i, 'away_team'], 800, 600, 0.06]], columns=['id', 'school', 'rating', 'rd', 'volatility'])
        df = df.append(df3).reset_index(drop=True)
    hp = sched.loc[i, 'home_points']
    ap = sched.loc[i, 'away_points']
    if hp > ap:
        win = True
    else:
        win = False
    df = update_ratings (id1,id2,win,df.copy())

sched = pd.read_csv('games2021.csv')
sched = sched[(sched.season == 2021)]
sched = sched[sched.home_points.notna()]
sched = sched.sort_values ('start_date', ascending=True)
sched = sched.reset_index (drop=True)
sched.to_csv ('games2021.csv', index=False)
s_ind = list(sched.index)

for j in range(50):
    year = sched.loc[0, 'season']
    #df['rd'] = 350*np.ones(len(df))
    df['wins'] = np.zeros(len(df))
    df['losses'] = np.zeros(len(df))
    for i in s_ind:
        id1 = sched.loc[i, 'home_id']
        id2 = sched.loc[i, 'away_id']
        try:
            _ = df[df.id == id1].values[0]
        except IndexError:
            df3 = pd.DataFrame ([[id1, sched.loc[i, 'home_team'], 800, 600, 0.06]], columns=['id', 'school', 'rating', 'rd', 'volatility'])
            df = df.append(df3).reset_index(drop=True)
        try:
            _ = df[df.id == id2].values[0]
        except IndexError:
            df3 = pd.DataFrame ([[id2, sched.loc[i, 'away_team'], 800, 600, 0.06]], columns=['id', 'school', 'rating', 'rd', 'volatility'])
            df = df.append(df3).reset_index(drop=True)
        hp = sched.loc[i, 'home_points']
        ap = sched.loc[i, 'away_points']
        if hp > ap:
            win = True
            df.loc[df.id == id1, 'wins'] += 1
            df.loc[df.id == id2, 'losses'] += 1
        else:
            win = False
            df.loc[df.id == id1, 'losses'] += 1
            df.loc[df.id == id2, 'wins'] += 1
        df = update_ratings (id1,id2,win,df.copy())

df = df[df.conference.notna()].reset_index(drop=True)

ranks = df.sort_values ('rating', ascending=False).reset_index(drop=True)[['school', 'conference', 'rating', 'wins', 'losses']].values

print ('| {:<5} | {:<20} | {:<20} | {:<8} | {:<6} |'.format('Rank', 'Team', 'Conference', 'Record', 'Rating'))
print ('| {:<5} | {:<20} | {:<20} | {:<8} | {:<6} |'.format('---:', '---:', '---:', '---:', '---:'))
for i in range(1,25+1):
    t,c,r,w,l = ranks[i-1]
    rec = str(int(w))+'-'+str(int(l))
    print ('| {:<5} | {:<20} | {:<20} | {:<8} | {:<6} |'.format(i, t, c, rec, int(r)))


df.to_csv ('teams_2021_rankings.csv', index=False)
