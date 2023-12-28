#!D:/Python3/python.exe
import os

included_vars = ["REQUEST_METHOD", "QUERY_STRING", "REQUEST_URI", "REMOTE_ADDR"]
vars = "<ul>"
for k, v in os.environ.items():
    if k in included_vars:
        vars += f"<li>{k} = {v}</li>";
vars += "</ul>"


query_params = {k: v for k, v in (pair.split('=') for pair in os.environ['QUERY_STRING'].split('&'))}
lang = query_params['lang']
resource = {
    'uk': 'Вітання',
    "en": 'Greetings',
    "de": 'Herzlich willkommen'
}
lang = lang if lang in resource else 'uk'

print("Content-Type: text/html")
print("")
print(f"""<!DOCTYPE html>
<html lang={lang}>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>{resource[lang]}</h1>
    {vars}
  </body>
</html>
""")