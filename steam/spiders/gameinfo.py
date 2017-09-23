import re
import config
import utils

from scrapy.spider import CrawlSpider
from scrapy import Request, FormRequest
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from sqlhelper import SqlHelper