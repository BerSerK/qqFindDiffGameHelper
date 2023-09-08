这是一个QQ找茬游戏的小外挂。

1. 需要安装如下python 包:

```
pip install opencv-python pillow pyautogui tkinter
```

2. 使用方法:

```
python find_diff.py
```

然后，不要让弹出来的窗口盖住QQ找茬游戏的窗口，点"截屏并比较"按钮，窗口中图片被涂成红色部分就是“不同”的位置。

3. 我对chatGPT描述了需求:
```
给我写一个 windows 下的 python 程序。
1. 截屏
2. 在截屏中找到小图片 a.png 的位置 x, y.
3. 在截屏中扣取两个小图长宽分别为 length, width, 小图的左上角分别为 x + x1, y 和 x + x1, y + y1
4. 比较两个小图每个像素的差别，在第一个小图上把不一样的部分标成红色，保存。

做一个带一个按钮的图形界面运行这段程序，点击按钮时运行。并在一个窗口中展示标红之后的小图。并且每次点击按钮时还在之前的窗口中展示新图，不开新窗口.
```
它给我了代码 find_diff_raw.py， 我在github copilot的帮助下修改成了find_diff.py的样子，并且实测好用。