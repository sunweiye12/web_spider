# Scrapy笔记
## 安装scrapy框架：
1. 安装`scrapy`：通过`pip install scrapy`即可安装。
2. 如果在windows下，还需要安装`pypiwin32`，如果不安装，那么以后运行scrapy项目的时候就会报错。安装方式：`pip install pypiwin32`。
3. 如果是在ubuntu下，还需要安装一些第三方库：`sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`。

## 创建项目和爬虫：
1. 创建项目：`scrapy startproject [爬虫的名字]`。
2. 创建爬虫：进入到项目所在的路径，执行命令：`scrapy genspider [爬虫名字] [爬虫的域名]`。注意，爬虫名字不能和项目名称一致。

## 项目目录结构：
1. items.py：用来存放爬虫爬取下来数据的模型。
2. middlewares.py：用来存放各种中间件的文件。
3. pipelines.py：用来将items的模型存储到本地磁盘中。
4. settings.py：本爬虫的一些配置信息（比如请求头、多久发送一次请求、ip代理池等）。
5. scrapy.cfg：项目的配置文件。
6. spiders包：以后所有的爬虫，都是存放到这个里面。

## 糗事百科Scrapy爬虫笔记：
1. response是一个`scrapy.http.response.html.HtmlResponse`对象。可以执行`xpath`和`css`语法来提取数据。
2. 提取出来的数据，是一个`Selector`或者是一个`SelectorList`对象。如果想要获取其中的字符串。那么应该执行`getall`或者`get`方法。
3. getall方法：获取`Selector`中的所有文本。返回的是一个列表。
4. get方法：获取的是`Selector`中的第一个文本。返回的是一个str类型。
5. 如果数据解析回来，要传给pipline处理。那么可以使用`yield`来返回。或者是收集所有的item。最后统一使用return返回。
6. item：建议在`items.py`中定义好模型。以后就不要使用字典。
7. pipeline：这个是专门用来保存数据的。其中有三个方法是会经常用的。
    * `open_spider(self,spider)`：当爬虫被打开的时候执行。
    * `process_item(self,item,spider)`：当爬虫有item传过来的时候会被调用。
    * `close_spider(self,spider)`：当爬虫关闭的时候会被调用。
    要激活piplilne，应该在`settings.py`中，设置`ITEM_PIPELINES`。示例如下：
    ```python
    ITEM_PIPELINES = {
       'qsbk.pipelines.QsbkPipeline': 300,
    }
    ```

## JsonItemExporter和JsonLinesItemExporter：
保存json数据的时候，可以使用这两个类，让操作变得得更简单。
1. `JsonItemExporter`：这个是每次把数据添加到内存中。最后统一写入到磁盘中。好处是，存储的数据是一个满足json规则的数据。坏处是如果数据量比较大，那么比较耗内存。示例代码如下：
    ```python
    from scrapy.exporters import JsonItemExporter

    class QsbkPipeline(object):
        def __init__(self):
            self.fp = open("duanzi.json",'wb')
            self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
            self.exporter.start_exporting()

        def open_spider(self,spider):
            print('爬虫开始了...')

        def process_item(self, item, spider):
            self.exporter.export_item(item)
            return item

        def close_spider(self,spider):
            self.exporter.finish_exporting()
            self.fp.close()
            print('爬虫结束了...')
    ```
2. `JsonLinesItemExporter`：这个是每次调用`export_item`的时候就把这个item存储到硬盘中。坏处是每一个字典是一行，整个文件不是一个满足json格式的文件。好处是每次处理数据的时候就直接存储到了硬盘中，这样不会耗内存，数据也比较安全。示例代码如下：
    ```python
    from scrapy.exporters import JsonLinesItemExporter
    class QsbkPipeline(object):
        def __init__(self):
            self.fp = open("duanzi.json",'wb')
            self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

        def open_spider(self,spider):
            print('爬虫开始了...')

        def process_item(self, item, spider):
            self.exporter.export_item(item)
            return item

        def close_spider(self,spider):
            self.fp.close()
            print('爬虫结束了...')
    ```


### CrawlSpider：
需要使用`LinkExtractor`和`Rule`。这两个东西决定爬虫的具体走向。
1. allow设置规则的方法：要能够限制在我们想要的url上面。不要跟其他的url产生相同的正则表达式即可。
2. 什么情况下使用follow：如果在爬取页面的时候，需要将满足当前条件的url再进行跟进，那么就设置为True。否则设置为Fasle。
3. 什么情况下该指定callback：如果这个url对应的页面，只是为了获取更多的url，并不需要里面的数据，那么可以不指定callback。如果想要获取url对应页面中的数据，那么就需要指定一个callback。

### Scrapy Shell：
1. 可以方便我们做一些数据提取的测试代码。
2. 如果想要执行scrapy命令，那么毫无疑问，肯定是要先进入到scrapy所在的环境中。
3. 如果想要读取某个项目的配置信息，那么应该先进入到这个项目中。再执行`scrapy shell`命令。

### 模拟登录人人网：
1. 想要发送post请求，那么推荐使用`scrapy.FormRequest`方法。可以方便的指定表单数据。
2. 如果想在爬虫一开始的时候就发送post请求，那么应该重写`start_requests`方法。在这个方法中，发送post请求。





