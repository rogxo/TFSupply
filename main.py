import datetime as dt
import os
import random
import time

import requests
from matplotlib import image as img, pyplot as plt


def login(s):
    img_url = 'http://tf.8yx.com/Base/verify_code.html?rand=0.07185286412285707'
    image = s.get(img_url)
    f = open('verify_code.jpg', 'wb')
    f.write(image.content)
    f.close()
    username = input("账号:")
    password = input("密码:")
    open_image()
    login_code = input("验证码:")
    login_url = 'http://tf.8yx.com/Auth/Member/doLogin.html'
    login_headers = {
        'Host': 'tf.8yx.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '99',
        'Origin': 'http://tf.8yx.com',
        'Connection': 'close',
        'Referer': 'http://tf.8yx.com/active/sign'}
    login_data = {'username': username,
                  'password': password, 'login_code': login_code}
    res = s.post(login_url, headers=login_headers, data=login_data)
    time.sleep(3)
    print((eval(res.text))["info"])
    if (eval(res.text))["status"] == 0:
        input("按任意键继续")
        exit()


def logout(s):
    url = 'http://tf.8yx.com/Auth/Member/loginout.html'
    s.post(url)


def open_image():
    lena = img.imread('verify_code.jpg')
    plt.imshow(lena)
    plt.axis('off')
    plt.show()


def fetch_score(s):
    # print('test')
    url = 'http://tf.8yx.com/Active/centretask.html'
    headers = {
        'Host': 'tf.8yx.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '90',
        'Origin': 'http://tf.8yx.com',
        'Connection': 'close',
        'Referer': 'http://tf.8yx.com/active/Supplypackage1'}

    data = {'id': '1011'}
    now_date_time = int(dt.datetime.now().strftime('%j'))
    for i in range(5):
        time.sleep(3)
        data['id'] = str(now_date_time + 100 + random.randint(0, 10000))
        try:
            res = s.post(url, headers=headers, data=data)
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        print("正在刷取活跃值。。。")
        try:
            if res:
                print((eval(res.text))["info"])
        except Exception:
            print(res.text)


def fetch_medal(s):
    url = 'http://tf.8yx.com/Active/centreact.html'
    headers = {
        'Host': 'tf.8yx.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '90',
        'Origin': 'http://tf.8yx.com',
        'Connection': 'close',
        'Referer': 'http://tf.8yx.com/active/Supplypackage'}
    data = {'id': '1'}
    for i in range(1, 6):
        time.sleep(3)
        data['id'] = str(i)
        # res = s.post(url, headers=headers, data=data)
        try:
            res = s.post(url, headers=headers, data=data)
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        print("正在领取勋章。。。")
        try:
            if res == {}:
                time.sleep(3)
            print((eval(res.text))["info"])
        except Exception:
            print(res.text)


if __name__ == '__main__':
    now_time = dt.datetime.now().strftime('%j')
    os.system("title 后勤补给刷取工具_v1.0  --by诸葛")
    judge = input("各位大佬游戏中少爆点诸葛的头?(y/n)")
    if judge != "y" and judge != "Y" and judge != "":
        exit()
    session = requests.session()
    login(session)
    fetch_score(session)
    fetch_medal(session)
    logout(session)
    input("祝各位新春快乐\n")
