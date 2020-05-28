# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:01:20 2020

@author: brand
"""

import pandas as pd
import matplotlib.pyplot as plt



def interceptionByDown(regularSeasonStatsFinal):
    firstDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==1) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    secondDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==2) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    thirdDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==3) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    fourthDownNumber = regularSeasonStatsFinal[(regularSeasonStatsFinal["down"]==4) & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    
    interceptionData = [firstDownNumber, secondDownNumber, thirdDownNumber, fourthDownNumber]
    labels = 'first down', 'second down', 'third down', 'fourth down' 
    plt.pie(interceptionData, labels=labels,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

def interceptionByPassDepth(regularSeasonStatsFinal):
    shortPassInterceptions = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="short") & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]

    deepPassInterception = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="deep") & (regularSeasonStatsFinal["passOutcomes"]=="interception")].shape[0]
    
    interceptionData = [shortPassInterceptions, deepPassInterception]
    labels = 'Short Pass', 'Deep Pass'
    plt.pie(interceptionData, labels=labels,autopct='%1.1f%%')
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
    labels = 'Low Run Game (< 3.5 yards avg)' , 'High Run Game (>3.5 yards avg)'
    plt.pie(interceptionData, labels=labels,autopct='%1.1f%%')
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
    plt.title('QB Completion Percentage')
    plt.xticks(x_pos, x)
    
def completionByPassDepth(regularSeasonStatsFinal):
    totalFirstDownThrows = regularSeasonStatsFinal[regularSeasonStatsFinal["passDepth"]=="short"].shape[0]
    firstDownCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="short") & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    firstDownEfficiency = firstDownCompletion/totalFirstDownThrows

    totalScndDownThrows = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="deep")].shape[0]
    scndDownCompletion = regularSeasonStatsFinal[(regularSeasonStatsFinal["passDepth"]=="deep") & (regularSeasonStatsFinal["passOutcomes"]=="complete")].shape[0]
    scndDownEfficiency = scndDownCompletion/totalScndDownThrows
    
    x = ['Short Pass', 'Deep Pass']
    performance = [firstDownEfficiency * 100, scndDownEfficiency * 100]  
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, performance)
    
    plt.ylabel('Completion %')
    plt.title('QB Completion Percentage')
    plt.xticks(x_pos, x)
    





def main():
    #Data files used
    playerCSV = "D://programming//envs//Fun_place//QB_analysys//players//players.csv"
    passerCSV = "D://programming//envs//Fun_place//QB_analysys//passer//passer.csv"
    playsCSV = "D://programming//envs//Fun_place//QB_analysys//plays//plays.csv"
    gamesCSV = "D://programming//envs//Fun_place//QB_analysys//games.csv"
    
    firstName = input("Please enter QB's first Name. ")
    lastName = input("Please enter QB's last Name. ")
    #Retrieve searched players unique id
    playerData = pd.read_csv(playerCSV, engine='python')
    chosenPlayer= playerData[(playerData['nameFirst']==firstName.strip()) & (playerData["nameLast"]==lastName.strip())]
    if chosenPlayer.empty:
        print("Selected player not found!")
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
        firstPrompt = input("Would you like to see QB's 1. Interception efficiency 2. Completion Efficency? (Select 1 or 2) ")
        if firstPrompt=="1":
            secondPrompt = input("Interception efficiency 1. Based on Down? 2. Based on pass depth? 3. Based on run game efficiency? (Select 1,2,3) ")
            if secondPrompt == "1":
                interceptionByDown(regularSeasonStatsFinal)
            elif secondPrompt == "2":
                interceptionByPassDepth(regularSeasonStatsFinal)
            elif secondPrompt == "3":
                interceptionResultsWithRunGameEfficiency(regularSeasonStatsFinal, playsData, gameid)
            else:
                print("Wrong input selected")
        elif firstPrompt=="2":
            secondPrompt = input("Completion Efficency based on 1. Down? 2. Pass Depth (Select 1 or 2) ")
            if secondPrompt == "1":
                completionByDown(regularSeasonStatsFinal)
            elif secondPrompt == "2":
                completionByPassDepth(regularSeasonStatsFinal)
        
if __name__== "__main__":
   main() 




