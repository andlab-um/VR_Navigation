# %%
import numpy as np
import pandas as pd
import scipy
import random
import matplotlib.pyplot as plt
from datetime import datetime, timezone, timedelta  
import csv  
from collections import deque
import math

# %%
def read_positon(subject,block,trial):
    file_name = 'PosTable/sub_'+str(300+subject)+'.xlsx'
    df = pd.read_excel(file_name)

    return df

# %%
def distance(a,b):
    # 欧几里得距离
    return np.sqrt(np.square(a[0]-b[0])+np.square(a[1]-b[1]))

# print(distance([45.8,-23.3],[46.401,-27.017]))




def interact_time(subject: int, navtype='space'):

    file_name = 'PosTable/sub_'+str(subject)+'.xlsx'
    
    df = pd.read_excel(file_name)

    target_pos = [[0.2,51.7],[45.8,28.5],[-14.1,28.6],[76,15.1],[15.3,-6.6],[45.8,-23.3],[-15.1,-38.5],[75.6,-43.6]]
    target_id = [0,1,2,3,4,5,6,7]
    target_reward = [1,1,-1,-1,1,-1,1,-1]

    target_social_pos = [[-1.5,50.1],[44.5,-25.3],[-15.6,-43.4],[75.7,-43.6],[46.1,28.3],[75.9,15.4],[9.1,-1.2],[-15.5,28.5]]
    target_social_id = [25,21,33,35,39,29,31,23]
    target_social_reward = [1,-1,1,-1,1,-1,1,-1]

    if navtype == 'social':
        target_pos = target_social_pos
        # target_id = target_social_id # 仅仅记录下标记
        target_reward = target_social_reward


    trial_target_list = []
    
    trial_list = []
    explored_target_list = []
    time_approach_list = []
    time_leave_list = []
    time_interact_list = []
    reward_list = []
    
    approach_distance = []
    leave_distance = []
    
    approach_speed = []
    leave_speed = []
    
    R_circle = 5
    
    interact_pos = []
    approach_pos = []
    leave_pos = []

    def collision_detection(x,x_standard,y,y_standard, navtype):
        if navtype == 'space':
            return np.abs(x-x_standard) <= 3 and np.abs(y-y_standard) <= 3
        else:
            return  -2.622 <= x - x_standard <= 2.484 and -1.266 <= y - y_standard <= 2.56


    
    for i in range(len(df['index'])):
        if df['index'][i]%6 != 0:
            for j in range(len(target_pos)):
                if collision_detection(df['x_pos'][i],target_pos[j][0],df['z_pos'][i],target_pos[j][1], navtype):
                    
                    if [df['index'][i],target_id[j]] not in trial_target_list:
                        trial_target_list.append([df['index'][i],target_id[j]])
                        explored_target_list.append(target_id[j])
                        trial_list.append(df['index'][i])
                        
                        time_interact_list.append(df['timestamp'][i])
                        reward_list.append(target_reward[j])
                        interact_pos.append([df['x_pos'][i],df['z_pos'][i]])
    # print("========================")
    # print(len(explored_target_list))

    # # if navtype == 'social':
    # #     social_list = [target_social_id[i] for i in explored_target_list]
    # #     explored_target_list = social_list

    # print(len(explored_target_list))

    trial_time_list = []
    trial_time_list.append(df['timestamp'][0])
    trial_index = df['index'][0]
    for i in range(len(df['index'])):
        # if df['index'][i]%6 != 0:
        if df['index'][i] != trial_index:
            trial_time_list.append(df['timestamp'][i])
            trial_index =df['index'][i]
    trial_time_list.append(df['timestamp'][len(df['index'])-1])
    


    for i in range(len(explored_target_list)):
        time_leave_list.append([])
        time_approach_list.append([])
        approach_pos.append([])
        leave_pos.append([])
        
        approach_distance.append(0)
        leave_distance.append(0)
    
    
    ccc = 0
    

    if_leave_circle = [False,False,False,False,False,False,False,False]
    index = df['index'][0]
    n_index = 1
    for i in range(len(df['index'])):
        # if df['index'][i]%6 != 0:
        if df['index'][i] != index:
            n_index+=1
            index = df['index'][i]
            if_leave_circle = [False,False,False,False,False,False,False,False]
        
        
        for j in range(len(explored_target_list)):
            if trial_list[j]==df['index'][i]:
                # print(explored_target_list[j]) # 35
                # print(len(target_pos)) # 8
                # print(target_pos[explored_target_list[j]])
                # print(distance([df['x_pos'][i],df['z_pos'][i]],target_pos[explored_target_list[j]]))

                if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[explored_target_list[j]])>= R_circle and df['timestamp'][i].value<time_interact_list[j].value and df['timestamp'][i].value>trial_time_list[n_index-1].value:
                    time_approach_list[j] = df['timestamp'][i]
                    approach_pos[j] = [df['x_pos'][i],df['z_pos'][i]]
                    # print(j)
                    # print('bbb')
                # elif not if_leave_circle[explored_target_list[j]] and distance([df['x_pos'][i],df['z_pos'][i]],target_pos[explored_target_list[j]])<= R_circle and df['timestamp'][i].value>time_interact_list[j].value:
                elif (not if_leave_circle[explored_target_list[j]]) and distance([df['x_pos'][i],df['z_pos'][i]],target_pos[explored_target_list[j]])<= R_circle and df['timestamp'][i].value>time_interact_list[j].value and df['timestamp'][i].value<trial_time_list[n_index].value:
        
                    time_leave_list[j] = df['timestamp'][i]
                    leave_pos[j] = [df['x_pos'][i],df['z_pos'][i]]
                    # print('aaa')
                
                elif (not if_leave_circle[explored_target_list[j]]) and distance([df['x_pos'][i],df['z_pos'][i]],target_pos[explored_target_list[j]])> R_circle and df['timestamp'][i].value>time_interact_list[j].value and df['timestamp'][i].value<trial_time_list[n_index].value:
                # elif distance([df['x_pos'][i],df['z_pos'][i]],target_pos[explored_target_list[j]])> R_circle and df['timestamp'][i].value>time_interact_list[j].value:

                    if_leave_circle[explored_target_list[j]] = True

    for j in range(len(time_approach_list)):
        if time_approach_list[j]==[]:
            time_approach_list[j] = time_interact_list[j]
            approach_pos[j] = target_pos[explored_target_list[j]]
    for j in range(len(time_leave_list)):
        if time_leave_list[j]==[]:
            time_leave_list[j] = time_interact_list[j]
            leave_pos[j] = target_pos[explored_target_list[j]]
    
    # print(time_approach_list)
    # print(time_interact_list)
    n = 0
    for i in range(len(df['index'])-1):
        if n <= len(time_approach_list)-1:
            if df['timestamp'][i].value>=time_approach_list[n].value and df['timestamp'][i].value<time_interact_list[n].value:
                approach_distance[n]+= np.abs(df['x_pos'][i+1]-df['x_pos'][i]) + np.abs(df['z_pos'][i+1]-df['z_pos'][i])
            elif df['timestamp'][i].value>=time_interact_list[n].value and df['timestamp'][i].value<=time_leave_list[n].value:
                leave_distance[n]+= np.abs(df['x_pos'][i+1]-df['x_pos'][i]) + np.abs(df['z_pos'][i+1]-df['z_pos'][i])
            elif df['timestamp'][i].value>time_leave_list[n].value:
                n+=1
            
    for i in range(len(explored_target_list)):
        if time_interact_list[i].value-time_approach_list[i].value != 0:
            approach_speed.append(approach_distance[i]*10000000*100/(time_interact_list[i].value-time_approach_list[i].value))
        else:
            approach_speed.append(0)
        if time_leave_list[i].value-time_interact_list[i].value != 0:
            leave_speed.append(leave_distance[i]*10000000*100/(time_leave_list[i].value-time_interact_list[i].value))
        else:
            leave_speed.append(0)
            

    if navtype == 'social':
        social_list = [target_social_id[i] for i in explored_target_list]
        explored_target_list = social_list
        

    return trial_list,explored_target_list,time_approach_list,time_interact_list,time_leave_list,approach_pos,interact_pos,leave_pos,reward_list,approach_distance,leave_distance,approach_speed,leave_speed
                


                
def forced_stay(subject):
    file_name = 'PosTable/sub_'+str(300+subject)+'.xlsx'
    df = pd.read_excel(file_name)
    forced_stay_time_list = []
    forced_stay_pos_list = []
    
    find_forced_stay = False
    
    prev_time = df['timestamp'][0]
    prev_time_value = df['timestamp'][0].value
    prev_pos = [df['x_pos'][0],df['z_pos'][0]]
    
    next_time = df['timestamp'][0].value
    next_pos = [df['x_pos'][0],df['z_pos'][0]]
    
    max_stay_time = 0
        
    for i in range(len(df['index'])-1):
        current_time = df['timestamp'][i]
        current_time_value = df['timestamp'][i].value
        current_pos = [df['x_pos'][i],df['z_pos'][i]]
        
        next_time_value = df['timestamp'][i+1].value
        next_pos = [df['x_pos'][i+1],df['z_pos'][i+1]]
        
        if prev_pos == current_pos and current_time_value >= prev_time_value:
            
            forced_stay_time = current_time_value - prev_time_value
            
            if forced_stay_time>max_stay_time:
                max_stay_time = forced_stay_time
            
            if next_pos != current_pos and forced_stay_time >= 1000000000:
                forced_stay_pos_list.append(current_pos)
                forced_stay_time_list.append(prev_time)
        else:
            prev_pos = current_pos
            prev_time = current_time
            prev_time_value = current_time_value
    
    print(max_stay_time)
    
    return forced_stay_pos_list,forced_stay_time_list

def min_target_distance(subject):
    file_name = 'PosTable/sub_'+str(300+subject)+'.xlsx'
    df = pd.read_excel(file_name)
    target_pos = [[0.2,51.7],[45.8,28.5],[-14.1,28.6],[76,15.1],[15.3,-6.6],[45.8,-23.3],[-15.1,-38.5],[75.6,-43.6]]
    target_id = [0,1,2,3,4,5,6,7]
    target_reward = [1,1,-1,-1,1,-1,1,-1]
    target_social_pos = [[-1.5,50.1],[44.5,-25.3],[-15.6,-43.4],[75.7,-43.6],[46.1,28.3],[75.9,15.4],[9.1,-1.2],[-15.5,28.5]]
    target_social_id = [25,21,33,35,39,29,31,23]
    target_social_reward = [1,-1,1,-1,1,-1,1,-1]
    
    min_distance_list = [200,200,200,200,200,200,200,200]
    min_distance_time_list = [0,0,0,0,0,0,0,0]
    
    for i in range(len(df['index'])):
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[0])<min_distance_list[0]:
            min_distance_list[0] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[0])
            min_distance_time_list[0] = df['timestamp'][i]
            
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[1])<min_distance_list[1]:
            min_distance_list[1] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[1])
            min_distance_time_list[1] = df['timestamp'][i]
            
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[2])<min_distance_list[2]:
            min_distance_list[2] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[2])
            min_distance_time_list[2] = df['timestamp'][i]
            
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[3])<min_distance_list[3]:
            min_distance_list[3] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[3])
            min_distance_time_list[3] = df['timestamp'][i]
            
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[4])<min_distance_list[4]:
            min_distance_list[4] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[4])
            min_distance_time_list[4] = df['timestamp'][i]
            
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[5])<min_distance_list[5]:
            min_distance_list[5] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[5])
            min_distance_time_list[5] = df['timestamp'][i]
            
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[6])<min_distance_list[6]:
            min_distance_list[6] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[6])
            min_distance_time_list[6] = df['timestamp'][i]
            
        if distance([df['x_pos'][i],df['z_pos'][i]],target_pos[7])<min_distance_list[7]:
            min_distance_list[7] = distance([df['x_pos'][i],df['z_pos'][i]],target_pos[7])
            min_distance_time_list[7] = df['timestamp'][i]
    
    return min_distance_list,min_distance_time_list


def gen_approach_leave_speed(start_participant, end_participant, condition):
    
    # 300 
    # 生成文件的速度比较慢，所以这里尽量不要重新生成数据，
    for i in range(start_participant,end_participant+1):
        print('Write item: ', i)

        if condition == 'social':

            trial_list,explored_target_list,time_approach_list,time_interact_list,time_leave_list,approach_pos,interact_pos,leave_pos,reward_list,approach_distance,leave_distance,approach_speed,leave_speed = interact_time(i,'social')
        
            csv_filename = 'approach_interact_leave_time_social/approach_interact_leave_time_'+str(i)+'.csv' 
            # csv_filename = 'demo/ailt_social_'+str(i)+'.csv'

        else:
            trial_list,explored_target_list,time_approach_list,time_interact_list,time_leave_list,approach_pos,interact_pos,leave_pos,reward_list,approach_distance,leave_distance,approach_speed,leave_speed = interact_time(i)
            
            csv_filename = 'approach_interact_leave_time/approach_interact_leave_time_'+str(i)+'.csv' 
            # csv_filename = 'demo/ailt_'+str(i)+'.csv'
        
        # 使用csv.writer写入CSV文件  
        with open(csv_filename, 'w', newline='') as csvfile:  
            fieldnames = [  
                'Trial',  
                'Explored Target',  
                'Time Approach',  
                'Time Interact',  
                'Time Leave',  
                'Pos Approach',  
                'Pos Interact',  
                'Pos Leave',  
                'Reward',  
                'Approach Distance',  
                'Leave Distance',  
                'Approach Speed',  
                'Leave Speed'  
            ]  
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
        
            # 写入标题行  
            writer.writeheader()  
        
            # 遍历列表并将它们作为字典写入CSV文件  
            for trial, target, time_approach, time_interact, time_leave, pos_approach, pos_interact, pos_leave, reward, ap_dist, le_dist, ap_speed, le_speed in zip(  
                    trial_list, explored_target_list, time_approach_list, time_interact_list, time_leave_list,approach_pos,interact_pos,leave_pos, reward_list,  
                    approach_distance, leave_distance, approach_speed, leave_speed  
            ):  
                writer.writerow({  
                    'Trial': trial,  
                    'Explored Target': target,  
                    'Time Approach': time_approach,  
                    'Time Interact': time_interact,  
                    'Time Leave': time_leave,  
                    'Pos Approach': pos_approach,
                    'Pos Interact': pos_interact,
                    'Pos Leave': pos_leave, 
                    'Reward': reward,  
                    'Approach Distance': ap_dist,  
                    'Leave Distance': le_dist,  
                    'Approach Speed': ap_speed,  
                    'Leave Speed': le_speed  
                })  






def if_in_road(pos):
    x = pos[0]
    y = pos[1]
    
    if -30<=x<=80 and 49<=y<=56:
        return True
    elif -30<=x<=50.5 and 25.5<=y<=33:
        return True
    elif 2.5<=x<=80 and -5.5<=y<=1.5:
        return True
    elif 41<=x<=80 and 10<=y<=17:
        return True
    elif -20<=x<=50 and -29<=y<=-21:
        return True
    elif 10<=x<=18 and -44<=y<=-36:
        return True
    elif -20<=x<=18 and -51.5<=y<=-44.5:
        return True
    elif -20<=x<=80 and -67<=y<=-59.5:
        return True
    elif -30<=x<=-20 and 25<=y<=56:
        return True
    elif -5<=x<=2.5 and 25<=y<=56:
        return True
    elif 18.5<=x<=26 and 25<=y<=56:
        return True
    elif 41<=x<=50 and -68<=y<=56:
        return True
    elif 72<=x<=80 and -68<=y<=56:
        return True
    elif -20<=x<=-12.5 and -51.5<=y<=34:
        return True
    elif 3<=x<=10.5 and -5.5<=y<=34:
        return True
    elif 10<=x<=18.5 and -68<=y<=2.5:
        return True
    else:
        return False
    
    

def pos_transition(init_pos,end_pos,obstacle_list):
    
    
    obstacle_list2 = []
    for i in obstacle_list:
        if if_in_road(i):
            obstacle_list2.append(i)
    
    x_axis = -25,-17,-1,7,14,22,33,45,60,76
    y_axis = 52,41,30,22,14,6,-2,-14,-25,-32,-40,-48,-56,-64
    
    position = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],
                [0,1],[2,1],[5,1],[7,1],[9,1],
                [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[9,2],
                [1,3],[3,3],[7,3],[9,3],
                [1,4],[3,4],[7,4],[8,4],[9,4],
                [1,5],[3,5],[7,5],[9,5],
                [1,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[9,6],
                [1,7],[4,7],[7,7],[9,7],
                [1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[9,8],
                [1,9],[4,9],[7,9],[9,9],
                [1,10],[4,10],[5,10],[6,10],[9,10],
                [1,11],[2,11],[3,11],[7,11],[9,11],
                [4,12],[7,12],[9,12],
                [1,13],[2,13],[3,13],[4,13],[5,13],[6,13],[7,13],[8,13],[9,13]]
    
    position_ture = []

    for i in range(len(position)):
        position_ture.append([x_axis[position[i][0]],y_axis[position[i][1]]])
    
    position_all_true = []
    for i in position_ture:
        for j in range(85-i[0]):
            if if_in_road([i[0]+j,i[1]]) and ([i[0]+j,i[1]] not in position_all_true):
                position_all_true.append([i[0]+j,i[1]])
        for j in range(70-i[1]):
            if if_in_road([i[0],i[1]+j]) and ([i[0],i[1]+j] not in position_all_true):
                position_all_true.append([i[0],i[1]+j])
                
    
    
    
    all_map = []
    
    for i in range(len(x_axis)):
        for j in range(len(y_axis)):
            all_map.append([x_axis[i],y_axis[j]])
            
    obstacle_list3 = []
    for i in range(len(obstacle_list2)):
        obstacle_list3.append([])
    
       
    for i in range(len(obstacle_list2)):
        min_distance_obstacle = 100
        for j in range(len(position_all_true)):
            if distance(obstacle_list2[i],position_all_true[j])<min_distance_obstacle:
                min_distance_obstacle = distance(obstacle_list2[i],position_all_true[j])
                obstacle_list3[i] = position_all_true[j]

    # obstacle_list3 = []
    # for i in obstacle_list2:
    #     if i in position_all_ture:
    #         obstacle_list3.append(obstacle_list2[i])
    
    postion_avliable = []
    for i in position_all_true:
        if i not in obstacle_list3:
            postion_avliable.append(i)
            
    init_pos2 = [100,100]
    end_pos2 = [100,100]
    
    min_distance_init = 100
    min_distance_end = 100
    
    for i in postion_avliable:
        if distance(init_pos,i)<min_distance_init:
            init_pos2 = i
            min_distance_init = distance(init_pos,i)
        if distance(end_pos,i)<min_distance_end:
            end_pos2 = i
            min_distance_end = distance(end_pos,i)

    return init_pos2,end_pos2,postion_avliable

def optimal_path(init_pos,end_pos,obstacle):
    start,end,postion_avliable = pos_transition(init_pos,end_pos,obstacle)
    
    start = tuple(start)
    end = tuple(end)
    # print(start,end)
    position_set = set(tuple(pos) for pos in postion_avliable)
    queue = deque([(start, [start])])
    
    # 访问过的点
    visited = set()
    visited.add(start)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        current, path = queue.popleft()
        
        # 检查当前点是否为目标点
        if current == end:
            return path
        
        # 探索四个方向的点
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # 检查邻居点是否在地图中且未被访问过
            if neighbor in position_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    # 如果没有找到路径
    return None
    
        

# 定义函数 path_entropy，输入参数为 subject（被试编号）
def path_entropy(subject):
    
    # 初始化一个空列表 all_map，用于存储路径数据
    all_map = []
    step = 1
    # 创建一个大小为 (86+35) x (66+80) 的二维网格，并将其展平成一维列表 all_map
    for i in range(0,200,step):
        for j in range(0,200,step):
            all_map.append(0)
            
    # 构建 Excel 文件的文件名，文件名格式为 'PosTable/sub_300+subject.xlsx'
    file_name = 'PosTable/sub_'+str(subject)+'.xlsx'
    paths = []  # 初始化一个空列表 paths，用于存储每条路径的数据
    df = pd.read_excel(file_name)  # 读取 Excel 文件，并将其内容存储在 df 数据框中
    
    scale = 1  # 设置缩放比例
    path = list(all_map)  # 初始化 path 列表，复制 all_map 的内容
    index = df['index'][0]  # 获取第一个 trial 值
    # 遍历数据框中的 index 列，按比例缩放路径数据
    for i in range(math.floor(len(df)/scale)):
    # for i in range(0,len(df), 2):
        # 如果当前 index 值与之前的不同，则保存当前路径并重新初始化 path (next trial) 进入下一个trial 初始化
        # print()
        if df['index'][i]!=index:
            index = df['index'][i]
            paths.append(path)
            path = list(all_map)
            print('len paths: ', len(paths), 'new index: ', index)
            

        # 将 x 和 z 坐标四舍五入并平移到正数范围内
        x_round = np.round(df['x_pos'][i*scale]+35)
        z_round = np.round(df['z_pos'][i*scale]+81)
        # print('x round: ', x_round, 'z round: ', z_round)
        # 将坐标转换为一维索引，并在相应位置累加计数
        path[int(z_round*(85+35)+x_round)]+=1
    
    entropys = []  # 初始化一个空列表 entropys，用于存储每条路径的熵值
    # 计算每条路径的熵值
    paths.append(path)
    
    for i in paths:
        unique, counts = np.unique(i, return_counts=True)  # 计算路径中每个位置的唯一值及其出现次数
        probabilities = counts / counts.sum()  # 计算每个位置的概率分布
        # 使用 Shannon 熵公式计算熵值，并添加到 entropys 列表中
        entropys.append(-np.sum(probabilities * np.log2(probabilities)))
    return entropys, df  # 返回熵值列表


# %%
# entropys, df = path_entropy(309)
# print(len(entropys))
# print(entropys)
# df_index = df['index'].drop_duplicates()
# df_index.to_list()

# entropys, df = path_entropy(302)
# print(len(entropys))
# print(entropys)
# df_index = df['index'].drop_duplicates()
# df_index.to_list()

# 生成2个entropy的  merged + grouped table

# Example


def gen_entropy(start_participant:int, end_participant:int, writefname:str):

    df = pd.DataFrame(columns=['sub_ID','trial','trial_type','trial_describe','entropy'])

    for subject_id in range(start_participant,end_participant+1):
        print(subject_id)
        df2 = pd.DataFrame()
        entropys, ndf = path_entropy(subject_id)
        
        df2['trial'] = ndf['index'].drop_duplicates().to_list()

        c = ndf['index'].drop_duplicates().to_list()

        df_type = []
        for i in c:
            if i % 6 == 0:
                df_type.append('Memory')
            else:
                if (1+i // 6) % 2 == 1:
                    df_type.append('Space')
                else:
                    df_type.append('Social')

        df2['trial_type'] = df_type
        df2['trial_describe'] = ndf['listname'].drop_duplicates().to_list()
        df2['sub_ID'] = subject_id
        df2['entropy'] = entropys
        # 筛选entropys过小的数据
        df2 = df2[df2['entropy'] > 0.01]

            # print(get_timeTable_mean(gen_timeTable(subject_id)))
            # df2 = pd.DataFrame([[subject_id,]], columns=['sub_ID','listname','delTime','delTime_second'])
        df = pd.concat([df,df2])

    # df.to_excel('demo/demo_Nav_Entropy_Merged.xlsx', index=None)
    df['block'] = ((df['trial']-1) // 6) +1
    df.to_excel(writefname,index=None)

    return df


def gen_entropy_grouped(df: pd.DataFrame, foutname: str):

    new_df = pd.DataFrame(columns=['sub_ID','Space_Entropy','Social_Entropy','Memory_Entropy',
                                    'Space1_Entropy','Social2_Entropy','Space3_Entropy','Social4_Entropy','Space5_Entropy','Social6_Entropy',
                                    'block1_mem_Entropy','block2_mem_Entropy','block3_mem_Entropy','block4_mem_Entropy','block5_mem_Entropy','block6_mem_Entropy'
                                    ])
    for item in set(df['sub_ID']):
        print(item)
        sub_data = df[df['sub_ID'] == item]
        space_entropy = sub_data[sub_data['trial_type'] == 'Space']['entropy'].mean()
        social_entropy = sub_data[sub_data['trial_type'] == 'Social']['entropy'].mean()
        memory_entropy = sub_data[sub_data['trial_type'] == 'Memory']['entropy'].mean()

        space1_entropy = sub_data[(sub_data['block'] == 1) & (sub_data['trial_type'] != 'Memory')]['entropy'].mean()
        social2_entropy = sub_data[(sub_data['block'] == 2) & (sub_data['trial_type'] != 'Memory')]['entropy'].mean()
        space3_entropy = sub_data[(sub_data['block'] == 3) & (sub_data['trial_type'] != 'Memory')]['entropy'].mean()
        social4_entropy = sub_data[(sub_data['block'] == 4) & (sub_data['trial_type'] != 'Memory')]['entropy'].mean()
        space5_entropy = sub_data[(sub_data['block'] == 5) & (sub_data['trial_type'] != 'Memory')]['entropy'].mean()
        social6_entropy = sub_data[(sub_data['block'] == 6) & (sub_data['trial_type'] != 'Memory')]['entropy'].mean()

        block1_mem_Entropy = sub_data[(sub_data['block'] == 1) & (sub_data['trial_type'] == 'Memory')]['entropy'].mean()
        block2_mem_Entropy = sub_data[(sub_data['block'] == 2) & (sub_data['trial_type'] == 'Memory')]['entropy'].mean()
        block3_mem_Entropy = sub_data[(sub_data['block'] == 3) & (sub_data['trial_type'] == 'Memory')]['entropy'].mean()
        block4_mem_Entropy = sub_data[(sub_data['block'] == 4) & (sub_data['trial_type'] == 'Memory')]['entropy'].mean()
        block5_mem_Entropy = sub_data[(sub_data['block'] == 5) & (sub_data['trial_type'] == 'Memory')]['entropy'].mean()
        block6_mem_Entropy = sub_data[(sub_data['block'] == 6) & (sub_data['trial_type'] == 'Memory')]['entropy'].mean()

        new_df.loc[len(new_df)] = [item, space_entropy, social_entropy, memory_entropy,
                                space1_entropy, social2_entropy, space3_entropy, social4_entropy, space5_entropy, social6_entropy,
                                block1_mem_Entropy, block2_mem_Entropy, block3_mem_Entropy, block4_mem_Entropy, block5_mem_Entropy, block6_mem_Entropy]


    # new_df.to_excel('Nav_Entropy_Grouped.xlsx', index=None)
    new_df.to_excel(foutname, index=None)


# df['entropy'].describe()
# # %%

# df['listname'].unique().to_list()

# # %%
# df['entropys']

# # %%
# entropys = path_entropy(40)
# print(len(entropys))
# entropys

def process(pstart, pend, pstart2, pend2):
    cond1 = 'space'
    cond2 = 'social'



    entropy_file = 'Trajectory_Tables/Nav_Entropy_Merged.xlsx'
    entropy_file_grouped = 'Trajectory_Tables/Nav_Entropy_Grouped.xlsx'

    gen_approach_leave_speed(pstart, pend, cond1)
    gen_approach_leave_speed(pstart, pend, cond2)

    data = gen_entropy(pstart2,pend2, entropy_file)

    gen_entropy_grouped(data, entropy_file_grouped)



if __name__ == '__main__':

    # gen_approach_leave_speed(start_participant, end_participant, condition):

    cond1 = 'space'
    cond2 = 'social'
    
    start_participant1 = # approach to leave and close speed and time
    end_participant1 = 

    start_participant2  # entropy
    end_participant2 = 

    process(start_participant1, end_participant1, start_participant2, end_participant2)


