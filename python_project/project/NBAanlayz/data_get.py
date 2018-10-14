#!/bash/bin/
import requests
import numpy as np
import pandas as pd
import json
import sys
class NBAspder(object) :

    def __init__(self,start_url,fdir):
        self.start_url = start_url
        self.dir = fdir

    def get_url(self) :
        base_url = self.start_url
        varl = [chr(i) for i in range(65,91)]
        pageNo_list = [base_url + n + '.json' for n in varl]
        self.url_list = pageNo_list

    def get_text(self) :
        resu_dic = []
        for l in self.url_list :
            response  = requests.get(l)
            resp = response.content.decode("utf-8")
            text = json.loads(resp)
            list_dic = text['payload']['players']
            resu_dic += list_dic

        self.get_josn = resu_dic

    def trans_dataf(self) :
        l_p = []
        n = 0
        da1 = self.get_josn
        while n < len(da1) :
            da_t = da1[n]['playerProfile']
            da_t['player_code'] = da_t['code']
            da_t.pop('code')
            da_t['player_leagueId'] = da_t['leagueId']
            da_t.pop('leagueId')
            da_t1 = da1[n]['teamProfile']
            da_t1['team_code'] = da_t1['code']
            da_t1.pop('code')
            da_t1['team_leagueId'] = da_t1['leagueId']
            da_t1.pop('leagueId')
            l_p.append(dict(da_t,**da_t1))
            n += 1
            da2 = pd.DataFrame(l_p)
        self.get_content = da2

    def write_to_file(self):

        self.get_content.to_csv(self.dir, encoding='utf-8', index=False)

#'http://china.nba.com/static/data/league/playerlist_','/Users/didiw/Documents/study/NBAanlayz/res1.csv'
#python3 data_get.py 'http://china.nba.com/static/data/league/playerlist_' '/Users/didiw/Documents/study/NBAanlayz/res1.csv'
if __name__ == '__main__':
    Nurl = sys.argv[1]
    Nwd = sys.argv[2]
    NBAs = NBAspder(Nurl,Nwd)
    NBAs.get_url()
    NBAs.get_text()
    NBAs.trans_dataf()
    NBAs.write_to_file()
