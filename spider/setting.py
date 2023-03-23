import os

# PAGE -- 每一个产品翻页的次数，可更改 2页搜索结果大概在60左右
PAGE = 2

chromedriverPath = r"D:\WorkSpace_Extra\TaoBao\TaoBao\util\chromedriver.exe"
cur_file = os.path.abspath(__file__)
cur_dir = cur_file.rsplit("\\", 1)[0]