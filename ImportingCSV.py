import pandas as pd
df = pd.read_csv("pokemon.csv", index_col="Name")
#print(df)
#print(df["Height"].to_string())
#print(df[["Name", "Height", "Weight"]].to_string())
# poke = input ("Enter Pokemon name : ")
# try:
#     print(df.loc[poke])
# except KeyError:
#     print(f"{poke} not found")

# t=df[df["Height"]>=2]
# print(t)

f=df[(df["Type1"]=="Fire")&(df["Type2"]=="Flying")]
print(f)