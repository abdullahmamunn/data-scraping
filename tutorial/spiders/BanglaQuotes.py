import scrapy


class BanglaquotesSpider(scrapy.Spider):
    name = "BanglaQuotes"
    allowed_domains = ["www.goodreads.com"]
    start_urls = [
      "https://www.goodreads.com/quotes/tag/bangla"
    ]

    def parse(self, response):
        for bangla_quote in response.css('div.quote'):
            autho_name   = bangla_quote.css('div.quoteDetails span.authorOrTitle::text').get()
            quote_text   = bangla_quote.css('div.quoteDetails div.quoteText::text').get()
            author_image = bangla_quote.css('div.quoteDetails a.leftAlignedImage img::attr(src)').get()
            tags         = bangla_quote.css('div.quoteDetails div.quoteFooter div.left a::text').getall()

            yield{
                "Author" : autho_name,
                "Quote" : quote_text,
                "Image" : author_image,
                "Tags" : tags,
            }

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)

        next_page = response.css("div a.next_page::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



