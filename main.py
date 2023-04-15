# 玄予（xuanyu）
# 2023/4/15
# git：git.xuanyu.info

import keyboard
from playsound import playsound
import threading
import os
import random

# 播放声音
def play():
    result = random.randint(0,len(sound_list) - 1)
    playsound('sound/' +  sound_list[result])

# 按下键盘
def Press(x):
    if x.event_type == 'down':
      threading.Thread(target=play).start()
        
# 入口函数
if __name__ == '__main__':
    sound_list  = os.listdir('./sound')
    keyboard.hook(Press)
    keyboard.wait()
  


