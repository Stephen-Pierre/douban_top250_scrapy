from scrapy.pipelines.images import ImagesPipeline  # scrapy图片下载器
from scrapy import Request
from scrapy.exceptions import DropItem


class DoubanMovieTop250Pipeline(ImagesPipeline):
    # 请求下载图片
    def get_media_requests(self, item, info):
        yield Request(item['pic_link'], meta={'name': item['name']})

    def item_completed(self, results, item, info):
        # 分析下载结果并剔除下载失败的图片
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    # 重写file_path方法，将图片以原来的名称和格式进行保存
    def file_path(self, request, response=None, info=None):
        name = request.meta['name']  # 接收上面meta传递过来的图片名称
        file_name = name + '.jpg'    # 添加图片后缀名
        return file_name