# Scraper

### How to launch a scrapy shell ? 


```shell
cd Scraper/twitch_crawler
scrapy shell "https://www.twitch.tv"
```

```python
import logging
from scrapy import Request
title = response.css("title::text").extract_first()
logging.warning(title)
```

### Info

**List of allowed domains from robot.txt**
```text
User-Agent: *
Allow: /
Allow: /directory
Allow: /directory/all
Allow: /directory/*
Allow: /videos/week
Allow: /.well-known/assetlinks.json
Disallow: /admin/*
Disallow: /email-unsubscribe/
Disallow: /login$
Disallow: /message/*
Disallow: /signup$
Disallow: /user/*

Sitemap: https://www.twitch.tv/sitemapv2_index.xml.gz
```