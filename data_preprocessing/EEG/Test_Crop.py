import mne
import os
import numpy as np
import zipfile
from mne.preprocessing import ICA
from mne.time_frequency import tfr_morlet
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from mne_icalabel import label_components
import Rest_State_Crop as rsc
import warnings
import h5py
from mne.time_frequency import AverageTFR
warnings.filterwarnings('ignore')
matplotlib.use('WXAgg')
from asrpy import ASR
# import cupy as cp


def gen_epoch(raw):
    # tmin = 0  # 事件前1秒
    # tmax = 31 if int(numfile) < 343 else 61  # 事件后60秒
    tmin = -1
    tmax = 4
    events, event_id = mne.events_from_annotations(raw)
    print("Events: ", events)
    print('Event id: ',event_id)
    # count = (events[:,2] == 103).sum()
    punishcase_id = 211
    rewardcase_id = 212
    punishava_id = 213
    rewardava_id = 214
    punishman_id = 215
    punishwoman_id = 216
    rewardman_id = 217
    rewardwoman_id = 218
    punishman_id_HRD = 219
    punishwoman_id_HRD = 220
    rewardman_id_HRD = 221
    rewardwoman_id_HRD = 222
    # event_id['103/104/106/108'] = punishcase_id
    # event_id['101/102/105/107'] = rewardcase_id
    # event_id['112/114/117/118'] = punishava_id
    # event_id['111/113/115/116'] = rewardava_id
    # event_id['112/117'] = punishman_id
    # event_id['114/118'] = punishwoman_id
    # event_id['111/116'] = rewardman_id
    # event_id['113/115'] = rewardwoman_id
    # event_id['112/114'] = punishman_id_HRD
    # event_id['117/118'] = punishwoman_id_HRD
    # event_id['111/113'] = rewardman_id_HRD
    # event_id['115/116'] = rewardwoman_id_HRD

    # mne.epochs.combine_event_ids()

    # punishcase_merged_events = mne.merge_events(events, punishcase_merge, punishcase_id)
    # rewardcase_merged_events = mne.merge_events(events, rewardcase_merge, rewardcase_id)
    # punishava_merged_events = mne.merge_events(events, punishava_merge, punishava_id)
    # rewardava_merged_events = mne.merge_events(events, rewardava_merge, rewardava_id)
    # punishman_merged_events = mne.merge_events(events, punishman_merge, punishman_id)
    # punishwoman_merged_events = mne.merge_events(events, punishwoman_merge, punishwoman_id)
    # rewardman_merged_events = mne.merge_events(events, rewardman_merge, rewardman_id)
    # rewardwoman_merged_events = mne.merge_events(events, rewardwoman_merge, rewardwoman_id)
    # punishman_merged_events_HRD = mne.merge_events(events, punishman_merge_HRD, punishman_id_HRD)
    # punishwoman_merged_events_HRD = mne.merge_events(events, punishwoman_merge_HRD, punishwoman_id_HRD)
    # rewardman_merged_events_HRD = mne.merge_events(events, rewardman_merge_HRD, rewardman_id_HRD)
    # rewardwoman_merged_events_HRD = mne.merge_events(events, rewardwoman_merge_HRD, rewardwoman_id_HRD)

    # print(np.where(events[:, 2] == event_id["20"])[0])
    # print(np.where(events[:, 2] == event_id["20"])[0].min())
    # '103','104','106','108'
    p_caselist = ['103','104','106','108']
    r_caselist = ['101','102','105','107']
    caselist = p_caselist + r_caselist
    p_avatarlist_male = ['112','117']
    r_avatarlist_male = ['111','116']
    p_avatarlist_female = ['114','118']
    r_avatarlist_female = ['113','115']
    p_avatarlist_male_HRD = ['112','114']
    r_avatarlist_male_HRD = ['111','113']
    p_avatarlist_female_HRD = ['117','118']
    r_avatarlist_female_HRD = ['115','116']
    p_avatarlist = ['112','114','117','118']
    r_avatarlist = ['111','113','115','116']
    avatarlist = p_avatarlist + r_avatarlist

    # matched_dic = {k:event_id[k] for k in p_caselist if k in event_id }


    def cal_sum_event(nlist, events, event_id:dict):
        """
        Calculate the sum of events based on the given list of event IDs.
        Args:
            nlist (list): A list of event IDs.
            events (numpy.ndarray): A 2D array of events.
            event_id (dict): A dictionary mapping event IDs to their corresponding values.
        Returns:
            int: The sum of events that match the event IDs in the given list.
        """
        cnt = 0
        for item in nlist:
            if item in event_id:
                cnt += (events[:,2] == event_id[item]).sum()
            else:
                cnt += 0
        return cnt

    print("\nCount: Punish Case -->",cal_sum_event(p_caselist, events, event_id))
    print("Count: Reward Case -->",cal_sum_event(r_caselist, events, event_id))
    print("Count: Punish Avatar -->",cal_sum_event(p_avatarlist, events, event_id))
    print("Count: Reward Avatar -->",cal_sum_event(r_avatarlist, events, event_id))

    print()

    # events_dic = {'Punishcase':event_id['103'],
    #               'Punishcase2': event_id['104'],
    #               'Punishcase3':event_id['106'],
    #               'Punishcase4': event_id['108'] }
    actual_events = set(events[:,2])
    print(actual_events)
    p_case_dic = {k:event_id[k] for k in p_caselist if k in event_id}
    r_case_dic = {k:event_id[k] for k in r_caselist if k in event_id}
    p_avatar_dic = {k:event_id[k] for k in p_avatarlist if k in event_id}
    r_avatar_dic = {k:event_id[k] for k in r_avatarlist if k in event_id}
    diclist = [p_case_dic,r_case_dic,p_avatar_dic,r_avatar_dic]
    print(diclist)
    diclistname = ['Punish_Cases','Reward_Cases','Punish_Avatar','Reward_Avatar']
    # events_dic = {key:value for key, value in events_dic.items() if int(value) in actual_events}
    # events_dic = {'CaseTrue':event_id['171'],
    #               'CaseFalse': event_id['172'],
    #               'HumanTrue':event_id['181'],
    #               'HumanFalse': event_id['182'],
    #               'BuldingTrue': event_id['161'],
    #               'BuldingFalse': event_id['162'], 
    #               'MarkTrue':event_id['151'], 
    #               'MarkFalse': event_id['152']  }

    epochlist = []
    
    try:
        epochs = None
        for itemdic in diclist:
            if itemdic == {}:
                epochs = None
                epochlist.append(epochs)
                print('Empty Sub-Epoch')
                continue

            print(itemdic)
            epochs = mne.Epochs(raw, 
                                events=events, 
                                event_id=itemdic, 
                                tmin=tmin, 
                                tmax=tmax, 
                                preload=True, 
                                reject_by_annotation=True, 
                                event_repeated='merge',
                                baseline=(-0.3, -0.1),
                                reject = dict(eeg = 150e-6)
                                )
            # epochs.plot_drop_log()
            print('Get Data Epoch: ',(epochs.get_data() == 0).all())
            # epochs = rsc.badchannel_interpolate(epochs)
        # epochs_combined = mne.epochs.combine_event_ids(epochs, old_event_ids=punishcase_merge, new_event_id={'211':211},copy=True)

            if (epochs.get_data() == 0).all(): # Empty Epoch
                epochs =  None
            else:
                epochs.plot(events = events, title = 'please delete epochs you want.....', block=True)
                
            epochlist.append(epochs)
    except Exception as e:
        # e.with_traceback()
        print('========\nError:',e,'\n========')
    print(epochlist)
    return epochlist,diclistname
    # 假设 bad_segments 是一个列表，其中包含坏段的时间范围（以秒为单位）
   
def gen_epoch_mem_reg(raw):
    tmin = -1
    tmax = 2
    events, event_id = mne.events_from_annotations(raw)
    print("Events: ", events)
    print('Event id: ',event_id)




def get_time_analysis(epoch:mne.Epochs, epochdir, fname):
    # 选取频率 4-30 Hz

    f = h5py.File(epochdir+'/'+fname+'_epoch.h5', 'w')
    # 使⽤Key+dataset的⽅式存储上述testdata矩阵，这⾥Key命名为'data'
    f.create_dataset(epochdir+'-'+fname, data=epoch.get_data())
    # 关闭调⽤
    f.close()

    freqs = np.logspace(*np.log10([4,30]), num=10)
    n_cycles = freqs / 2.
    power = tfr_morlet(epoch, freqs=freqs, n_cycles=n_cycles, use_fft=True, average=False, return_itc = False)
    print(power.data)

    f = h5py.File(epochdir+'/'+fname+'_power.h5', 'w')
    # 使⽤Key+dataset的⽅式存储上述testdata矩阵，这⾥Key命名为'data'
    f.create_dataset(epochdir+'-'+fname, data=power.data)
    # 关闭调⽤
    f.close()

    np.save(epochdir+'/'+fname+'_power.npy', power)


    power, itc = tfr_morlet(epoch, freqs=freqs, n_cycles=n_cycles, use_fft=True, average=True)
    print(power.data.shape)
    # power.get_data()
    np.save(epochdir+'/'+fname+'_power_avg.npy', power)

    f = h5py.File(epochdir+'/'+fname+'_power_avg.h5', 'w')
    # 使⽤Key+dataset的⽅式存储上述testdata矩阵，这⾥Key命名为'data'
    f.create_dataset(epochdir+'-'+fname, data=power.data)
    # 关闭调⽤
    f.close()

    np.save(epochdir+'/'+fname+'_itc.npy', itc)
    f = h5py.File(epochdir+'/'+fname+'_itc.h5', 'w')
    # 使⽤Key+dataset的⽅式存储上述testdata矩阵，这⾥Key命名为'data'
    f.create_dataset(epochdir+'-'+fname, data=itc.data)
    # 关闭调⽤
    f.close()

    # 绘制 lPFC/rPFC/lTPJ/rTPJ 导联
    # power.plot(picks=['F3','F7','FC5'], baseline=(-0.5, 0), mode='logratio', title='auto')
    
    # fig = power.plot(picks=['F4','F8','FC6'], baseline=(-0.3, -0.1), mode='logratio', title='rPFC-mean', combine='mean')
    
    # # fig.savefig(epochdir+'/'+fname+'_rPFC_wave_power.png',dpi=600)
    # fig = power.plot(picks=['CP5','P7','P3'], baseline=(-0.3, -0.1), mode='logratio', title='lTPJ-mean', combine='mean')
    # # fig.savefig(epochdir+'/'+fname+'_lTPJ_wave_power.png',dpi=600)

    # fig = power.plot(picks=['CP6','P4','P8'], baseline=(-0.3, -0.1), mode='logratio', title='rTPJ-mean', combine='mean')
    # fig.savefig(epochdir+'/'+fname+'_rTPJ_wave_power.png',dpi=600)
    # fig = power.plot(picks=['F3','F7','FC5'], baseline=(-0.3, -0.1), mode='logratio', title='lPFC-mean', combine='mean')
    # fig.savefig(epochdir+'/'+fname+'_lPFC_wave_power.png',dpi=600)
    # power.plot_topo(baseline=(-0.3, -0.1), mode='logratio', title='Average power')
    
    # 绘制不同频率的power拓扑图
    # theta power
    fig = power.plot_topomap(tmin=0, tmax=0.5, fmin=4, fmax=8,baseline=(-0.3, -0.1), mode='logratio')
    fig.savefig(epochdir+'/'+fname+'_theta_wave_power.png',dpi=600)
    # alpha power
    fig=power.plot_topomap(tmin=0, tmax=0.5, fmin=8, fmax=13,baseline=(-0.3, -0.1), mode='logratio')
    fig.savefig(epochdir+'/'+fname+'_alpha_wave_power.png',dpi=600)
    # beta power
    fig = power.plot_topomap(tmin=0, tmax=0.5, fmin=13, fmax=30,baseline=(-0.3, -0.1), mode='logratio')
    fig.savefig(epochdir+'/'+fname+'_beta_wave_power.png',dpi=600)

    bands = [(4, 8, 'Theta'), (8, 13, 'Alpha'), (13, 30, 'Beta')]
    epoch.plot_psd_topomap(bands=bands, vlim='joint')

    # itc.plot_topo(baseline=(-0.5, 0), mode='logratio', title='Average Inter-Trial coherence')
    # 取-0.5s⾄1.5s的结果
    # 并绘制0.5s时10Hz左右的结果和1s时8Hz左右的结果
    # power.plot_joint(baseline=(-0.3, -0.1), mode='mean', tmin=-0.5, tmax=1.5,timefreqs=[(0.5, 10), (1, 8)])
    print(epoch.get_data().shape)
    print(epoch.get_data())
    
    return power
    # print(epoch.get_data())

def gen_ASR(raw, raw_rest=None):

    # 提取数据和采样率
    sfreq = raw.info['sfreq']

    # 初始化ASR对象
    asr = ASR(sfreq)

    # 使用 GPU 进行 ASR 训练
    # with cp.cuda.Device(0):
    if raw_rest:
        print("Has Resting File")
        asr.fit(raw_rest)  # 传递 mne.io.Raw 对象
    else:
        print("No fit file.")
        asr.fit(raw)  # 传递 mne.io.Raw 对象

    # 运行ASR预处理
    # with cp.cuda.Device(0):
    raw_asr = asr.transform(raw,mem_splits=15)  # 传递 mne.io.Raw 对象
    
    raw.plot(duration=10, n_channels=33, clipping=None, title='ASR Before......')
    raw_asr.plot(duration=10, n_channels=33, clipping=None, title='ASR After......', block=True)
    # plt.show(block=True)
    return raw_asr

def gen_asr_task(raw):
    sfreq = raw.info['sfreq']
    asr = ASR(sfreq)
    asr.fit(raw)

    raw_asr = asr.transform(raw,mem_splits=15)  # 传递 mne.io.Raw 对象
    # raw.plot(title='ASR Before......')
    # raw_asr.plot(title='ASR After......',block=True)
    print('ASR Generated...')
    return raw_asr



def getrest(fname:str):
    
    restlist = os.listdir('Rest_state_II')
    for restitem in restlist :
        if fname.split('/')[1][0:4] in restitem :
            return "Rest_state_II/"+restitem
        
    return 0 


def main(file, icaed_name, epoch_dir, asr=False):
    raw = rsc.read_raw(file)
    print(raw.info)

    # restfile = getrest(file)

    # if restfile != 0 :
    #     raw_rest = rsc.read_raw(restfile)
    #     raw = gen_ASR(raw,raw_rest)

    
    # raw.plot_psd(fmax=60)
    # raw.plot(start=0, duration=25, n_channels=33, clipping=None,block=True, title = 'Please check the bad channel as well as bad epochs! Filename: '+file)
    
    # 读取原始 EEG 数据

    raw.plot(start=0, duration=20, n_channels=33, clipping=None,block=True, title = 'Please check the bad channel as well as bad epochs! Filename: '+file)
    # 打印检测到的坏导联
    raw_cropped = rsc.badchannel_interpolate(raw)

    if asr == True:
        raw_cropped = gen_asr_task(raw_cropped)



    raw_recons = rsc.ICALabel(raw_cropped)

    # raw_recons = raw_cropped
    ## 做完 ICA 后先存储一组到Test_Triggered文件夹中
    # rsc.data_Save_fif(raw_recons, 'Test_Triggered/', file.split('/')[1].split('.')[0])
    # epoch_recons = rsc.gen_epoch(raw_recons, file[-7:-4])
    # 'Test/s301_2.xdf'
    # file.split('/')[1].split('.')[0]
    # raw_recons = rsc.filter(raw_recons)

    # icaed_name = 'Test_ASRed_ICAed
    print(icaed_name)
    print(file.split('/')[1].split('.')[0]+'-raw')
    rsc.data_Save_fif(raw_recons, icaed_name + '/', file.split('/')[1].split('.')[0]+'-raw')



    # 设置新的采样率
    # new_sampling_rate = 500  # 以Hz为单位
    # 对Raw数据进行重新采样
    # raw_recons = raw_recons.resample(new_sampling_rate)
    # print(1/0)
    epoch_recons, fnames = gen_epoch(raw_recons)
    
    print('Len: ', len(epoch_recons))
    for number in range(len(fnames)):
        print(epoch_recons)
        if epoch_recons[number]:
        # rsc.cal_asymmetry(epoch_recons[number], fnames[number],location = "Test_Triggered/brain_asymmetry.xlsx")
            # get_time_analysis(epoch_recons[number],'Test_Triggered/'+fnames[number]+'/',file.split('/')[1].split('.')[0])
            # file.split('/')[1].split('.')[0][1:]

        # epoch_dir
            print(epoch_recons[number], epoch_dir + '/'+fnames[number]+'/', file.split('/')[1].split('.')[0]+'-epo')
            rsc.data_Save_fif(epoch_recons[number], epoch_dir + '/'+fnames[number]+'/', file.split('/')[1].split('.')[0]+'-epo')

    
    # rsc.cal_asymmetry(epoch_recons, file[-7:-4],location = "Test_Triggered/brain_asymmetry.xlsx")
    # rsc.data_Save_fif(epoch_recons, 'Test_Triggered/', file[-8:-4])


if __name__ == '__main__':
    # Test 需要处理不同的情况 接触箱子/人的trigger 是不同的，所以要做一定的归纳和规划

    for f in os.listdir('Test'):
        if 'xlsx' not in f :
            if f.split('.')[0][1:] >= '340' and f.split('.')[0][1:] < '348':

                # print(f.split('.')[0][1:]) # Example: 330_2
                file = 'Test/'+ f
                # print(file.split('/')[1].split('.')[0]) # Example: s330_2
                # print(file) # Example:Test_ICAed/s330_2.fif
                main(file, 'Test_ICAed', 'Test_Epochs', asr=False)
                main(file, 'Test_ICAed_ASRed','Test_Epochs_ASRed', asr=True)



    # main('Test_ICAed/s330_2.fif')