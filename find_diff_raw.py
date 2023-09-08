import cv2
import numpy as np
import pyautogui
from tkinter import Tk, Button, Label, Image, PhotoImage
from PIL import Image, ImageTk

def screenshot():
    # 截屏
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # 在截屏中找到小图片 a.png 的位置
    template = cv2.imread('a.png', 0)
    screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x, y = max_loc

    # 在截屏中扣取两个小图
    x1, y1 = 10, 10  # 这里您可以根据需要调整
    length, width = 50, 50  # 这里您可以根据需要调整
    roi1 = screenshot_rgb[y:y+width, x+x1:x+x1+length]
    roi2 = screenshot_rgb[y+y1:y+y1+width, x+x1:x+x1+length]

    # 比较两个小图每个像素的差别
    diff = cv2.absdiff(roi1, roi2)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    roi1[thresh == 255] = [0, 0, 255]

    # 保存
    cv2.imwrite('diff.png', roi1)

    # 展示
    img = Image.open('diff.png')
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

# GUI
root = Tk()
root.title("截屏比较工具")

btn = Button(root, text="截屏并比较", command=screenshot)
btn.pack(pady=20)

label = Label(root)
label.pack(pady=20)

root.mainloop()
