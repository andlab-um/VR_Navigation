import datetime
import time
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def save_file(df, file):
    df['timestamp'] = df['timestamp'].astype(str)
    df.to_excel(file, index=False)


def table_preprocess(file)-> pd.DataFrame:
    data = pd.read_csv(file, header=None)
    data.columns = ["x_pos","y_pos","z_pos","timestamp"]
    # data = data.drop_duplicates(subset=['x_pos','z_pos']).reset_index(drop=True)[2:].reset_index(drop=True)
    data = data.reset_index(drop=True)[2:].reset_index(drop=True)
    data['x_pos'] = data['x_pos'].str.replace(r'(', '').astype("float64")
    data['y_pos'] = data['y_pos'].astype("float64")
    data['z_pos'] = data['z_pos'].str.replace(r')', '').astype("float64")
    # z_pos
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S:%f')
    return data


def gen_total_file(subject_id:int):
    stuck = []
    df = pd.DataFrame(stuck, columns=['sub_ID','index','block','type','stats','listname','x_pos','y_pos','z_pos','timestamp'])

    timeStructList = []
    for dirpath, dirnames, filenames in os.walk(str(subject_id)):
        for filename in filenames:
            if filename.endswith('.csv') and filename.startswith('Player_Position'):
                csv_path = os.path.join(dirpath, filename)
                listname = csv_path.split('\\')[1]
                index = dirpath.split('_')[-1]# 1，2，3，......
                # value, distance = table_preprocess(csv_path)
                if listname != 'Train_0':
                    df2 = table_preprocess(csv_path) # x_pos, y_pos, z_pos, timestamp
                    df2['sub_ID'] = subject_id
                    df2['listname'] = listname
                    df2['index'] = index
                    
                    if 'Memory' in listname:
                        df2['type'] = 'Memory'
                    else:
                        df2['type'] = 'Test'

                    if int(index) > 36:
                        block = 6
                    else:
                        block = (int(index)-1) // 6 + 1
                    df2['block'] = block


                    if 'Space' in listname:
                        df2['stats'] = 'Space'
                    else:
                        df2['stats'] = 'Social'

                    # 构建一条pandas的数据
                    # print(index,listname,value)
                    # df2 = pd.DataFrame([[index,listname, value,distance]], columns=['index','listname','delTime','distance'])
                    df = pd.concat([df,df2])
    df.sort_values(by=['timestamp'], inplace=True)
    return df
# gen_total_file(353)

def gen_trajectory_data(location: str, start_participant:int, end_participant: int):
    '''Location: PosTable'''
    # df = pd.DataFrame(columns=['sub_ID','index','block','type','stats','listname','x_pos','y_pos','z_pos','timestamp'])
    DIR = location

    for subject_id in range(start_participant,end_participant):
        print(subject_id)
        df2 = gen_total_file(subject_id)
        print(df2)
        df2.to_excel(DIR+f'sub_{subject_id}.xlsx',index=False)


if __name__ == '__main__':
    start_participant = 348
    end_participant =  360
    location = 'PosTable/'
    gen_trajectory_data(location=location, start_participant=start_participant, end_participant= end_participant)