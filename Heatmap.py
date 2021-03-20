import os
import pandas as pd
import seaborn as sns; sns.set_theme(color_codes=True)
file_name=os.path.join('folder_path','similarity_res.csv')
df=pd.read_csv(file_name,index_col='ligand') # rows are decoys and columns are edcs
df=df.drop(columns=df.columns[df.isna().all()].tolist()) # removing columns with all na values
df=df.dropna() # removing rows with all na values
heatplt = sns.clustermap(df)
heatplt.savefig(os.path.join('save_folder_path','similarity_heatmap.png'))
