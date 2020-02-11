# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import csv
import urllib.request
import random

proxy_list = [
    {"http" :'183.95.80.102:8080'},
    {"http" :'123.160.31.71:8080'},
    {"http" :'115.231.128.79:8080'},
    {"http" :'166.111.77.32:80'},
    {"http" :'43.240.138.31:8080'},
    {"http" :'218.201.98.196:3128'}
]

# 收集到的常用Header
my_headers = [
    {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
    {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
    {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"},
    {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"},
    {'User-Agent': "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'},
    {'User-Agent': 'Opera/9.25 (Windows NT 5.1; U; en)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
    {'User-Agent': 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'},
    {'User-Agent': 'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'},
    {'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7"},
    {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "}
]
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
# }

pwd = os.getcwd()
pwd = os.path.join(pwd, '样本')
names = []
jianjie = []
quanxian = []
qxshuoming = []
dlurl = []

server = 'https://appstore.huawei.com'
target = 'https://appstore.huawei.com/app/C10336398'



def deal_url(url):
    req = requests.get(url, headers=random.choice(my_headers), proxies=random.choice(proxy_list),timeout = 2)
    req.encoding = 'utf-8'
    return req.text


def deal(html):
    global names, jianjie, quanxian, qxshuoming, dlurl
    bf = BeautifulSoup(html, 'lxml')

    # 名称
    div = bf.find_all('span', class_='title')
    s = str(div[0].string)
    names.append(s)
    # print(s)

    # 简介
    div = bf.find_all('div', id='app_desc')
    div_bf = BeautifulSoup(str(div), 'lxml')
    div_str = str(div_bf)
    div_str = (div_str.replace('<br>', '')).replace('<br/>', '')
    bf_jianjie = BeautifulSoup(div_str, 'lxml')
    con = bf_jianjie.find_all('div')
    s = str(con[0].string)
    jianjie.append(s)
    # print(s)

    # 权限
    ul = bf.find_all('ul', class_="hidepermission")
    li = BeautifulSoup(str(ul), 'lxml')
    qx = li.find_all('li', class_='hide')
    f = 0
    tmp1 = ''
    tmp2 = ''
    for i in qx:
        if i.string == '敏感隐私权限用途说明：':
            f = 1
            continue
        if f == 0:
            tmp1 = tmp1 + i.string + '\n'
        else:
            tmp2 = tmp2 + i.string + '\n'
    quanxian.append(tmp1)
    qxshuoming.append(tmp2)

    # 下载
    dl = bf.find_all('a', class_='mkapp-btn mab-download')
    s = dl[0].get('onclick')
    t = s.split(',')
    t = t[5][1:]
    t = t.strip("'")
    t = t.replace("'", '')
    dlurl.append(t)


def deal_page(html, id):
    global names, jianjie, quanxian, qxshuoming, dlurl

    ul = []
    ubase = 'https://appstore.huawei.com/soft/list_'
    for i in range(1, 2):
        tmp = ubase + str(id) + '_0_' + str(i)
        ul.append(tmp)
    # print(ul)
    for uu in ul:
        htm = deal_url(uu)
        bf = BeautifulSoup(htm, 'lxml')
        div = bf.find_all('div', class_='list-game-app dotline-btn nofloat')
        for i in div:
            bf2 = BeautifulSoup(str(i), 'lxml')
            u = bf2.find_all('a')
            u = u[0].get('href')
            url = server + u
            ht = deal_url(url)
            deal(ht)


def change_sort(html):
    global names, jianjie, quanxian, qxshuoming, dlurl

    bf = BeautifulSoup(html, 'lxml')

    a = bf.find_all('a', class_='link-dblue txt-sml')
    for i in a:
        names = []
        jianjie = []
        quanxian = []
        qxshuoming = []
        dlurl = []
        clname = i.string
        url = server + i.get('href')
        no = url.split('_')
        id = no[1]
        ht = deal_url(url)
        deal_page(ht, id)
        sz = len(jianjie)
        twd = os.path.join(pwd, clname)
        if not os.path.exists(twd):
            os.makedirs(twd)
        appwd = os.path.join(twd, 'app')
        if not os.path.exists(appwd):
            os.makedirs(appwd)
        fname = os.path.join(twd, 'detail.csv')
        with open(fname, 'w+') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            head = ['名称', '简介', '权限', '敏感隐私权限用途说明', '下载地址']
            spamwriter.writerow(head)
            for j in range(sz):
                ddlurl = dlurl[j]
                nnames = names[j]
                ap = os.path.join(appwd, nnames + '.apk')
                try:
                    urllib.request.urlretrieve(ddlurl, ap)
                except:
                    continue
                info = []
                print(nnames)
                info.append(names[j])
                info.append(jianjie[j])
                info.append(quanxian[j])
                info.append(qxshuoming[j])
                info.append(dlurl[j])
                spamwriter.writerow(info)



if __name__ == "__main__":
    t2 = 'https://appstore.huawei.com/soft/list'
    html2 = deal_url(t2)
    change_sort(html2)
