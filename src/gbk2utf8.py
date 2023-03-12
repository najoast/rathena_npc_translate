
# args 0 is inputDir
# args 1 is outputDir

import os
import sys
import codecs


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

# 判断文件编码
# def getEncoding(file):
# 	# 读取文件前 1024 字节
# 	data = open(file, 'rb').read(1024)
# 	# 判断文件编码
# 	if data[:3] == codecs.BOM_UTF8:
# 		return 'utf-8-sig'
# 	elif data.startswith(codecs.BOM_UTF32_LE) or data.startswith(codecs.BOM_UTF32_BE):
# 		return 'utf-32'
# 	elif data.startswith(codecs.BOM_UTF16_LE) or data.startswith(codecs.BOM_UTF16_BE):
# 		return 'utf-16'
# 	else:
# 		return 'gbk'

def gbk2utf8(inputUri, outputUri):
	# 如果 inputUri 指向的文件编码已经是 utf-8 编码了，就不用转换了
	# if codecs.open(inputUri, 'r', 'utf-8').readline() == codecs.open(inputUri, 'r', 'gbk').readline():
	# 	return
	print('converting ' + inputUri + ' to ' + outputUri)
	inputFile = codecs.open(inputUri, 'r', 'gbk')
	outputFile = codecs.open(outputUri, 'w', 'utf-8')
	for line in inputFile:
		outputFile.write(line)
	inputFile.close()
	outputFile.close()


def walkFunc(inputUri):
	outputUri = os.path.join(outputDir, inputUri)
	# 创建 outputUri 的目录
	if not os.path.exists(os.path.dirname(outputUri)):
		os.makedirs(os.path.dirname(outputUri))
	# 捕获异常，防止遇到不可读的文件时程序崩溃
	try:
		gbk2utf8(inputUri, outputUri)
	except Exception as e:
		# 尝试用 iconv 转码
		
		print(inputUri + " err: " + str(e))

if __name__ == '__main__':
	inputDir = sys.argv[1]
	outputDir = sys.argv[2]
	walkDir(inputDir, walkFunc)
