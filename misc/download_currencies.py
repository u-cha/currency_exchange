import csv
import httpx
from bs4 import BeautifulSoup


def get_html_from_page(url: str) -> str:
    response = httpx.get(url)
    return response.text


def get_unique_codes_names(html_page: str) -> dict:
    codes_names_dict = dict()
    soup = BeautifulSoup(html_page, "html.parser")
    table_rows = soup.find_all("tr")
    for table_row in table_rows:
        columns = table_row.find_all("td")
        if len(columns) == 4:
            country, name, cur_code = columns[0].text, columns[1].text, columns[2].text
            if len(cur_code) == 3 and codes_names_dict.get(cur_code) is None:
                codes_names_dict[cur_code] = name
    return codes_names_dict


def save_to_csv(filename: str, codes_names_dict: dict) -> None:
    with open(filename, "w", newline="") as csv_file:
        fieldnames = ["code", "fullname"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        for code, fullname in codes_names_dict.items():
            writer.writerow({"code": code, "fullname": fullname})


CURRENCY_CODES_SOURCE_PAGE = "https://www.iban.com/currency-codes"

if __name__ == "__main__":
    html = get_html_from_page(CURRENCY_CODES_SOURCE_PAGE)
    unique_codes = get_unique_codes_names(html)
    save_to_csv("../resources/codes_currencies.csv", unique_codes)

    with open("../resources/codes_currencies.csv", newline="") as csvfile:
        rows = csv.reader(csvfile, delimiter=",")
        for row in rows:
            print(row)
