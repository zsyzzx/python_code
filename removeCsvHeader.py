#! python3
# 删除CSV文件的第一行内容

import csv, os

os.makedirs('headerRemoved', exist_ok=True)
filePath = 'Automate_the_Boring_Stuff_onlinematerials/automate_online-materials/removeCsvHeader/'

# 遍历文件夹中的csv文件，不是csv文件则跳过
# 先读文件，跳过第一行，将剩余内容写入一个新文件(reader和writer 对象)

for csvFileName in os.listdir(filePath):
    if not csvFileName.endswith('.csv'):
        continue
    print('Removing Header From ' + csvFileName + '...')

    # 读CSV文件，
    csvRows = []
    csvFileObj = open(filePath + csvFileName)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
