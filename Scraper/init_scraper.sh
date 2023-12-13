echo "--------------------------"
echo "<--   init_scraper.sh  -->"
echo ""

scrapy startproject twitch_crawler
CD twitch_crawler && scrapy genspider twitch https://www.twitch.tv/
scrapy shell "https://www.twitch.tv/"
