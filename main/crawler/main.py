from main.crawler.players_url_crawler.player_url import PlayerUrl, crawl_list
from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    player_url = PlayerUrl(driver)
    crawl_list(player_url)

if __name__=="__main__":
    main()