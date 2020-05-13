import os
import time
from urllib.parse import urlparse
from selenium import webdriver

urls = [
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Aquarium.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Autorennen.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/BananenHergezaubert.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Buchstaben.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/FangMich.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Farben.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/FindeDasTier.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Labyrinth.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/MausZumKaese.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Pacman.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Trampolin.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Wettrennen.cubi',
	'https://raw.githubusercontent.com/IT4Kids/levels/master/Solutions/Zeichnen.cubi',
]

driver = webdriver.Chrome()

count = 0
for url in urls:
	a = urlparse(url)
	base = os.path.basename(a.path)
	driver.get('https://i.oltdaniel.at/Cubi/development?level=' + url)
	while driver.execute_script('return document.readyState;') != 'complete':
		time.sleep(0.1)
	time.sleep(1)
	image = driver.find_element_by_id("pixi-app-container").screenshot_as_png
	f = open(base + '.png', 'w+b')
	f.write(image)
	f.close()
	count += 1

driver.close()
