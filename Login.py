import time


class Login:
	def __init__(self, driver, By):
		self.driver = driver
		self.By = By

	# login
	def login(self, url, name, password):
		self.driver.get(url)
		self.driver.implicitly_wait(5)
		username_input = self.driver.find_element_by_css_selector(
			"input[name='username']")
		password_input = self.driver.find_element_by_css_selector(
			"input[name='password']")
		username_input.send_keys(name)
		password_input.send_keys(password)
		login_button = self.driver.find_element_by_xpath(
			"//button[@type='submit']")
		login_button.click()
		time.sleep(2)
		# созранить пароль?
		assert "Не сейчас" in self.driver.page_source
		get_btn = self.driver.find_element_by_xpath(
			"//button[text()='Не сейчас']")
		get_btn.click()
		time.sleep(3)
		# включить уведомления?
		assert "Не сейчас" in self.driver.page_source
		esc = self.driver.find_element_by_xpath('//button[text()="Не сейчас"]')
		esc.click()
		time.sleep(1)
		print('Вошли...')

	# subscribe
	def subscribe(self):
		all_btn = self.driver.find_element_by_xpath('//a[contains(@href,"/explore/people/")]')
		all_btn.click()
		buttons_subsrcibe = self.driver.find_elements(self.By.XPATH, '//button[text()="Подписаться"]')
		print('Подписка пошла...')
		count = 0
		for i in buttons_subsrcibe:
			count += 1
			if count <= 31:
				i.click()

		print('Подписка закончилась...')
		time.sleep(10)
		self.driver.close()


