import datetime as dt
from encodings import utf_8_sig
import pandas as pd
import numpy as np

#読み込むfilename
filename="CT-FY21.xlsx"

#エクセル読み込み
df = pd.read_excel(rf"" ,sheet_name="")

#Columnsの追加
df["Problem"]=""
df["PLAN OF ACTION"]=""
df["EXPECTED COLLECTION DATE"]=""
df["Month"]=dt.datetime.now().strftime("%b %d")
df["TI"]=df["DEP"]
df["Age Category"]=str("")
df["Site ID"]="JP"
df["Type"]="Travel"
df["DUE DATE"]=""
df["AGE DUE DATE"]=""

#columnsの並び替え
df = df[['Problem',"PLAN OF ACTION","EXPECTED COLLECTION DATE","Month","TI","Age Category",
       "Site ID","Type",'FY', 'EOE', 'APC', 'ODC', 'DOCNR', 
       'DISBURSE', 'DISBJD', "DUE DATE",
       'DISB AGE',"AGE DUE DATE", 'PD1', 'PD2', 'QTY', 'DEP', 'BS', 'LMT', 'PY',
       'OA', 'RD', 'ASN', 'AMS', 'FSN', 'LC']][0:]


#"DISBURSE"ゼロの行を消す
df = df.query("DISBURSE != 0")


#DUE DATE,AGE DUE DATEの計算
df["DUE DATE"]=df["DISBJD"]+30
df["AGE DUE DATE"]=df["DISBJD"]-df["DUE DATE"]+df['DISB AGE']


#AGE DUE DATE 28日以内を抽出
df = df.query("`AGE DUE DATE` > -29")
#AGE DUE DATE数が少ない順に並び替え
df.sort_values("AGE DUE DATE",inplace=True)


#numpyで条件分岐でセルに追加#########################3
conditions =[df["AGE DUE DATE"] <= 0,df["AGE DUE DATE"] <= 30,df["AGE DUE DATE"] <= 60,df["AGE DUE DATE"] <= 90,df["AGE DUE DATE"] <= 120,
              df["AGE DUE DATE"] <= 180,df["AGE DUE DATE"] <= 360,df["AGE DUE DATE"] <= 730,df["AGE DUE DATE"] > 730]
choices= ["Current(A)","Current(B)","31 - 60(C)","61 - 90(D)","91 - 120(E)","121 - 180(F)","181 - 360(G)","C316 - 730(H)","730 - (J)"]
df["Age Category"]= np.select(conditions,choices,default=0)


#エクセルに書き出し
today=dt.datetime.now().strftime("%b %d %Y")
df.to_excel(rf"C:\Users\AA\Desktop\picc\Aged and Credit Travel Debts as of {today}.xlsx",sheet_name="Pub_Travel_Salary_Debt_Detail",encoding="utf_8_sig", index=False)

