import subprocess
import os


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='identify_picture_code.log')
def identify_picture_code():
    # 使用ocr工具
    p = subprocess.Popen(['tesseract', '3.png', '3.png'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()

    # 读取识别结果
    test_file = open('3.png.txt', 'r')
    line = test_file.readline()
    line = line.replace('\n', '')

    logger.debug(type(line))
    logger.debug(line)
    pass


if __name__ == '__main__':
    identify_picture_code()
    pass