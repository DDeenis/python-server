#!D:/Python3/python.exe
import os

query_params = {k: v for k, v in (pair.split('=') for pair in os.environ['QUERY_STRING'].split('&'))}
lang = query_params['lang']
resource = {
    'uk': 'Кошик',
    "en": 'Cart',
}
lang = lang if lang in resource else 'uk'

print("Content-Type: text/html")
print("")
print(f"""<!DOCTYPE html>
<html lang={lang}>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{resource[lang]}</title>
  </head>
  <body>
    <h1>{resource[lang]}</h1>
  </body>
</html>
""")