import matplotlib .pyplot as plt
import psutil as p

appNameList=[]
appNamePercentageList=[]
count=0

for process in p.process_iter():
    count=count+1
    if count<=6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        
        print("name: ",name," -- cpu usage: ",cpu_usage)
        appNameList.append(name)
        appNamePercentageList.append(cpu_usage)
        
plt.figure(figsize=(15,7))
plt.xlabel("application name")
plt.ylabel("cpu_usage")
plt.bar(appNameList,appNamePercentageList,width=0.6,color=("red","blue","green","yellow","orange","violet"))
plt.show()
