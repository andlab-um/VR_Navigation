# %%
import datetime
import time
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# data = pd.read_csv("304/SocialNavigation_Memory_36/Player_Position_20240117_18_08_52_ID_304.csv", header=None)
# data.columns = ["x_axis","y_axis","z_axis","timestamp"]


# # data = data.drop_duplicates(subset=['x_axis','z_axis']).reset_index(drop=True)

# x_pos = data[2:].iloc[:,0].str.replace("(","").astype("float64").reset_index(drop=True)
# y_pos = data[2:].iloc[:,1].reset_index(drop=True)
# z_pos = data[2:].iloc[:,2].str.replace(")","").astype("float64").reset_index(drop=True)
# tiemstep = data[2:].iloc[:,3].reset_index(drop=True)
# # z_pos
# data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S:%f')
# c = data["timestamp"][len(data['timestamp'])-1] - data["timestamp"][0]
# c

# %%
# To get deltatime in each trial each block and each experiment
def cal_distance(data):
    # 欧氏距离
    distance = np.sqrt(data['x_pos'].diff()**2 + data['z_pos'].diff()**2)
    return distance.sum()


def get_DelTime_and_Distance(file):
    data = pd.read_csv(file, header=None)
    data.columns = ["x_pos","y_pos","z_pos","timestamp"]
    # data = data.drop_duplicates(subset=['x_pos','z_pos']).reset_index(drop=True)[2:].reset_index(drop=True)
    data = data[2:].reset_index(drop=True)
    data['x_pos'] = data['x_pos'].str.replace(r'(', '').astype("float64")
    data['y_pos'] = data['y_pos'].astype("float64")
    data['z_pos'] = data['z_pos'].str.replace(r')', '').astype("float64")
    # z_pos
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S:%f')
    # print(data['timestamp'])
    # print(file)
    # print(data['timestamp'])
    c = data["timestamp"][len(data['timestamp'])-1] - data["timestamp"][0]


    # calculate pausing time

    data['paused'] = (data[['x_pos','z_pos']].shift() == data[['x_pos','z_pos']]).all(axis=1)
    # 计算相邻样本之间的时间差
    # 将'paused'列向上移动一行
    data['paused'] = data['paused'].shift(-1).fillna(False)
    data['time_diff'] = data['timestamp'].diff().shift(-1).fillna(0)
    data['time_diff'] = pd.to_timedelta(data['time_diff'])
    data['pausing_time_second'] = data["time_diff"].dt.total_seconds().astype(float)

    pausetimedata = data[data['paused'] == True]


    pausetimesum = pausetimedata['pausing_time_second'].sum()

    distance = cal_distance(data)

    return [c, distance,pausetimesum]


# %%
# make a dict with key: value:
# stuck = []
# df = pd.DataFrame(stuck, columns=['index','listname','delTime', 'distance','pausetimesum'])



# timeStructList = []
# for dirpath, dirnames, filenames in os.walk('310'):
#     for filename in filenames:
#         if filename.endswith('.csv') and filename.startswith('Player_Position'):
#             csv_path = os.path.join(dirpath, filename)
#             listname = csv_path.split('\\')[1]
#             index = dirpath.split('_')[-1]# 1，2，3，......

#             value = get_DelTime_and_Distance(csv_path)[0]
#             distance = get_DelTime_and_Distance(csv_path)[1]
#             pausetimesum = get_DelTime_and_Distance(csv_path)[2]

#             # value, distance = get_DelTime_and_Distance(csv_path) # nav-time and whole distance

#             # 构建一条pandas的数据
#             # print(index,listname,value)
#             df2 = pd.DataFrame([[index,listname, value, distance, pausetimesum]], columns=['index','listname','delTime', 'distance', 'pausetimesum'])
#             df = pd.concat([df,df2])
# df.index = pd.to_numeric(df['index'])
# df = df.sort_index()
# df = df.loc[df["listname"] != "Train_0"]

# # df = df[~(df['distance'] < 100) & (df['delTime'] > pd.Timedelta("0 days 00:05:00"))]
# df = df[df['distance'] >= 20 ]
# df = df.loc[df["delTime"] >= pd.Timedelta("0 days 00:00:05")]
# df = df.loc[df["delTime"] <= pd.Timedelta("0 days 00:10:00")]
# # df = df.loc[df["delTime"] <= pd.Timedelta("0 days 00:05:00")]

# df

# # %%
# df = df.sort_values("delTime")
# df.head()

# %%

def gen_timeTable(subject_id:int):
    stuck = []
    df = pd.DataFrame(stuck, columns=['trialnum','listname','delTime','distance','pausetimesum'])

    timeStructList = []
    for dirpath, dirnames, filenames in os.walk(str(subject_id)):
        for filename in filenames:
            if filename.endswith('.csv') and filename.startswith('Player_Position'):
                csv_path = os.path.join(dirpath, filename)
                listname = csv_path.split('\\')[1]
                index = dirpath.split('_')[-1]# 1，2，3，......

                value = get_DelTime_and_Distance(csv_path)[0]
                distance = get_DelTime_and_Distance(csv_path)[1]
                pausetimesum = get_DelTime_and_Distance(csv_path)[2]
                
                # 构建一条pandas的数据
                # print(index,listname,value)
                df2 = pd.DataFrame([[index,listname, value,distance, pausetimesum]], columns=['trialnum','listname','delTime','distance','pausetimesum'])
                df = pd.concat([df,df2])
    
    df.index = pd.to_numeric(df['trialnum'])
    df = df.sort_index()
    # 去掉练习时的数据
    # print(df)
    df = df.loc[df["listname"] != "Train_0"]
    # df['trial'] = df['listname'].str.split('_')[-1]
    # 剔除5min以上的异常数据
    df = df[df['distance'] >= 20 ]
    df = df.loc[df["delTime"] <= pd.Timedelta("0 days 00:10:00")]
    
    df['delTime_second'] = df["delTime"].dt.total_seconds()
    df['delTime'] = df['delTime'].astype(str)
    df = df[df['delTime_second'] >= 10]

    return df

def get_timeTable_mean(data:pd.DataFrame):
    return data['delTime'].mean()


def gen_merged_navtime(targetfile:str):

    deltime_list = []

    # with pd.ExcelWriter('NavTotalTime.xlsx') as writer:
    df = pd.DataFrame(deltime_list, columns=['sub_ID','listname','delTime','delTime_second','distance','pausetimesum'])

    sublist = [item for item in os.listdir() if item.isdigit()]


    for subject_id in sublist:
        print(subject_id)
        subject_id = int(subject_id)
        df2 = gen_timeTable(subject_id)
        df2['sub_ID'] = subject_id
            # print(get_timeTable_mean(gen_timeTable(subject_id)))
            # df2 = pd.DataFrame([[subject_id,]], columns=['sub_ID','listname','delTime','delTime_second'])
        df = pd.concat([df,df2])
    # print(df)
    df['speed'] = df['distance']/df['delTime_second']

    df['pausetime_percent'] = df['pausetimesum']/ df['delTime_second']
    print('LEN_df:', len(df))
    # df.to_excel('Trajectory_Tables/NavTotalTime_Distance_Merged.xlsx', index=None)


    # df_non_mem = df[~df['listname'].str.contains('Memory')]

    # df_non_mem.sort_values(by='pausetime_percent')


    # %%
    df_filtered = df[df['pausetime_percent'] <= 0.7]
    


    df_filtered['block'] = df_filtered['trialnum'].astype(int) // 6 + 1 
    print(df_filtered)

    df_filtered.to_excel(targetfile, index=None)

    print('LEN: ',len(df_filtered))

    return df_filtered

# %%
def gen_grouped_navtime(df:pd.DataFrame, outgroupname: str):

    new_df = pd.DataFrame(columns=['sub_ID','space_nav_seconds','social_nav_seconds','memory_nav_seconds',
                                'space_nav_distance','social_nav_distance','memory_nav_distance',
                                'space_nav_speed','social_nav_speed','memory_nav_speed',
                                'space_nav_pausetime','social_nav_pausetime','memory_nav_pausetime',
                                'space_nav_pausetime_percent','social_nav_pausetime_percent','memory_nav_pausetime_percent',
                                'block1_nav_seconds','block2_nav_seconds','block3_nav_seconds',
                                'block4_nav_seconds','block5_nav_seconds','block6_nav_seconds',
                                'block1_nav_distance','block2_nav_distance','block3_nav_distance',
                                'block4_nav_distance','block5_nav_distance','block6_nav_distance',
                                'block1_nav_speed','block2_nav_speed','block3_nav_speed',
                                'block4_nav_speed','block5_nav_speed','block6_nav_speed',
                                'block1_nav_pausetime', 'block2_nav_pausetime','block3_nav_pausetime',
                                'block4_nav_pausetime','block5_nav_pausetime','block6_nav_pausetime',
                                'block1_nav_pausetime_percent','block2_nav_pausetime_percent','block3_nav_pausetime_percent',
                                'block4_nav_pausetime_percent','block5_nav_pausetime_percent','block6_nav_pausetime_percent'
                                ])

    for item in set(df['sub_ID']):
        sub_data = df[df['sub_ID'] == item]
        space_subdata = sub_data[sub_data['listname'].str.startswith('SpaceNavigation') & ~sub_data['listname'].str.contains('_Memory')]
        social_subdata = sub_data[sub_data['listname'].str.startswith('SocialNavigation') & ~sub_data['listname'].str.contains('_Memory')]
        memory_subdata = sub_data[sub_data['listname'].str.contains('_Memory')]
        
        sub_data['trialnum'] = pd.to_numeric(sub_data['trialnum'], errors='coerce').fillna(0).astype(int)
        
        block1_data = sub_data[(sub_data['trialnum'] < 6) & (sub_data['trialnum'] > 0)]
        print(block1_data)
        block2_data = sub_data[(sub_data['trialnum'] > 6) & (sub_data['trialnum'] < 12)]
        # print(block2_data)
        block3_data = sub_data[(sub_data['trialnum'] > 12) & (sub_data['trialnum'] < 18)]
        block4_data = sub_data[(sub_data['trialnum'] > 18) & (sub_data['trialnum'] < 24)]
        block5_data = sub_data[(sub_data['trialnum'] > 24) & (sub_data['trialnum'] < 30)]
        block6_data = sub_data[(sub_data['trialnum'] > 30) & (sub_data['trialnum'] < 36)]

        space_time = space_subdata['delTime_second'].mean()
        social_time = social_subdata['delTime_second'].mean()
        memory_time = memory_subdata['delTime_second'].mean()

        space_distance = space_subdata['distance'].mean()
        social_distance = social_subdata['distance'].mean()
        memory_distance = memory_subdata['distance'].mean()

        space_speed = space_subdata['speed'].mean()
        social_speed = social_subdata['speed'].mean()
        memory_speed = memory_subdata['speed'].mean()

        space_pausetime = space_subdata['pausetimesum'].mean()
        social_pausetime = social_subdata['pausetimesum'].mean()
        memory_pausetime = memory_subdata['pausetimesum'].mean()

        space_nav_pausetime_percent = space_subdata['pausetime_percent'].mean()
        social_nav_pausetime_percent = social_subdata['pausetime_percent'].mean()
        memory_nav_pausetime_percent = memory_subdata['pausetime_percent'].mean()

        block1_nav_seconds = block1_data['delTime_second'].mean()
        block2_nav_seconds = block2_data['delTime_second'].mean()
        block3_nav_seconds = block3_data['delTime_second'].mean()
        block4_nav_seconds = block4_data['delTime_second'].mean()
        block5_nav_seconds = block5_data['delTime_second'].mean()
        block6_nav_seconds = block6_data['delTime_second'].mean()

        block1_nav_distance = block1_data['distance'].mean()
        block2_nav_distance = block2_data['distance'].mean()
        block3_nav_distance = block3_data['distance'].mean()
        block4_nav_distance = block4_data['distance'].mean()
        block5_nav_distance = block5_data['distance'].mean()
        block6_nav_distance = block6_data['distance'].mean()

        block1_nav_speed = block1_data['speed'].mean()
        block2_nav_speed = block2_data['speed'].mean()
        block3_nav_speed = block3_data['speed'].mean()
        block4_nav_speed = block4_data['speed'].mean()
        block5_nav_speed = block5_data['speed'].mean()
        block6_nav_speed = block6_data['speed'].mean()    
        
        block1_nav_pausetime = block1_data['pausetimesum'].mean()
        block2_nav_pausetime = block2_data['pausetimesum'].mean()
        block3_nav_pausetime = block3_data['pausetimesum'].mean()
        block4_nav_pausetime = block4_data['pausetimesum'].mean()
        block5_nav_pausetime = block5_data['pausetimesum'].mean()
        block6_nav_pausetime = block6_data['pausetimesum'].mean()

        block1_nav_pausetime_percent = block1_data['pausetime_percent'].mean()
        block2_nav_pausetime_percent = block2_data['pausetime_percent'].mean()
        block3_nav_pausetime_percent = block3_data['pausetime_percent'].mean()
        block4_nav_pausetime_percent = block4_data['pausetime_percent'].mean()
        block5_nav_pausetime_percent = block5_data['pausetime_percent'].mean()
        block6_nav_distance_percent = block6_data['pausetime_percent'].mean()

        new_df.loc[len(new_df)] = [item, space_time, social_time, memory_time,
                                space_distance, social_distance, memory_distance,
                                space_speed, social_speed, memory_speed,
                                space_pausetime,social_pausetime, memory_pausetime,
                                space_nav_pausetime_percent, social_nav_pausetime_percent, memory_nav_pausetime_percent, 
                                block1_nav_seconds, block2_nav_seconds, block3_nav_seconds,
                                block4_nav_seconds, block5_nav_seconds, block6_nav_seconds,
                                block1_nav_distance, block2_nav_distance, block3_nav_distance,
                                block4_nav_distance, block5_nav_distance, block6_nav_distance,
                                block1_nav_speed, block2_nav_speed, block3_nav_speed,
                                block4_nav_speed, block5_nav_speed, block6_nav_speed,
                                block1_nav_pausetime, block2_nav_pausetime, block3_nav_pausetime,
                                block4_nav_pausetime, block5_nav_pausetime, block6_nav_pausetime,
                                block1_nav_pausetime_percent, block2_nav_pausetime_percent, block3_nav_pausetime_percent,
                                block4_nav_pausetime_percent, block5_nav_pausetime_percent, block6_nav_distance_percent
                                ]
        
    new_df['sub_ID'] = new_df['sub_ID'].astype(int)
    # new_df.to_excel('Trajectory_Tables/NavTotalTime_Distance_Grouped.xlsx', index=None)
    new_df.to_excel(outgroupname,index=None)

    return new_df


def process():

    target_fname = 'Trajectory_Tables/NavTotalTime_Distance_Merged.xlsx'
    target_fname_grouped = 'Trajectory_Tables/NavTotalTime_Distance_Grouped.xlsx'

    ndata = gen_merged_navtime(target_fname)

    finaldata = gen_grouped_navtime(ndata, target_fname_grouped)
    # finaldata
    return 0


if __name__ == '__main__':
    process()