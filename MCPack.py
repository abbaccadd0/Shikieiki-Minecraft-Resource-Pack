import os
import shutil
import wget
import zipfile

print("正在下载资源包")
url = 'http://downloader1.meitangdehulu.com:22943/Minecraft-Mod-Language-Modpack-1-16.zip'
# url = 'https://ghproxy.com/https://github.com/CFPAOrg/Minecraft-Mod-Language-Package/releases/latest/download/Minecraft-Mod-Language-Package-1.16.zip'
r = wget.download(url)

print("\n正在解压资源包")
zFile = zipfile.ZipFile(".\\Minecraft-Mod-Language-Modpack-1-16.zip", "r")
for fileM in zFile.namelist():
    zFile.extract(fileM, ".\\Shikieiki-Minecraft-Resource-Pack")
zFile.close()
zFile = zipfile.ZipFile(".\\HJ状数条显示资源包v3.0.zip", "r")
for fileM in zFile.namelist():
    zFile.extract(fileM, ".\\Shikieiki-Minecraft-Resource-Pack")
zFile.close()

print("正在清理冗余文件")
os.remove(".\\Shikieiki-Minecraft-Resource-Pack\\license")
os.remove(".\\Shikieiki-Minecraft-Resource-Pack\\readme.md")
os.remove(".\\Shikieiki-Minecraft-Resource-Pack\\pack.mcmeta")
os.remove(".\\Shikieiki-Minecraft-Resource-Pack\\pack.png")
os.remove("Minecraft-Mod-Language-Modpack-1-16.zip")

print("正在添加版本信息")
shutil.copy('pack.mcmeta', '.\\Shikieiki-Minecraft-Resource-Pack')
shutil.copy('pack.png', '.\\Shikieiki-Minecraft-Resource-Pack')

print("正在压缩资源包")
startdir = ".\\Shikieiki-Minecraft-Resource-Pack"  #要压缩的文件夹路径
file_news = '.\\Shikieiki-Minecraft-Resource-Pack.zip'  # 压缩后文件夹的名字
z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  #参数一：文件夹名
for dirpath, dirnames, filenames in os.walk(startdir):
    fpath = dirpath.replace(startdir, '')  #这一句很重要，不replace的话，就从根目录开始复制
    fpath = fpath and fpath + os.sep or ''  #这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
    for filename in filenames:
        z.write(os.path.join(dirpath, filename), fpath + filename)
z.close()
print("正在清理临时文件")
shutil.rmtree('.\\Shikieiki-Minecraft-Resource-Pack')
print("完成")
