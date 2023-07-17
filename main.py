import pandas as pd


#读入数据
df = pd.DataFrame(pd.read_excel('G:/hwt/498.xlsx'))

#处理空值
df.loc[:,"TP"] = df["TP"].fillna(-1)
df.loc[:,"TN"] = df["TN"].fillna(-1)

zl_ls = []
zd_ls = []
time_ls = []

# 把需要的列数据读进来
for i in df['time']:
    i = str(i)
    time_ls.append(i)
for i in df['TP']:
    zl_ls.append(i)
for i in df['TN']:
    zd_ls.append(i)

x = time_ls[0][:6]
wait_lls = []
wait_dls = []
ind = 0
d_cnt = 0
l_cnt = 0

for i in time_ls:
    if(x == i[:6]):
        if(zl_ls[ind] != -1):
            l_cnt += 1
            wait_lls.append(zl_ls[ind])
        if(zd_ls[ind] != -1):
            d_cnt += 1
            wait_dls.append(zd_ls[ind])
    else:
        temp1 = 0
        temp2 = 0
        for num in wait_lls:
            temp1 += num
        for num in wait_dls:
            temp2 += num
        # print('磷cnt：%d sum:%f 氮cnt:%d sum:%f'%(l_cnt,temp1,d_cnt,temp2)) 这句是用于查错的
        
        temp1 /= l_cnt
        temp2 /= d_cnt
        print('%s :       %f          %f'%(x,temp1,temp2))
        l_cnt = 0
        d_cnt = 0
        wait_lls = []
        wait_dls = []
        x = i[:6]
        if(zl_ls[ind] != -1):
            l_cnt += 1
            wait_lls.append(zl_ls[ind])
        if(zd_ls[ind] != -1):
            d_cnt += 1
            wait_dls.append(zd_ls[ind])
    ind += 1




