import os
import pandas as pd

# Define the columns for the DataFrame
columns = ['sub_ID']
for i in range(36):
    columns.append(str(i+1))

# Create an empty DataFrame with the specified columns
fdata = pd.DataFrame(columns=columns)
fdata

# List all directories in the current folder that are numerical
folders = [f for f in os.listdir() if os.path.isdir(f) and f.isdigit()]
print(folders)

# Iterate through each folder
for folditem in folders:
    if folditem > '':  # Only process folders with IDs greater than 347
        trial = []
        
        # Iterate through files in the folder
        for item in os.listdir(str(folditem)):
            if item.startswith('SpaceNavi') or item.startswith('SocialNavi'):
                print(item)
                if item.split('_')[-2] != '0':  # Filter out trials where the second-to-last part is '0'
                    trial.append(item.split('_')[-1])  # Add the trial number to the list
                    # print(item.split('_')[-2], end=',')
        print(trial)
        
        # Create a new row for the DataFrame with values for each trial (1 if the trial exists, 0 if not)
        new_row = pd.DataFrame([{str(i): (1 if str(i) in trial else 0) for i in range(1, 37)}])
        new_row['sub_ID'] = folditem

        # Add the new row to the DataFrame
        fdata = pd.concat([fdata, new_row], ignore_index=True)

# Process the DataFrame to add a sum column
fdatacal = fdata.iloc[:, 1:]
fdata['Sum'] = fdatacal.sum(axis=1)

# Uncomment the following line if you want to save the DataFrame to an Excel file
# fdata.to_excel('Trajectory_Loss_Trial.xlsx', index=None)

fdata

# Read the existing 'Trajectory_Loss_Trial.xlsx' file and concatenate the new data
generated_data = pd.read_excel('Trajectory_Loss_Trial.xlsx')
generated_data = pd.concat([generated_data, fdata], ignore_index=True)

# Save the combined data back to an Excel file
generated_data.to_excel('Trajectory_Tables/Trajectory_Loss_Trial.xlsx', index=False)
generated_data

# Generate a second table that shows [subID, type valid (0-1)]
new_data = pd.read_excel('Trajectory_Loss_Trial.xlsx')[:-1]
new_data_droped = new_data.drop(columns=['sub_ID', 'Sum'])
new_data_droped.T

new_data

# Create a new DataFrame with 'sub_id', 'trial', and 'value' columns
new_df = pd.DataFrame(columns=['sub_id', 'trial', 'value'])

# Iterate over the rows of the original data to restructure it
for index, row in new_data.iterrows():
    sub_id = row['sub_ID']
    for trial_number in range(1, 7):  # Assume there are 6 trials
        trial_value = row[f'trial_{trial_number}']
        new_df = new_df.append({'sub_id': sub_id, 'trial': trial_number, 'value': trial_value}, ignore_index=True)

# Print the new DataFrame
print(new_df)
