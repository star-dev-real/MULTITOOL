from Config.Util import *
from Config.Config import *
try:
    import requests
    import time
    from itertools import cycle
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Theme Changer")

try:
    Slow(discord_banner)
    token = Choice1TokenDiscord()

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        try:
            amount = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter the number of cycles -> {color.RESET}"))
        except:
            ErrorNumber()
                
        modes = cycle(["light", "dark"])
        for i in range(amount):
            try:
                theme = next(modes)
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Changed{red} Theme: {white}{theme}{red}")
                time.sleep(0.5)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status:  {white}Error{red}  Theme: {white}{theme}{red}")

        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Finish.")
        Continue()
        Reset()
    else:
        ErrorToken()
except Exception as e:
    Error(e)