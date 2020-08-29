'''
爬取博客园某个作者所有文章
'''
from bs4 import BeautifulSoup
import requests
import sys

original_stdout = sys.stdout  # Save a reference to the original standard output


def get_bs(author, page=1):
    '''
    传入作者博客园的id，页数（不传页数则从第一页开始查找）
    如果存在下一页按钮，则递归调用自己获取下一页的数据
    '''
    r = requests.get(f'https://www.cnblogs.com/{author}/default.html?page={page}')
    soup = BeautifulSoup(r.content, 'html5lib')
    # print(f'第{page}页：')
    data_print(soup)
    # if soup.select(f'a[href="https://www.cnblogs.com/{author}/default.html?page={page+1}"]'):  # 如果有下一页的链接
    #     get_bs(author, page+1)


def data_print(soup):  # 这里可以优化显示文章链接啥的
    '''
    通过css选择器打印所有日期和文章标题
    '''
    with open('README.md', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('<p><a href="https://count.getloli.com/"><img src="https://count.getloli.com/get/@github.readme"></a><img src="https://weather-icon.journeyad.repl.co/@binzhou?v=1" align="right"></p>')
        print('\n## :memo:最近的笔记\n')
        for day in soup.select('div.day'):
            for date in day.select('div.dayTitle a'):# 每天只有一个日期
                for aritle in day.select('a.postTitle2'): # 每天可能有多篇文章
                        print('- ',date.text, ' ', '[', aritle.get_text().strip(), '](', aritle.get('href'), ')', sep='')

        print('\n:point_right: **[阅读更多](https://www.cnblogs.com/yjlaugus/p/)**')
        print('  :house: **[仓库索引](https://github.com/yjlaugus/box)**')
		print('\n⬇️点击下方图片留言⬇️\n')
        print('<a href="https://chat.getloli.com/room/@YJLAugus.github?title=YJLAugus-chatroom"><img src="https://chat.getloli.com/room/@YJLAugus.github/svg?width=600&height=280&limit=20&theme=light&title=YJLAugus@github:%20~&fontSize=13" align="left"></a>')
        sys.stdout = original_stdout  # Reset the standard output to its original value


if __name__ == "__main__":
    get_bs('yjlaugus')
