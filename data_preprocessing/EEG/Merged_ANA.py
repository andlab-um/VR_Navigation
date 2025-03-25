import mne
import os

import Test_Crop as TC
import Rest_State_Crop as RSC

### concatenate_raws 整合不同的raw脑电数据

# d = [i for i in os.listdir('Preprocessed_Data_FIF_I') if i.endswith('.fif')]
fif_dir = 'Test'
# 假设所有 FIF 文件都在同一个文件夹中
# fif_dir = 'Test_ICAed'
fif_files = os.listdir(fif_dir)


def join_EEG(label: str):

    for f in fif_files :
        if f.endswith('.fif') and f.startswith(label):
            print(f)

    # 读取所有 FIF 文件并创建 Raw 对象的列表
    raws = [mne.io.read_raw_fif(os.path.join(fif_dir, f), preload=True) 
            for f in fif_files if f.endswith('.fif') and f.startswith(label)]

    # 拼接所有 Raw 对象

    # for ritem in raws:
    #     ritem.plot(title= 'Single | '+label, duration=10, block=True)

    raws_concatenated = mne.concatenate_raws(raws)
    raws_concatenated.plot(title= 'Merged | '+label, duration=10, block=True)
    # 保存拼接后的 Raw 对象 
    raws_concatenated.save(fif_dir + '/'+label+'_M.fif', overwrite=True)


labels = ['s'+str(i) for i in range(358,361)]
print(labels)
for label in labels:
    join_EEG(label)



# Notice: 先不做ERP和时频分析，只做去坏导 ICA 生成Epoch 三个工作 生成的结果放到Test_Epoch文件夹中


