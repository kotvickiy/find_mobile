import requests

headers = {
    'authority': 'www.avito.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'u=2tfnwol5.lt39rd.2uf9b7l19bw0; luri=ekaterinburg; f=5.9fd3735f16182a2836b4dd61b04726f14f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca42668c76b1faaa3582668c76b1faaa3582668c76b1faaa3584f0aa6d4f7157ca402b7af2c19f2d05c02b7af2c19f2d05c0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9ad42d01242e34c7968e2978c700f15b6831064c92d93c3903815369ae2d1a81d07d0ef63b705ec762da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eabb892c6c84ad16848a9b4102d42ade879dcb5a55b9498f642064b2665a067d85545309f1f7f8743dad60adb528b72609e74933f3ff634b6e34525907271a6a0eb908a53f984f980487ce819c488ec879091e52da22a560f550df103df0c26013a0df103df0c26013aaaa2b79c1ae9259574776191d67371731709dee4e32edee33de19da9ed218fe2c772035eab81f5e110e95b305e77352aa1a4201a28a6ec9b059080ed9becc4cd; ft="5NiRmfHlVOe4sHZLo1KLHNfMkO6XYJwC7VZT5cfVInPGQuSvsSc0GnEO4Un15ytx3dA6cYp0vISeKSuWZIj5TrNHsBtSXbFV5e0scdjWtQ3gWBgu4ypuRBZaZyQfGrCwmuLdayM8CUpibXTQEJYyobU1eKE1vOYd7I4lDnjENjPd8f+1OYLwQvpsivHFMCsk"; v=1659497208; buyer_location_id=654070; dfp_group=87; sx=H4sIAAAAAAAC%2FwTAQQ6CMBAF0Lv8tYtOcWDsbX6ZYaFJAyRaDOHuvBPLU1w9ItOqsw5iUyaz%2B2JTzLOgnPihoH1XSre6%2B8b%2B2b3x%2Fz62dGhfWzDhgUCRUV9qw5jsuu4AAAD%2F%2F90ZentbAAAA; SEARCH_HISTORY_IDS=4; buyer_from_page=catalog',
    'if-none-match': 'W/"2282e3-c6TIhXbKP/SpRkEqORlnJarVfEc"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
