import discord
import os
import io
import pathlib
from lib import *

PATH = pathlib.Path(__file__).parent.resolve()

personagens = {
    'lutador':['Luffy', 'Sanji', 'Koala', 'Yonji', 'Hina', 'Urouge', 'Bellamy', 'Drake', 'Chopper',
    'Smoker', 'Bonney', 'Ichiji', 'Jesus', 'Bepo', 'Mr2', 'Arlong', 'Kuroobi', 'Pearl', 'Gin', 'Alvida'],
    'atirador':['Ace', 'Usopp TS', 'Doflamingo', 'Franky', 'Niji', 'Usopp', 'Capone', 'Kid', 'Apoo', 'Van',
    'Daddy', 'Mr4', 'Jango', 'Krieg', 'Gin', 'Chew', 'Wapol', 'Eric', 'Mr5', 'Buggy'],
    'cortante':['Hatchan', 'Vivi', 'Eric', 'Law', 'Kuro', 'Zoro', 'Killer', 'Tashigi', 'Morgan', 'Bastille',
    'Cabaji', 'Buchi', 'Rebecca', 'Brook', 'Dalmatian', 'Doublefinger', 'Mr1'],
    'especialista': ['Ace', 'Goldenweek', 'Doflamingo', 'Crocodile', 'Mohji', 'Pearl', 'Law', 'Nami', 'Leo',
    'Basil', 'Reiju', 'Robin', 'Bartolomeo', 'Perona', 'Mr3']
}

def InfoChar(name):
        image = CreateImageInfo(name.lower())
        if isinstance(image,str):
            print(name, image)
            return image
        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            return discord.File(fp=image_binary, filename='image.png')
            #await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

class MainMenu(discord.ui.Select):
    def __init__(self, context):
        self.context = context
        options=[
            discord.SelectOption(label="Estrelas",emoji="⭐",description="Informação sobre Estrelas"),
            discord.SelectOption(label="Personagens",emoji="🦸",description="Informação sobre Personagens"),
            discord.SelectOption(label="Quebra-Cabeça",emoji="🧩",description="Imagem dos Quebra-Cabeça de tumba resolvidos")
            ]
        super().__init__(placeholder="Selecione:",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == 'Estrelas':
            await interaction.response.send_message(view=ViewStars(self.context), ephemeral=True)
        elif self.values[0] == 'Personagens':
            await interaction.response.send_message(view=ViewChar(self.context), ephemeral=True)
        elif self.values[0] == 'Quebra-Cabeça':
            await interaction.response.send_message(view=ViewPuzzles(self.context), ephemeral=True)

                
class ViewMainMenu(discord.ui.View):
    def __init__(self, context, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(MainMenu(context))

#-----Stars (Start)
class MenuStars(discord.ui.Select):
    def __init__(self, context):
        self.context = context
        options=[
            discord.SelectOption(label="power",emoji="💪",description="Força"),
            discord.SelectOption(label="price",emoji="💰",description="Preço"),
            discord.SelectOption(label="frags",emoji="🔢",description="Quantidade")
            ]
        super().__init__(placeholder="Selecione:",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(attachments=[discord.File(f'stars/stars_{self.values[0]}.png')])

                
class ViewStars(discord.ui.View):
    def __init__(self, context, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(MenuStars(context))
#-----Stars (End)

#-----Characters (Start)
class MenuChar1(discord.ui.Select):
    def __init__(self, context):
        self.context = context
        options = []
        for i in range(0,len(os.listdir(f'{PATH}/personagens/imgs'))):
            if len(options) > 24:
                break
            x = os.listdir(f'{PATH}/personagens/imgs')
            x.sort()
            x = x[i]
            if 'png' in x:
                options.append(discord.SelectOption(label=x[:-10], emoji="🗒️",description=x[:-10]))

        super().__init__(placeholder="Selecione:",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(attachments=[InfoChar(self.values[0])])

#Menu 2
class MenuChar2(discord.ui.Select):
    def __init__(self, context):
        self.context = context
        options = []
        for i in range(25,len(os.listdir(f'{PATH}/personagens/imgs'))):
            if len(options) > 24:
                break
            x = os.listdir(f'{PATH}/personagens/imgs')
            x.sort()
            x = x[i]
            if 'png' in x:
                options.append(discord.SelectOption(label=x[:-10], emoji="🗒️",description=x[:-10]))        

        super().__init__(placeholder="Selecione:",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(attachments=[InfoChar(self.values[0])])

#Menu 3
class MenuChar3(discord.ui.Select):
    def __init__(self, context):
        self.context = context
        options = []
        for i in range(50,len(os.listdir(f'{PATH}/personagens/imgs'))):
            if len(options) > 24:
                break
            x = os.listdir(f'{PATH}/personagens/imgs')
            x.sort()
            x = x[i]
            if 'png' in x:
                options.append(discord.SelectOption(label=x[:-10], emoji="🗒️",description=x[:-10]))

        super().__init__(placeholder="Selecione:",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(attachments=[InfoChar(self.values[0])])

#Menu 4
class MenuChar4(discord.ui.Select):
    def __init__(self, context):
        self.context = context
        options = []
        for i in range(75,len(os.listdir(f'{PATH}/personagens/imgs'))):
            if len(options) > 24:
                break
            x = os.listdir(f'{PATH}/personagens/imgs')
            x.sort()
            x = x[i]
            if 'png' in x:
                options.append(discord.SelectOption(label=x[:-10], emoji="🗒️",description=x[:-10]))

        super().__init__(placeholder="Selecione:",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(attachments=[InfoChar(self.values[0])])

#View
class ViewChar(discord.ui.View):
    def __init__(self, context, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(MenuChar1(context))
        self.add_item(MenuChar2(context))
        self.add_item(MenuChar3(context))
        self.add_item(MenuChar4(context))
#-----Characters (End)

#-----Puzzles (Start)
class PuzzlesMenu(discord.ui.Select):
    def __init__(self, context):
        self.context = context
        emojis = ['☠️','🐉','🦂','🈳','🦎','🦁','🐱','🐦','🐯','🐻']
        options = []
        for i in range(0,len(os.listdir(f'{PATH}/puzzles/'))):
            x = os.listdir(f'{PATH}/puzzles/')
            print(x[:-4], emojis[i])
            x.sort()
            x = x[i]
            options.append(discord.SelectOption(label=x[:-4], emoji=emojis[i],description=x[:-4]))
        print(options, 's')
        super().__init__(placeholder="Selecione:",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(attachments=[discord.File(f'{PATH}/puzzles/{self.values[0]}.png')])

#View
class ViewPuzzles(discord.ui.View):
    def __init__(self, context, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(PuzzlesMenu(context))

#-----Puzzles (End)