#! python3

import zipfile, os


def backupToZip(folder):
    folder = os.path.abspath(folder)

    # 记录备份次数，保证不生成同名zip文件
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFileName):
            break
        number += 1

    # 创建zipfile文件
    print('Creating %s' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # 将文件夹下所有非备份文件，文件夹都添加到zip中
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)

        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue  # 不重复备份zip备份文件
            backupZip.write(os.path.join(foldername, filename))

    # 注意缩进，不同的环节
    backupZip.close()
    print('Done.')


backupToZip('xkcd')
