import plotly
from plotly.offline import plot
import plotly.graph_objs as go
from SingleMatchDashboard import *
from flask import Flask, request, render_template, session, redirect, current_app, Markup
import os
import numpy as np
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

kda=("{}/{}/{}".format(foodtanariKills,foodtanariDeaths,foodtanariAssists))
overall_kda=("{}/{}/{}".format(overall_foodtanariKills,overall_foodtanariDeaths,overall_foodtanariAssists))

@app.route('/', methods=("POST", "GET"))
def index():
    
    return render_template('home.html',
                            plt_pieGold=plt_pieGold, 
                            plt_goldEarned=plt_goldEarned,
                            plt_pieDeaths=plt_pieDeaths,
                            plt_tDeaths=plt_tDeaths,
                            plt_pieAssists=plt_pieAssists,
                            plt_tAssists=plt_tAssists,
                            plt_pieKills=plt_pieKills,
                            plt_tKills=plt_tKills,
                            plt_pieMinion=plt_pieMinion,
                            plt_tMinion=plt_tMinion,
                            foodtanariDate=foodtanariDate,
                            foodtanariDuration=foodtanariDuration,
                            kda=kda,
                            overall_kda=overall_kda,
                            foodtanariMinions=foodtanariMinions,
                            foodtanariGoldEarned=foodtanariGoldEarned,
                            killsStats=killsStats(),
                            deathsStats=deathsStats(),
                            assistsStats=assistsStats(),
                            minionStats=minionStats(),
                            goldStats=goldStats(),
                            matchResult=matchResult(),
                            overall_killsStats=overall_killsStats(),
                            overall_deathsStats=overall_deathsStats(),
                            overall_assistsStats=overall_assistsStats(),
                            overall_minionStats=overall_minionStats(),
                            overall_goldStats=overall_goldStats(),
                            overall_foodtanariDuration=overall_foodtanariDuration,
                            #overall_foodtanariDate=overall_foodtanariDate(),    
                            overall_foodtanariKills =overall_foodtanariKills,
                            overall_foodtanariDeaths =overall_foodtanariDeaths,
                            overall_foodtanariAssists=overall_foodtanariAssists, 
                            overall_foodtanariMinions=overall_foodtanariMinions, 
                            overall_foodtanariGoldEarned=overall_foodtanariGoldEarned
                            ) 

app.run()
