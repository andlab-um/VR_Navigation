import numpy as np
import mne
import os
import zipfile
from mne.time_frequency import tfr_morlet

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from typing import List, Tuple
import matplotlib
matplotlib.use('TkAgg')
import shutil

def read_raw(filename: str) -> mne.io.Raw:
    """
    Read raw data from a .fif or .set file.

    Parameters
    ----------
    filename : str
        The name of the file to read.

    Returns
    -------
    mne.io.Raw
        The raw data.
    """
    if filename.endswith('.fif'):
        raw = mne.io.read_raw_fif(filename, preload=True)
    elif filename.endswith('.set'):
        raw = mne.io.read_raw_eeglab(filename, preload=True)
    else:
        print("ERROR: File suffix not recognized. Please check the file extension.")
        
    return raw

def locate(raw: mne.io.Raw) -> mne.io.Raw:
    """
    Set the montage for the raw data to the 'standard_1020' system.

    Parameters
    ----------
    raw : mne.io.Raw
        The raw data.

    Returns
    -------
    mne.io.Raw
        The raw data with the montage set.
    """
    raw = mne.add_reference_channels(raw, ref_channels=['FCz'])
    raw.set_montage("standard_1020", on_missing="warn")
    # raw.plot(start=0, duration=5, n_channels=33, clipping=None, block=True, title='Montage set complete...')
    return raw

def filter_data(fname: str, raw_data: mne.io.Raw) -> mne.io.Raw:
    """
    Apply a band-pass filter to the raw data and plot the result.

    Parameters
    ----------
    fname : str
        The file name used for title purposes.
    raw_data : mne.io.Raw
        The raw data to be filtered.

    Returns
    -------
    mne.io.Raw
        The filtered data.
    """
    raw_filter = raw_data.copy()
    raw_filter.filter(l_freq=0.1, h_freq=30, fir_design='firwin')
    # raw_filter.notch_filter(freqs=50, fir_design='firwin')
    # raw_filter.plot_psd(fmax=60)
    raw_filter.plot(start=0, duration=5, n_channels=33, clipping=None, block=True, title=fname + ' | Filter completed...')
    return raw_filter

def reference(raw_data: mne.io.Raw) -> mne.io.Raw:
    """
    Set the EEG reference to the average reference.

    Parameters
    ----------
    raw_data : mne.io.Raw
        The filtered raw data.

    Returns
    -------
    mne.io.Raw
        The data with the reference set.
    """
    raw_ref = raw_data.copy()
    # raw_ref.set_eeg_reference(ref_channels=['TP9', 'TP10'])
    raw_ref.set_eeg_reference('average')
    # raw_ref.plot(start=0, duration=15, n_channels=33, clipping=None, block=True, title='Reference set complete...')
    return raw_ref

def data_Save_fif(raw: mne.io.Raw, writename: str) -> None:
    """
    Save the raw data to a FIF file.

    Parameters
    ----------
    raw : mne.io.Raw
        The raw data.
    writename : str
        The file name without extension.

    Returns
    -------
    None
    """
    print('Saving file at: ', writename + '.fif')
    raw.save(writename + '.fif', overwrite=True)

def move_fif_files(source_dir: str, target_dir: str) -> None:
    """
    Move FIF files from the source directory to the target directory.

    Parameters
    ----------
    source_dir : str
        The source directory.
    target_dir : str
        The target directory.

    Returns
    -------
    None
    """
    os.makedirs(target_dir, exist_ok=True)
    
    for filename in os.listdir(source_dir):
        if filename.endswith('.fif'):
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)
            shutil.move(source_file, target_file)

def main(subID_file: str) -> mne.io.Raw:
    """
    Main function for processing the EEG data.

    Parameters
    ----------
    subID_file : str
        The file path of the subject data.

    Returns
    -------
    mne.io.Raw
        The preprocessed data.
    """
    raw = read_raw(subID_file)
    raw = locate(raw)  # Set montage

    current_sfreq = raw.info['sfreq']
    if current_sfreq != 500:
        print(f"{subID_file}: Current sampling rate is {current_sfreq} Hz. Resampling to 500 Hz.")
        raw.resample(500, npad="auto")

    raw_ref = reference(raw)  # Set reference
    raw_filter = filter_data(subID_file, raw_ref)  # Apply filter
    data_Save_fif(raw_filter, subID_file[:-4])
    return raw_filter

if __name__ == '__main__':
    subID_file_list = ['Set_Data/' + i for i in os.listdir('Set_Data/') if i.endswith('.fif')]
    for file in subID_file_list:
        if file >= 'Set_Data/s':  
            print("Subject ID File: ", file)
            main(file)

    s_dir = 'Set_Data'
    t_dir = 'Preprocessed_Data_FIF_I'
    move_fif_files(s_dir, t_dir)

