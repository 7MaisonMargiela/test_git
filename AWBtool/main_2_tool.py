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
window = tk.Tk()
window.title('awb 组内小工具')
width = int(window.winfo_screenwidth()*0.35)
height = int(window.winfo_screenheight()*0.4)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size = '%dx%d+%d+%d' %(width,height,(screenwidth - width)/4, (screenheight - height)/4)
window.geometry(size)

#定义导入优化场景的路径
def select_color_path():
	# file_path = filedialog.askopenfilename()
	file_path = tkinter.filedialog.askdirectory()
	color_path.set(file_path)
	print(file_path)
	global set_txt
	set_txt=file_path
	# print(selected_folder)
	# r"C:\Users\heyin.wu\Desktop\PY\txt"


	pass
#定义获取lv&cct函数
def get_txt():
	path1 = set_txt  # 找到txt所在位置
	print(path1)

	# print(path1)
	# files = os.listdir(path1)  # 得到文件夹下所有txt

	files = os.listdir(path1)

	# print(files)
	i = 0  # 定义变量

	for file in files:  # 让txt循环起来
		i += 1  # 用于后续查看完成进度
		position = path1 + '\\' + file  # 构造绝对路径
		# print(file) #打印txt的名字
		# print(type(file))

		t = file.split()
		f1 = open(position, "r", encoding='utf-8')  # 打开并读取文件信息
		data = f1.read()  # 读取信息

		# print(data)  #循环打印txt文件夹

		parrern = "AWB_TAG_ALGO_SCENE_LV.*"  # 用正则匹配所需要的信息
		parrern1 = "AWB_TAG_CCT : .+ ?"

		# parrern1 = "AWB_TAG_CCT.*"
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
def get_one_excel():


	# file_path = tkinter.filedialog.askopenfilename()
	# excel_path.set(file_path)
	font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=25) ##添加字体解决中文乱码-wqx0731

	# 读取文件C:\Users\heyin.wu\Desktop\PY\test1
	# df = pd.read_excel("C:/Users/heyin.wu/Desktop/PY/test/数据表.xlsx")

	df = pd.read_excel(one_excel)
	# df1 = pd.read_excel(file_path)
	# 输出数据行数
	# print("数据行数:", len(df))
	'''
    由于只有一列数据我们使用 excel 行号作为 x 值的列表
    用range()函数来创建一个列表 [1,24)
    range()函数 遍历数字序列
    '''
	x = df['lv']
	y = df['cct']
	

	# x = df1['lv1']  # [1,24)
	# 读取指定的单列也就是 datas列，数据会存在列表里面
	# y = df1['cct1']

	# xx = df1['lv2']
	# 读取指定的单列也就是 datas列，数据会存在列表里面
	# yy = df1['cct2']
	# xxx = df1['lv3']
	# yyy = df1['cct3']

	# for 循环输出数据行数

	# 设置 x值 和y值的列表
	# plt.scatter(x, y, 20, color='MediumPurple', marker='h')
	# plt.scatter(xx, yy, 20, color='blue', marker='D')
	# plt.scatter(xxx, yyy, 20, color='green')
	plt.figure()
	plt.scatter(x, y, 15, color='red', marker='*') #maker 散点图

	#for xy in zip(x, y):
		#plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')

	# 图表名称
	plt.title('红色五角星=优化  菱形=重庆  圆行=深圳  x= 上海', fontproperties=font_set, size=10, color='green')
	# 设置x轴名称
	plt.xlabel("LV")
	# 设置y轴名称
	plt.ylabel("CCT")
	plt.show()
	pass
#获取优化场景的落点图+坐标
def get_one1_excel():


	# file_path = tkinter.filedialog.askopenfilename()
	# excel_path.set(file_path)
	font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=25)

	# 读取文件C:\Users\heyin.wu\Desktop\PY\test1
	# df = pd.read_excel("C:/Users/heyin.wu/Desktop/PY/test/数据表.xlsx")

	df = pd.read_excel(one_excel)
	# df1 = pd.read_excel(file_path)
	# 输出数据行数
	# print("数据行数:", len(df))
	'''
    由于只有一列数据我们使用 excel 行号作为 x 值的列表
    用range()函数来创建一个列表 [1,24)
    range()函数 遍历数字序列
    '''
	x = df['lv']
	y = df['cct']


	# x = df1['lv1']  # [1,24)
	# 读取指定的单列也就是 datas列，数据会存在列表里面
	# y = df1['cct1']

	# xx = df1['lv2']
	# 读取指定的单列也就是 datas列，数据会存在列表里面
	# yy = df1['cct2']
	# xxx = df1['lv3']
	# yyy = df1['cct3']

	# for 循环输出数据行数

	# 设置 x值 和y值的列表
	# plt.scatter(x, y, 20, color='MediumPurple', marker='h')
	# plt.scatter(xx, yy, 20, color='blue', marker='D')
	# plt.scatter(xxx, yyy, 20, color='green')
	plt.figure()
	plt.scatter(x, y, 15, color='red', marker='*')

	for xy in zip(x, y):
		plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')

	# 图表名称
	plt.title('红色五角星=优化  菱形=重庆  圆行=深圳  x= 上海', fontproperties=font_set, size=10, color='green')
	# 设置x轴名称
	plt.xlabel("LV")
	# 设置y轴名称
	plt.ylabel("CCT")
	plt.show()


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
def get_all_excel():
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

	# for 循环输出数据行数

	# 设置 x值 和y值的列表
	plt.scatter(x, y, 20, color='green', marker='x')
	plt.scatter(xx, yy, 20, color='green', marker='D')
	plt.scatter(xxx, yyy, 20, color='green')
	#plt.scatter(x, y, marker='o')
	#for xy in zip(x,y):
		#plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')


	# plt.scatter(x1, y1, 15, color='red', marker='*')
	# 图表名称

	# 设置x轴名称
	plt.xlabel("LV")
	# 设置y轴名称
	plt.ylabel("CCT")
	plt.show()
	pass

#定义checkbutton函数，实现色温线的可选
def cct_check():
		 
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

	# for 循环输出数据行数

	# 设置 x值 和y值的列表
	plt.scatter(x, y, 20, color='green', marker='x')
	plt.scatter(xx, yy, 20, color='green', marker='D')
	plt.scatter(xxx, yyy, 20, color='green')
	plt.plot([0,160], [2300,2300],color='brown')
	plt.plot([0,160], [3000,3000],color='brown')
	plt.plot([0,160], [3300,3300],color='brown')
	plt.plot([0,160], [4000,4000],color='brown')
	plt.plot([0,160], [4500,4500],color='brown')
	plt.plot([0,160], [5200,5200],color='brown')
	plt.plot([0,160], [5550,5550],color='brown')
	plt.plot([0,160], [6250,6250],color='brown')
	plt.plot([0,160], [7100,7100],color='brown')
	# 设置x轴名称
	plt.xlabel("LV")
	# 设置y轴名称
	plt.ylabel("CCT")
	plt.show()


	pass

    #fig, ax = plt.subplots()
    # ax.plot([1, 2, 3, 4], [10,10,10,10], label='Philadelphia')
    # ax.plot([1, 2, 3, 4], [30, 23, 13, 4], label='Boston')
    # ax.scatter([1, 2, 3, 4], [20, 10, 30, 15], label='Point')
    # ax.legend()

def cct_check_hide():
		 
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

	# for 循环输出数据行数

	# 设置 x值 和y值的列表
	plt.scatter(x, y, 20, color='green', marker='x')
	plt.scatter(xx, yy, 20, color='green', marker='D')
	plt.scatter(xxx, yyy, 20, color='green')
	plt.plot([0,160], [2300,2300],c='white')
	plt.plot([0,160], [3000,3000],c='white')
	plt.plot([0,160], [3300,3300],c='white')
	plt.plot([0,160], [4000,4000],c='white')
	plt.plot([0,160], [4500,4500],c='white')
	plt.plot([0,160], [5200,5200],c='white')
	plt.plot([0,160], [5550,5550],c='white')
	plt.plot([0,160], [6250,6250],c='white')
	plt.plot([0,160], [7100,7100],c='white')
	# 设置x轴名称
	plt.xlabel("LV")
	# 设置y轴名称
	plt.ylabel("CCT")
	plt.show()


	pass



def checkbutton_cct():
	if(var1.get()==1):
		cct_check()
	else:
		cct_check_hide()

	
    
 



color_path = tk.StringVar()
excel_path = tk.StringVar()
ccm_path = tk.StringVar()

"""
1 修改添加一个主窗口Frame
2 第二层有两个窗口frame：一个是Path_config_Frame 一个是Function_config_Frame
3 Path_config_Frame，沿用之前的功能，其中更新界面布局，增加可选的色温控制按钮
4 Function_config_Frame，新增，补充Function help,补充工具作用，叙述使用说明

"""

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
btn_submit = Button(Path_Config_Frame, text='优化场景的落点图',command=get_one_excel)
btn_submit.grid(row=5, column=1, padx=1, pady=1)

btn_submit = Button(Path_Config_Frame, text='优化场景落点+坐标', command=get_one1_excel)
btn_submit.grid(row=5, column=2, padx=1, pady=1)

tk.Button(Path_Config_Frame,text="导入全场景的路径",command=select_ccm_path,height=1).grid(row=6,column=0)  # 获取 全场景 的落点路径
btn_submit = Button(Path_Config_Frame, text='生成场景库落点图', command=get_all_excel)
btn_submit.grid(row=6, column=1, padx=2, pady=10)

#新增加checkbutton,点击按钮会在两个变量中切换，选择或者取消选择
var1 = tk.IntVar()  # 定义var1整型变量用来存放选择行为返回值
btn_check = tk.Checkbutton(Path_Config_Frame,
                            text="添加色温参考线",
                            variable=var1,
                            command=checkbutton_cct,
                            activebackground='yellow',
                            onvalue=1, offvalue=0)    # 传值原理类似于radiobutton部件
btn_check.grid(row=6, column=2, padx=2, pady=10)

#新增function help 显示的massage
massage1=tk.Message(Function_config_Frame, text=" 1、点击导入优化场景路径，会导入仿真后的txt路径；点击获取lv&&cct信息,运行后会新生成：提取的信息.text,并更新 数据表.xlsx ; \n 2、点击导入数据表路径，点击优化场景落点图或者点击优化场景落点+坐标，会得到对应的图；\n 3、点击导入全场景路径，点击生成全场景落点图，会生成对应的图，若优化场景图未关闭，会生成二者总图; \n 4、 选择添加色温曲线，会给出代码的参考色温线，", bg='lightblue').pack()

window.mainloop()
