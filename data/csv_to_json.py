import pandas as pd
import json

df = pd.read_csv('k-root-ddos-20151130.csv')

df['timestamp'] = df['timestamp']*1000

df_probes = df[['timestamp', 'nProbes']]

df_median_rtt = df[['timestamp', 'q50RTT']]
df_rtt_ranges = df[['timestamp', 'q25RTT', 'q75RTT']]

f = open('reachability.json', 'w')
f.write(df_probes.to_json(orient='values'))

f = open('rtt.json', 'w')
f.write(df_median_rtt.to_json(orient='values'))

f = open('rtt_ranges.json', 'w')
f.write(df_rtt_ranges.to_json(orient='values'))
