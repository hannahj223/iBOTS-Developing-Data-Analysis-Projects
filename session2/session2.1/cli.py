import pandas as pd
import argparse
from pathlib import Path

dfs = []

parser = argparse.ArgumentParser(description="find the performance files and merge")

parser.add_argument("in",type=str,help="input path to folder containing csvs")
parser.add_argument("out",type=str,help="output path to csv merged")

args = parser.parse_args()

task_csv_paths = list(Path(args.input.glob('*.csv')))

for i, p in enumerate(task_csv_paths):
    df = pd.read_csv(p)
    dfs.append(df)
    #print(df)


df0 = pd.concat(dfs)
#df0.set_index(0)
#df0.sort_index()
print(df0)





#task_csv_combined = 'C:\\Users\\User\\Documents\\ibots-data-pipelines\\iBOTS-Developing-Data-Analysis-Projects\\session2\\session2.1\\combined_task_data.csv'

# Save DataFrame to CSV
df0.to_csv(args.output, index=False)