import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gen_filtered_practice(times_fname: str,outfname:str):


    times_data = pd.read_excel(times_fname)
    times_data['correct_times'] = times_data['correct_times'].astype(str) 
    times_data['practice_times'] = times_data['correct_times'].apply(lambda x: x.count('/')+1)

    dir = 'Practice_Analysis/Pracdata'

    pracdata = pd.DataFrame()
    for csvf in os.listdir(dir):
        if ('.csv' in csvf) :
            pracdata = pd.concat([pracdata,pd.read_csv(dir+'/'+csvf)])

    pracdata = pracdata.dropna(subset=['corr']).loc[:,
                        ['image1','image2','image3','order','participant','textbox_2.text','corr','button.timesOn','date']]
    # pracdata.to_excel('Practice_Analysis/practice_data_filtered.xlsx',index= None)
    pracdata.to_excel(outfname,index= None)
    return pracdata
    

def gen_grouped_practice(in_data: pd.DataFrame, outfname: str):
    # 1. 平均准确率 
    # 2. 平均花费时间 
    # 3. 最后一轮准确率 
    # 4. 最后一轮平均花费时间
    
    df = in_data
    new_df = pd.DataFrame(columns=['sub_ID','correct_mean','time_mean','correct_last_mean','time_last_mean'])

    for item in set(df['participant']):
        # print(item)
        sub_data = df[df['participant'] == item]
        sub_data['timesOnList'] = sub_data['button.timesOn'].apply(lambda x: len(eval(x)))
        sub_data = sub_data[sub_data['timesOnList'] > 2]
        
        sub_data_mean = sub_data['corr'].mean()
        sub_data_timesum = sub_data[sub_data['timesOnList'] == 18]
        tlist = []
        for i in sub_data_timesum['button.timesOn']:
            tlist += eval(i)[2:]

        tmean = sum(tlist)/len(tlist)

        lastdate = sub_data['date'].iloc[-1]
        sub_lastdate_data = sub_data[sub_data['date'] == lastdate]
        sub_data_mean_last = sub_lastdate_data['corr'].mean()
        tlist_last = eval(sub_data['button.timesOn'].iloc[-1])[2:]
        tmean_last = sum(tlist_last)/len(tlist_last)


        new_df.loc[len(new_df)] = [item, 
                                sub_data_mean, tmean, sub_data_mean_last, tmean_last]

    # new_df.to_excel('Psychopy_Tables/Practice_Grouped.xlsx', index=None)
    new_df.to_excel(outfname, index=None)


def process():
    

    target_fname = 'Practice_Analysis/practice_record.xlsx'
    target_fname_filtered = 'Practice_Analysis/practice_data_filtered.xlsx'
    target_fname_grouped = 'Psychopy_Tables/Practice_Grouped.xlsx'

    ndata = gen_filtered_practice(target_fname, target_fname_filtered)

    gen_grouped_practice(ndata, target_fname_grouped)

    return 0


if __name__ == '__main__':
    process()