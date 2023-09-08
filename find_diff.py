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
    template = cv2.imread('anchor.png', 0)
    screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x, y = max_loc
    print("anchor position:", x, y)

    # 在截屏中扣取两个小图
    x1, y1 = 92, 311  # 这里您可以根据需要调整
    length, width = 382, 287  # 这里您可以根据需要调整
    # 获取 合适的 x2
    min_x2 = x1 + length + 100
    min_x2_diff = 1e8
    for x2 in range(x1 + length, x1 + length + 100):
        roi1 = screenshot_rgb[y+y1:y+y1+width, x+x1:x+x1+length]
        roi2 = screenshot_rgb[y+y1:y+y1+width, x+x2:x+x2+length]
        diff = cv2.absdiff(roi1, roi2) # 比较两个小图每个像素的差别, 尽量小
        diff_sum = np.sum(diff)
        if diff_sum < min_x2_diff:
            min_x2_diff = diff_sum
            min_x2 = x2
    
    x2 = min_x2
    print("x2:", x2, " x2 - x1:", x2 - x1)
    roi1 = screenshot_rgb[y+y1:y+y1+width, x+x1:x+x1+length]
    roi2 = screenshot_rgb[y+y1:y+y1+width, x+x2:x+x2+length]

    #save roi1 and roi2
    cv2.imwrite('roi1.png', roi1)
    cv2.imwrite('roi2.png', roi2)

    # 比较两个小图每个像素的差别
    diff = cv2.absdiff(roi1, roi2)
    # 保存diff
    cv2.imwrite('diff1.png', diff)
    # 将roi1差别值大于25的像素设置为红色
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    th = 25
    imask = mask > th
    canvas = np.zeros_like(roi1, np.uint8)
    canvas[imask] = (0, 0, 255)
    roi1[imask] = (0, 0, 255)
    
    # 放大两倍并保存
    roi1 = cv2.resize(roi1, (0, 0), fx=2, fy=2)
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
