import os   
import pypinyin
from pypinyin import pinyin, lazy_pinyin
# 这是修改DJI Robomaster 数据集文件名的脚本，替换中文字符和空格
# 适配模型：yolov5

# 批量替换文件名的中文字符
def rename():
    # 需要替换的文件路径
    # python路径改变也要重新改写路径
    user_path="E://DJI ROCO//robomaster_South"

    image_path=user_path+"//image"
    image_annotation_path=user_path+"//image_annotation"

    path_list=[image_path,image_annotation_path]

    for i in path_list:

        filelist=os.listdir(i)#该文件夹下所有的文件（包括文件夹）

        for files in filelist:#遍历所有文件
        
            Olddir=os.path.join(i,files);#原来的文件路径
        
            if os.path.isdir(Olddir):#如果是文件夹则跳过
        
                continue
        
            filename=os.path.splitext(files)[0]; #获取文件名
            #把文件名里的汉字转换成其首字母，切割了字符串
            filename1 = pinyin(filename, style=pypinyin.FIRST_LETTER) 
            #创建一个空列表
            filename2 = []
            for ch in filename1:
                filename2.extend(ch)
            #把列表转换成没有间隔的字符串，因为文件名要以字符串形式存在
            filenameToStr = ''.join(filename2)
            #空格替换
            unfilename=filenameToStr.replace(' ','_')

            filetype=os.path.splitext(files)[1];#文件扩展名

            Newdir=os.path.join(i,unfilename + filetype);#新的文件名

            os.rename(Olddir,Newdir);#重命名
    
        print(i+" Execution complete")
    
rename()
