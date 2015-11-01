# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:48:11 2015

@author: chris
"""

##### This takes URLs and turns them into raw text that will be submitted to opencalais

from goose import Goose
url = 'http://www.reuters.com/article/2015/10/30/us-retail-banks-cards-idUSKCN0SO24D20151030?feedType=RSS&feedName=technologyNews'
g = Goose()
article = g.extract(url=url)

article.title ## returns article title

article.meta_description ## returns article meta description

article.top_image.src ## returns path for main image in article

article = g.extract(url=url) ## these scrape full text from article
article.cleaned_text

save testarticle.py _oh[33] ## this is broken (in Ipython it saves the article scrapes into a file that will be used to submit to opencalaisscript)