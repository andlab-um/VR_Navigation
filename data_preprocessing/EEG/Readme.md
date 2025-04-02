## EEG preprocessing and analysis code for *An EEG Dataset of Exploring Navigation in Virtual Reality* dataset

### Introduction

This is Preprocessing code, TFA and ERP analyse code of *An EEG Dataset of Exploring Navigation in Virtual Reality DATASET*

Before you use it, please set your own path and pair the name of the data you are using,
after that you need to use it in the order of bash.txt or you can just run the bash command

**mne_processing_template.py**: Preliminary filtering and re-referencing, resample, generated files moved to Preprocessed_Data_FIF file

**preprocess_crop.py**:Crop the EEG data by items'number, removing flat segments.

**EEG_Data_Crop.py**: Multiple decentralised EEG fif data for the first round of classification.Splitting by stage,generate the pending resting-state&practice-state&task-state,into three different name file

**Merged_ANA.py**: Merge the same subject information for each crop segment.we has lots of runs in practice and task state, this code is to put together the data under the corresponding states for subsequent de-artifacting process.

**ASR+ICA_Preprocessing.py**:bad channel Interpolation De-artifact to task-state data, we set using asr in sub1 to sub 47, we highly recommand to open ASR function, after ASR will do ICA progress and generate the epoch

**Rest_State_Crop.py**: for resting-state data processing to cut the pending data into 60s Resting_state_data,There are a number of functions that need to be called from this, and we do not recommend removing or modifying this

**Test_crop.py**:There are a number of functions that need to be called from this, and we do not recommend removing or modifying this

### Experiment Procedure

We preprocessed by following process:

1. Re-Referencing:

   - A dedicated reference electrode '**FCz**' was recorded alongside the regular EEG channels.
   - Data were re-referenced to the average of all channels after including the '**FCz**'.
2. Filtering:

   - A band-pass filter with low-pass cutoff set at 0.1 Hz and high-pass cutoff set at 30.0 Hz was applied.
   - Detailed filtering parameters can be found in each subject's corresponding sub-`<ID>`_sub-01_task-XX_run-YY_eeg.json file under the raw EEG folder.
3. Merging Runs:

   - For each subject, multiple runs (recorded during the same task session but interrupted by electromagnetic interference) were merged.
   - This step ensured the time series continuity for subsequent analyses.
4. Task Segmentation:

   - The continuous EEG data were segmented into three distinct task conditions:
     • "**rest_state**": Resting state recording
     • "**practice**": Navigation practice task
     • "**task**": Navigation task actual performance
   - Sub-datasets were generated per subject and task type.
   - 
5. Bad Channel Interpolation:

   - For each segmented data, channels identified with excessive noise or artifacts were interpolated to reduce their effect on data quality.
6. ASR (Artifact Subspace Reconstruction):

   - The ASR algorithm was applied to reduce movement artifacts.
   - Note: For subjects sub_48 to sub_60, real-time ASR was applied during data acquisition.
7. ICA (Independent Component Analysis):

   - ICA was performed to isolate and remove components associated with eye movements, cardiac signals, muscle artifacts etc.
   - Components for removal were manually or semi-automatically determined based on spatial, temporal, and spectral characteristics.#in here we use automatic
