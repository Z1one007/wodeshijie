import os
import time
import keyboard
import pyautogui
from termcolor import colored
from colorant import Colorant
from datetime import datetime 


# 获取当前时间  
now = datetime.now()  
  
# 显示时间  
print("当前时间：", now.strftime("%Y-%m-%d %H:%M:%S")) 
   
#Settings
TOGGLE_KEY = 'F1'  # Colorant开关
XFOV = 60  # X-Axis FOV范围
YFOV = 60  # Y-Axis FOV范围
INGAME_SENSITIVITY = 0.45 # 游戏内灵敏度
FLICKSPEED = 1.07437623 * (INGAME_SENSITIVITY ** -0.9936827126)  # 扳机速度
MOVESPEED = 1 / (5 * INGAME_SENSITIVITY) # 自瞄速度

monitor = pyautogui.size()
CENTER_X, CENTER_Y = 1920 // 2, 1080 // 2 # 分辨率数值2不要动

def main():
    os.system('title Colorant Pro')
    colorant = Colorant(CENTER_X - XFOV // 2, CENTER_Y - YFOV // 2, XFOV, YFOV, FLICKSPEED, MOVESPEED)
    print(colored('''
                                                                              
               ██                                                             
             █████                                              ██████        
            ███ ██        ███                                 █████████       
           ███ ██        ███                           █      ███ █  ███      
          ███  ██        ███                         ████        ██   ██      
          ██ ███   ███  ███  ███  ███     ███     █ ████         █   ██ ███   
         ██ ███   ████  ██  ████ ████   █████ █████  ██        ████ ███████  █
        ███ ██   █████ ██  █████ ███   ███ █ █████  ██        ████████ ███  ██
        ██  █   ███ ██ ██ ███ ██ ███ █ ██ ██ ████████  █      ██████   ███ ███
        ██     █ █████ █████████  ███  ████████ ███████       ██        ███ ██
        ██   ██   ██   ███  ██    ██    █ ██ █  ██ ███        ██        ██   █
        ██████                                                █               
        █████                                                                 
                                                                              
                                                                              
                                              COLORANT PRO - v12.1''', 'magenta'))
    print()
    print(colored('[信息]', 'green'), colored('设置敌人颜色为', 'white'), colored('紫色', 'magenta'))
    print(colored('[信息]', 'green'), colored(f'按下 {colored(TOGGLE_KEY, "magenta")} 来打开或关闭 Colorant', 'white'))
    print(colored('[信息]', 'green'), colored(f'按下', 'white'), colored('F2', 'magenta'), colored('来打开或关闭Coloran中心视窗', 'white'))
    print(colored('[信息]', 'green'), colored('长按鼠标右键', 'magenta'), colored('= 自瞄,', 'white'))
    print(colored('[信息]', 'green'), colored('左ALT', 'magenta'), colored('= 自动扳机', 'white'))
    print(colored('[信息]', 'green'), colored('别管！', 'magenta'), colored('= 别管！', 'white'))
    print(colored('[信息]', 'green'), colored('QQ账号:', 'white'),
          '\033[35;4mQQ864613558\033[0m')
    print(colored('[信息]', 'green'), colored('2024', 'white'), colored('Tiankong#54763', 'magenta'))
    status = '未启动'
    
    
    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                colorant.toggle()
                status = '启动 ' if colorant.toggled else '未启动'
            print(f'\r{colored("[启动状态]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[信息]', 'green'), colored('Exiting...', 'white') + '\n')
    finally:
        colorant.close()

if __name__ == '__main__':
    main()
