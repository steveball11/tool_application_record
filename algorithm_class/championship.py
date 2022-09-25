#%%
input_list = [1,2,6,8787,54,8,45,8,454564]

def champ(input_list):
    j = 0
    for i in range(len(input_list)):
        if (input_list[i] > input_list[j]):
            j = i
    return j
champ(input_list)
# %%
def add_str(string:str) -> str:
    string1 = string + "1"
    return string1

add_str("100")
#%%
for i in range(2):
    print(i)
#%%