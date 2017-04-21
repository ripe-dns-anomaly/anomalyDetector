import pandas as pd
import json

names = ['type', 'timestamp', 'y']
#df = pd.read_csv('k-root-ddos-20151130-ad-hoc.csv', header=None, names=names)
df = pd.read_csv('./site-ddos/k-linx.csv', header=None, names=names)

df['timestamp'] = df['timestamp']*1000

df_probes_anom = df[(df['type']=='F1 Anomaly at:') 
                     | (df['type']=='F3 Anomaly at:')][['timestamp', 'y']]
df_rtt_anom = df[df['type']=='F2 Anomaly at:'][['timestamp', 'y']]

f = open('lhr_reachability_anom.json', 'w')
f.write(df_probes_anom.to_json(orient='values'))

f = open('lhr_rtt_anom.json', 'w')
f.write(df_rtt_anom.to_json(orient='values'))
