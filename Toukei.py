import csv
import statistics
import re

Jinkou = [] #人口総数を配列として格納するため

with open('./People_Toukei.csv','r',encoding='UTF-8') as f:
    toukei = csv.reader(f)

    for line in toukei:
        if ('000' in str(line[0])): # コードの列に000という文字列(連続した数字)が並んでいるか
            Jinkou.append(str(line[2])) # "総数"の列項目だけを格納。この状態では47都道府県と全人口のデータが格納されてる
    
    del Jinkou[0] # 全国の人口データを削除

    for h in range(47):
       Jinkou[h] = re.sub(r'[,]', '', Jinkou[h]) # CSVの総数文字列内にあった",(桁区切り)"を削除

    Jinkou = list(map(int, Jinkou)) # 文字列である配列を数値型に変換
    Jinkou = sorted(Jinkou, reverse=True) #リストを降順にソート

    # print(Jinkou) # 配列が機能しているかの確認用

###################################################################################################
# 基本統計量を求める　今回はimportしたstatisticeを用いる

Heikin = statistics.mean(Jinkou) # 平均
Tyuou = statistics.median(Jinkou) # 中央値
Max = Jinkou[0] # 最大値　既にソートしてあるため最初の値が最大値
Min = Jinkou[46] # 最小値　最大値と同様に最後の値が最小値
Bunsan = statistics.variance(Jinkou) # 分散  標本分散の方
Hhensa = statistics.stdev(Jinkou) # 標準偏差  標本標準偏差の方

##########################################################################
# 以下は表示

print() # 見やすさを意識
print("都道府県毎の平均人口は、%d 人です" %Heikin)
print("都道府県毎の人口の中央値は、%d 人です" %Tyuou)
print("都道府県で最大の人口は %d 人です" %Max)
print("都道府県で最小の人口は %d 人です" %Min) # ここまでは整数(小数点以下は切り捨て)
print("都道府県毎の人口の分散は、%f です" %Bunsan)
print("都道府県毎の人口の標準偏差は、%f です" %Hhensa)
print() # 37行目と同様
