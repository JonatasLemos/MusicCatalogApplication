from django.test import LiveServerTestCase
from selenium import webdriver

class WebApplicationTest(LiveServerTestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # LOGIN
        self.driver.get('http://127.0.0.1:8000/login')
        self.user = self.driver.find_element_by_id("name")
        self.password = self.driver.find_element_by_id("password")
        self.login = self.driver.find_element_by_id("login-button")
        self.user.send_keys("jamil")
        self.password.send_keys("123")
        self.login.click()
        # ADD-NEW-ALBUM
        self.driver.get("http://127.0.0.1:8000/add-new-album")
        self.artist = self.driver.find_element_by_id("add_artist")
        self.album = self.driver.find_element_by_id("add_album")
        self.submit = self.driver.find_element_by_id("search-album")

    def test_repeated_album(self):
        """Test if a repeated album returns 'Album already in catalog' message"""
        self.artist.send_keys("Pink Floyd")
        self.album.send_keys("Animals")
        self.submit.click()
        message = self.driver.find_element_by_id("message-container")
        self.assertEqual(message.text, 'Album already in catalog')

    def test_album_not_found(self):
        """Test if a not found album returns 'Album not found' message"""
        self.artist.send_keys("dasdsaasd")
        self.album.send_keys("dsadsadsa")
        self.submit.click()
        message = self.driver.find_element_by_id("message-container")
        self.assertEqual(message.text, 'Album not found')

    def test_master_not_found(self):
        """Test if a wrong master name returns the message 'Unable to find a master release for this album,
         look in discogs for its master name' """
        self.artist.send_keys("led zeppelin")
        self.album.send_keys("led zeppelin IV")
        self.submit.click()
        message = self.driver.find_element_by_id("message-container")
        self.assertEqual(message.text,
                         'Unable to find a master release for this album, look in discogs for its master name')

    def test_rate_out_of_range(self):
        """Test if out of range rate returns a validationMessage"""
        self.artist.send_keys("Pink Floyd")
        self.album.send_keys("Animals")
        rate = self.driver.find_element_by_name("rate")
        rate.send_keys("8")
        self.assertEqual(rate.get_attribute("validationMessage"),
                         'O valor deve ser menor ou igual a 5.')

    def tearDown(self):
        self.driver.quit()
