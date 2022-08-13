import requests

headers = {
    'authority': 'www.avito.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'u=2tfug9b5.lt39rd.gdkj3mpzweg0; v=1660406177; luri=ekaterinburg; buyer_location_id=654070; sx=H4sIAAAAAAAC%2FwTAQRKCMAwF0Lv8tQtSA%2Fn2NqFpXNQFjo46MtydtyNVYo7ei3MNX69CK%2B4lImm9NUHd8UEFydy%2BW9x%2FqpM%2Fm4xhHm%2Fyoa8cf1zQUWVZJr2V2ew4zgAAAP%2F%2FdHZ5s1sAAAA%3D; dfp_group=52; abp=0; SEARCH_HISTORY_IDS=4; _gcl_au=1.1.730758377.1660406178; _ym_uid=166040617840222685; _ym_d=1660406178; _ga_9E363E7BES=GS1.1.1660406178.1.0.1660406178.60; _ga_M29JC28873=GS1.1.1660406178.1.0.1660406178.60; _ym_isad=2; tmr_lvid=a4ba86e39c3cd8eaa73bd4e22abac266; tmr_lvidTS=1660406178251; _ga=GA1.2.1390211445.1660406178; _gid=GA1.2.419271487.1660406178; _dc_gtm_UA-2546784-1=1; _ym_visorc=b; cto_bundle=JWduqF9kJTJGUllIYm5VSmxLQTB5c1BFbEx4SGtoVzV5S0ZPdEM0JTJGUmg2bjElMkZKYjJ6cUVZQUNPaEFLN2VoaUJHZ2hDUVhWMWFuZUZlQVpxa25NWElpTWdNUEhsSkU0V3V1Y0JEQiUyRkE4TWx0Mm9zc3lTZTdCOWcwRnNoZkJLT1lTNXliZzN5; f=5.9fd3735f16182a2836b4dd61b04726f14f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca44f0aa6d4f7157ca42668c76b1faaa3582668c76b1faaa3582668c76b1faaa3584f0aa6d4f7157ca402b7af2c19f2d05c02b7af2c19f2d05c0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9ad42d01242e34c7968e2978c700f15b6831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013aba0ac8037e2b74f9268a7bf63aa148d22ebf3cb6fd35a0ac8b1472fe2f9ba6b97b0d53c7afc06d0b71e7cb57bbcb8e0f03c77801b122405c2da10fb74cac1eab2da10fb74cac1eab2ebf3cb6fd35a0ac20f3d16ad0b1c546b892c6c84ad16848a9b4102d42ade879dcb5a55b9498f642064b2665a067d85545309f1f7f8743dad60adb528b72609e74933f3ff634b6e34525907271a6a0eb908a53f984f980487ce819c488ec879091e52da22a560f550df103df0c26013a0df103df0c26013aaaa2b79c1ae92595c09566dc16d687632379f5c1a84b7d743de19da9ed218fe2c772035eab81f5e110e95b305e77352aa1a4201a28a6ec9b059080ed9becc4cd; ft="EnI2SN+unWyq1UCtKQiN1p7qjdh3AjHgDUW/BotqQJghupD1rRi/g0KWF2bNz/kJzMB+D6GW96fTt9ALxT8SuZjqY1jg89Lf7BeaVidJYfOAEX5VLvdzPXgT4C9XK4HgGun7mvrJMkgYeiiR8BS6xjOySMVt16Aw9c3ESS+V6tP1QRscbwUdjH0Upshuvl+s"; adrdel=1; adrcid=AsbUKG0cMndsYFayWvOTDXw; tmr_detect=0%7C1660406180992; buyer_from_page=catalog; tmr_reqNum=4',
    'if-none-match': 'W/"23eb80-D79MOh27RLwvrEgDxmGu06vRfN0"',
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
