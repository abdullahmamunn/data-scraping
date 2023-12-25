import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]



    def parse(self, response):
        for qoute in response.css("div.quote"):
            title = qoute.css("span.text::text").get()
            author = qoute.css("small.author::text").get()
            tags = qoute.css("div.tags a.tag::text").getall()
            yield{
                'Title' : title,
                'Author' : author,
                'Tags' : tags
            }


        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

