import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import concurrent.futures  # Import concurrency library
from mpl_toolkits.mplot3d import Axes3D
import datetime
import pytz
import warnings
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg
from matplotlib.transforms import Affine2D
import matplotlib.animation as animation
warnings.filterwarnings("ignore")

prev_xt = []
prev_zt = []

class StructureD:
    def __init__(self, location:str, nav_type:str, memory: str, number_values:str):
        '''
        params: 
            location: the location of the csv files
            nav_type: the type (Spatial or Social) of the Navigation in the csv files
            memory: whether it is the memory part in the csv files
            number_values: the number of the complete trials
        '''
        self.location = location
        self.nav_type = nav_type
        self.memory = memory
        self.number_values = number_values

    def show_location(self):
        return self.location
    
    def show_nav_type(self):
        return self.nav_type
    
    def show_memory(self):
        return self.memory
    
    def show_number_values(self):
        return self.number_values
    

class Track():
    def __init__(self, filename:str, title):
        self.data =  pd.read_csv(filename, header=None)
        self.type = filename.split("_")[0]
        self.title = title

        self.data.columns = ["x_axis", "y_axis", "z_axis", "timestamp"]
        self.data = self.data.drop_duplicates(subset=['x_axis','z_axis']).reset_index(drop=True)
        self.x_pos = self.data[2:].iloc[:,0].str.replace(r'(', '').astype("float64").reset_index(drop=True)
        self.y_pos = self.data[2:].iloc[:,1].reset_index(drop=True)
        self.z_pos = self.data[2:].iloc[:,2].str.replace(r')', '').astype("float64").reset_index(drop=True)
        self.timestamp = self.data[2:].iloc[:,1].reset_index(drop=True)


    def get_xpos(self):
        return self.x_pos
    
    def get_ypos(self):
        return self.y_pos
    
    def get_zpos(self):
        return self.z_pos

    def plot_animation(self, image='bacgnd.png', normalized_width=125, move_x_pos=38, move_z_pos=84, save_dir:str = "", save_fname:str = ""):
        """Plot Animation of the track"""

        image = mpimg.imread(image)
        fig1, ax1 = plt.subplots(figsize=(10, 10))
        width, height = image.shape[1], image.shape[0]

        # Calculate width and height ratio
        aspect_ratio = width / height
        # Set the normalized coordinate range
        normalized_width = normalized_width
        normalized_height = normalized_width / aspect_ratio

        # Create coordinate transformation to map original coordinates to normalized system
        transform = Affine2D().scale(normalized_width / width, normalized_height / height)

        # Display the image as background with coordinate transformation
        ax1.imshow(image, extent=[0, width, 0, height], zorder=0, transform=transform + ax1.transData)

        x1_pos = move_x_pos + self.x_pos
        z1_pos = move_z_pos + self.z_pos

        # Set coordinate range and labels
        ax1.set_xlim(0, normalized_width)
        ax1.set_ylim(0, normalized_height)
        ax1.set_xticks(np.linspace(0, normalized_width, 15))
        ax1.set_yticks(np.linspace(0, normalized_height, 15))

        scat = ax1.scatter(x1_pos, z1_pos, color='r', marker='o', zorder=1)

        def nupdate(frame):
            global prev_xt, prev_zt
            scat.set_offsets([[self.x_pos[frame] + move_x_pos, self.z_pos[frame] + move_z_pos]])
            prev_xt.append(self.x_pos[frame] + move_x_pos)
            prev_zt.append(self.z_pos[frame] + move_z_pos)
            scat.set_offsets(list(zip(prev_xt, prev_zt)))

            return scat
    
        ani = animation.FuncAnimation(fig1, nupdate, frames=len(self.x_pos), interval=20, blit=False)
        print(save_dir + '/' + save_fname + '.mp4')
        ani.save(save_dir + '/' + save_fname + '.mp4', writer='ffmpeg')
        global prev_xt, prev_zt
        prev_xt = []
        prev_zt = []
    
    def print_len(self):
        print(len(self.x_pos))
        print(len(self.z_pos))
        print(print(len(self.data.iloc[:, 0]), len(self.data.iloc[:, 1]), len(self.data.iloc[:, 2])))

    def show_data(self):
        print(self.data)
        print(self.z_pos)

    def new_dataFrame(self)-> pd.DataFrame:
        return pd.DataFrame({'x': self.x_pos, 'y': self.y_pos, 'z': self.z_pos})


def extract_csv_paths(root_dir=os.getcwd()):
    social_list = []
    space_list = []
    social_mem_list = []
    space_mem_list = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        if os.path.basename(dirpath).startswith('Space'):
            nav_type = "Space"
            if "Memory" in dirpath:
                memory = "T"
                for filename in filenames:
                    if filename.endswith('.csv') and filename.startswith('Player_Position'):
                        csv_path = os.path.join(dirpath, filename)

                        number_values = dirpath.split("_")[-1]
                        structureD = StructureD(location=csv_path, nav_type=nav_type, memory=memory, number_values=number_values)
                        space_mem_list.append(structureD)
            else:
                memory = "F"
                for filename in filenames:
                    if filename.endswith('.csv') and filename.startswith('Player_Position'):
                        csv_path = os.path.join(dirpath, filename)
                        number_values = dirpath.split("_")[-1]
                        structureD = StructureD(location=csv_path, nav_type=nav_type, memory=memory, number_values=number_values)   
                        space_list.append(structureD)

        elif os.path.basename(dirpath).startswith('Social'):
            nav_type = "Social"
            if "Memory" in dirpath:
                memory = "T"
                for filename in filenames:
                    if filename.endswith('.csv') and filename.startswith('Player_Position'):
                        csv_path = os.path.join(dirpath, filename)
                        number_values = dirpath.split("_")[-1]
                        structureD = StructureD(location=csv_path, nav_type=nav_type, memory=memory, number_values=number_values)
                        social_mem_list.append(structureD)

            else:
                memory = "F"
                for filename in filenames:
                    if filename.endswith('.csv') and filename.startswith('Player_Position'):
                        csv_path = os.path.join(dirpath, filename)
                        

                        number_values = dirpath.split("_")[-1]
                        structureD = StructureD(location=csv_path, nav_type=nav_type, memory=memory, number_values=number_values)   
                        social_list.append(structureD)

    return [space_list, space_mem_list, social_list, social_mem_list]


def plot_acc(lists: list, plot_cols: int, image='bacgnd.png', normalized_width=125, move_x_pos=36, move_z_pos=84):

    image = mpimg.imread(image)

    nrows = (len(lists) + plot_cols - 1) // plot_cols
    fig = plt.figure(constrained_layout=True, figsize=(20, 20))
    gs = fig.add_gridspec(ncols=plot_cols, nrows=nrows)

    for i, df in enumerate(lists):
        row = i // plot_cols
        col = i % plot_cols
        ax = fig.add_subplot(gs[row, col])

        memory = "Memory" if  df.show_memory() == "T" else ""
        title = "Num-" + df.show_number_values() + " Type:" + df.show_nav_type() + memory

        df_dataFrame = Track(df.show_location(), title)

        width, height = image.shape[1], image.shape[0]

        aspect_ratio = width / height
        normalized_width = normalized_width
        normalized_height = normalized_width / aspect_ratio
        transform = Affine2D().scale(normalized_width / width, normalized_height / height)
        ax.imshow(image, extent=[0, width, 0, height], zorder=0, transform=transform + ax.transData)
        x1_pos = move_x_pos + df_dataFrame.get_xpos()
        z1_pos = move_z_pos + df_dataFrame.get_zpos()

        plt.scatter(x1_pos, z1_pos, color='red', marker='o', zorder=1)
        plt.plot(x1_pos, z1_pos)

        ax.set_xlim(0, normalized_width)
        ax.set_ylim(0, normalized_height)
        ax.set_xticks(np.linspace(0, normalized_width, 10))
        ax.set_yticks(np.linspace(0, normalized_height, 16))
        plt.title(title)
    
    plt.savefig("exp.png", dpi=600)

def make_dirs(subdir:str, x:str):
    try:
        folder_path = os.path.join(os.getcwd(), subdir, x)
        if not os.path.exists(folder_path):
            print(folder_path)
            os.makedirs(folder_path)
        return 0
    except Exception:
        return 1


def process_participant(sub):
    """Process each participant separately for multithread execution"""
    print('Participant: ', sub)
    root_dir = sub
    nav_lists = extract_csv_paths(root_dir=root_dir)

    for itemlist in nav_lists:
        print(len(itemlist), end=" ")

    for itemlist in nav_lists:
        itemlist = sorted(itemlist, key=lambda x: int(x.number_values))
        print([x.show_number_values() for x in itemlist])
        plot_acc(itemlist, 4)

        if itemlist[0].show_memory() == "T":
            plt.savefig(root_dir + '/' + itemlist[0].show_nav_type() + '_' + "Mem_Exp.png", dpi=600)
        else:
            plt.savefig(root_dir + '/' + itemlist[0].show_nav_type() + "_Exp.png", dpi=600)

        for subitem in itemlist:
            memory = "Memory" if subitem.show_memory() == "T" else ""
            title = "Num_" + subitem.show_number_values() + "_" + subitem.show_nav_type() + memory
            df_data = Track(subitem.show_location(), title)

            if subitem.show_memory() == "T":
                if subitem.show_nav_type() == "Space":
                    save_dir = "Space_Memory"
                elif subitem.show_nav_type() == "Social":
                    save_dir = "Social_Memory"
            else:
                save_dir = subitem.show_nav_type()
            print(save_dir, title)

if __name__ == '__main__':
    print('\334LMN')

    # Define the subnumbers you want to process, e.g., a range from 1 to 10.
    sublist = [str(i) for i in range(1, 60)]  # Define your own number setting
    dirlist = ['Space', 'Space_Memory', 'Social', 'Social_Memory']

    # Create the necessary directories for each participant and directory type
    for sub in sublist:
        for dir in dirlist:
            make_dirs(sub, dir)

    # Process each participant in parallel using threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(process_participant, sub) for sub in sublist]

        # Wait for all futures to finish and handle any exceptions
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error: {e}")

    # After processing, re-run the plots and save the output for each subnumber
    for sub in sublist:
        print('Participant: ', sub)
        root_dir = sub

        # Extract navigation data for the participant
        nav_lists = extract_csv_paths(root_dir=root_dir)

        # Plot the data for each navigation list (sorted by the number of trials)
        for itemlist in nav_lists:
            print(len(itemlist), end=" ")

        for itemlist in nav_lists:
            itemlist = sorted(itemlist, key=lambda x: int(x.number_values))
            print([x.show_number_values() for x in itemlist])
            plot_acc(itemlist, 4)

            # Save the plot for each navigation type (with or without memory)
            if itemlist[0].show_memory() == "T":
                plt.savefig(root_dir + '/' + itemlist[0].show_nav_type() + '_' + "Mem_Exp.png", dpi=600)
            else:
                plt.savefig(root_dir + '/' + itemlist[0].show_nav_type() + "_Exp.png", dpi=600)

            # Process each individual item in the list
            for subitem in itemlist:
                memory = "Memory" if subitem.show_memory() == "T" else ""
                title = "Num_" + subitem.show_number_values() + "_" + subitem.show_nav_type() + memory
                df_data = Track(subitem.show_location(), title)

                # Determine the save directory based on memory and navigation type
                if subitem.show_memory() == "T":
                    if subitem.show_nav_type() == "Space":
                        save_dir = "Space_Memory"
                    elif subitem.show_nav_type() == "Social":
                        save_dir = "Social_Memory"
                else:
                    save_dir = subitem.show_nav_type()

                print(save_dir, title)

