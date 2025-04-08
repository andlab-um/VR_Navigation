# VR Navigation Experiment Project (VR_Navigation)

## Introduction

This project implements a virtual reality (VR) based spatial navigation task designed for behavioral research. The primary goal is to collect behavioral and electroencephalography (EEG) data to investigate various aspects of spatial cognition and social interaction within a virtual environment.

The collected data can be utilized for EEG signal analysis and related research work, focusing on:

1.  **Spatial Memory and Reward/Punishment:** Exploring the relationship between individual spatial memory capacity, navigational preferences, and the influence of receiving rewards or punishments during the task.
2.  **Social Navigation, Anxiety, and Exploration:** Investigating how individuals with varying levels of anxiety are affected by positive or negative social feedback during social navigation tasks. This includes examining the impact on their spatial navigation abilities, exploratory curiosity, and uncovering potential underlying cognitive patterns.

## Requirements

* **VR System:** Compatible VR headset and controllers.
* **EEG System:** mbt smarting streamer compatible EEG system (e.g., 32-channel EEG cap).
* **Software:**
    * Unity 2020
    * Psychopy (v2022.2.4 recommended)
    * mbt smarting streamer software
    * Python (for running Psychopy scripts and LSL)
    * Required Python packages (see LSL section)
* **Hardware:** A computer capable of running VR applications and EEG recording simultaneously.

## Psychopy Setup

* **Version:** This experiment was developed and tested using **Psychopy v2022.2.4**.
* **Purpose:** Psychopy is used to present instructions, control the resting-state EEG recording phase, run the memory order test (practice and potentially main task), and send experimental event markers via LabStreamingLayer (LSL) for synchronization with EEG data.

## LabStreamingLayer (LSL) Setup

LabStreamingLayer (LSL) is used to synchronize data streams, primarily the EEG data from the smarting streamer and event markers sent from Psychopy.

* **Unity Plugin:**
    * Ensure the LSL plugin compatible with Unity 2020 is installed in your Unity project. This allows the VR environment (if needed) to potentially send or receive LSL markers/data. *(Self-note: Confirm if the Unity part actually *sends* LSL markers in this specific setup or just receives triggers perhaps)*.
* **Psychopy Package:**
    * The `pylsl` Python package is required for Psychopy to send markers over the network. Install it using pip:
      ```bash
      pip install pylsl
      ```

## Code Explanation

The core experimental logic is controlled by Psychopy and Unity. Key Psychopy files include:

* **Resting State:**
    * `EEG_Statistic.psyexp`: The Psychopy Builder file for the resting-state EEG recording phase.
    * `EEG_Statistic_lastrun.py`: The Python script generated from `EEG_Statistic.psyexp`, which is executed by Psychopy.
* **Memory Order Test (Practice):**
    * `VR_Memory_Test_Practice.psyexp`: The Psychopy Builder file for the practice phase of the memory order test.
    * `VR_Memory_Test_Practice_lastrun.py`: The Python script generated from `VR_Memory_Test_Practice.psyexp`.
* **Unity Application:**
    * *(Specify Unity Project/Scene name here, e.g., `VR_Navigation_Scene`)*: The Unity application presenting the virtual environment for navigation and interaction.

## Markers

Event markers are crucial for synchronizing behavioral events with the EEG data stream. For a detailed list and description of the markers used in this experiment (sent via LSL from Psychopy), please refer to the `markers.md` file. *(Note: You should create this separate `markers.md` file detailing what each marker number/string corresponds to, e.g., 'start_trial', 'stimulus_onset', 'response_correct', 'feedback_positive', etc.)*

## Experiment Procedure

Follow these steps to run an experimental session:

1.  **Start EEG System:** Launch the **mbt smarting streamer** software. Connect the software to the EEG cap worn by the participant.
2.  **Check Impedances & Configure Streamer:**
    * Apply conductive gel/paste to the reference electrode(s) and adjust until impedance is low.
    * Check and lower the impedance for all 32 channels according to your lab's standards (e.g., <10 kΩ).
    * In the smarting streamer software, set the **Resample** rate to **500 Hz**.
3.  **Record Resting State EEG:**
    * Start the **Resting State** Psychopy program (`EEG_Statistic.psyexp` or run the `.py` script).
    * In the smarting streamer software, click **Connect** and then **Record** to begin saving the resting-state EEG data stream (ensure LSL streaming is enabled if markers are sent from Psychopy during this phase).
4.  **VR Familiarization & Practice Setup:**
    * Once resting state is complete, **Stop** the recording in the smarting streamer software.
    * Launch the **Unity VR application**. Guide the participant on how to use the controller(s) for movement within the virtual environment.
    * Start the **Memory Order Test Practice** Psychopy program (`VR_Memory_Test_Practice.psyexp` or run the `.py` script).
    * In the smarting streamer software, start a **New Recording** (Connect -> Record) to capture EEG data during the practice phase.
5.  **VR Environment Learning & Memory Test Practice:**
    * Guide the participant to navigate around the virtual environment (e.g., walk in circles or explore freely) to learn and memorize the spatial layout.
    * After sufficient exploration, have the participant complete the **Memory Order Test** presented via Psychopy.
    * **Repeat** the environment learning phase if the participant's accuracy on the memory test is below the required threshold.
6.  **Start Main Experiment:**
    * Once the participant passes the practice memory order test, **click the designated area** (e.g., top-right corner) within the VR interface using the mouse to transition to the main experimental phase.
    * The participant will now alternate between performing the **Spatial Navigation** tasks and the **Social Navigation** tasks as defined in the experimental design. *(Ensure EEG recording is ongoing throughout this main phase)*.

## Data Output

* **EEG Data:** Saved by the mbt smarting streamer software (e.g., in `.xdf` format if using LSL recording tools like LabRecorder, or the software's native format).
* **Behavioral Data:** Saved by Psychopy (typically `.csv`, `.log`, `.psydat` files) containing timings, responses, accuracy, marker information, etc. for both practice and main tasks.
* *(Add any other data outputs if applicable, e.g., Unity logs)*.