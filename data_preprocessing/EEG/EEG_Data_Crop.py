import numpy as np
import mne
import os
import zipfile
from mne.preprocessing import ICA
from mne.time_frequency import tfr_morlet
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from mne_icalabel import label_components
matplotlib.use('WXAgg')

# First cut mode for all data

# File target: data cut conversion datacrop
# filenum ='s347_2'
# raw = mne.io.read_raw_eeglab('Set_Data/'+filenum+'.set', preload=True)
# # raw.plot(start=20, duration=1, n_channels=32, clipping=None, title = 'Bad channel reconstruction completed...')
# events, event_id = mne.events_from_annotations(raw)



def read_raw(filename: str) -> mne.io.Raw:
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
    if filename.endswith('.fif'):
        raw = mne.io.read_raw_fif(filename, preload=True)
    elif filename.endswith('.set'):
        raw = mne.io.read_raw_eeglab(filename, preload=True)
    else:
        print("ERROR File suffix.Pls check again.")
        
    return raw


def data_Save_fif(raw: mne.io.Raw, dir: str,writename: str) :
    """
    Save the Raw data to a file in FIF format.
    Parameters
    ----------
    raw : Raw
        The MNE Raw object containing the data to be saved.
    writename : str
        The name of the file to which the data will be written, without the '.fif' extension.

    Returns
    -------
    NoReturn
        This function does not return a value.
    """
    writename = writename.split('/')[-1]
    name = input("Writename Now: "+ writename + 'If you accept this name,just print enter,\n otherwise print other name: ')

    if name == "":
        raw.save(dir+writename + '.fif', overwrite=True)
    else:
        raw.save(dir+name + '.fif', overwrite=True)


def EEG_Rest_State_Cut(raw, filenum):
    """
    Extracts and crops the rest state period from raw EEG data based on a specific event marker.

    Parameters:
    raw : mne.io.Raw
        The raw EEG data to be processed.

    Returns:
    raw_cropped : mne.io.Raw
        The cropped raw EEG data containing only the rest state period.
    """
    # You need to Manually check the data against the plotted results
    print('================================================\n本部分的功能是对数据进行初步切分，由于被试的数据有特异性，\n需要您针对数据的标记点半自动进行切分\n本部分的切分标准：\nTrigger 20开始，到Trigger 40结束，EEG数据作为Rest State数据\nTrigger 40开始，到Trigger 54结束，EEG数据作为Practice数据\nTrigger从54开始，EEG数据作为Test数据\n================================================')
    print('This part is used to simulate the data splitting process.\nDue to the specifics of the data, Please manually check the data against the plotted results.\n')
    print('Segmentation criteria of this part: \nTrigger 20 to Trigger 40 as Rest State data \nTrigger 40 to Trigger 54 as Practice data \nTrigger starts at 54 as Test data.\n================================================')
    cues = []
    dir = ""

    # different conditions:
    
    events, event_id = mne.events_from_annotations(raw)
    print("Trigger Detection: ")
    print("Trigger 20:  ",'20' in event_id)
    print("Trigger 40: ",'40' in event_id)
    print("Trigger 54: ",'54' in event_id)
    cues.append(1) if '20' in event_id else cues.append(0)
    cues.append(1) if '40' in event_id else cues.append(0)
    cues.append(1) if '54' in event_id else cues.append(0)
    print(cues)

    def crop_rest_state(raw,cues:list, writename):
        '''Trigger 20'''
        raw_cropped = raw.copy()
        events, event_id = mne.events_from_annotations(raw_cropped)
        if sum(cues) == 0:  # Limit cases, no target trigger #
            return raw_cropped
        else:
            
            if cues[0] == 1: # Trigger 20 Exists,No Trigger 40 or 54
                if cues[1] == 0:
                    # Trigger 40 not exists
                    ind = np.where(events[:, 2] == event_id["20"])[0].min()
                    start_t = events[ind, 0] - 500
                    raw_cropped.crop(tmin=start_t / 500)

                else:
                    # Trigger 40 exists
                    ind = np.where(events[:, 2] == event_id["20"])[0].min()
                    start_t = events[ind, 0] - 500
                    ind = np.where(events[:, 2] == event_id["40"])[0].min()
                    end_t = events[ind, 0] - 500
                    raw_cropped.crop(tmin=start_t / 500, tmax=end_t / 500)


            elif cues[1] == 1: # Trigger 20 not exists but 40 exists
                print("Trigger 20 not exists but 40 exists\n")
                ind = np.where(events[:, 2] == event_id["40"])[0].min()
                start_t = events[ind, 0] - 500
                raw_cropped.crop(tmax=start_t / 500)
        raw_cropped.load_data()
        dir = 'Rest_state/'
        data_Save_fif(raw_cropped, dir, writename)

        return raw_cropped

    
    def crop_practice_state(raw,cues:list, writename:str):
        dir = 'Practice/'
        raw_cropped = raw.copy()
        events, event_id = mne.events_from_annotations(raw_cropped)

        if cues[1] == 1: # has trigger 40
            ind = np.where(events[:, 2] == event_id["40"])[0].min()
            start_t = events[ind, 0] - 500
            if cues[2] == 1: # has trigger 54
                print("Has trigger 54")
                ind2 = np.where(events[:, 2] == event_id["54"])[0].min()
                end_t = events[ind2, 0] - 500
                raw_cropped.crop(tmin=start_t / 500, tmax = end_t / 500)
            else: # no trigger 54
                # pass
                raw_cropped.crop(tmin=start_t / 500)
        else:
            if cues[2] == 1: # has trigger 54
                ind = np.where(events[:, 2] == event_id["54"])[0].min()
                start_t = events[ind, 0] - 500
                raw_cropped.crop(tmax=start_t / 500)
            
        data_Save_fif(raw_cropped, dir, writename)
        return
     
    def crop_test_state(raw,cues:list, writename:str):
        dir = 'Test/'
        raw_cropped = raw.copy()
        events, event_id = mne.events_from_annotations(raw_cropped)
        ind = np.where(events[:, 2] == event_id["54"])[0].min()
        start_t = events[ind, 0] - 500
        raw_cropped.crop(tmin=start_t / 500)
        data_Save_fif(raw_cropped, dir, writename)


      # ans = input(“This part is”)
    print("====================\nDefault Choice in suggestion: ",sum(cues)," Choice(s)")
    
    if cues[0] == 1:
        print("Detect: Save as Rest State data\n")
    if cues[1] == 1:
        print("Detect: Save as Practice State data\n")
    if cues[2] == 1:
        print("Detect: Save as Test State data\n")
    if sum(cues) == 0: # In the extreme case, there's no trigger for the target.
        print('No target Trigger Distribution. Please check by yourself.\n')

    raw.plot(start=0, duration=6, n_channels=32, clipping=None,block=True, title = str(filenum)+'| Please Check The Trigger Distribution.A')

    template_choice = ['','1','2','3','12','13','23','123']
    while True:
        res = input("Please choose type of save: (''/1/2/3/12/13/23/123 \n")
        # if res == '4'
        
        if res not in template_choice:
            print("Error response. Please input the correct format of the command.")
        else:
            if res == "":
                print('Auto mode.')
                if sum(cues) == 0: # In the extreme case, there's no trigger for the target.
                    print('No target Trigger Distribution. Please re-check again.\n')
                    continue
                else:
                    if cues[0] == 1:
                        crop_rest_state(raw,cues,filenum)
                    if cues[1] == 1:
                        crop_practice_state(raw,cues,filenum)
                    if cues[2] == 1:
                        crop_test_state(raw, cues,filenum)
                    break
            else:
                if sum(cues) == 0:
                    print("No target Trigger Distribution. Please be cautious.\n")
                    # In this case, just store it directly to the target file
                    if res == '1':
                        dir = 'Rest_state/'
                        data_Save_fif(raw, dir, filenum)
                        break
                    elif res == '2':
                        dir = 'Practice/'
                        data_Save_fif(raw, dir, filenum)
                        break
                    elif res == '3':
                        dir = 'Test/'
                        data_Save_fif(raw, dir, filenum)
                        break
                    else:
                        print("Cannot split into multipul types. Please check again.\n")
                        continue
                    
                else:
                    if '1' in res:
                        print("\n====== Handle Rest State Data.======\n")
                        crop_rest_state(raw,cues,filenum)
                    if '2' in res:
                        print("\n====== Handle Practice Data. ======\n")
                        crop_practice_state(raw,cues,filenum)
                    if '3' in res:
                        print("\n====== Handle Test Data. ======\n")
                        crop_test_state(raw, cues,filenum)
                    break
                # auto crop data

    # crop_rest_state(raw)
    #  Rest State Period: Trigger 20
    #  Practice period:   Trigger 21/40 to 54
    #  Test period: Trigger After 54
    return raw

def main(subID_file):
    raw = read_raw(subID_file)
    EEG_Rest_State_Cut(raw, subID_file[:-4])
    return raw


# Define a function to filter the list 3
def filter_list(lst, target):
    try:
        # Find the index of the target element
        if target == "":
            return lst
        
        index = lst.index(target)
        
    except ValueError:
        # Returns an empty list if the target element does not exist
        return []
    #  Returns the sub-list after the target element
    return lst[index:]

# Call the function to get the filtered list
# filtered_list = filter_list(my_list, target_element)

subID_file_list = ['Preprocessed_Data_FIF_II/' + i  for i in os.listdir('Preprocessed_Data_FIF_II/') if i.endswith('.fif')]

breakpoint = 'Preprocessed_Data_FIF_II/s309.fif'#  Set_Data/s302_2.set

subID_file_list = filter_list(subID_file_list, breakpoint)
print(subID_file_list)


for file in subID_file_list:
    print()
    print("Subject ID File: ", file)
    main(file)


#  ['s305_2']

# raw_cropped.plot(start=20, duration=1, n_channels=32, clipping=None, title = 'Bad channel reconstruction completed...')