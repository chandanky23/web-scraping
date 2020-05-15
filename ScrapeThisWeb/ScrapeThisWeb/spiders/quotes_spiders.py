import scrapy
from ..items import ScrapethiswebItem

class QuoteSpider(scrapy.Spider) :
  name = 'quotes';
  page_number = 2
  start_urls = [
    'http://quotes.toscrape.com/page/1/'
  ];

  def parse(self, response):

    items = ScrapethiswebItem();

    all_div_quotes = response.css('div.quote');

    for quotes in all_div_quotes:
      title = quotes.css('span.text::text').extract();
      author = quotes.css('.author::text').extract();
      tags = quotes.css('.tag::text').extract();
      
      items['title'] = title
      items['author'] = author
      items['tags'] = tags
      
      yield items

    # next_page = response.css('li.next a::attr(href)').get() # get() to get the value
    next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) +'/';
    print(all_div_quotes)
    if len(all_div_quotes):
      QuoteSpider.page_number += 1;
      yield response.follow(next_page, callback=self.parse)