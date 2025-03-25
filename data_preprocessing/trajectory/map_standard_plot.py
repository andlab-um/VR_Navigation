import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns
import os
import plotly.offline as offline
import plotly
import base64





def draw_tra(subdata: pd.DataFrame, block: int):

    blockpos = pd.read_excel('blockpos.xlsx')
    blockpos = blockpos[blockpos['block'] == block]
    avatar = pd.read_excel('avatar_info.xlsx')

    mark = ''
    dy = 0
    if block % 2 != 0:
        avatar = avatar[avatar['type'] == 'Case']
        mark = 'Case'
        dy = 0.495 # Image trajectory calibration

    else:
        avatar = avatar[(avatar['type'] == 'RoleM')|(avatar['type'] == 'RoleF')]
        mark = 'Role'
        dy = 0.505  # Image trajectory calibration

    avatar_p = avatar[avatar['Reward_Punish'] == 'Punishment']
    avatar_r = avatar[avatar['Reward_Punish'] == 'Reward']

    fig = px.scatter()
    fig.add_scatter(
        x=subdata['x_pos'], 
        y=subdata['z_pos'], 
        mode='markers', 
        name='Participant', 
        marker=dict(color='red', size=0.5)
    )
    # please differ dots in different cases
    # fig.add_scatter(
    #     x=avatar['posx'], 
    #     y=avatar['posy'], 
    #     mode='markers', 
    #     name=mark, 
    #     marker=dict(color='yellow',size=15)
    # )

    fig.add_scatter(
    x=avatar_r['posx'], 
    y=avatar_r['posy'], 
    mode='markers', 
    name= mark+'-Reward', 
    marker=dict(color='yellow',size=15)
    )

    fig.add_scatter(
        x=avatar_p['posx'], 
        y=avatar_p['posy'], 
        mode='markers', 
        name=mark+'-Punish', 
        marker=dict(color='blue',size=15)
    )



    fig.add_scatter(
        x=blockpos['block_posx'], 
        y=blockpos['block_posy'], 
        mode='markers', 
        name='Road Block', 
        marker=dict(symbol='x', color='white', size=15)
    )

    # 添加标题
    fig.update_layout(
        title='Trajectory',
        font=dict(color='white', size=16, weight='bold'),
        title_x=0.5,  # 将标题的x位置设置在中间
        title_y= 0.92,  # 将标题的y位置设置在图表的底部
        title_xanchor='center',
        title_yanchor='bottom'  
            # 设置标题字体颜色、大小和粗细
        )

    # 将点阵颜色变成红色
    # fig.update_traces(marker=dict( size=15))

    # 显示坐标的x和y，保留两位小数
    fig.update_traces(hovertemplate='(%{x:.2f}, %{y:.2f})')

    # 背景颜色变成白色
    # fig.update_layout(plot_bgcolor='white')
    with open('bacgnd.png', 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    # 将 Base64 编码的图片嵌入图表中
    fig.add_layout_image(
        dict(
            source=f'data:image/png;base64,{encoded_image}',
            xref='paper',
            yref='paper',
            x=0.48,
            y=dy,
            sizex=1.05,
            sizey=14.2,
            xanchor='center',
            yanchor='middle',
            layer='below'
        )
    )

    # 设置图表的宽度和高度（以像素为单位）
    fig.update_layout(
        width=int(800), 
        height=int(785),
        paper_bgcolor='black',  # 设置图表外围背景颜色
        plot_bgcolor='black'    # 设置图表内部背景颜色
        )

    # fig.update_xaxes(showgrid=True,dtick=5)
    # fig.update_yaxes(showgrid=True,dtick=5)

    # fig.write_image('plot_mul_block'+str(block)+'.png')
    offline.plot(fig, filename='plot_mul_block_II_'+str(block)+'.html', auto_open=False)


def set_block_inf(sub_s:int, sub_ed:int,block:int):
    
    subdata = pd.DataFrame()
    for num in range(sub_s,sub_ed):
        df = pd.read_excel('PosTable/sub_'+str(300+num)+'.xlsx')
        df = df.drop_duplicates(subset=['x_pos','z_pos'], keep='last')
        if block == 1:
            df = df[(df['index'] < 6)]

        elif block == 2:
            df = df[(df['index'] > 6) & (df['index'] < 12) ]
        elif block == 3:
            df =df[(df['index'] > 12) & (df['index'] < 18) ]
        elif block == 4:
            df =df[(df['index'] > 18) & (df['index'] < 24) ]
        elif block == 5:
            df =df[(df['index'] > 24) & (df['index'] < 30) ]
        else:
            df =df[(df['index'] > 30) & (df['index'] < 36) ]


        subdata = pd.concat([subdata, df])   
    print('Data Merged Ready...')
    return subdata



if __name__ == '__main__':

    for block in range(1,7):
        print('Block: ', block)
        subdata = set_block_inf(15,48,block) # 327-347
        draw_tra(subdata,block)


    
    
