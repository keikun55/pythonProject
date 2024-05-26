import numpy as np
# 図の作成
import matplotlib.pyplot as plt
fig = plt.figure()

# 部署A年齢構成
ages1 = np.random.normal(40, 5, 100) 
ax1 = fig.add_subplot(1, 2, 1) #(行数, 列数, 番号 : 左=1, 右 = 2)
ax1.hist(ages1, bins=20)
ax1.set_title("Department A")

# 部署A男女比  
labels2 = ["Men", "Women"]
data2 = [70, 30] 
ax2 = fig.add_subplot(1, 2, 2) #(行数, 列数, 番号 : 左=1, 右 = 2)
ax2.pie(data2, labels=labels2)
ax2.set_title("Department A")

plt.show()