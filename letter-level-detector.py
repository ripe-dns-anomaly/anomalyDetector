#giovane moura  2017-04-21
#giovane.moura@sidn.nl
#this code detects anomalies at letter level -- see README.md

import os
import sys
import pandas as pd
import numpy as np

def letterDetector(infile,outFile):

    #read the input csv file

    df=pd.read_csv(infile,header=True,sep=",")
    medianProbes=df["nProbes"].median()
    sdProbes=df["nProbes"].std()



    return 0



if len(sys.argv)==3:
    letterDetector(sys.argv[1],sys.argv[2])

else:
    print("Usage error: please use :\npython letter-level-detector.py $infile $outfile")