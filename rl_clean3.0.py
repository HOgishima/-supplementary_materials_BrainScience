#! python3

import csv, os
import sys
import re
import pandas as pd

#os.chdir('.XXXXXXXXX') # select folder here
#os.makedirs('clean', exist_ok=True)

result = pd.DataFrame(columns=['subjID', 'trial', 'choice', 'outcome'])

# CSVファイルのみを探して変数に格納
for (folder, subfolders, files) in os.walk('XXXXXXXX'): # Enter the folder where you stored your reverse learning task data here.
    os.chdir('{}'.format(folder))
    for file in files:
        if not file.endswith('.csv'):
            continue # skip if a file is not .csv

        print('cleaning ' + file + '...')

        # データの整理
        file_delete = pd.read_csv(file,
            usecols=['stim1_posx', 'stim1_posy',
            'stim2_posx','stim2_posy','correctAns', 'faulseAns',
            'key_resp_correct.keys','key_resp_faulse.keys'])
        file_delete = file_delete.dropna(how='all') # 全行空白削除
        file_delete = file_delete.drop([1,2]) # 最初の２行削除

        # 座標をベクトルに
        file_delete.loc[(file_delete['stim1_posx'] == 0) & (file_delete['stim1_posy'] == 200), 'stim1'] = 'up'
        file_delete.loc[(file_delete['stim1_posx'] == 400) & (file_delete['stim1_posy'] == 0), 'stim1'] = 'right'
        file_delete.loc[(file_delete['stim1_posx'] == -400) & (file_delete['stim1_posy'] == 0), 'stim1'] = 'left'
        file_delete.loc[(file_delete['stim1_posx'] == 0) & (file_delete['stim1_posy'] == -200), 'stim1'] = 'down'
        file_delete.loc[(file_delete['stim2_posx'] == 0) & (file_delete['stim2_posy'] == 200), 'stim2'] = 'up'
        file_delete.loc[(file_delete['stim2_posx'] == 400) & (file_delete['stim2_posy'] == 0), 'stim2'] = 'right'
        file_delete.loc[(file_delete['stim2_posx'] == -400) & (file_delete['stim2_posy'] == 0), 'stim2'] = 'left'
        file_delete.loc[(file_delete['stim2_posx'] == 0) & (file_delete['stim2_posy'] == -200), 'stim2'] = 'down'

        # define subjID & trial
        file_delete['subjID'] = '{}'.format(file)
        file_delete['trial'] = list(file_delete.reset_index(drop=True).index+1)

        # define choice
        file_delete.loc[(file_delete['stim1'] == file_delete['key_resp_correct.keys']) |
            (file_delete['stim1'] == file_delete['key_resp_faulse.keys']), 'choice'] = 1
        file_delete.loc[(file_delete['stim2'] == file_delete['key_resp_correct.keys']) |
            (file_delete['stim2'] == file_delete['key_resp_faulse.keys']), 'choice'] = 2

        # define outcome
        file_delete.loc[file_delete['key_resp_correct.keys'] == 'up', 'outcome'] = 1
        file_delete.loc[file_delete['key_resp_correct.keys'] == 'right', 'outcome'] = 1
        file_delete.loc[file_delete['key_resp_correct.keys'] == 'left', 'outcome'] = 1
        file_delete.loc[file_delete['key_resp_correct.keys'] == 'down', 'outcome'] = 1
        file_delete.loc[file_delete['key_resp_correct.keys'] == 'None', 'outcome'] = -1

        # 
        result = result.append(file_delete)

        print(result)

#
result.to_csv('XXXXXXXXXXX',  #Enter the folder in which you want to save the dataset here.
columns=['subjID', 'trial', 'choice', 'outcome'],header=True, index=False, mode='w', sep='\t')

print('completed')
