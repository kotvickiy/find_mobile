import requests

headers = {
    'authority': 'www.avito.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'u=2tft7fg7.lt39rd.1tgefnl26sc00; buyer_location_id=654070; sessid=ae98c61a6db6305cb561344963ec8597.1660202962; uxs_uid=13da6340-1a3d-11ed-8f16-27a34370760a; buyer_laas_location=654070; v=1660557429; luri=ekaterinburg; sx=H4sIAAAAAAAC%2FwTASwrCMBAG4Lv8axdJmseY20zmoRUEFTFCyd37HfActahZYhrKY4vUEnNSdWomEtEP%2FNAxbp953%2FVRgnxz4%2Bfrv1ef79DEmcvEBYYeaw01b5Sua50BAAD%2F%2F1tU2%2B1bAAAA; dfp_group=24; isLegalPerson=0; SEARCH_HISTORY_IDS=4; f=5.9fd3735f16182a2836b4dd61b04726f14f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca42668c76b1faaa3582668c76b1faaa3582668c76b1faaa3584f0aa6d4f7157ca402b7af2c19f2d05c02b7af2c19f2d05c0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9ad42d01242e34c7968e2978c700f15b6831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013aba0ac8037e2b74f9268a7bf63aa148d22ebf3cb6fd35a0ac8b1472fe2f9ba6b97b0d53c7afc06d0b71e7cb57bbcb8e0f03c77801b122405c2da10fb74cac1eab2da10fb74cac1eab2ebf3cb6fd35a0ac20f3d16ad0b1c546b892c6c84ad16848a9b4102d42ade879dcb5a55b9498f642064b2665a067d85545309f1f7f8743dad60adb528b72609e74933f3ff634b6e34525907271a6a0eb908a53f984f980487ce819c488ec879091e52da22a560f550df103df0c26013a0df103df0c26013aaaa2b79c1ae925950a627954dbe97a760cc86da995147ae63de19da9ed218fe2c772035eab81f5e110e95b305e77352aa1a4201a28a6ec9b059080ed9becc4cd; ft="yPPMmaQ+BUEZinXnIq7Uid8Nl4YXEeyUvea6d+cVrBsCVx3UME0O5g+ItWl2QLPwlBuw9n2iYyjN54kquRVCGZdhGwOgN5xiLXhju4kb7HUUkPXtRM8LhfUz464DXBAXijpdowdU7cfzEgx8Bv8tq2/RjbYsnc8s7wUFHCHfPay5GaO+yVhlBhwEe/p7AZGi"; buyer_from_page=catalog',
    'if-none-match': 'W/"24e7af-AWltO2YZFgzSMGgAXFADcqwBFcY"',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
