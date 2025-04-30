import requests
from bs4 import BeautifulSoup
import csv

# URL страницы, которую нужно спарсить
url = 'https://rsport.ria.ru/20220514/kaloriynost-1788483172.html'  # Замените на нужный URL

# Отправляем GET-запрос на страницу
response = requests.get(url)

# Проверяем, что запрос прошел успешно
if response.status_code == 200:
    print(f"Страница {url} успешно загружена!")
    # Парсим страницу с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')


    headers = soup.find_all('h3')
    h3s = [header.text for header in headers]
    print(h3s)
    print(len(h3s))
    data = [['Тип продукта', 'Продукт', 'Белки', 'Жиры', 'Углеводы', 'Ккал']]
    tables = soup.find_all('table')
    for table in range(len(list(tables))):
        if table + 1 == len(list(tables)):
            break
        rows = list(tables[table].find_all('tr'))[1:]
        # Проходим по всем строкам
        for row in rows:
            # Находим все ячейки в строке
            cells = list(row.find_all('td'))

            # Если в строке есть ячейки
            if len(cells) > 0:
                # Извлекаем данные из ячеек (по порядку)
                if table < 2:
                    product = [h3s[table]]
                elif table == 2:
                    product = ['Колбасные изделия']
                else:
                    product = [h3s[table - 1]]
                for cell in cells:
                    product.append(cell.text)
                data.append(product)
        print(data)
        print(len(data))
else:
    print(f"Ошибка при загрузке страницы: {response.status_code}")

with open('data.csv', 'w', encoding='utf-8') as o:
    writer = csv.writer(o)
    for row in data:
        writer.writerow(row)
