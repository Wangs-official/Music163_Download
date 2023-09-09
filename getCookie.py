# 获取Cookie并存储到cookie.json，用于获取 喜欢的音乐 歌单和下载VIP歌曲（前提你得有VIP）
import time
print('Music163Download 作者：Wangs_official')
print('欢迎使用,请先执行命令：pip3 install -r requirements.txt 将在3秒后继续')
time.sleep(3)
# import库
import requests
import json
import os
from colorama import Fore, Back, Style
import getpass
# 这里设置下全局请求URL（我就是懒）
apiurl = 'https://m163.a.vercel.stardawn.xyz/'
# 让用户登录自己的网易云
print('这个脚本用于获取您的Cookie信息（保存到本地）Cookie仅用于用于获取 喜欢的音乐 歌单和下载VIP歌曲（前提你得有VIP）')
phone_code = input('请输入您的账号（手机号码）：')
countrycode = input('输入国家码（中国填86）：')
user_password = getpass.getpass('请输入您的密码（不显示，输入后回车即可）：')
time.sleep(1)
# 发送登录请求
print(Back.BLUE + '正在登录...')
login_back = requests.get(apiurl + '/login/cellphone?phone=' + phone_code + '&password=' + user_password + '&countrycode=' + countrycode)
# 判断返回状态码
print(Style.RESET_ALL)
if login_back.status_code == 200 :
    # 返回200，可以获取cookie了
    origin_login_back_json = json.loads(login_back.text)
    cookie_value = origin_login_back_json.get("cookie")
    user_name = origin_login_back_json.get("profile" , {}).get("nickname")
    with open("cookie.txt" , "w") as ck_file:
        ck_file.write(cookie_value)
    # 写入完毕，反馈，终止
    print(Fore.GREEN + '欢迎您！' + user_name + '，Cookie文件已保存到cookie.txt文件，请妥善保存！五秒后退出')
    time.sleep(5)
    exit()
else:
    # 返回其他，反馈，终止
    print(Fore.RED + '出现错误!这是错误代码：' + login_back.status_code + '这是返回内容：\n' + login_back.text + '\n 五秒后退出')
    time.sleep(5)
    exit()