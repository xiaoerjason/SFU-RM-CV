# SFU-RM-CV
#=======说明========*
#1 为了避免中文路径带来的bug，使用pretreament.py替换所有标签、图片名的中文字符。

#2 把xml标注文件转化为txt格式：https://blog.csdn.net/qq_36756866/article/details/109111065

#3 创建训练数据文件：train、val、test 在labels文件夹下 ：同上

#4 创建yaml文件，训练配置文件

*=======步骤========*
把下面三个文件放到images,images_annotation等文件夹同级目录里

step1：pretreament.py

step2：split_train_val.py

step3：voc_label.py