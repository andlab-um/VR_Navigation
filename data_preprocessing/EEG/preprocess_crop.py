import mne
import os
import numpy as np
import Rest_State_Crop as rsc  # Assuming this module provides cropping parameters if needed
import matplotlib.pyplot as plt

def filter_data(raw_cropped: mne.io.Raw) -> mne.io.Raw:
    """
    Apply band-pass (and optionally notch) filtering to the raw EEG data and plot the results.

    Parameters
    ----------
    raw_cropped : mne.io.Raw
        The cropped raw data to be filtered.

    Returns
    -------
    mne.io.Raw
        The filtered EEG data.
    """
    raw_cropped.plot(start=0, duration=20, n_channels=33, clipping=None, title='Before Filtering...')
    raw_filter = raw_cropped.copy()
    raw_filter.filter(l_freq=0.1, h_freq=20, fir_design='firwin')
    # To apply a notch filter at 50 Hz, uncomment the following line:
    # raw_filter.notch_filter(freqs=50, fir_design='firwin')
    raw_filter.plot_psd(fmax=60)
    raw_filter.plot(start=0, duration=20, n_channels=33, clipping=None, block=True, title='After Filtering...')
    return raw_filter

def read_raw(filename: str) -> mne.io.Raw:
    """
    Read raw EEG data from a .fif, .set, or .edf file.

    Parameters
    ----------
    filename : str
        The file name of the EEG data.

    Returns
    -------
    mne.io.Raw
        The raw EEG data.
    """
    if filename.endswith('.fif'):
        raw = mne.io.read_raw_fif(filename, preload=True)
    elif filename.endswith('.set'):
        raw = mne.io.read_raw_eeglab(filename, preload=True)
    elif filename.endswith('.edf'):
        raw = mne.io.read_raw_edf(filename, preload=True)
    else:
        raise ValueError("ERROR: File extension not recognized. Please check the file extension.")
    
    print("Loaded file:", filename)
    raw.plot_psd(fmax=60)
    raw.plot(start=0, duration=15, n_channels=33, block=True, title=filename)
    
    # Optionally crop the raw data using predefined tmin and tmax values.
    # For example, these values might be provided by the Rest_State_Crop module.
    # Uncomment and modify the following lines if cropping is desired:
    # tmin, tmax = rsc.get_crop_times(raw)
    # raw = raw.copy().crop(tmin=tmin, tmax=tmax)
    
    return raw

def remove_flat_segments(raw: mne.io.Raw, flat_threshold: float = 1e-12, min_duration: float = 1.0) -> mne.io.Raw:
    """
    Remove flat segments from the raw EEG data.
    
    A flat segment is defined here as a continuous period where the standard deviation
    across all channels is below a specified threshold for at least min_duration seconds.
    
    Parameters
    ----------
    raw : mne.io.Raw
        The raw EEG data.
    flat_threshold : float, optional
        The threshold for the standard deviation below which the signal is considered flat.
        Default is 1e-12.
    min_duration : float, optional
        The minimum duration (in seconds) for a segment to be considered flat.
        Default is 1.0 second.
        
    Returns
    -------
    mne.io.Raw
        The raw EEG data with flat segments removed.
    """
    sfreq = raw.info['sfreq']
    data = raw.get_data()  # shape: (n_channels, n_times)
    # Compute standard deviation over channels for each time point
    std_vals = np.std(data, axis=0)
    flat_mask = std_vals < flat_threshold

    # Identify continuous flat segments
    flat_segments = []
    n_samples = len(flat_mask)
    i = 0
    while i < n_samples:
        if flat_mask[i]:
            start = i
            while i < n_samples and flat_mask[i]:
                i += 1
            end = i - 1
            # Check if the segment lasts at least min_duration seconds
            if (end - start + 1) / sfreq >= min_duration:
                flat_segments.append((start / sfreq, (end + 1) / sfreq))
        else:
            i += 1

    if not flat_segments:
        print("No flat segments detected.")
        return raw  # Nothing to remove

    # Determine segments to keep (i.e. parts not marked as flat)
    keep_segments = []
    t_start = 0.0
    for seg in flat_segments:
        seg_start, seg_end = seg
        if seg_start > t_start:
            keep_segments.append((t_start, seg_start))
        t_start = seg_end
    if t_start < raw.times[-1]:
        keep_segments.append((t_start, raw.times[-1]))

    # Concatenate the kept segments
    raw_segments = []
    for seg in keep_segments:
        tmin_seg, tmax_seg = seg
        raw_seg = raw.copy().crop(tmin=tmin_seg, tmax=tmax_seg)
        raw_segments.append(raw_seg)
    if len(raw_segments) == 0:
        raise ValueError("No non-flat segments remain after removal.")
    new_raw = mne.concatenate_raws(raw_segments)
    print("Removed flat segments:", flat_segments)
    return new_raw

if __name__ == '__main__':
    # Process files in the 'Preprocessed_Data_FIF_I' directory.
    # Only process files whose names (via string comparison) are greater than ''
    for item in os.listdir('Preprocessed_Data_FIF_I'):
        if item > 'using yours':
            print("Processing file:", item)
            filepath = os.path.join('Preprocessed_Data_FIF_I', item)
            raw_data = mne.io.read_raw_fif(filepath, preload=True)
            raw_data.plot(title=filepath, duration=10, block=True)
            
            # Ask the user if cropping is needed
            crop_input = input('Cropping? (Y/N): ')
            if crop_input.upper() == 'Y':
                stime = float(input('Start time (in seconds): '))
                etime = float(input('End time (in seconds): '))
                raw_data = raw_data.copy().crop(tmin=stime, tmax=etime)
                raw_data.plot(title='Cropped ' + filepath, duration=10, block=True)
            
            # Remove flat segments from the data
            remove_flat = input('Remove flat segments? (Y/N): ')
            if remove_flat.upper() == 'Y':
                raw_data = remove_flat_segments(raw_data)
                raw_data.plot(title='After Flat Segment Removal ' + filepath, duration=10, block=True)
            
            # Optionally, filter the data after cropping and flat segment removal.
            filter_input = input('Apply filtering? (Y/N): ')
            if filter_input.upper() == 'Y':
                raw_data = filter_data(raw_data)
            
            # Save the processed file (overwriting the original)
            raw_data.save(filepath, overwrite=True)
