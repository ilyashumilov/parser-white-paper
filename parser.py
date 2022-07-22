import requests

class main_parser:

	def __init__(self):
		self.wb_svetocopy = 'https://www.wildberries.ru/catalog/0/search.aspx sort=popular&search=Svetocopy'
		self.wb_navigator = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=Navigator+universal'

		self.ozon_svetocopy = 'https://www.ozon.ru/category/bumaga-dlya-pechati-18002/?category_was_predicted=true&from_global=true&text=Svetocopy'
		self.ozon_navigator = 'https://www.ozon.ru/search/?text=navigator%20universal&from_global=true'

		self.komus_svetokopy = 'https://www.komus.ru/search?text=Svetocopy&qid=6273530897'
		self.komus_navigator = 'https://www.komus.ru/search?text=Navigator+universal&qid=6095891362'

	@classmethod
	def get_page(cls, url):
		response = requests.get(url)
		return response.text

if __name__ == '__main__':
	print(main_parser.get_page())

