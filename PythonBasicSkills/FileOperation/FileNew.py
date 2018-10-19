#新增一个文件 删除一个文件
import os

'''
@desc   在filePath下生成fileNum个txt文件
@:param filePath    文件夹的路径
@:param fileNum     文件的数量
'''
def makeFiles(filePath,fileNum):
    #判断 文件夹 不存在
    if not os.path.exists(filePath):
        #不存在 则创建文件夹
        os.makedirs(filePath)
    for i in range(1,fileNum+1,1):
        path = filePath+str(i)+".txt"
        with open(path,"w") as f1:
            f1.close()

'''
@desc   删除某个文件夹下的所有文件
@:param filePath    需要删除的文件夹的路径 
@:param delEmpty    是否删除空文件夹
@:param delSelf     是否删除自身
'''
def delFiles(filePath,delEmpty=0,delSelf=0):
    for root,dirs,files in os.walk(filePath,topdown=False):
        for current_file in files:
            os.remove(os.path.join(root,current_file))
        for current_file in dirs:
            if delEmpty == 0:
                pass
            if delEmpty == 1:
                os.rmdir(os.path.join(root,current_file))
    if delSelf == 0:
        pass
    elif delSelf == 1:
        os.rmdir(filePath)




filePath=r"D:/Caches/PythonCaches/"
#新增文件
# for i in ["jianglp1","jianglp2","jianglp3"]:
#     tempFilePath = filePath + i + r"/"
#     makeFiles(tempFilePath,10)
# makeFiles(filePath,10)

delFiles(filePath)


