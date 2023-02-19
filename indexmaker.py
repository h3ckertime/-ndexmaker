import os

banner = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
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
  
                                Indexmaker V1
                     Telegram: https://t.me/h3ckertime                                                                                            

  
"""
print(banner)


image_url = input("Enter the URL of the image: ")
hacked_by = input("Enter the 'Hacked By' message exam:(Hacked by Sahmeran): ")
bottom_text = input("Enter the text for the bottom of the page: ")

with open('index.html', 'w') as f:
    f.write('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Hacked by</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-image: url("{}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                height: 100vh;
            }}
            h1 {{
                color: red;
                font-size: 6em;
                text-align: center;
                margin-top: 15%;
            }}
            #bottom {{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: rgba(0, 0, 0, 0.7);
                color: white;
                text-align: center;
                padding: 20px 0;
                font-size: 2em;
                font-weight: bold;
            }}
            #snake {{
                position: fixed;
                bottom: -100px;
                width: 200px;
                height: 200px;
                left: 50%;
                transform: translateX(-50%);
                animation: snake 10s linear infinite;
                z-index: -1;
            }}
            @keyframes snake {{
                0% {{
                    transform: translateX(-50%) rotate(0deg) translateY(0px);
                }}
                25% {{
                    transform: translateX(-50%) rotate(90deg) translateY(200px);
                }}
                50% {{
                    transform: translateX(-50%) rotate(180deg) translateY(0px);
                }}
                75% {{
                    transform: translateX(-50%) rotate(270deg) translateY(200px);
                }}
                100% {{
                    transform: translateX(-50%) rotate(360deg) translateY(0px);
                }}
            }}
        </style>
    </head>
    <body>
        <h1>{}</h1>
        <div id="bottom">{}</div>
        <img id="snake" src="https://www.freeiconspng.com/thumbs/snake-png/snake-png-14.png">
    </body>
    </html>
    '''.format(str(image_url), str(hacked_by).upper(), str(bottom_text).upper()))


