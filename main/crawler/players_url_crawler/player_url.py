import os

from numpy.ma.core import append
from selenium import webdriver
from selenium.webdriver.common.by import By

from main.crawler.constant import *
from main.system.file_reader import read_file_by_line
from main.system.file_writer import write_file_by_line


class PlayerUrl:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def crawl_club_url(self, competition_urls: []):
        driver = self.driver
        club_urls = []
        try:
            for c in competition_urls:
                driver.get(c + '/plus/?saison_id=2023')
                td_elements = driver.find_elements(By.XPATH, '//td[@class="hauptlink no-border-links"]')
                for t in td_elements:
                    link_elements = t.find_element(By.TAG_NAME, 'a')
                    href = link_elements.get_attribute('href')
                    club_urls.append(href)
            write_file_by_line(CLUB_URLS_FILE_PATH, club_urls,"w")
            return True
        except Exception as e:
            print("craw club url failed: ", e)
            return False

    def crawl_competition_url(self):
        driver = self.driver
        try:
            driver.get(EUROPEAN_COMPETITION_PAGE_URL)
            competition_urls = []
            for title in [PREMIER_LEAGUE, SERIE_A, BUNDESLIGA, LA_LIGA, LIGUE_1]:
                element = driver.find_element(By.XPATH, f'//a[@title="{title}"]')
                competition_urls.append(element.get_attribute('href'))
            write_file_by_line(COMPETITION_URLS_FILE_PATH, competition_urls,"w")
            return True
        except Exception as e:
            print("craw competition urls failed: ", e)
            return False

    def crawl_player_url(self, club_urls: []):
        driver = self.driver
        try:
            for c in club_urls:
                driver.get(c)
                player_url = []
                td_elements = driver.find_elements(By.XPATH, '//td[@class="hauptlink"]')
                for t in td_elements:
                    link_elements = t.find_element(By.TAG_NAME, 'a')
                    href = link_elements.get_attribute('href')
                    player_url.append(href)
                write_file_by_line(PLAYER_URLS_FILE_PATH,player_url,"a")
            return True
        except Exception as e:
            print("crawl player url failed: ", e)
            return False

def crawl_list(player_urls: PlayerUrl):
   is_success = player_urls.crawl_competition_url()
   if is_success:
       competition_urls = read_file_by_line(COMPETITION_URLS_FILE_PATH)
       is_success = player_urls.crawl_club_url(competition_urls)
       if is_success:
           club_urls = read_file_by_line(CLUB_URLS_FILE_PATH)
           is_success = player_urls.crawl_player_url(club_urls)
   return is_success