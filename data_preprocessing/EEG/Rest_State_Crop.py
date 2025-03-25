import mne
import os
import numpy as np
from mne.preprocessing import ICA
from mne.time_frequency import tfr_morlet
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from mne_icalabel import label_components
from mne_icalabel.iclabel import iclabel_label_components
import warnings

warnings.filterwarnings('ignore')
matplotlib.use('WXAgg')

import os

if not os.path.exists('Rest_state_II'):
    os.makedirs('Rest_state_II')

def read_raw(filename: str):
    """
    Read raw data from a .fif file.

    Parameters
    ----------
    filename : str
        The name of the .fif file to read.

    Returns
    -------
    mne.io.Raw
        The raw data from the .fif file.
    """
    raw = 0
    if filename.endswith('.fif'):
        raw = mne.io.read_raw_fif(filename, preload=True)
    elif filename.endswith('.set'):
        raw = mne.io.read_raw_eeglab(filename, preload=True)
    else:
        print("ERROR File suffix.Pls check again.")

    # raw.crop(tmin=10.0, tmax=80.0)
    # raw.save(filename, overwrite=True)
    return raw


def crop_state(raw,filename):
    dir = 'Rest_state/'
    raw_cropped = raw.copy()
    
    events, event_id = mne.events_from_annotations(raw_cropped)
    
    if '20' in event_id:

        # tmax = 31 if int(filename[-7:-4]) < 343 else 61  # 事件后60秒
        # raw_cropped.crop(tmin=0, tmax = tmax)
        # raw_cropped.load_data()
        # fig = raw_cropped.plot(start=0, duration=20, n_channels=33,block=True, clipping=None, title = filename)
        # return raw_cropped

        tmin = 0
        fig = raw_cropped.plot(start=0, duration=20, n_channels=33,block=True, clipping=None, title = filename)
        while True:
            s_input = input("Please input start time you want to cut: [Default: 0]:\n")
            if s_input == '':
                break
            elif type(eval(s_input)) == int:
                tmin = eval(s_input)
                break
            else:
                print("Error format of input.\nYou need to input a number or enter as using Default 0 start!")
        
        
        tmax = tmin +60
        while True:
            e_input = input("Please input end time point(not time but time point added with start time) you want to cut: [Default: "+str(tmin)+"+60]:\n")
            if e_input == '':

                break
            elif type(eval(e_input)) == int:

                tmax = eval(e_input)
                break
            else:
                print("Error format of input.\nYou need to input a number or enter as using Default 0 start!")

        raw_cropped.crop(tmin=tmin, tmax = tmax)
        raw_cropped.load_data()
        fig = raw_cropped.plot(start=0, duration=20, n_channels=33,block=True, clipping=None, title = filename)
        
        return raw_cropped




    else:
        # return 0
        tmin = 0
        fig = raw_cropped.plot(start=0, duration=20, n_channels=33,block=True, clipping=None, title = filename)
        while True:
            s_input = input("Please input start time you want to cut: [Default: 0]:\n")
            if s_input == '':
                break
            elif type(eval(s_input)) == int:
                tmin = eval(s_input)
                break
            else:
                print("Error format of input.\nYou need to input a number or enter as using Default 0 start!")
        
        
        tmax = tmin +60
        while True:
            e_input = input("Please input end time point(not time but time point added with start time) you want to cut: [Default: "+str(tmin)+"+60]:\n")
            if e_input == '':
                break
            elif type(eval(e_input)) == int:
                tmax = eval(e_input)
                break
            else:
                print("Error format of input.\nYou need to input a number or enter as using Default 0 start!")

        raw_cropped.crop(tmin=tmin, tmax = tmax)
        raw_cropped.load_data()
        fig = raw_cropped.plot(start=0, duration=20, n_channels=33,block=True, clipping=None, title = filename)
        
        return raw_cropped

#  badchannel_interpolate
def badchannel_interpolate(raw_cropped: mne.io.Raw) -> mne.io.Raw:
    """
    Interpolate bad channels in the raw EEG data and plot the reconstructed data.

    Parameters
    ----------
    raw_cropped : mne.io.Raw
        The cropped raw data with marked bad channels.

    Returns
    -------
    mne.io.Raw
        The raw data after interpolation of bad channels.
    """
    bad_flag = False
    if raw_cropped.info['bads']:
        print('Bad channel clicked: ', raw_cropped.info['bads'], "Now start reconstruction......")
        bad_flag = True
    else:
        print("No bad channel, break reconstruction routine")
        
    if bad_flag:
        raw_cropped.load_data()
        raw_cropped.interpolate_bads()
        raw_cropped.plot(start=0, duration=5, n_channels=33, clipping=None, block=True, title='Bad channel reconstruction completed...')
    return raw_cropped

 

# ICA

def ICALabel(raw, n_components=0):
    """
    Perform Independent Component Analysis (ICA) to identify artifacts in EEG data,
    label the components, exclude non-brain components, and reconstruct the signal.

    Parameters
    ----------
    raw_ref : Raw
        The preprocessed MNE Raw object to perform ICA on.
-
    Returns
    -------
    Raw
        The reconstructed MNE Raw object after artifact removal.

    """
    # ICA
    if n_components == 0:
        print('Default n_component')
        ica = ICA(max_iter='auto', method='picard', random_state=500)
    else:
        ica = ICA(n_components=n_components, max_iter='auto', method='picard', random_state=500)

    raw_for_ica = raw.copy().filter(l_freq=1, h_freq=None)
    ica.fit(raw_for_ica)


    raw.load_data()
    # ica.plot_components()
    # ica.plot_sources(raw_ref, show_scrollbars=True, title = 'Choose deleted item you want: ')
    # plt.show(block=True)
    print(ica)

    ic_labels = label_components(raw, ica, method='iclabel')
    print(ic_labels)
    categories = ['Brain', 'Muscle Artifact', 'Eye Blink', 'Heart Beat', 'Line Noise', 'Channel Noise', 'Other']
    labels_pred_proba = iclabel_label_components(raw, ica, inplace=True)

    labels_df = pd.DataFrame(labels_pred_proba, columns=categories)



    bad_components = []
    for index, row in labels_df.iterrows():
        sorted_indices = row.argsort()[::-1]
        max_idx = sorted_indices[0]
        second_max_idx = sorted_indices[1]

        print(f"ICA{index}")
        for cat, prob in zip(categories, row):
            print(f"{cat}: {prob:.2f}")
        print(f"max: {categories[max_idx]}")
        print(f"second max: {categories[second_max_idx]}")

        other_brain_prob = row['Other'] + row['Brain']
        print(f"Other + Brain: {other_brain_prob:.2f}")
        print()  
    
        if other_brain_prob < 0.65:
            bad_components.append(index)
        else:
            if other_brain_prob < 0.75:
                if categories[max_idx] == 'Other':
                    if second_max_idx - row['Brain']  > 0.05:
                        bad_components.append(index)
                else:
                    if max_idx - row['Brain'] > 0.05:
                        bad_components.append(index)

            
    print('Found bad componet: ', bad_components)
    #########

    # print(ic_labels['labels'])
    # for index,(k, v) in enumerate(zip(ic_labels['labels'], ic_labels['y_pred_proba'])):
    #     print('ICA'+str(index),k,': ',v)

    # labels =  list(set(ic_labels['labels']) | set(bad_components))

    labels =  ic_labels['labels']
    exclude_idx = [idx for idx, label in enumerate(labels) if label not in ['brain', 'other']]
    print('Excluded ICA components: ', exclude_idx)

    exclude_idx =  list(set(exclude_idx) | set(bad_components))

    raw_recons = raw.copy()
    ica.exclude = exclude_idx  # Set the components to be excluded
    
    ica.plot_overlay(raw_recons, exclude=exclude_idx)
    # for pic in exclude_idx:
    #     ica.plot_properties(raw_recons, picks=pic)
    raw_recons = ica.apply(raw_recons)
    
    raw.plot(duration=10, n_channels=33, clipping=None, title='ICA Before......')
    raw_recons.plot(duration=10, n_channels=33, clipping=None, title='ICA After......')

    # return raw_recons
    plt.show(block=True)
    while True:
        ans = input("Do you want to accept this ICA method and continue? (y/n): ")
        if ans == 'y':
            # auto result accepted
            return raw_recons
        elif ans == 'n':
            # iclabel result rejected
            
            raw_recons = raw.copy()
            ica.plot_components()
            print("Exclude Components: ",ica.exclude)
            ica.plot_overlay(raw_recons, exclude=ica.exclude)
            # while True:
            #     manual_idx = input("Input number to choose ICA component to check [0-24 or other option]\n other options to end up: ")
            #     if manual_idx.isdigit():
            #         if int(manual_idx) < 25 and int(manual_idx) >= 0:
            #             ica.plot_properties(raw_recons, picks=[int(manual_idx)])
            #         else:
            #             break
            #     else:
            #         break
            
            ica.plot_sources(raw)
            plt.show(block=True)

            raw_recons = ica.apply(raw_recons)

            raw.plot(duration=10, n_channels=33, clipping=None, title='ICA Before......')
            raw_recons.plot(duration=10, n_channels=33, clipping=None, title='ICA After......', block=True)
            # plt.show(block=True)
            
            nans = input("Accepted or Rejected ICA result? (y/n): ")
            if nans == 'y':
                return raw_recons
            else:
                continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        
def get_time_analysis(epoch:mne.Epochs):
    freqs = np.logspace(*np.log10([4,30]), num=10)
    



def data_Save_fif(raw: mne.Epochs, dir: str, writename: str) -> None:
    """
    Save the epoch data to a file in FIF format.

    Parameters
    ----------
    epoch : mne.Epochs
        The epochs object to save.
    dir : str
        The directory where the file will be saved.
    writename : str
        The name of the file without the extension.

    Returns
    -------
    None
    """
    # raw.save(f"{dir}{writename}.set", overwrite=True)

    raw.save(f"{dir}{writename}.fif", overwrite=True)



# Left-right brain asymmetry differentiation and data processing
def cal_asymmetry(raw_recon, fnamecut, location):
    location = location
    alpha_band = (8, 13)
    left_channels = ['F3','F7','FC5','F5']
    right_channels = ['F4','F8','FC6','F6']
    psd = raw_recon.compute_psd(method="welch", fmin=1, fmax=30, picks="eeg")
    alpha_mask = ((psd.freqs >= 8) & (psd.freqs <= 13))

    def cal_FAA_index(lftch1, lftch2,lftch3,rgtch1, rgtch2, rgtch3):
        print("======== Handle brain asymmetry ========= ")
        lft1 = psd.copy().pick([lftch1]).get_data().squeeze()[alpha_mask] # numpy array
        lft2 = psd.copy().pick([lftch2]).get_data().squeeze()[alpha_mask] # numpy array
        lft3 = psd.copy().pick([lftch3]).get_data().squeeze()[alpha_mask] # numpy array

        
        rgt1 = psd.copy().pick([rgtch1]).get_data().squeeze()[alpha_mask] # numpy array
        rgt2 = psd.copy().pick([rgtch2]).get_data().squeeze()[alpha_mask] # numpy array
        rgt3 = psd.copy().pick([rgtch3]).get_data().squeeze()[alpha_mask] # numpy array

        Fleft = (lft1.sum()+lft2.sum()+lft3.sum())/3
        Fright = (rgt1.sum()+rgt2.sum()+rgt3.sum())/3
        return [Fleft,Fright, (Fleft - Fright) / (Fleft + Fright)]


    def cal_FAA_index_log(lftch1, lftch2,lftch3,rgtch1, rgtch2, rgtch3):
        print("======== Handle brain asymmetry LogData ========= ")
        lft1 = psd.copy().pick([lftch1]).get_data().squeeze()[alpha_mask] # numpy array
        lft2 = psd.copy().pick([lftch2]).get_data().squeeze()[alpha_mask] # numpy array
        lft3 = psd.copy().pick([lftch3]).get_data().squeeze()[alpha_mask] # numpy array

        rgt1 = psd.copy().pick([rgtch1]).get_data().squeeze()[alpha_mask] # numpy array
        rgt2 = psd.copy().pick([rgtch2]).get_data().squeeze()[alpha_mask] # numpy array
        rgt3 = psd.copy().pick([rgtch3]).get_data().squeeze()[alpha_mask] # numpy array

        Fleft = 10*np.log10((lft1.sum()+lft2.sum()+lft3.sum())/3)
        Fright = 10*np.log10((rgt1.sum()+rgt2.sum()+rgt3.sum())/3)
        return (Fleft - Fright) 

    if not os.path.exists(location):
        channel_names = ['sub_id']
        channel_names += raw_recon.info['ch_names']
        channel_names.append('LFC_index')
        channel_names.append('RFC_index')
        channel_names.append('LTPJ_index')
        channel_names.append('RTPJ_index')
        channel_names.append('LFC_AA_index')
        channel_names.append('LFC_AA_index_log')
        channel_names.append('LTPJ_AA_index')
        channel_names.append('LTPJ_AA_index_log')
        whole_channel_welch_data = pd.DataFrame(columns=channel_names)
        whole_channel_welch_data.to_excel(location, index=None)
    whole_channel_welch_data = pd.read_excel(location)
    print('Columns: ',len(whole_channel_welch_data.columns))
    welchlist = [int(fnamecut[1:])]
    print(raw_recon.info['ch_names'])
    for chname_item in range(len(raw_recon.info['ch_names'])):

        print('Channel: ',chname_item)
        ch = psd.copy().pick([chname_item])
        welchlist.append(ch.get_data().squeeze()[alpha_mask].sum())
    # 33 + 8 + 1 = 42
    frontal_cortex_asy = cal_FAA_index('F3','F7','FC5','F4','F8','FC6')
    frontal_cortex_asy_log = cal_FAA_index_log('F3','F7','FC5','F4','F8','FC6')
    tpj_asy = cal_FAA_index('CP5','P7','P3','CP6','P4','P8')
    tpj_asy_log = cal_FAA_index_log('CP5','P7','P3','CP6','P4','P8')

    welchlist.append(frontal_cortex_asy[0])
    welchlist.append(frontal_cortex_asy[1])
    welchlist.append(tpj_asy[0])
    welchlist.append(tpj_asy[1])
    
    welchlist.append(frontal_cortex_asy[-1])
    welchlist.append(frontal_cortex_asy_log)
    welchlist.append(tpj_asy[-1])
    welchlist.append(tpj_asy_log)
    print('Frontal Cortex Asymmetry: ',frontal_cortex_asy, 'TPJ Asymmetry: ',tpj_asy)
    print('Frontal Cortex Asymmetry 10Log10: ',frontal_cortex_asy_log, 'TPJ Asymmetry 10Log10: ',tpj_asy_log)
    print('Len welch data: ',len(welchlist))
    whole_channel_welch_data.loc[len(whole_channel_welch_data)] = welchlist
    
    whole_channel_welch_data.to_excel(location, index=None)



# main



# read_raw(file)
# raw = read_raw(file)
# raw_cropped = raw.copy()
# events, event_id = mne.events_from_annotations(raw_cropped)
# raw_cropped.plot(start=0, duration=20, n_channels=33, clipping=None, title = 'raw')
# ind = np.where(events[:, 2] == event_id["20"])[0].min()
# print(ind)
# start_t = events[ind, 0] -500
# print(start_t)
# raw_cropped.crop(tmin=start_t / 500, tmax = start_t / 500 + 31)
# raw_cropped.load_data()
# raw_cropped.plot(start=0, duration=2, n_channels=33, clipping=None,block=True, title = file)
def main(file):
    raw = read_raw(file)
    raw = crop_state(raw, file)
    if raw:
        raw.plot(start=0, duration=10, n_channels=33, clipping=None,block=True, title = 'Please check the bad channel as well as bad epochs!')
        raw.plot_sensors(ch_type='eeg', show_names=True)
        raw_cropped = badchannel_interpolate(raw)
        # epoch = gen_epoch(raw_cropped, file[-7:-4])
        raw_recons = ICALabel(raw_cropped)
        # Let's not do Epoch yet.
        location = "Rest_state_II/brain_asymmetry.xlsx"
        cal_asymmetry(raw_recons, file[-7:-4],location)
        
        data_Save_fif(raw_recons, 'Rest_state_II/', file[-8:-4])
    else:
        print("Error. No Trigger named 20")



def main_II(file):
    raw = read_raw(file)
    # raw = crop_state(raw, file)
    # raw.plot_sensors(ch_type='eeg', show_names=True)

    if raw:
        raw.plot(start=0, duration=10, n_channels=33, clipping=None,block=True, title = 'Please check the bad channel as well as bad epochs!')
        # raw_cropped = badchannel_interpolate(raw)
        # epoch = gen_epoch(raw_cropped, file[-7:-4])
        # raw_recons = ICALabel(raw_cropped)
        # Let's not do Epoch yet.
        location = "Rest_state_II/brain_asymmetry.xlsx"
        cal_asymmetry(raw, file[-7:-4],location)
        
        # data_Save_fif(raw_recons, 'Rest_state_II/', file[-8:-4])
    else:
        print("Error. No Trigger named 20")


if __name__ == '__main__':
    print("The script starts executing")
    try:
        data_dir = r
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        for f in os.listdir(data_dir):
            if '_nt' not in f and 'xlsx' not in f:
                file_number = int(f[-7:-4])
                if 360 <= file_number < 361:
                    print(f"Processing of files: {f}")
                    file = os.path.join(data_dir, f)
                    main(file)
    except FileNotFoundError as e:
        print("Error: The specified path was not found. Please check if the path is correct.", e)

'''if __name__ == '__main__'.
    # file = 'Rest_state/s346.fif'
    for f in os.listdir('Rest_state_II'):: if '_nt' not in f: # file = 'Rest_state/s346.fif'.
        if '_nt' not in f.
            if 'xlsx' not in f .
                if int(f[-7:-4]) >= 358 and int(f[-7:-4]) < 358.
                    print(int(f[-7:-4]))
                    file = 'Rest_state_II/'+ f
                    print(file)
                    main(file)

# raw_cropped.plot(start=0, duration=20, n_channels=33, clipping=None, title = filename)
# Since some of the data is buggy during the acquisition process, we theoretically need to manually do the Crop culling of the time, where we do this on the generated file.
# 1. manually find the time of the interruption
# 2. raw.crop(start_t = int(input()), end_t = int(input()))
# 3. save the file raw.save(filename, overwrite=True)''''