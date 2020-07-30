#!/usr/bin/env python
# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

cookie = '__mta=222264615.1595669226302.1595770485224.1595770677085.8; uuid_n_v=v1; uuid=FFB18790CE5811EAB0594FFAA70EE9CE2172607F3ADF4964BFFC75C12AB37926; _csrf=f9e1373a918a44874bc9ef122158964727dbd21841e9895c0c90254d9dba2b5f; _lxsdk_cuid=173854c22f8c8-0e37d274b20583-31617402-13c680-173854c22f9c8; _lxsdk=FFB18790CE5811EAB0594FFAA70EE9CE2172607F3ADF4964BFFC75C12AB37926; mojo-uuid=aa75919ef8a0fbca814a242f58cd6806; mojo-session-id={"id":"a047a26c6a641386c05bca528ef07ec1","time":1595809798632}; lt=fEi_ehrO9NehMM-JygW7mi8mlgAAAAAAOQsAAPJO4BApZvxrHcCkbXEiUOteaot9Du2fTk4ma6m6lNWQ-RCnc2efq2AtJ9z2Yhsu7g; lt.sig=9TY61OLCbwXe1i7eHXxGQVXmtVY; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595669226,1595809972,1595811318; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595812069; __mta=222264615.1595669226302.1595770677085.1595812069146.9; _lxsdk_s=1738dad054b-d8a-e59-2b9%7C%7C11'

header = {'User-Agent': user_agent, 'Cookie': cookie}
myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')

MOVIE_COUNT = 10
i = 0
movie_names = []
movie_type = []
movie_date = []

for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    print(f"tags:{tags}")
    if i == MOVIE_COUNT:
        break
    i += 1
    for j, atag in enumerate(tags.find_all('div')):
        if j == 0:
            movie_names.append(atag.text.strip().split("\n")[0])
        elif j == 1:
            movie_type.append(atag.text.strip().split("\n")[1].strip())
        elif j == 3:
            movie_date.append(atag.text.strip().split("\n")[1].strip())
file = pd.DataFrame({'movie_name': movie_names, 'movie_type': movie_type, 'movie_date': movie_date})
file.to_csv("./manyan_movie.csv",index=False)


