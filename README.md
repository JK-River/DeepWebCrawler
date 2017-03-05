# DeepWebCrawler
1.GoogleKnowledge.py：谷歌知识爬虫，先看看谷歌知识的搜索用法，例如我们可以查找老虎体重是多少；![](res/GoogleKnowledge.png)

_ _ _

如果想用程序取到这个结果，直接抓取页面是没办法做到的，因为这部分DOM结构是动态加载的，
GoogleKnowledge.py利用selenium调用chrome，可以查找到页面加载后的DOM结构，从而取到想要的结果；
关于selenium调用chrome的配置可以参考[http://blog.csdn.net/mmc2015/article/details/53064021](http://blog.csdn.net/mmc2015/article/details/53064021)。

