# 简体中文转繁体中文
# python src\zhcn2zhtw.py zh-CN zh-TW

import os
import sys
import codecs
from zhconv import convert

# args 0 is inputDir
# args 1 is outputDir

# 递归遍历 inputDir, 对每个文件执行 func
def walkDir(inputDir, func):
	for root, dirs, files in os.walk(inputDir):
		for file in files:
			# 如果是目录，递归遍历
			if os.path.isdir(os.path.join(root, file)):
				walkDir(os.path.join(root, file), func)
			# 如果是文件，执行 func
			else:
				func(os.path.join(root, file))

# 把 inputUri 指向的文件转为繁体中文，输出到 outputUri
def zhcn2zhtw(inputUri, outputUri):
	print('converting ' + inputUri + ' to ' + outputUri)
	inputFile = codecs.open(inputUri, 'r', 'utf-8')
	outputFile = codecs.open(outputUri, 'w', 'utf-8')
	for line in inputFile:
		outputFile.write(convert(line, 'zh-tw'))
	inputFile.close()
	outputFile.close()

def walkFunc(inputUri):
	outputUri = os.path.join(outputDir, inputUri)
	# 创建 outputUri 的目录
	if not os.path.exists(os.path.dirname(outputUri)):
		os.makedirs(os.path.dirname(outputUri))
	# 捕获异常，防止遇到不可读的文件时程序崩溃
	try:
		zhcn2zhtw(inputUri, outputUri)
	except Exception as e:
		print(inputUri + " err: " + str(e))

if __name__ == '__main__':
	inputDir = sys.argv[1]
	outputDir = sys.argv[2]
	walkDir(inputDir, walkFunc)
