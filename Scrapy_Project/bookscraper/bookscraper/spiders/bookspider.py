import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["book.toscrape.com"]
    start_urls = ["https://book.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            yield{
                'name' : book.css('h3 a::text').get(),
                'price' : book.css('div.product_price .price_color::text').get()
            }