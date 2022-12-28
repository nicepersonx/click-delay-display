import time, win32api

# In case you want to replace the key that it uses to calculate delay
# 0x01 is the virtual key code for left click, you can find more codes here:
# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

code = 0x01
count = 0
while True:
    t1 = time.time()
    val = win32api.GetKeyState(code)
    while True:
        if val != win32api.GetKeyState(code):
            done = time.time()-t1
            count += 1
            print("Click #{}\n{}".format(count,done))
            while True:
                z = win32api.GetKeyState(code)
                if z == 0 or z == 1:
                    break
            break
