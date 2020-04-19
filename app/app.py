import flask
import pandas
import os
from flask import request
from ircm import callThisirc
from bs4 import BeautifulSoup
from flask_cors import CORS
import requests
from hospital import callThisHos
from data1 import callThis
from flask import jsonify as json
app=flask.Flask(__name__)
app_setting=os.getenv("APP_SETTINGS")
app.config.from_object(app_setting)
CORS(app)
app.config["DEBUG"]=True
class Scraper:

    def __init__(self):
        pass
    def returnData(self):
        respond = requests.get('https://www.worldometers.info/coronavirus/').text
        soup = BeautifulSoup(respond, 'lxml')

        globalCases = []
        for each in soup.find_all('div', class_='maincounter-number'):
            i = int(''.join(each.span.text.strip().split(',')))
            globalCases.append(i)

        blockCases_1 = []
        for each in soup.find_all('div',class_='number-table-main'):
            i = int(''.join(each.text.strip().split(',')))
            blockCases_1.append(i)

        blockCases_2 = []
        for each in soup.find_all('span', class_='number-table'):
            i = int(''.join(each.text.strip().split(',')))
            blockCases_2.append(i)

        return {
            'data': {
                'coronaCases': globalCases[0],
                'deaths': globalCases[1],
                'recovered': globalCases[2],
                'activeCase': {
                    'totalInfected': blockCases_1[0],
                    'mildCondition': blockCases_2[0],
                    'critical': blockCases_2[1]
                },
                'closedCase': {
                    'totalSolved': blockCases_1[1],
                    'recovered': blockCases_2[2],
                    'deaths': blockCases_2[3]
                }
            }
        }

  
@app.route("/",methods=["GET"])
def home():
    return json({"data":"This is the Home Page designed by Aashish Peepra. Follow Github www.github.com/aashishpeepra for more.Stay Safe"})
@app.route("/info",methods=["GET"])
def info():
    obj=Scraper()
    output={}
    try:
        output=obj.returnData()
    except:
        output={"data":"Some Error Occured"}
    return json(output)


@app.route("/covidinfo",methods=["GET"])
def covid_info():
    try:
        value=request.args.get("name")
        if value=="covid":
            return json(callThis())
        elif value=="hospital":
            return json(callThisHos())
        elif value=="ircm":
            return json(callThisirc())
        elif value=="patient":
            return json(pandas.read_csv("./IndividualDetails.csv").to_dict())
        elif value=="heatmap":
            return json(pandas.read_csv("./population_india_census2011.csv").to_dict())
        else:
            return json({"data":"Wrong argument aashish didn't coded this"})
    except:
        return json({"data":"Some Error Occured"})
@app.route("/bye",methods=["GET"])
def bye():
    return json({"bye":1})


if __name__=="__main__":
    app.run()