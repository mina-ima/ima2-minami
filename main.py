import time


print("ロケット発射まで。。。")
for i in range(5,0,-1):
    print(f"{i}....")
    time.sleep(1) #１秒まつ
print("発射！！")
