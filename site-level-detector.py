#giovane moura  2017-04-21
#giovane.moura@sidn.nl
#this code detects anomalies at letter level -- see README.md

import os
import sys
import pandas as pd
import numpy as np

def letterDetector(infile,outFile):

    #read the input csv file

    df=pd.read_csv(infile)

    outputFile=open(outFile,"w")

    #these values below are for the ENTIRE data sample;
    medianProbes=df["nProbes"].median()
    sdProbes=df["nProbes"].std()
    probesThreshold = medianProbes - 3*sdProbes
    probesUpThreshold= medianProbes + 3*sdProbes

    #then now, we need to go line by line and see if it's an anomaly


    for index, row in df.iterrows():
        rownProbes=row["nProbes"]
        #print(str(rownProbes) + "," + str(probesThreshold))
        if rownProbes < probesThreshold :
            outputFile.write("F1 Anomaly at:," + str(row["timestamp"])+"," + str(row["nProbes"])+"\n")
        elif  rownProbes > probesUpThreshold :
            outputFile.write("F3 Anomaly at:," + str(row["timestamp"]) +"," + str(row["nProbes"])+"\n")
    #now, detect F2 types of failures:
            
    medianRTT=df["q50RTT"].median()
    sdRTT=df["q50RTT"].std()
    rttThreshold = medianRTT + 3*sdRTT

    #then now, we need to go line by line and see if it's an anomaly

    for index, row in df.iterrows():
        rowRTT=row["q50RTT"]
        #print(str(rownProbes) + "," + str(probesThreshold))
        if rowRTT > rttThreshold:
            outputFile.write("F2 Anomaly at:," + str(row["timestamp"])+"," +str(row["q50RTT"])+"\n")


if len(sys.argv)==3:
    letterDetector(sys.argv[1],sys.argv[2])

else:
    print("Usage error: please use :\npython letter-level-detector.py $infile $outFile")