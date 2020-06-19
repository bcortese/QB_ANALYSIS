# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:01:20 2020

@author: brand
"""

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

root = Tk()
root.title('QB Analysis')
root.geometry("400x250")

#Get players first and last name
labelFirstName = Label(root, text="First Name:").place(x=10, y=40) 
firstName = StringVar()
entryFirstName = Entry(root, textvariable=firstName, width=25, bg="white").place(x=150, y=40) 

#Get players first and last name
labelLastName = Label(root, text="Last Name:").place(x=10, y=60) 
lastName = StringVar()
entryLastName = Entry(root, textvariable=lastName, width=25, bg="white").place(x=150, y=60) 

efficiencyDropDown = StringVar()
efficiencyDropDown.set("Interception efficiency")

efficiencyDropDownList = OptionMenu(root, efficiencyDropDown, "Interception efficiency", "Completion Efficency")
efficiencyDropDownList.place(x = 50, y = 100)


efficiencyDropDownTwo = StringVar()
efficiencyDropDownTwo.set("Down")

efficiencyDropDownListTwo = OptionMenu(root, efficiencyDropDownTwo, "Down",  "Pass Depth", "Run game efficiency")
efficiencyDropDownListTwo.place(x = 250, y = 100)

def interceptionByDown(regularSeasonStatsFinal):
    firstDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==1) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    secondDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==2) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    thirdDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==3) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    fourthDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==4) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    
    interceptionData = [firstDownNumber, secondDownNumber, thirdDownNumber, fourthDownNumber]
    labels = 'first down', 'second down', 'third down', 'fourth down' 
    plt.pie(interceptionData, labels=labels,autopct='%1.1f%%')
    plt.title('QB Interception BreakDown by Down')
    plt.axis('equal')
    plt.show()

def interceptionByPassDepth(regularSeasonStatsFinal):
    shortPassInterceptions = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="short") & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]

    deepPassInterception = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="deep") & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    
    interceptionData = [shortPassInterceptions, deepPassInterception]
    labels = 'Short Pass', 'Deep Pass'
    plt.pie(interceptionData, labels=labels,autopct='%1.1f%%')
    plt.title('QB Interception BreakDown by Pass Depth')
    plt.axis('equal')
    plt.show()

def interceptionResultsWithRunGameEfficiency(regularSeasonStatsFinal, playsData, gameid):
    lowRushYardAvg = []
    highRushYardAvg = []

    for gamestr in gameid:
        runsPerGame = playsData[(playsData["gameId"]==gamestr) & (playsData["playType"]=="rush") & (playsData["possessionTeamId"].isin(regularSeasonStatsFinal["teamId"].unique()))]
        runningPlays =runsPerGame.shape[0]
        totalRushYards = runsPerGame["netYards"].sum()
        rushAvg = totalRushYards/runningPlays 

        if(rushAvg<3.5):     
            lowRushYardAvg.append(gamestr)
        else:
            highRushYardAvg.append(gamestr)  
    lowRunGameInterceptions = regularSeasonStatsFinal[(regularSeasonStatsFinal["gameId"].isin(lowRushYardAvg)) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    highRunGameInterceptions = regularSeasonStatsFinal[(regularSeasonStatsFinal["gameId"].isin(highRushYardAvg)) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]

    interceptionData = [lowRunGameInterceptions, highRunGameInterceptions]
    labels = '< 3.5 yards avg)' , '>3.5 yards avg)'
    plt.pie(interceptionData, labels=labels,autopct='%1.1f%%')
    plt.title('QB Interception BreakDown by Running Efficiency')
    plt.axis('equal')
    plt.show()

    
def completionByDown(regularSeasonStatsFinal):
    totalFirstDownThrows = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==1) & (regularSeasonStatsFinal["passOutcomes"] != "sack")].shape[0]
    firstDownCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==1) & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    firstDownEfficiency = firstDownCompletion/totalFirstDownThrows

    totalScndDownThrows = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==2) & (regularSeasonStatsFinal["passOutcomes"] != "sack")].shape[0]
    scndDownCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==2) & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    scndDownEfficiency = scndDownCompletion/totalScndDownThrows

    totalThirdDownThrows = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==3) & (regularSeasonStatsFinal["passOutcomes"] != "sack")].shape[0]
    thirdDownCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==3) & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    thirdDownEfficiency = thirdDownCompletion/totalThirdDownThrows

    totalFourthDownThrows = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==4) & (regularSeasonStatsFinal["passOutcomes"] != "sack")].shape[0]
    fourthDownCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==4) & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    fourthDownEfficiency = fourthDownCompletion/totalFourthDownThrows
        
    
    x = ['First Down', 'Second Down', 'Third Down', 'Fourth Down']
    performance = [firstDownEfficiency * 100, scndDownEfficiency * 100, thirdDownEfficiency * 100, fourthDownEfficiency * 100]  
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, performance)
    
    plt.ylabel('Completion %')
    plt.title('QB Completion Percentage by Down')
    plt.xticks(x_pos, x)
    
def completionByPassDepth(regularSeasonStatsFinal):
    totalShortThrows = regularSeasonStatsFinal[regularSeasonStatsFinal["passDepth"]=="short"].shape[0]
    shortCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="short") & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    shortEfficiency = shortCompletion/totalShortThrows

    totaldeepThrows = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="deep")].shape[0]
    deepCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="deep") & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    deepEfficiency = deepCompletion/totaldeepThrows
    
    x = ['Short Pass', 'Deep Pass']
    performance = [shortEfficiency * 100, deepEfficiency * 100]  
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, performance)
    
    plt.ylabel('Completion %')
    plt.title('QB Completion Percentage By Pass Depth')
    plt.xticks(x_pos, x)
    

def completionResultsWithRunGameEfficiency(regularSeasonStatsFinal, playsData, gameid):
    lowRushYardAvg = []
    highRushYardAvg = []

    for gamestr in gameid:
        runsPerGame = playsData[(playsData["gameId"]==gamestr) & (playsData["playType"]=="rush") & (playsData["possessionTeamId"].isin(regularSeasonStatsFinal["teamId"].unique()))]
        runningPlays =runsPerGame.shape[0]
        totalRushYards = runsPerGame["netYards"].sum()
        rushAvg = totalRushYards/runningPlays 

        if(rushAvg<3.5):     
            lowRushYardAvg.append(gamestr)
        else:
            highRushYardAvg.append(gamestr)  
    totalThrows = regularSeasonStatsFinal[(regularSeasonStatsFinal["passOutcomes"] != "sack")].shape[0]
    completedPassesLowRush = regularSeasonStatsFinal[(regularSeasonStatsFinal["gameId"].isin(lowRushYardAvg)) & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    completedPassesHighRush = regularSeasonStatsFinal[(regularSeasonStatsFinal["gameId"].isin(highRushYardAvg)) & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    lowRushEfficiency = completedPassesLowRush/totalThrows
    highRushEfficiency =completedPassesHighRush/totalThrows
    
    x = ['Low Run Game', 'High Run Game']
    performance = [lowRushEfficiency * 100, highRushEfficiency * 100]  
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, performance)
    
    plt.ylabel('Completion %')
    plt.title('QB Completion Percentage by Run Efficiency')
    plt.xticks(x_pos, x)



def main():
    #Data files used
    playerCSV = "D://programming//envs//Fun_place//QB_analysys//players//players.csv"
    passerCSV = "D://programming//envs//Fun_place//QB_analysys//passer//passer.csv"
    playsCSV = "D://programming//envs//Fun_place//QB_analysys//plays//plays2//plays.csv"
    gamesCSV = "D://programming//envs//Fun_place//QB_analysys//games.csv"
    
    #Retrieve searched players unique id
    playerData = pd.read_csv(playerCSV, engine='python')
    chosenPlayer= playerData[(playerData['nameFirst']==firstName.get().strip()) & (playerData["nameLast"]==lastName.get().strip())]
    if chosenPlayer.empty:
        messagebox.showwarning(title="Wrong Input", message="Invalid Player, no player found")
        return
    playerId = chosenPlayer["playerId"].to_string(index=False).strip()
    
    #retrieve passer
    passerData =  pd.read_csv(passerCSV, engine='python')
    chosenPasser =  passerData[(passerData["playerId"]==int(playerId)) & (passerData["passNull"]==0)]
    
    #merge all nfl plays data and passer data to create players passing stats
    playsData =  pd.read_csv(playsCSV, engine='python')
    passerStats = pd.merge(chosenPasser,  playsData, on='playId')
    
    gameid = passerStats["gameId"].unique()

    #grab only regular season games
    gamesData =  pd.read_csv(gamesCSV, engine='python')
    regularSeason =  gamesData[gamesData["weekNameAbbr"].str.contains("Week")]
    #merge on the passer stats data frame to only include regular season games.
    regularSeasonStatsFinal = pd.merge(passerStats, regularSeason, on='gameId')
    regularSeasonStatsFinal.to_csv('output_CSV.csv', index=False)
    
    while True:
        if efficiencyDropDown.get()=="Interception efficiency":
            if efficiencyDropDownTwo.get() == "Down":
                interceptionByDown(regularSeasonStatsFinal)
            elif efficiencyDropDownTwo.get() == "Pass Depth":
                interceptionByPassDepth(regularSeasonStatsFinal)
            elif efficiencyDropDownTwo.get() == "Run game efficiency":
                interceptionResultsWithRunGameEfficiency(regularSeasonStatsFinal, playsData, gameid)
            else:
                print("Wrong input selected")
        elif efficiencyDropDown.get()=="Completion Efficency":
            if efficiencyDropDownTwo.get() == "Down":
                completionByDown(regularSeasonStatsFinal)
            elif efficiencyDropDownTwo.get() == "Pass Depth":
                completionByPassDepth(regularSeasonStatsFinal)
            elif efficiencyDropDownTwo.get() == "Run game efficiency":
                completionResultsWithRunGameEfficiency(regularSeasonStatsFinal, playsData, gameid)
            else:
                print("Wrong input selected")
        else:
            print("Wrong input selected")
        break

retrieveData = Button(root, text="Retrieve results", command=lambda: main())
retrieveData.place(x = 175, y = 175)
root.mainloop()        




