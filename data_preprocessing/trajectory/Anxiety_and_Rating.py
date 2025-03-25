import pandas as pd
import numpy as np
import os

def gen_anxiety_willings_rating(df: pd.DataFrame):
    # df.columns = ['Condition', 'TrialNums', 'Anxious', 'Will']
    df[0] = df[0].str.replace("ExpState:", "")
    df[1] = df[1].str.replace("TrailNum:", "")
    df[2] = df[2].str.replace("Will", "Will:")
    df.columns = ['ExpState', 'Trial', 'Stage']
    df['Anxiety'] = df.apply(lambda row: row['Stage'].split(':')[1] if 'Anxious' in row['Stage'] else None, axis=1)
    df['Will'] = df.apply(lambda row: row['Stage'].split(':')[1] if 'Will' in row['Stage'] else None, axis=1)
    # 删除原始的 'Stage' 列
    df.drop('Stage', axis=1, inplace=True)
    df_combined = df.groupby(['ExpState', 'Trial']).agg(lambda x: x.dropna().tolist()[0] if x.dropna().tolist() else None).reset_index()
    # df_sorted = df.sort_values(by=['Trial'])
    df_combined['Trial'] = df_combined['Trial'].astype(int)
    df_c = df_combined.sort_values(by=['Trial'], ascending=True)
    return df_c


def gen_anxiety_will_xlsx(outfname:str):
    '''Generate xlsx dataset of anxiety and will '''
    folders = [f+'/'+f+'.csv' for f in os.listdir() if os.path.isdir(f) and f.isdigit() ]
    expf = folders[-1]
    print(len(folders))

    df = pd.read_csv(expf, header=None)
    # print(df)
    # gen_anxiety_willings_rating(df)

    datalist = folders
    # with pd.ExcelWriter('Trajectory_Tables/Anxiety_and_Willing_Rate.xlsx') as writer:
    with pd.ExcelWriter(outfname) as writer:
        for datalist_item in datalist:
            print(datalist_item.split('/')[0])
            # exp_data = pd.read_csv(datalist_item)
            try:
                df = pd.read_csv(datalist_item, header=None)
            except Exception as e:
                print(e)
                continue
            merged_df  = gen_anxiety_willings_rating(df)
            print(merged_df)
            merged_df.to_excel(writer, sheet_name=datalist_item.split('/')[0], index=None)


def filter_anxiety_will(infname:str, outfname:str):

    # xlsx = pd.ExcelFile('Trajectory_Tables/Anxiety_and_Willing_Rate.xlsx')
    xlsx = pd.ExcelFile(infname)
        # 使用字典推导式读取所有工作表，并将工作表名称作为 keys
    sheets_dict = {sheet_name: xlsx.parse(sheet_name) 
                for sheet_name in xlsx.sheet_names}

    # 合并所有工作表成一个 DataFrame，并将工作表名称作为新的索引层
    df_combined = pd.concat(sheets_dict, ignore_index=False)

    # 重置索引，将工作表名称从索引转移到 'sub_ID' 列
    df_combined.reset_index(level=0, inplace=True)
    df_combined.rename(columns={'level_0': 'sub_ID'}, inplace=True)
    df_combined.to_excel(outfname,index=None)
    # df_combined.to_excel('Trajectory_Tables/Anxiety_and_Willing_Rate_Merged.xlsx',index=None)

        # print(df_combined)
    return df_combined

def group_anxiety_will(df:pd.DataFrame, outfinalname: str):
    '''get table and group data'''

    # Part_III Merged
    data = df

    new_df = pd.DataFrame(columns=['sub_ID','space anxiety','social anxiety','space will','social will'])
    data
    # nlist = []
    for item in set(data['sub_ID']):
        
        sub_data = data[data['sub_ID'] == item]
        space_subdata = sub_data[sub_data['ExpState'] == 'SpaceNavigation']
        social_subdata = sub_data[sub_data['ExpState']== 'SocialNavigation']
        
        space_anxiety = space_subdata['Anxiety'].mean()
        social_anxiety = social_subdata['Anxiety'].mean()

        space_will = space_subdata['Will'].mean()
        social_will = social_subdata['Will'].mean()

        new_df.loc[len(new_df)] = [item, space_anxiety, social_anxiety, space_will, social_will]

    df_sorted = new_df.sort_values(by='sub_ID')
    # df_sorted.to_excel('Trajectory_Tables/Anxiety_and_Willing_Rate_Grouped.xlsx', index=None)
    df_sorted.to_excel(outfinalname, index=None)



def main():
    participant_start = 302

    target_fname = 'Trajectory_Tables/Anxiety_and_Willing_Rate.xlsx'
    target_fname_filtered = 'Trajectory_Tables/Anxiety_and_Willing_Rate_Merged.xlsx'
    target_fname_grouped = 'Trajectory_Tables/Anxiety_and_Willing_Rate_Grouped.xlsx'

    gen_anxiety_will_xlsx(target_fname)

    filtered_data = filter_anxiety_will(target_fname, target_fname_filtered)

    new_grouped_data = group_anxiety_will(filtered_data, target_fname_grouped)

    return 0


if __name__ == '__main__':
    k = main()


