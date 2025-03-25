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
#matplotlib.use('WXAgg')
from asrpy import ASR
# import cupy as cp


def gen_epoch(raw):
    # tmin = 0  # 1 second before the event
    # tmax = 31 if int(numfile) < 343 else 61  # 60 seconds after the event
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
    # Assume bad_segments is a list containing the time ranges of bad segments (in seconds)
   
def gen_epoch_mem_reg(raw):
    tmin = -1
    tmax = 2
    events, event_id = mne.events_from_annotations(raw)
    print("Events: ", events)
    print('Event id: ',event_id)




def get_time_analysis(epoch:mne.Epochs, epochdir, fname):
    # Select frequency range 4-30 Hz

    f = h5py.File(epochdir+'/'+fname+'_epoch.h5', 'w')
    # Store the testdata matrix using the Key+dataset method, where the Key is named 'data'
    f.create_dataset(epochdir+'-'+fname, data=epoch.get_data())
    # Close the file
    f.close()

    freqs = np.logspace(*np.log10([4,30]), num=10)
    n_cycles = freqs / 2.
    power = tfr_morlet(epoch, freqs=freqs, n_cycles=n_cycles, use_fft=True, average=False, return_itc = False)
    print(power.data)

    f = h5py.File(epochdir+'/'+fname+'_power.h5', 'w')
    # Store the testdata matrix using the Key+dataset method, where the Key is named 'data'
    f.create_dataset(epochdir+'-'+fname, data=power.data)
    # Close the file
    f.close()

    np.save(epochdir+'/'+fname+'_power.npy', power)


    power, itc = tfr_morlet(epoch, freqs=freqs, n_cycles=n_cycles, use_fft=True, average=True)
    print(power.data.shape)
    # power.get_data()
    np.save(epochdir+'/'+fname+'_power_avg.npy', power)

    f = h5py.File(epochdir+'/'+fname+'_power_avg.h5', 'w')
    # Store the testdata matrix using the Key+dataset method, where the Key is named 'data'
    f.create_dataset(epochdir+'-'+fname, data=power.data)
    # Close the file
    f.close()

    np.save(epochdir+'/'+fname+'_itc.npy', itc)
    f = h5py.File(epochdir+'/'+fname+'_itc.h5', 'w')
    # Store the testdata matrix using the Key+dataset method, where the Key is named 'data'
    f.create_dataset(epochdir+'-'+fname, data=itc.data)
    # Close the file
    f.close()

    # Plot lPFC/rPFC/lTPJ/rTPJ channels
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
    
    # Plot power topomaps for different frequency bands
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
    # Take results from -0.5s to 1.5s
    # And plot results around 10Hz at 0.5s and around 8Hz at 1s
    # power.plot_joint(baseline=(-0.3, -0.1), mode='mean', tmin=-0.5, tmax=1.5,timefreqs=[(0.5, 10), (1, 8)])
    print(epoch.get_data().shape)
    print(epoch.get_data())
    
    return power
    # print(epoch.get_data())

def gen_ASR(raw, raw_rest=None):
    """
    Clean data using ASR.

    Parameters:
    - raw: mne.io.Raw object, task data.
    - raw_rest: optional, mne.io.Raw object, resting state data.

    Returns:
    - raw_asr: Task data cleaned by ASR.
    """
    sfreq = raw.info['sfreq']
    asr = ASR(sfreq)

    # Fit the ASR model using resting state data or task data
    if raw_rest:
        print("Fitting ASR with resting state data...")
        asr.fit(raw_rest)
    else:
        print("No resting state file provided. Fitting ASR with task data...")
        asr.fit(raw)

    # Apply ASR filtering to task data
    print("Applying ASR to task data...")
    raw_asr = asr.transform(raw, mem_splits=15)

    # Compare data before and after processing (optional)
    raw.plot(duration=10, n_channels=33, title='ASR Before...', block=False)
    raw_asr.plot(duration=10, n_channels=33, title='ASR After...', block=True)

    return raw_asr


def getrest(fname: str):
    """
    Get the path to the resting state file corresponding to the task file.

    Parameters:
    - fname: str, task state filename.

    Returns:
    - str: Path to the resting state file, or None if not found.
    """
    try:
        # Get the prefix of the filename, assuming the prefix is the same for resting and task files
        base_name = os.path.basename(fname)[:4]
        restlist = os.listdir('Rest_state_II')

        # Print debugging information
        print(f"Debug: Base name to match: {base_name}")
        print(f"Debug: Available files in Rest_state_II: {restlist}")

        for restitem in restlist:
            # Check if the filename contains the matching prefix
            if base_name in restitem:
                print(f"Debug: Matched resting file: {restitem}")
                return os.path.join('Rest_state_II', restitem)
        print("Debug: No matching resting state file found.")
    except Exception as e:
        print(f"Error in getrest function: {e}")

    return None




def main(file, icaed_name, epoch_dir, asr=False):
    """
    Main function to preprocess task data, including ASR, ICA, manual bad segment selection, event extraction, and saving.

    Parameters:
    - file: str, path to the task data file.
    - icaed_name: str, folder path to save ICA-processed data.
    - epoch_dir: str, folder path to save epoch data.
    - asr: bool, whether to use ASR.
    """
    raw = rsc.read_raw(file)
    print(raw.info)

    # Check if ASR is enabled, ensuring ASR is executed only once per subject
    if asr:
        # Get the corresponding resting state file
        restfile = getrest(file)
        print(f"Debug: Resting state file returned: {restfile}")

        if restfile:
            print(f"Resting state file found: {restfile}")
            raw_rest = rsc.read_raw(restfile)

            # Perform ASR on task data
            raw = gen_ASR(raw, raw_rest)  # ASR processes task data
            print("ASR applied successfully. Moving to ICA...")
        else:
            print("No resting state file found. Skipping ASR.")

    # Data cropping and bad channel interpolation
    print("Interpolating bad channels...")
    raw_cropped = rsc.badchannel_interpolate(raw)

    # Perform ICA and label artifacts
    print("Performing ICA...")
    raw_recons = rsc.ICALabel(raw_cropped)

    # Save ICA-processed data
    ica_save_path = os.path.join(icaed_name, f"{os.path.basename(file).split('.')[0]}-raw.fif")
    print(f"Saving ICA-processed data to {ica_save_path}...")
    rsc.data_Save_fif(raw_recons, icaed_name + '/', os.path.basename(file).split('.')[0] + '-raw')

    # Manually select bad segments
    print("Opening interactive window for manual bad segment selection...")
    raw_recons.plot(start=0, duration=10, n_channels=33, clipping=None, block=True,
                    title=f"Inspect and clean bad segments! Filename: {file}")

    # Extract events and generate epochs
    print("Generating epochs...")
    epoch_recons, fnames = gen_epoch(raw_recons)

    # Save the generated epochs
    print("Saving generated epochs...")
    for number, epoch in enumerate(epoch_recons):
        if epoch:
            epoch_save_path = os.path.join(epoch_dir, fnames[number], f"{os.path.basename(file).split('.')[0]}-epo.fif")
            os.makedirs(os.path.join(epoch_dir, fnames[number]), exist_ok=True)
            print(f"Saving epoch: {epoch_save_path}")
            rsc.data_Save_fif(epoch, os.path.join(epoch_dir, fnames[number]), os.path.basename(file).split('.')[0] + '-epo')

    print(f"Processing complete for {file}.\n")




if __name__ == '__main__':
    task_dir = 'Test'
    icaed_dir = 'Test_ICAed_ASRed'
    epoch_dir = 'Test_Epochs_ASRed'
    use_asr = True  # Enable ASR

    for f in os.listdir(task_dir):
        if f.endswith('.fif'):  # Process only .fif files
            file = os.path.join(task_dir, f)
            print(f"Processing file: {file}")
            main(file, icaed_dir, epoch_dir, asr=use_asr)
        else:
            print(f"Skipping non-FIF file: {f}")