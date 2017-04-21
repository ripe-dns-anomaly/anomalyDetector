import pandas as pd
import json

names = ['type', 'timestamp', 'y']
df = pd.read_csv('k-root-ddos-20151130-ad-hoc.csv', header=None, names=names)

df['timestamp'] = df['timestamp']*1000

df_probes_anom = df[df['type']=='F1 Anomaly at:'][['timestamp', 'y']]
df_rtt_anom = df[df['type']=='F2 Anomaly at:'][['timestamp', 'y']]

f = open('reachability_anom.json', 'w')
f.write(df_probes_anom.to_json(orient='values'))

f = open('rtt_anom.json', 'w')
f.write(df_rtt_anom.to_json(orient='values'))
