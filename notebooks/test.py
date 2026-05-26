import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    response = requests.get(doc_url)
    soup = BeautifulSoup(response.text, "html.parser")

    cells = [cell.get_text(strip=True) for cell in soup.find_all("td")]

    points = []

    for i in range(0, len(cells), 3):
        try:
            x = int(cells[i])
            char = cells[i + 1]
            y = int(cells[i + 2])

            points.append((x, y, char))

        except:
            continue

    if not points:
        print("No valid coordinate data found.")
        return

    max_x = max(x for x, y, c in points)
    max_y = max(y for x, y, c in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    for row in grid:
        print("".join(row))


decode_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)
