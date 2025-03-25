# %%
import pandas as pd
import os
import numpy as np

sub_ID = '302'
rewardlist_csv = [item for item in os.listdir(str(sub_ID)) if item.endswith('RewardList.csv')]
print(rewardlist_csv)
stuck = []
df = pd.DataFrame(stuck, columns=['sub_ID','trial','type','score'])

# 横轴坐标 sub_ID trial trialname score
for item in rewardlist_csv:
    if not 'Train' in item:
        trialnum = int(item.split('_')[-2])
        
        trialtype = item.split('_')[1]
        if 'Memory' in item:
            trialtype += '_Memory'
        file = os.path.join(str(sub_ID),item)
        data= pd.read_csv(file, header=None)
        score = int(data.iloc[-1,0].split(':')[-1])
        df2 = pd.DataFrame([[sub_ID,trialnum, trialtype, score]], columns=['sub_ID','trial','type','score'])
        df2['sub_ID'].astype(int)
        df = pd.concat([df,df2])

df = df.sort_values(by='trial', ascending=True)
df['score'].sum()


# %%
loss = pd.read_excel('Trajectory_Loss_Trial.xlsx')
loss = loss.loc[:len(loss)-1]

print(loss)


# %%
def gen_valid(df, sub_ID):
    subdata = loss[loss['sub_ID'] == sub_ID]
    subdata_reversed = subdata.T.iloc[1:-1]
    subdata_reversed.columns = ['valid']
    subdata_reversed['trial'] = subdata_reversed.index

    # # df['valid'] = subdata_reversed['valid'].to_list()
    subdata_reversed['trial'] = subdata_reversed['trial'].astype(int)

    df_cut = pd.merge(df,subdata_reversed, on='trial', how='left')
    # df = df[df['valid'] == 1]
    return df_cut

gen_valid(df,302)

# %%
# 结合上面的代码，尝试构建一个xlsx 其中sheet_name = 被试的编号 每个表格值如上所示：

# 再建一个xlsx 其中 包含被试编号和奖励总计

def gen_newtabel(sub_ID: str)-> list:
    rewardlist_csv = [item for item in os.listdir(str(sub_ID)) if item.endswith('RewardList.csv')]
    stuck = []
    df = pd.DataFrame(stuck, columns=['sub_ID','trial','type','score'])

    # 横轴坐标 sub_ID trial trialname score
    for item in rewardlist_csv:
        if not 'Train' in item:
            trialnum = int(item.split('_')[-2])
            
            trialtype = item.split('_')[1]
            if 'Memory' in item:
                trialtype += '_Memory'
            file = os.path.join(str(sub_ID),item)
            data= pd.read_csv(file, header=None)
            score = int(data.iloc[-1,0].split(':')[-1])
            df2 = pd.DataFrame([[sub_ID,trialnum, trialtype, score]], columns=['sub_ID','trial','type','score'])
            df = pd.concat([df,df2])
    df = df.sort_values(by='trial', ascending=True)
    score_sum = df['score'].sum()
    print(df.shape)    
    if df.shape[0] > 36:
        print(df)
        print(sub_ID)
    return [df, sub_ID,score_sum]


def gen_merged_reward(targetfile:str):

    whole_score = []
    df_whole_score = pd.DataFrame(whole_score, columns=['sub_ID','trial','type','score','valid'])

    folders = [f for f in os.listdir() if os.path.isdir(f) and f.isdigit()]
    for folditem in folders:
            # print(folditem)
        data = gen_newtabel(folditem)[0]
        sub_ID = gen_newtabel(folditem)[1]
            # print('dis-merged')
            # print(data.shape)
            # print(data)
        data = gen_valid(data,int(sub_ID))
            # print('merged')
            # print(data.shape)
            # print(data)
        score_sum = gen_newtabel(folditem)[2]
            # print(sub_ID)
            # data.to_excel(writer, sheet_name=sub_ID, index=None)
            # print(data)
            # print(sub_ID)
            # print(score_sum)

            # df_whole_score2 = pd.DataFrame([[sub_ID,score_sum]], columns=['sub_ID','score_sum'])
            # print(df_whole_score2)
            # print(data)

        df_whole_score = pd.concat([df_whole_score,data])

            # print(df_whole_score)
            # print(df_whole_score.shape)
    # df_whole_score.to_excel('Reward_Merged.xlsx', index=False)

    df_whole_score = df_whole_score[df_whole_score['valid'] == 1]
    # df_whole_score.to_excel('Reward_Merged.xlsx', index=False)

    df_whole_score.to_excel(targetfile, index=False)

    return df_whole_score

# %%

def gen_grouped_reward(df:pd.DataFrame, outgroupname: str):

    new_df = pd.DataFrame(columns=['sub_ID','space_nav_mean_reward','social_nav_mean_reward','space_nav_sum_reward','social_nav_sum_reward','mean_reward','sum_reward'])

    df_whole_score = df

    for item in set(df_whole_score['sub_ID']):
        
        sub_data = df_whole_score[df_whole_score['sub_ID'] == item]

        space_subdata = sub_data[sub_data['type'].str.startswith('SpaceNavigation') & ~sub_data['type'].str.contains('_Memory')]
        social_subdata = sub_data[sub_data['type'].str.startswith('SocialNavigation') & ~sub_data['type'].str.contains('_Memory')]
        

        space_score = space_subdata['score'].mean()
        social_score = social_subdata['score'].mean()

        space_score_sum = space_subdata['score'].sum()
        social_score_sum = social_subdata['score'].sum()

        score_whole_mean = sub_data[ ~sub_data['type'].str.contains('_Memory')]['score'].mean()
        score_whole_sum = sub_data[ ~sub_data['type'].str.contains('_Memory')]['score'].sum()

        new_df.loc[len(new_df)] = [item, space_score, social_score, 
                                space_score_sum,social_score_sum, score_whole_mean, score_whole_sum]
        

    sorted_df = new_df.sort_values(by='sub_ID').reset_index(drop=True)

    loss2 = pd.read_excel('Trajectory_Loss_Trial.xlsx')
    sorted_df['valid_trials'] = loss2['Sum']


    # sorted_df.to_excel('Reward_Grouped.xlsx', index=None)
    sorted_df.to_excel(outgroupname, index=None)

    return sorted_df


def gen_rate_reward(df: pd.DataFrame, outcsv:str):

    df_sorted = df.sort_values(by='mean_reward', ascending=False)

    # 计算每个等级的数量
    num_values = len(df_sorted)
    num_per_group = num_values // 5

    # # 分配评分
    # df_sorted['avg_reward_rate'] = pd.cut(
    #     range(num_values),
    #     bins=[0, num_per_group, 2 * num_per_group, 3 * num_per_group, 4 * num_per_group, num_values],
    #     labels=[5, 4, 3, 2, 1]
    # )
    # df_sorted_back = df_sorted.sort_values(by='sub_ID', ascending=True)


    # 分成10个等级，使用 labels 参数指定等级标签
    df_sorted['rating'] = pd.cut(
        df_sorted['mean_reward'],
        bins=10,
        labels=[1,2,3,4,5,6,7,8,9,10]
    )

    # 打印结果
    # df_sorted_back.to_csv('scores.csv')
    df_sorted = df_sorted.sort_values(by='sub_ID', ascending=True)
    df_sorted['rating'] = df_sorted['rating'].astype(int) + 10
    df_sorted.to_csv(outcsv,index=False)

    return df_sorted

def process():

    target_fname = 'Trajectory_Tables/Reward_Merged.xlsx'
    target_fname_grouped = 'Trajectory_Tables/Reward_Grouped.xlsx'

    ndata = gen_merged_reward(target_fname)

    finaldata = gen_grouped_reward(ndata, target_fname_grouped)

    gen_rate_reward(finaldata, 'whole_score2.csv')
    # finaldata
    return 0


if __name__ == '__main__':
    process()








# %%
# df_sorted = new_data.sort_values(by='avg_reward', ascending=False)

# # 计算每个等级的数量
# num_values = len(df_sorted)
# num_per_group = num_values // 5

# # # 分配评分
# # df_sorted['avg_reward_rate'] = pd.cut(
# #     range(num_values),
# #     bins=[0, num_per_group, 2 * num_per_group, 3 * num_per_group, 4 * num_per_group, num_values],
# #     labels=[5, 4, 3, 2, 1]
# # )
# # df_sorted_back = df_sorted.sort_values(by='sub_ID', ascending=True)


# # 分成10个等级，使用 labels 参数指定等级标签
# df_sorted['rating'] = pd.cut(
#     df_sorted['avg_reward'],
#     bins=10,
#     labels=[1,2,3,4,5,6,7,8,9,10]
# )

# # 打印结果
# # df_sorted_back.to_csv('scores.csv')
# df_sorted = df_sorted.sort_values(by='sub_ID', ascending=True)
# df_sorted['rating'] = df_sorted['rating'].astype(int) + 10
# df_sorted.to_csv('whole_score.csv',index=False)



