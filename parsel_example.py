from parsel import Selector

# # Create a Selector object for the HTML or XML text that you want to parse
# tag = "<html><body><h1>Hello Parsel!</h1></body></html>"
# selector = Selector(text=tag)
#
# # use CSS or XPath expressions to select elements
# select_css = selector.css("h1")
# select_xpath = selector.xpath("//h1")
#
# # extract data from those elements
# text = selector.css("h1::text").getall()
#
# print(text)

tag = '''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>'''
selector = Selector(text=tag)

title = selector.xpath("//title/text()").get()

# get all image
images_all = selector.css("img").xpath("@src").getall()
images_all = selector.xpath("//img/@src").getall()

# extract only the first matched element
a_first_text = selector.xpath("//div[@id='images']/a/text()").get()
# It returns None if no element was found
ifnone = selector.xpath('//div[@id="not-exists"]/text()').get() is None


# Instead of using e.g. '@src' XPath it is possible to query for attributes using .attrib property of a Selector
images_attrs = [img.attrib['src'] for img in selector.css('img')]
'''   OR    '''
# for img in selector.css('img'):
#     print(img.attrib["src"])

selector.xpath('//base/@href').get()
# 'http://example.com/'

selector.css('base::attr(href)').get()
# 'http://example.com/'

selector.css('base').attrib['href']
'http://example.com/'

selector.css('a[href*=image]::attr(href)').getall()
selector.xpath('//a[contains(@href, "image")]/@href').getall()
# ['image1.html',
#  'image2.html',
#  'image3.html',
#  'image4.html',
#  'image5.html']

selector.css('a[href*=image] img::attr(src)').getall()
selector.xpath('//a[contains(@href, "image")]/img/@src').getall()
# ['image1_thumb.jpg',
#  'image2_thumb.jpg',
#  'image3_thumb.jpg',
#  'image4_thumb.jpg',
#  'image5_thumb.jpg']

links = selector.xpath('//a[contains(@href, "image")]').getall()
# ['<a href="image1.html">Name: My image 1 <br><img src="image1_thumb.jpg"></a>',
#  '<a href="image2.html">Name: My image 2 <br><img src="image2_thumb.jpg"></a>',
#  '<a href="image3.html">Name: My image 3 <br><img src="image3_thumb.jpg"></a>',
#  '<a href="image4.html">Name: My image 4 <br><img src="image4_thumb.jpg"></a>',
#  '<a href="image5.html">Name: My image 5 <br><img src="image5_thumb.jpg"></a>']

# for index, link in enumerate(links):
#     args = (index, link.xpath('@href').get(), link.xpath('img/@src').get())
#     print('Link number %d points to url %r and image %r' % args)

# Removing elements : remove ad from blogspot
doc = """
<article>
    <div class="row">Content paragraph...</div>
    <div class="row">
        <div class="ad">
            Ad content...
            <a href="http://...">Link</a>
        </div>
    </div>
    <div class="row">More content...</div>
</article>
"""
sel = Selector(text=doc)
sel.xpath('//div/text()').getall()
# ['Content paragraph...', '\n        ', '\n            Ad content...\n            ', '\n        ', '\n    ', 'More content...']
sel.xpath('//div[@class="ad"]').drop()
sel.xpath('//div//text()').getall()
# ['Content paragraph...', 'More content...']

