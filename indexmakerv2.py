import os

banner = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⠀⠀⠊⣉⡉⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⠂⠀⣀⠠⡀⠈⠀⡀⠀⠀⠂⠄⠀⢀⠀
⠀⠁⠉⠉⠁⠀⠀⠀⠌⠉⠙⠀⠀⠀⠐⠉⠉⠀⠃
⠀⢇⠈⠉⠀⠂⠀⠀⠀⠉⠁⡀⠀⠀⠇⠈⠉⠀⠂
⠈⢀⠒⠒⠊⠉Indexmaker⠁⠐⠒⠒⠂⠂
⠀⠆⠘⠙⠀⠀⠀⠀By⠀⠆⠘⠛⢈⠀
⠀⠈⠖⠒⠂ Sahmeran⠒⠒⠂⠄
⠀⡆⠐⠒⠀⠄⠀⠀⠀⠒⠂⠀⠀⠀⡆⠐⠒⠀⠄
⠐⡈⠤⠤⠔⠀⠒⠀⡢⠤⠤⠁⠒⠂⠠⠤⠤⠄⠄
⠀⠀⠀⠈⠄⠀⠀⠐⠀⠶⠆⠡⠀⠀⠄⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⠄⠀⠀⠂⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀
  
                                Indexmaker V2
                     Telegram: https://t.me/h3ckertime                                                                                               

  
"""
print(banner)


image_url = input("Enter the URL of the image: ")
hacked_by = input("Enter the 'Hacked By' message: ")
bottom_text = input("Enter the text for the bottom of the page ")

html = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Hacked by {}</title>
        <style>
            body {{
                background-image: url("{}");
                background-size: cover;
                background-position: center;
            }}
            
            h1 {{
                text-align: center;
                color: white;
                margin-top: 150px;
                font-size: 6em;
                font-family: Arial, sans-serif;
                text-shadow: 2px 2px 4px #000000;
            }}
            
            p {{
                text-align: center;
                color: white;
                margin-top: 20px;
                font-size: 2em;
                font-family: Arial, sans-serif;
                text-shadow: 2px 2px 4px #000000;
            }}
        </style>
    </head>
    
    <body>
        <h1>Hacked by {}</h1>
        <p>{}</p>
    </body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html.format(hacked_by, image_url, hacked_by, bottom_text))



