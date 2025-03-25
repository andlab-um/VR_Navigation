# %%
import os
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt


# dir = 'approach_interact_leave_time'
# df_demo = pd.read_csv(dir+'/'+os.listdir(dir)[1])

# # get table  block|Approach Speed|Leave Speed
# #  block1 block3 block5

# df_demo['block1'] = df_demo['Trial'] // 6 + 1
# # only 1 3 5 block because spatial navigation
# df_demo = df_demo[df_demo['block1'] % 2 == 1]
# df_demo.head()

# # %%
# # new_df = df_demo.groupby(['block1']).describe()['Approach Speed']['mean'].reset_index()
# # # new_df['B'] = df_demo.groupby(['block1']).describe()['Leave Speed'].reset_index()['mean']
# # new_df

# df_grouped = df_demo.groupby(['block1']).describe().reset_index()
# df_grouped['Approach Speed']['mean']
# df_grouped['Leave Speed']['mean']

# data = pd.DataFrame()
# data['block'] = df_grouped['block1']
# data['Approach_Speed'] = df_grouped['Approach Speed']['mean']
# data['Leave_Speed'] = df_grouped['Leave Speed']['mean']
# data['Approach_Distance'] = df_grouped['Approach Distance']['mean']
# data['Leave_Distance'] = df_grouped['Leave Distance']['mean']


# data['mean_Approach_Distance'] = df_demo['Approach Distance'].mean()
# data['mean_Leave_Distance'] = df_demo['Leave Distance'].mean()
# data['mean_Approach_Speed'] = df_demo['Approach Speed'].mean()
# data['mean_Leave_Speed'] = df_demo['Leave Speed'].mean()

# data

# %%
# column subject_ID 

def gen_space_close_leave_merged(start_participant , end_participant , foutname):

    df = pd.DataFrame()

    dir = 'approach_interact_leave_time'


    for subject_id in range(start_participant,end_participant+1):
        # approach_interact_leave_time_301.csv
        
        df_demo = pd.read_csv(dir+'/approach_interact_leave_time_'+str(subject_id)+'.csv')
        df_demo['block1'] = df_demo['Trial'] // 6 + 1
        # only 1 3 5 block because spatial navigation
        df_demo = df_demo[df_demo['block1'] % 2 == 1]
        

        
        df_grouped = df_demo.groupby(['block1']).describe().reset_index()

        data = pd.DataFrame()

        data['block'] = df_grouped['block1']
        data['Approach_Speed'] = df_grouped['Approach Speed']['mean']
        data['Leave_Speed'] = df_grouped['Leave Speed']['mean']
        data['Approach_Distance'] = df_grouped['Approach Distance']['mean']
        data['Leave_Distance'] = df_grouped['Leave Distance']['mean']


        data['whole_Approach_Distance'] = df_demo['Approach Distance'].mean()
        data['whole_Leave_Distance'] = df_demo['Leave Distance'].mean()
        data['whole_Approach_Speed'] = df_demo['Approach Speed'].mean()
        data['whole_Leave_Speed'] = df_demo['Leave Speed'].mean()

        
        data['pos_Approach_Distance'] = df_demo[df_demo['Reward'] == 1 ]['Approach Distance'].mean()
        data['pos_Leave_Distance'] = df_demo[df_demo['Reward'] == 1 ]['Leave Distance'].mean()
        data['pos_Approach_Speed'] = df_demo[df_demo['Reward'] == 1 ]['Approach Speed'].mean()
        data['pos_Leave_Speed'] = df_demo[df_demo['Reward'] == 1 ]['Leave Speed'].mean()
        data['neg_Approach_Distance'] = df_demo[df_demo['Reward'] == -1 ]['Approach Distance'].mean()
        data['neg_Leave_Distance'] = df_demo[df_demo['Reward'] == -1 ]['Leave Distance'].mean()
        data['neg_Approach_Speed'] = df_demo[df_demo['Reward'] == -1 ]['Approach Speed'].mean()
        data['neg_Leave_Speed'] = df_demo[df_demo['Reward'] == -1 ]['Leave Speed'].mean()



        data['sub_ID'] = subject_id

        df = pd.concat([df,data])
        # df.to_excel('Spatial_Approach_Leave_Distance_Speed_Merged.xlsx', index=False)
        df.to_excel(foutname, index=None)
    return df


# %%
# df[df['sub_ID'] == 302]

def gen_space_close_leave_grouped(df: pd.DataFrame, foutname: str):

    new_df = pd.DataFrame(columns=['sub_ID','Space_Approach_Distance','Space_Leave_Distance','Space_Approach_Speed','Space_Leave_Speed',
                                'Space_block1_Approach_Distance','Space_block1_Leave_Distance','Space_block1_Approach_Speed','Space_block1_Leave_Speed',
                                'Space_block3_Approach_Distance','Space_block3_Leave_Distance','Space_block3_Approach_Speed','Space_block3_Leave_Speed',
                                'Space_block5_Approach_Distance','Space_block5_Leave_Distance','Space_block5_Approach_Speed','Space_block5_Leave_Speed',
                                'pos_Space_Approach_Distance','pos_Space_Leave_Distance','pos_Space_Approach_Speed','pos_Space_Leave_Speed',
                                    'neg_Space_Approach_Distance','neg_Space_Leave_Distance','neg_Space_Approach_Speed','neg_Space_Leave_Speed',
                                ])


    for item in set(df['sub_ID']):
        print(item)
        sub_data = df[df['sub_ID'] == item]

        appproach_distance = sub_data['whole_Approach_Distance'].to_list()[0]
        leave_distance = sub_data['whole_Leave_Distance'].to_list()[0]
        appproach_speed = sub_data['whole_Approach_Speed'].to_list()[0]
        leave_speed = sub_data['whole_Leave_Speed'].to_list()[0]
        
        block1_subdata = sub_data[sub_data['block'] == 1]
        block1_Approach_Distance = block1_subdata['Approach_Distance'].to_list()[0]
        block1_Leave_Distance = block1_subdata['Leave_Distance'].to_list()[0]
        block1_Approach_Speed = block1_subdata['Approach_Speed'].to_list()[0]
        block1_Leave_Speed = block1_subdata['Leave_Speed'].to_list()[0]

        block3_subdata = sub_data[sub_data['block'] == 3]
        block3_Approach_Distance = block3_subdata['Approach_Distance'].to_list()[0]
        block3_Leave_Distance = block3_subdata['Leave_Distance'].to_list()[0]
        block3_Approach_Speed = block3_subdata['Approach_Speed'].to_list()[0]
        block3_Leave_Speed = block3_subdata['Leave_Speed'].to_list()[0]

        block5_subdata = sub_data[sub_data['block'] == 5]

        if block5_subdata.empty:
            block5_Approach_Distance = pd.NA
            block5_Leave_Distance = pd.NA
            block5_Approach_Speed = pd.NA
            block5_Leave_Speed = pd.NA
        else:

            block5_Approach_Distance = block5_subdata['Approach_Distance'].to_list()[0]
            block5_Leave_Distance = block5_subdata['Leave_Distance'].to_list()[0]
            block5_Approach_Speed = block5_subdata['Approach_Speed'].to_list()[0]
            block5_Leave_Speed = block5_subdata['Leave_Speed'].to_list()[0]

        print(block5_subdata['Approach_Distance'].to_list())

        pos_Space_Approach_Distance = sub_data['pos_Approach_Distance'].to_list()[0]
        pos_Space_Leave_Distance = sub_data['pos_Leave_Distance'].to_list()[0]
        pos_Space_Approach_Speed = sub_data['pos_Approach_Speed'].to_list()[0]
        pos_Space_Leave_Speed = sub_data['pos_Leave_Speed'].to_list()[0]

        neg_Space_Approach_Distance = sub_data['neg_Approach_Distance'].to_list()[0]
        neg_Space_Leave_Distance = sub_data['pos_Leave_Distance'].to_list()[0]
        neg_Space_Approach_Speed = sub_data['neg_Approach_Speed'].to_list()[0]
        neg_Space_Leave_Speed = sub_data['neg_Leave_Speed'].to_list()[0]



        new_df.loc[len(new_df)] = [item, appproach_distance, leave_distance, appproach_speed, leave_speed,
                                    block1_Approach_Distance, block1_Leave_Distance, block1_Approach_Speed, block1_Leave_Speed,
                                    block3_Approach_Distance, block3_Leave_Distance, block3_Approach_Speed, block3_Leave_Speed,
                                    block5_Approach_Distance, block5_Leave_Distance, block5_Approach_Speed, block5_Leave_Speed,
                                    pos_Space_Approach_Distance,pos_Space_Leave_Distance,pos_Space_Approach_Speed,pos_Space_Leave_Speed,
                                    neg_Space_Approach_Distance,neg_Space_Leave_Distance,neg_Space_Approach_Speed,neg_Space_Leave_Speed
                                    ]

    new_df['sub_ID'] = new_df['sub_ID'].astype(int)
    new_df['type'] = 'space'
    new_df.to_excel(foutname, index=None)
    return new_df
# new_df


# %%
## Social Navigation Speed Generation

# column subject_ID 

def gen_social_close_leave_merged(start_participant , end_participant , foutname):

    df = pd.DataFrame()

    dir = 'approach_interact_leave_time_social'


    for subject_id in range(start_participant,end_participant):
        # approach_interact_leave_time_301.csv
        
        df_demo = pd.read_csv(dir+'/approach_interact_leave_time_'+str(subject_id)+'.csv')
        df_demo['block1'] = df_demo['Trial'] // 6 + 1
        # only 1 3 5 block because spatial navigation
        df_demo = df_demo[df_demo['block1'] % 2 == 0]
        
        
        df_grouped = df_demo.groupby(['block1']).describe().reset_index()

        data = pd.DataFrame()

        data['block'] = df_grouped['block1']
        data['Approach_Speed'] = df_grouped['Approach Speed']['mean']
        data['Leave_Speed'] = df_grouped['Leave Speed']['mean']
        data['Approach_Distance'] = df_grouped['Approach Distance']['mean']
        data['Leave_Distance'] = df_grouped['Leave Distance']['mean']


        data['whole_Approach_Distance'] = df_demo['Approach Distance'].mean()
        data['whole_Leave_Distance'] = df_demo['Leave Distance'].mean()
        data['whole_Approach_Speed'] = df_demo['Approach Speed'].mean()
        data['whole_Leave_Speed'] = df_demo['Leave Speed'].mean()


        data['pos_Approach_Distance'] = df_demo[df_demo['Reward'] == 1 ]['Approach Distance'].mean()
        data['pos_Leave_Distance'] = df_demo[df_demo['Reward'] == 1 ]['Leave Distance'].mean()
        data['pos_Approach_Speed'] = df_demo[df_demo['Reward'] == 1 ]['Approach Speed'].mean()
        data['pos_Leave_Speed'] = df_demo[df_demo['Reward'] == 1 ]['Leave Speed'].mean()
        data['neg_Approach_Distance'] = df_demo[df_demo['Reward'] == -1 ]['Approach Distance'].mean()
        data['neg_Leave_Distance'] = df_demo[df_demo['Reward'] == -1 ]['Leave Distance'].mean()
        data['neg_Approach_Speed'] = df_demo[df_demo['Reward'] == -1 ]['Approach Speed'].mean()
        data['neg_Leave_Speed'] = df_demo[df_demo['Reward'] == -1 ]['Leave Speed'].mean()


        data['sub_ID'] = subject_id

        df = pd.concat([df,data])

    df.to_excel( foutname, index=False)
    # df.to_excel('Social_Approach_Leave_Distance_Speed_Merged.xlsx', index=False)
    return df

def gen_social_close_leave_grouped(df: pd.DataFrame, foutname: str):

    new_df = pd.DataFrame(columns=['sub_ID','Social_Approach_Distance','Social_Leave_Distance','Social_Approach_Speed','Social_Leave_Speed',
                                'Social_block2_Approach_Distance','Social_block2_Leave_Distance','Social_block2_Approach_Speed','Social_block2_Leave_Speed',
                                'Social_block4_Approach_Distance','Social_block4_Leave_Distance','Social_block4_Approach_Speed','Social_block4_Leave_Speed',
                                'Social_block6_Approach_Distance','Social_block6_Leave_Distance','Social_block6_Approach_Speed','Social_block6_Leave_Speed',
                                'pos_Social_Approach_Distance','pos_Social_Leave_Distance','pos_Social_Approach_Speed','pos_Social_Leave_Speed',
                                'neg_Social_Approach_Distance','neg_Social_Leave_Distance','neg_Social_Approach_Speed','neg_Social_Leave_Speed',
                                ])


    for item in set(df['sub_ID']):
        print(item)
        sub_data = df[df['sub_ID'] == item]

        appproach_distance = sub_data['whole_Approach_Distance'].to_list()[0]
        leave_distance = sub_data['whole_Leave_Distance'].to_list()[0]
        appproach_speed = sub_data['whole_Approach_Speed'].to_list()[0]
        leave_speed = sub_data['whole_Leave_Speed'].to_list()[0]
        
        block2_subdata = sub_data[sub_data['block'] == 2]
        block2_Approach_Distance = block2_subdata['Approach_Distance'].to_list()[0]
        block2_Leave_Distance = block2_subdata['Leave_Distance'].to_list()[0]
        block2_Approach_Speed = block2_subdata['Approach_Speed'].to_list()[0]
        block2_Leave_Speed = block2_subdata['Leave_Speed'].to_list()[0]

        block4_subdata = sub_data[sub_data['block'] == 4]
        block4_Approach_Distance = block4_subdata['Approach_Distance'].to_list()[0]
        block4_Leave_Distance = block4_subdata['Leave_Distance'].to_list()[0]
        block4_Approach_Speed = block4_subdata['Approach_Speed'].to_list()[0]
        block4_Leave_Speed = block4_subdata['Leave_Speed'].to_list()[0]

        block6_subdata = sub_data[sub_data['block'] == 6]

        if block6_subdata.empty:
            block6_Approach_Distance = pd.NA
            block6_Leave_Distance = pd.NA
            block6_Approach_Speed = pd.NA
            block6_Leave_Speed = pd.NA
        else:

            block6_Approach_Distance = block6_subdata['Approach_Distance'].to_list()[0]
            block6_Leave_Distance = block6_subdata['Leave_Distance'].to_list()[0]
            block6_Approach_Speed = block6_subdata['Approach_Speed'].to_list()[0]
            block6_Leave_Speed = block6_subdata['Leave_Speed'].to_list()[0]

        print(block6_subdata['Approach_Distance'].to_list())


        pos_Social_Approach_Distance = sub_data['pos_Approach_Distance'].to_list()[0]
        pos_Social_Leave_Distance = sub_data['pos_Leave_Distance'].to_list()[0]
        pos_Social_Approach_Speed = sub_data['pos_Approach_Speed'].to_list()[0]
        pos_Social_Leave_Speed = sub_data['pos_Leave_Speed'].to_list()[0]

        neg_Social_Approach_Distance = sub_data['neg_Approach_Distance'].to_list()[0]
        neg_Social_Leave_Distance = sub_data['pos_Leave_Distance'].to_list()[0]
        neg_Social_Approach_Speed = sub_data['neg_Approach_Speed'].to_list()[0]
        neg_Social_Leave_Speed = sub_data['neg_Leave_Speed'].to_list()[0]


        new_df.loc[len(new_df)] = [item, appproach_distance, leave_distance, appproach_speed, leave_speed,
                                    block2_Approach_Distance, block2_Leave_Distance, block2_Approach_Speed, block2_Leave_Speed,
                                    block4_Approach_Distance, block4_Leave_Distance, block4_Approach_Speed, block4_Leave_Speed,
                                    block6_Approach_Distance, block6_Leave_Distance, block6_Approach_Speed, block6_Leave_Speed,
                                    pos_Social_Approach_Distance,pos_Social_Leave_Distance,pos_Social_Approach_Speed,pos_Social_Leave_Speed,
                                    neg_Social_Approach_Distance,neg_Social_Leave_Distance,neg_Social_Approach_Speed,neg_Social_Leave_Speed
                                    ]

    new_df['sub_ID'] = new_df['sub_ID'].astype(int)
    new_df['type'] = 'social'


    # new_df
    # new_df.to_excel('Social_Approach_Leave_Distance_Speed_Grouped.xlsx', index=None)
    new_df.to_excel(foutname, index=None)
    return new_df



def process(start_participant, end_participant):

    target_fname_space = 'Trajectory_Tables/Spatial_Approach_Leave_Distance_Speed_Merged.xlsx'
    target_fname_grouped_space = 'Trajectory_Tables/Spatial_Approach_Leave_Distance_Speed_Grouped.xlsx'

    target_fname_social = 'Trajectory_Tables/Social_Approach_Leave_Distance_Speed_Merged.xlsx'
    target_fname_grouped_social = 'Trajectory_Tables/Social_Approach_Leave_Distance_Speed_Grouped.xlsx'

    start_p = start_participant
    end_p = end_participant

    space_merged_data = gen_space_close_leave_merged(start_p, end_p, target_fname_space)
    gen_space_close_leave_grouped(space_merged_data, target_fname_grouped_space)

    social_merged_data = gen_social_close_leave_merged(start_p,end_p, target_fname_social)
    gen_social_close_leave_grouped(social_merged_data,target_fname_grouped_social )


    # finaldata
    return 0


if __name__ == '__main__':
    start = 301
    end = 347
    process(start, end)