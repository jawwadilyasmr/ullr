import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import plot


pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',500)
#pd.set_option('display.min_rows',500)
pd.set_option('display.max_colwidth',150)
pd.set_option('display.width',120)
pd.set_option('expand_frame_repr', True)

#filePath = "/Users/jawwadilyas/Documents/gameData/"
fileName = 'result_Final.csv'
readCSV  = pd.read_csv(fileName,index_col='summonerName')
del readCSV['index']

readCSV.rename(columns={'MatchId':'Match Id','damageDealtToBuildings':'Damage Dealt To Buildings','damageDealtToObjectives':'Damage Dealt To Objectives',
                       'damageDealtToTurrets':'Damage Dealt To Turrets','damageSelfMitigated':'Damage Self Mitigated','magicDamageDealt':'Magic Damage Dealt',
                       'magicDamageDealtToChampions':'Magic Damage Dealt To Champions','magicDamageTaken':'Magic Damage Taken', 'physicalDamageDealt':'Physical Damage Dealt',
                       'physicalDamageDealtToChampions':'Physical Damage Dealt To Champions','physicalDamageTaken':'Physical Damage Taken',
                       'totalDamageDealt':'Total Damage Dealt', 'totalDamageDealtToChampions':'Total Damage Dealt To Champions',
                       'totalDamageShieldedOnTeammates':'Total Damage Shielded On Teammates','totalDamageTaken':'Total Damage Taken',
                       'goldEarned':'Gold Earned','goldSpent':'Gold Spent','neutralMinionsKilled':'Neutral Minions Killed','totalMinionsKilled':'Total Minions Killed'}, 
                 inplace=True)

firstMatch = readCSV.loc[readCSV['Match Id']=='NA1_3964922963']

def damageDealtToBuilding():
    title= 'Damage Dealt To Buildings'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def damageDealtToObjectives():
    title= 'Damage Dealt To Objectives'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
   
    return fig

def damageDealtToTurrets():
    title= 'Damage Dealt To Turrets'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def damageSelfMitigated():
    title= 'Damage Self Mitigated'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig
def magicDamageDealt():
    title='Magic Damage Dealt'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
   
    return fig 

def magicDamageDealtToChampions():
    title='Magic Damage Dealt To Champions'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def magicDamageDealtToChampions():
    title='Magic Damage Dealt To Champions'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def physicalDamageDealt():
    title='Physical Damage Dealt'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def physicalDamageDealtToChampions():
    title='Physical Damage Dealt To Champions'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def physicalDamageTaken():
    title='Physical Damage Taken'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def totalDamageDealt():
    title='Total Damage Dealt'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def totalDamageDealtToChampions():
    title='Total Damage Dealt To Champions'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def totalDamageShieldedOnTeammates():
    title='Total Damage Shielded On Teammates'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=800)
    
    return fig

def totalDamageTaken():
    title='Total Damage Taken'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=7500)
    
    return fig

def totalMinionsKilled():
    title='Total Minions Killed'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=750)
    return fig

def neutralMinionsKilled():
    title='Neutral Minions Killed'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=750)
    return fig

def goldSpent():
    title='Gold Spent'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=750)
    return fig
def tKills():
    title='kills'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=750)
    return fig

def tAssists():
    title='assists'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=750)
    return fig

def tDeaths():
    title='deaths'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=750)
    return fig

def goldEarned():

    fig = make_subplots(rows=1, cols=2)
    title='Gold Earned'
    fig = px.bar(firstMatch,x=[title],color="win",title=title,height=400, width=750)

    return fig

def minionsdashboard():
    # Create the main dashboard
    title="Minions Killed"
    minionsdashboard = pn.Column(title,pn.Tabs(
        ("Total Minions Killed", totalMinionsKilled()),
        ("Neutral Minions Killed", neutralMinionsKilled()),
        ("Gold Spent", goldSpent()),
        ("Gold Earned", goldEarned())
    )).servable()
    return minionsdashboard

teamPerformance = firstMatch[['win','kills','deaths','assists','Total Minions Killed','Gold Earned']]
teamWinTotal    = teamPerformance.loc[teamPerformance['win']== True].sum()
teamLostTotal   = teamPerformance.loc[teamPerformance['win']== False].sum()
label       = ['Team Win', 'Team Lost']
teamGold    = [teamWinTotal['Gold Earned'],teamLostTotal['Gold Earned']]
teamMinion  = [teamWinTotal['Total Minions Killed'],teamLostTotal['Total Minions Killed']]
teamKills   = [teamWinTotal['kills'],teamLostTotal['kills']]
teamDeaths  = [teamWinTotal['deaths'],teamLostTotal['deaths']]
teamAssists = [teamWinTotal['assists'],teamLostTotal['assists']]

pieGold   =  px.pie(labels=label, values=teamGold, names=label, title="Gold Earned")
pieMinion  = px.pie(labels=label, values=teamMinion, names=label, title="Minions Killed")
pieKills   = px.pie(labels=label, values=teamKills, names=label, title="kills")
pieDeaths  = px.pie(labels=label, values=teamDeaths, names=label, title="Deaths")
pieAssists = px.pie(labels=label, values=teamAssists, names=label, title="Assists")

#==================================================#
# Gamer Stats particular match
#==================================================#
foodtanariWin        = firstMatch.loc['foodtanari']['win']
foodtanariDuration   = firstMatch.loc['foodtanari']['Duration']
foodtanariDate       = firstMatch.loc['foodtanari']['Creation']
foodtanariKills      = firstMatch.loc['foodtanari']['kills']
foodtanariDeaths     = firstMatch.loc['foodtanari']['deaths']
foodtanariAssists    = firstMatch.loc['foodtanari']['assists'] 
foodtanariMinions    = firstMatch.loc['foodtanari']['Total Minions Killed']
foodtanariGoldEarned = firstMatch.loc['foodtanari']['Gold Earned']
#=======================================================#
kill_stats      = firstMatch['kills'].describe()
death_stats     = firstMatch['deaths'].describe()
assists_stats   = firstMatch['assists'].describe()
gold_stats      = firstMatch['Gold Earned'].describe()
minons_stats    = firstMatch['Total Minions Killed'].describe()
#=======================================================#

def killsStats():
    if foodtanariKills > kill_stats['mean']:
        return("your kills score {} is above average {}".format(foodtanariKills,kill_stats['mean']))
    else:
        return("Your kills score is below average, you should concentrate on kills")
        
def deathsStats():
    if foodtanariDeaths > death_stats['mean']:
        return("Your deaths score is good ")
    else:
        return("Your deaths score is below average, you should focus on deaths")

def assistsStats():
    if foodtanariAssists > assists_stats['mean']:
        return("Your assists score is good ")
    else:
        return("Your assists score is below average, you should focus on it")
        
def minionStats():
    if foodtanariMinions > minons_stats['mean']:
        return("Your minions score is good ")
    else:
        return("Your minions score is below average, you should put more effort on it")

def goldStats():
    if foodtanariGoldEarned > gold_stats['mean']:
        return("Your earned lot of Gold ")
    else:
        return("You earned less Gold, you should put more effort on it")
        
def matchResult():
    lose = "Your team need more training to win the next match"
    if foodtanariWin == True:
        return('Your team put a good effort and win this match')
        
    else:
        return(lose)
#====================================================#
#Overall performance
overall_kill_stats      = readCSV['kills'].describe()
overall_death_stats     = readCSV['deaths'].describe()
overall_assists_stats   = readCSV['assists'].describe()
overall_gold_stats      = readCSV['Gold Earned'].describe()
overall_minons_stats    = readCSV['Total Minions Killed'].describe()
#====================================================#
#====================================================#

overall_foodtanariWin        = readCSV.loc['foodtanari']['win']

overall_foodtanariDuration   = readCSV.loc['foodtanari']['Duration'].sum().round(2)
overall_foodtanariDate       = readCSV.loc['foodtanari']['Creation'].sum()
overall_foodtanariKills      = readCSV.loc['foodtanari']['kills'].sum()
overall_foodtanariDeaths     = readCSV.loc['foodtanari']['deaths'].sum()
overall_foodtanariAssists    = readCSV.loc['foodtanari']['assists'].sum() 
overall_foodtanariMinions    = readCSV.loc['foodtanari']['Total Minions Killed'].sum()
overall_foodtanariGoldEarned = readCSV.loc['foodtanari']['Gold Earned'].sum()
#====================================================#
#====================================================#
def overall_killsStats():
    if overall_foodtanariKills > overall_kill_stats['mean']:
        return "You are good in kills, Your overall score on kills is above average "
    else:
        return "Your overall score on kills is below average, you should concentrate on kills"
        
def overall_deathsStats():
    if overall_foodtanariDeaths > overall_death_stats['mean']:
        return("Your overall score on deaths is good ")
    else:
        return("Your overall score on deaths is below average, you should focus on deaths")

def overall_assistsStats():
    if overall_foodtanariAssists > overall_assists_stats['mean']:
        return("Your overall score on assists is good ")
    else:
        return("Your overall score on assists is below average, you should focus on it")
        
def overall_minionStats():
    if overall_foodtanariMinions > overall_minons_stats['mean']:
        return("Your overall score on minions is good ")
    else:
        return("Your overall score on minions is below average, you should put more effort on it")

def overall_goldStats():
    if overall_foodtanariGoldEarned > overall_gold_stats['mean']:
        return("Your overall score on Gold Earned is very good ")
    else:
        return("You earned less Gold, you should put more effort on it")
        
def overall_matchResult():
    lose = "Your team need to work hard to win the next match"
    if overall_foodtanariWin == True:
        return('Your team put a good effort and win this match')
    else:
        return(lose)

#===================================================================#    
# Get the data in to the variables
#============================================================+#
#==================================================
plt_goldEarned = plot(goldEarned(), output_type='div')
plt_pieGold = plot(pieGold, output_type='div')

plt_pieDeaths = plot(pieDeaths, output_type='div')
plt_tDeaths = plot(tDeaths(), output_type='div')

plt_pieAssists = plot(pieAssists, output_type='div')
plt_tAssists = plot(tAssists(), output_type='div')

plt_pieKills = plot(pieKills, output_type='div')
plt_tKills = plot(tKills(), output_type='div')

plt_pieMinion = plot(pieMinion, output_type='div')
plt_tMinion = plot(totalMinionsKilled(), output_type='div')
