import os	
import re
import tkinter.messagebox
import tkinter.filedialog
import tkinter as tk
from tkinter.ttk import *
import pandas as pd
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # 大小写无所谓 tkaGg ,TkAgg 都行
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import xlwt
import numpy as np
from matplotlib.widgets import CheckButtons


window = tk.Tk()
window.title('awb 组内小工具')
width = int(window.winfo_screenwidth()*0.4)
height = int(window.winfo_screenheight()*0.42)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size = '%dx%d+%d+%d' %(width,height,(screenwidth - width)/4, (screenheight - height)/4)
window.geometry(size)
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=25) ##添加字体解决中文乱码-wqx0731

#定义导入优化场景的路径
def select_color_path():
	file_path = tkinter.filedialog.askdirectory()
	color_path.set(file_path)
	print(file_path)
	global set_txt
	set_txt=file_path

	pass
#定义获取lv&cct函数
def get_txt():
	path1 = set_txt  # 找到txt所在位置
	print(path1)

	files = os.listdir(path1)

	i = 0  # 定义变量

	for file in files:  # 让txt循环起来
		i += 1  # 用于后续查看完成进度
		position = path1 + '\\' + file  # 构造绝对路径
		t = file.split()
		f1 = open(position, "r", encoding='utf-8')  # 打开并读取文件信息
		data = f1.read()  # 读取信息

		parrern = "AWB_TAG_ALGO_SCENE_LV.*"  # 用正则匹配所需要的信息
		parrern1 = "AWB_TAG_CCT : .+ ?"

		str2 = re.findall(parrern, data)  # 查找所有符合条件的信息
		str3 = re.findall(parrern1, data)

		str4 = t + str2[0:1] + str3[0:1]

		f2 = open("提取的信息.text", 'a+', encoding="utf-8")  # 打开并写入信息
		print(";".join(str4).replace(";", ":"))

		f2.write(";".join(str4).replace(";", ":") + "\n")  # 先转为非数组类型，再用分行输出
		print("完成" + str(i))
		f2.close()  # 有开就有关
		f1.close()  # 有开就有关
	f = open('提取的信息.text', 'r', encoding='utf-8')  # 打开数据文本文档，注意编码格式的影响

	wb = xlwt.Workbook(encoding='utf-8')  # 新建一个excel文件
	ws1 = wb.add_sheet('sheet1')  # 添加一个新表，名字为first
	ws1.write(0, 0, '文件名')
	ws1.write(0, 2, 'lv')
	ws1.write(0, 4, 'cct')

	row = 1  # 写入的起始行
	col = 0  # 写入的起始列
	# 通过row和col的变化实现指向单元格位置的变化
	k = 1

	for lines in f:
		a = lines.split(':')
		# txt文件中每行的内容按逗号分割并存入数组中
		k += 1
		for i in range(len(a)):
			ws1.write(row, col, a[i])  # 向Excel文件中写入每一项
			col += 1
		row += 1
		col = 0

	wb.save("数据表.xlsx")
	pass
#获取优化场景的落点图
def GetOneExcel():
	
	global font_set,x_list,y_list
	font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=25) ##添加字体解决中文乱码-wqx0731
	df = pd.read_excel(one_excel)
	x = df['lv']
	y = df['cct']
	x_list=list(x)
	y_list=list(y)
	pass
#获取优化场景的落点图+坐标
def GetOneExcelXY():

	global x1_list,y1_list

	font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=25)
	df = pd.read_excel(one_excel)
	x = df['lv']
	y = df['cct']
	x1_list=list(x)
	y1_list=list(y)
	plt.figure()
	plt.scatter(x, y, 15, color='red', marker='*')

	for xy in zip(x, y):
		plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')

	# 图表名称
	plt.title('场景落点图',fontproperties=font_set,fontsize=15,color='k')
	# 设置x轴名称
	plt.xlabel("LV")
	# 设置y轴名称
	plt.ylabel("CCT")
	plt.show
	pass
#获取数据表的路径
def select_excel_path():
	file_path = tkinter.filedialog.askopenfilename()
	excel_path.set(file_path)
	global one_excel
	one_excel = file_path
	print(one_excel)
	pass
#获取全场景的落点路径
def select_ccm_path():
	# file_path = filedialog.askopenfilename()
	file_path = tkinter.filedialog.askopenfilename()
	ccm_path.set(file_path)
	global all_excel
	all_excel=file_path
	print(all_excel)


	pass
#获取场景库落点图
def Get_all_excel():
	global xall_list1,xall_list2,xall_list3,yall_list1,yall_list2,yall_list3,xall_list4,yall_list4,xall_list5,yall_list5

	df1 = pd.read_excel(all_excel)
	# 输出数据行数
	# print("数据行数:", len(df))
	'''
    由于只有一列数据我们使用 excel 行号作为 x 值的列表
    用range()函数来创建一个列表 [1,24)
    range()函数 遍历数字序列
    '''
	# x1 = df['lv']
	# y1 = df['cct']

	x = df1['lv1']  # [1,24)
	# 读取指定的单列也就是 datas列，数据会存在列表里面
	y = df1['cct1']
	xx = df1['lv2']
	# 读取指定的单列也就是 datas列，数据会存在列表里面
	yy = df1['cct2']
	xxx = df1['lv3']
	yyy = df1['cct3']
	x4 = df1['lv4']
	y4 = df1['cct4']
	x5 = df1['lv5']
	y5 = df1['cct5']

	xall_list1=list(x)
	yall_list1=list(y)
	xall_list2=list(xx)
	yall_list2=list(yy)
	xall_list3=list(xxx)
	yall_list3=list(yyy)
	xall_list4=list(x4)
	yall_list4=list(y4)
	xall_list5=list(x5)
	yall_list5=list(y5)

	pass


	


def DrawPicture():
	GetOneExcel()
	Get_all_excel()
	a1=np.array(x_list)
	b1=np.array(y_list)
	a2=np.array(xall_list1)
	b2=np.array(yall_list1)
	a3=np.array(xall_list2)
	b3=np.array(yall_list2)
	a4=np.array(xall_list3)
	b4=np.array(yall_list3)
	a5=np.array(xall_list4)
	b5=np.array(yall_list4)
	a6=np.array(xall_list5)
	b6=np.array(yall_list5)

	fig, ax = plt.subplots()                     # subplots()用于创建子图

	#为图形添加标签（面向对象编程方式，ax.set_xlabel,set_ylabel）

	ax.set_title('场景落点图',fontproperties=font_set,fontsize=15,color='k')
	ax.set_xlabel('LV',fontsize=10,color='b')

	ax.set_ylabel('CCT',fontsize=10,color='b')

	l0 = ax.scatter(a1, b1, visible=False, lw=2, color='deeppink',marker='*',label='Optimization')           #plot（）用于画线图和散点图
	l1 = ax.scatter(a2, b2, lw=2, color='r', label='YCY',marker='p',s=12)
	l2 = ax.scatter(a3, b3, lw=2, color='g', label='SC',marker='p',s=12)
	l3 = ax.scatter(a4, b4, lw=2, color='b', label='SWGY',marker='p',s=12)

	l4 =ax.hlines([2300, 3000, 3300, 3700, 4000, 4500, 5200, 5550, 6250, 7100],-40,180,color='g',label='CCt')
	l5 = ax.scatter(a5, b5, lw=2, color='k', label='XBK',marker='p',s=12)
	l6 = ax.scatter(a6, b6, lw=2, color='pink', label='YJ',marker='p',s=12)

	plt.legend(loc='upper right')
	# 调整子图大小，在左侧留出复选框区域
	plt.subplots_adjust(left=0.3)
	global lines,labels
	lines = [l0,l1,l2,l3,l4,l5,l6] 
	# 构造复选框实例化时用到的属性
	# 创建复选框的容器子图
	rax = plt.axes([0.01, 0.4, 0.18, 0.2])
	# 创建复选框的标签列表，标签自动对应曲线的标签
	labels = [str(line.get_label()) for line in lines]
	# 根据对应曲线可见状态初始化复选框初始状态
	visibility = [line.get_visible() for line in lines]
	# 构造复选框实例
	check = CheckButtons(rax, labels, visibility)   
	# 绑定复选框选中事件
	check.on_clicked(func)
	print(check.labels,check.lines,check.rectangles,check.get_status(),check.get_active())

	plt.show() 
	pass
# 创建复选框选中事件的回调函数，注意回调函数的参数默认为选中复选框的label
def func(label):
    index = labels.index(label)
    # 根据选中状态设置对应曲线的可见属性
    lines[index].set_visible(not lines[index].get_visible())
    # 注意！matplotlib中出现窗体之后的交互中如果修改图像需要重绘图像
    plt.draw()

 






color_path = tk.StringVar()
excel_path = tk.StringVar()
ccm_path = tk.StringVar()

if __name__ == '__main__':
	frame =tk.Frame(window)
	frame.pack()
	Path_Config_Frame = tk.LabelFrame(frame,text='Path Config',width=90)   # width、height 框架的宽度和高度
	Path_Config_Frame.grid(row=0, column=0,sticky='N'+'S'+'W'+'E',pady=6)   # padx/pady 水平、垂直方向上的内边距
	#增加function help frame
	Function_config_Frame = tk.LabelFrame(frame,text='Function help',width=90)   # width、height 框架的宽度和高度
	Function_config_Frame.grid(row=1, column=0,sticky='N'+'S'+'W'+'E',pady=6)   # padx/pady 水平、垂直方向上的内边距


	tk.Label(Path_Config_Frame,text="获取lv&&cct: ").grid(row=0,column=0,sticky='E')                        #以网格grid方法进行界面排列---WQX0801 (0,0)
	tk.Entry(Path_Config_Frame,width=40,textvariable =color_path).grid(row=0,column=1,columnspan=4)


	tk.Label(Path_Config_Frame,text="优化 lv cct: ").grid(row=1,column=0,sticky='E')							#grid(1,0)
	tk.Entry(Path_Config_Frame,width=40,textvariable =excel_path).grid(row=1,column=1,columnspan=4)				

	tk.Label(Path_Config_Frame,text="场景库:  ").grid(row=2,column=0,sticky='E')								#grid(2,0)
	tk.Entry(Path_Config_Frame,width=40,textvariable =ccm_path).grid(row=2,column=1,columnspan=4)

	#定义按钮
	tk.Button(Path_Config_Frame,text="导入优化场景路径",command=select_color_path,height=1).grid(row=4,column=0)  #grid(4,0)  # 获取 优化场景 的路径
	btn_submit = Button(Path_Config_Frame, text='获取lv&&cct信息', command=get_txt)
	btn_submit.grid(row=4, column=1, padx=2, pady=10)

	tk.Button(Path_Config_Frame,text="导入数据表的路径",command=select_excel_path,height=1).grid(row=5,column=0)  #获取 数据表 的落点路径
	btn_submit = Button(Path_Config_Frame, text='场景的落点图',command=DrawPicture)
	btn_submit.grid(row=5, column=1, padx=1, pady=1)

	# btn_submit = Button(Path_Config_Frame, text='优化场景落点+坐标', command=GetOneExcelXY)
	# btn_submit.grid(row=5, column=2, padx=1, pady=1)

	tk.Button(Path_Config_Frame,text="导入全场景的路径",command=select_ccm_path,height=1).grid(row=6,column=0)  # 获取 全场景 的落点路径
	# btn_submit = Button(Path_Config_Frame, text='生成场景库落点图', command=Get_all_excel)
	# btn_submit.grid(row=6, column=1, padx=2, pady=10)


	#新增function help 显示的massage
	massage1=tk.Message(Function_config_Frame, text=" 1、点击导入优化场景路径，会导入仿真后的txt路径；点击获取lv&&cct信息,运行后会新生成：提取的信息.text,并更新 数据表.xlsx ; \n 2、点击导入数据表路径，点击优化场景落点图或者点击优化场景落点+坐标，会得到对应的图；\n 3、点击导入全场景路径，点击生成全场景落点图，会生成对应的图，若优化场景图未关闭，会生成二者总图; \n 4、 选择添加色温曲线，会给出代码的参考色温线，", bg='lightblue').pack()

	window.mainloop()


