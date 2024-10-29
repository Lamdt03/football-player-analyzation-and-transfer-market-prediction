import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from main.crawler.constant import COMPETITION_URLS_FILE_PATH, PLAYER_URLS_FILE_PATH, CLUB_URLS_FILE_PATH
from main.crawler.players_url_crawler.player_url import PlayerUrl
from main.system.file_reader import read_file_by_line


class TestPlayerUrl(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_crawl_competition_url(self):
        player_url = PlayerUrl( self.driver)
        got = player_url.crawl_competition_url()
        expected = True
        self.assertEqual(got, expected)

    def test_crawl_club_url(self):
        player_url = PlayerUrl( self.driver)
        competition_urls = read_file_by_line(COMPETITION_URLS_FILE_PATH)
        got = player_url.crawl_club_url(competition_urls)
        expected = True
        self.assertEqual(got, expected)
    def test_crawl_player_url(self):
        player_url = PlayerUrl( self.driver)
        club_urls = read_file_by_line(CLUB_URLS_FILE_PATH)
        got = player_url.crawl_player_url(club_urls)
        expected = True
        self.assertEqual(got, expected)