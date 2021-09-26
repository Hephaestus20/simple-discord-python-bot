## Merhabalar, Ben Hephaestus20
Sizler için basit bir anlatım ile, Python kullanarak bot çalıştırmayı ve Komut eklemeyi gösterdim.

[Buraya](#https://discord.gg/qAThZUqTNN) tıklayarak discord sunucumuza katılabilirsiniz.
[Buraya](#https://www.youtube.com/channel/UCqupqKWmpEB50Zqel8HSigw) tıklayarak ise youtube kanalıma bakabilirsiniz.

## Nasıl İndirilir
Öncelikle bazı python uzantıları eklememiz gerekiyor.
Bunları sizler için ayarladım.

```py
pip install -r requirements.txt
```

## Nasıl Komut Açılır
\
Öncelikle klasör içerisinde bulunan "cmds"'nin içine istediğiniz bir komutu oluşturun, oluşturacağımız komut "Küfür-Engel" olsun.
İçerisinde bazı importlar atmamız gerekecek.

```py
import discord
from discord.ext import commands
import os
import sys
import json
```
Sonra "config.json" ve daha kolay düzenleyebilmemiz için "message_TR" dosyalarını aratalım.
```py
import discord
from discord.ext import commands
import os
import sys
import json

if not os.path.isfile("config.json"):
    sys.exit("'config.json' Bulunamıyor.")
else:
    with open("config.json") as file:
        config = json.load(file)

if not os.path.isfile("lang\.\message_TR.json"):
    sys.exit("'message_TR.json' Bulunamıyor.")
else:
    with open("lang\.\message_TR.json", encoding='utf8') as file:
        message_TR = json.load(file)
```
Artık son 1-2 hamle ile komutumuzu çalışır duruma getirelim.
```py
import discord
from discord.ext import commands
import os
import sys
import json
if not os.path.isfile("config.json"):
    sys.exit("'config.json' Bulunamıyor.")
else:
    with open("config.json") as file:
        config = json.load(file)
if not os.path.isfile("lang\.\message_TR.json"):
    sys.exit("'message_TR.json' Bulunamıyor.")
else:
    with open("lang\.\message_TR.json", encoding='utf8') as file:
        message_TR = json.load(file)
class ModerationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases=["küfür-engel"])
    async def küfürengel(self, ctx, *, member: discord.Member = None):
        if not member:member=ctx.message.author
        message = discord.Embed()
        message.add_field(name=(f"{message_TR['kufurengel_titleerror']}"),value=(f"{message_TR['kufurengel_error']}"), inline=False)
        await ctx.send(embed=message)
def setup(client):
    client.add_cog(ModerationCommands(client))
    
```

Bu şekilde basit bir komut eklemiş olduk.
