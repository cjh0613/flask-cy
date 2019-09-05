# -*- coding: utf-8 -*-  
import os
import time
import jieba
import random
import requests
from wordcloud import WordCloud
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/cytools/',methods=['GET','POST'])
def form_wordcloud():
	if request.method == 'POST':
		form_content = request.form['content']
		fname = str(random.randint(0,99))+str(int(time.time()))
		text_path = os.getcwd()+"\\text\\"
		text_fname = text_path+ fname+ ".txt"
		try:
			with open(text_fname,"a+") as f:
				f.write(form_content)
		except:
			print("文本写入错误")
		options_1 = request.form['sel1']
		options_2 = request.form['sel2']
		options_3 = request.form['keyword']
		ttf_path = os.getcwd()+"\\fonts\\"
		if options_1 == "中等尺寸:720*300":
			png_width = 720
			png_height = 300
		else:
			png_width = 1280
			png_height = 720
		if options_2 == "方正书宋简体":
			png_ttf = ttf_path+'fzttf1.ttf'
		elif options_2 == "方正细黑一简体":
			png_ttf = ttf_path+'fzttf2.ttf'
		else:
			png_ttf = ttf_path+'fzttf3.ttf'
		if options_3 != "":
			for i in options_3.split(","):
				form_content=form_content.replace(i,"")
		if form_content != "":
			res_url = parse_text(form_content,png_width,png_height,png_ttf)
			return render_template('form_cy.html',imgurl = res_url)
		else:
			return render_template('form_cy.html')
	return render_template('form_cy.html')

def parse_text(text,px_w,px_h,png_ttf):
	# 中文分词
	text = ' '.join(jieba.cut(text))
	# 生成对象
	wc = WordCloud(font_path=png_ttf, width=px_w, height=px_h, mode='RGBA', background_color=None).generate(text)
	# 保存到文件
	png_path = os.getcwd()+"\\images\\"
	fname = str(random.randint(0,99))+str(int(time.time()))
	png_fname = png_path+fname + ".png"
	wc.to_file(png_fname)
	url='https://sm.ms/api/upload'
	file_obj=open(png_fname,'rb')
	file={'smfile':file_obj}	#参数名称必须为smfile
	data_result=requests.post(url,data=None,files=file)
	if data_result.json()['code'] == "success":
		print(data_result.json()['data']['url'])
		return data_result.json()['data']['url']
	else:
		print("上传出现错误")

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)
