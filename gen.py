import random
import csv
import datetime

class Daily_Sword:
    def __init__(self,r_csv,name,up,total):
        self.select_swords=[]
        self.all_list=[]
        self.upper_swords=[]
        self.n=0
        self.up=up
        self.total=total
        self.name=name
        self.r_csv=r_csv
    
    #CSV読み込み(ヘッダ削除機能付き)
    def regist_csv(self):
        file_name="data/"+self.r_csv
        with open(file_name,encoding='utf-8') as f:
            reader=csv.reader(f)
            for x in reader:
                self.all_list.append(x)
        self.all_list=self.all_list[1:]
    
    #存在可否判定
    def exist_check(self,name):
        flag=False
        for x in self.select_swords:
            if(name==x):
                flag=True
                break
        return flag

    #乱数生成
    def gen_num(self):
        self.n=random.randint(0,9999)

    #新顔枠探索・決定
    def regi_newface(self):
        for x in self.all_list:
            if(int(x[2])==2):
                self.select_swords.append([x[0]])
                break
    
    #優先枠探索
    def regi_upper_swords(self):
        for x in self.all_list:
            if(int(x[2])==1):
                self.upper_swords.append(x[0])
    
    #優先枠決定
    def select_up_swords(self):
        self.regi_upper_swords()
        buff=random.sample(self.upper_swords,self.up)
        for x in buff:
            self.select_swords.append([x])

    
    #ランダム枠決定
    def regist_random(self):
        self.gen_num()
        buff=""
        for x in range(1,len(self.all_list)-1):
            if(int(self.all_list[x-1][1])<=self.n)and(self.n<int(self.all_list[x][1])):
                buff=self.all_list[x][0]
                break

        if(0<=self.n) and (self.n<int(self.all_list[0][1])):
            buff=self.all_list[0][0]
        
        if not(self.exist_check(buff)):
            self.select_swords.append([buff])
    
    #セーブ
    def save(self):
        file_name=self.name
        today=str(datetime.date.today())
        with open(file_name,encoding='utf-8') as f:
            check=csv.reader(f)
            for x in check:
                if not(x[0]==today):
                    with open(file_name,'w',encoding='utf-8') as z:
                        self.select_swords.insert(0,[str(today)])
                        writer=csv.writer(z,lineterminator='\n')
                        writer.writerows(self.select_swords)
                break

    #全体登録用
    def run_generate(self):
        self.regist_csv()
        self.regi_newface()
        self.select_up_swords()
        
        while True:
            if(len(self.select_swords)>=self.total):
                break

            self.regist_random()
        
        self.save()
        
tonkatsu=Daily_Sword('tonkatsu.csv','とんかつそーす.csv',2,6)
tonkatsu.run_generate()


oister=Daily_Sword('oister.csv','おいすたーそーす.csv',2,6)
oister.run_generate()
