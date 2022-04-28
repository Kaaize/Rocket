from discord.ext.commands.errors import BadArgument, BadBoolArgument
from lib import *
from discord.ext import commands
import discord
import asyncio
from datetime import datetime, time, timedelta
import io
from PIL import Image, ImageFont, ImageDraw


def main():
    intents = discord.Intents.default()
    intents.members = True
   # bot = commands.Bot(command_prefix='?')
    bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)
    
#----------------EVENTOS
    @bot.event
    async def on_ready():
        print("BOT ONLINE!")
    
    @bot.event
    async def on_member_join(member):
        channel = bot.get_channel(846191030164520970)
        msg = f"{member.mention} entrou no Servidor."
        await channel.send(msg)

    @bot.event
    async def on_member_remove(member):
        channel = bot.get_channel(846191030164520970)
        msg = f"{member.name} deixou o Servidor."
        await channel.send(msg)
#----------------COMANDOS

#----------------Começo do comando GetPots
    @bot.command(brief="Calcula as Poções Necessárias", 
                usage="<exp atual> <level desejado> <tier>", 
                description="Calcula a quantidade de poções necessárias \
                para atingir o level desejado. \nTIERS: \nDIAMANTE: 0.5 \nOURO: 1 \nPRATA: 2 \nBRONZE: 3")
    async def getpots(ctx, current: int, target: int, tier: float):
        if target < 1000:
                await ctx.send(GetPots(current,target,tier))
        else:
            await ctx.send("Level muito alto")
        
    @getpots.error
    async def getpots_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Argumentos invalidos, tente `!help getpots`")
#----------------Fim do comando GetPots


#----------------Começo do comando GetLvl
    @bot.command(brief="Calcula o Level Atingido", 
                usage="<exp atual> <poções grandes> <poções medias> <poções pequenas> <tier>", 
                description="Calcula o level atingido ao usar a quantidade informada de poções. \
                \nTIERS: \nDIAMANTE: 0.5 \nOURO: 1 \nPRATA: 2 \nBRONZE: 3")
    async def getlvl(ctx, current: int, grande: int, media: int, pequena: int, tier: float):
        await ctx.send(GetLvl(current,grande, media, pequena, tier))

    @getlvl.error
    async def getlvl_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Argumentos invalidos, tente `!help getlvl`")
#----------------Fim do comando GetLvl

#----------------Começo do comando Stars
    @bot.command(brief="Tabela de estrelas (preço ou força)", 
                usage="<tipo>", 
                description="Mostra uma tabela de Estrelas (Preço ou Força).\nTipos:\npower\nprice")
    async def stars(ctx):
        await ctx.send(file=discord.File('imgs/stars_percent.png'))
        await ctx.send(file=discord.File('imgs/stars.png'))
        await ctx.send(file=discord.File('imgs/frags.png')) 
#----------------Fim do comando Stars

#----------------Começo do comando Craft
    @bot.command(brief="Mostra a quantidade de itens para craftar", 
                usage="<\"comida\"> <quantidade>", 
                description="Mostra a quantidade de itens necessária para para Craftar algo na quantidade \
                esolhida.\nEX: !craft \"ramen misto\" 10\n**Nomes com espaço precisam estar entre aspas.**")
    async def craft(ctx, nome, qty = 1):
        if qty > 1000:
            await ctx.send("Quantidade muito alta")
        else:
            custo = 0
            msg = ''
            try:
                x = GetRecipe(nome.lower(), qty)
                for local, recipes in x.items():
                    for ing, qty in recipes.items():
                        if isinstance(qty[0], int) and qty[0] > 0:
                            msg += f"```>>>>>{local.upper()}<<<<<\n"
                            break
                    for ing, qty in recipes.items():
                        if isinstance(qty[0], int) and qty[0] > 0:
                            custo += qty[1]
                            msg += f"{ing.capitalize()} - {qty[0]} > ${qty[1]}\n"
                    for ing, qty in recipes.items():
                        if isinstance(qty[0], int) and qty[0] > 0:
                            msg += '```'
                            break
                await ctx.send(msg)
                await ctx.send(f"Custo total: {custo}")
            except:
                await ctx.send("""Item não encontrado (utilize ç e ~).
Para encontrar o nome correto do item, tente o comando `!buscarcraft <parte do nome>`
EX (procurar o nome do item "Medalhão de carne"): `!buscarcraft medalh`
""")
    
    @craft.error
    async def craft_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("Argumentos invalidos. \nPara nomes com espaço, use Aspas (\"sopa mista picante\") \
            \ntente também `!help craft`")
#----------------Fim do comando Craft

#----------------Começo do comando Find

    @bot.command(brief="Busca um craft por parte do nome", usage="<texto procurado>")
    async def find(ctx, nome):
        if len(nome) >= 3:
            msg = Find(nome)
            print(msg)
            if msg == '':
                await ctx.send("Nenhum item encontrado")
            else:
                await ctx.send(f'```{Find(nome)}```')
        else:
            await ctx.send("Minimo de 3 letras para procura.")
#----------------Fim do comando Find

#----------------Começo do Comando InfoChar
    @bot.command(brief="Mostra informações sobre um personagem",
                usage="<char>",
                description="Mostra informações de um personagem.")
    async def infochar(ctx, name):
        image = CreateImageInfo(name)
        with io.BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

    @infochar.error
    async def infochar_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("Argumento invalido.")
#----------------Fim do Comando InfoChar

#----------------Começo do Comando Bau
    @bot.command(brief="Simula uma rotação de bau",
                usage="<char1> <char2> <char3> <keyn>",
                description="Simula um bau de rotação")
    async def bau(ctx, char1, char2, char3, keyn: int):
        c = BauRot(char1, char2, char3, keyn)
        text = '```'
        for k,v in c.items():
            text += f"{k.capitalize()}: {v}\n"
        text += '```'
        await ctx.send(text)
#----------------Fim do comando Bau

#----------------Começo do Comando Keys
    @bot.command(brief="Média de Chaves",
                usage="<chance> <frags_target>",
                description="Calcula a média de chaves necessária para conseguir X fragmentos")
    async def keys(ctx, chance: float, target: int):
        text = GetKeys(chance, target)
        keys = text[0]
        min = text[1]
        max = text[2]
        await ctx.send(f'```Média de Chaves: {keys:.2f} \nMinimo: {min}  \nMáximo: {max}```')
        
#----------------Fim do comando Keys

#----------------Começo do Comando Boost
    @bot.command(brief="Mostra a Média de preço para boostar um item de x até y",
                usage="<boost_start> <boost_end> <try_cost> <sky_pric> <wise_price> <crimson_price>",
                description="Calcula o preço Médio para boostar um item de X até Y")
    async def boost(ctx, start: int, end: int, try_cost: int, sky: float, wise: float, crimson: float):
            text = Boosts(start, end, try_cost, sky, wise, crimson)
            await ctx.send(f'```Custo Médio: {text}```')
 
    @boost.error
    async def boost_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("Argumento invalido.")
#----------------Fim do comando Boost

#----------------Fim do comando Cargo
    @bot.command(brief='Cargo Evento')
    async def cargo(ctx):
        role = discord.utils.find(lambda r: r.name == 'Evento', ctx.message.guild.roles)
        user = ctx.message.author
        if role not in ctx.author.roles:
            await user.add_roles(role)
            await ctx.send(f'{user.mention} Cargo Adicionado')
        else:
            await user.remove_roles(role)
            await ctx.send(f'{user.mention} Cargo Removido')
#----------------Fim do comando Cargo

#---------------------------------PxG Start
#---------------------------------Quantidade/Preço Boost
    @bot.command(brief='Stones necessárias')
    async def stones(ctx,boost: int, now: int, target: int, price: int, bonus=False):
        result = GetStones(boost,target,bonus)-GetStones(boost,now,bonus)
        await ctx.send(f'Stones: {result} | Preço: {result*price//1000}K')

#---------------------------------Celebi Decoder
    @bot.command(brief='Decodificador Celebi')
    async def celebi(ctx, posx: int, posy: int, code):
        await ctx.send(CelebiDecoder(posx,posy,code))

#---------------------------------PxG End

#---------------------------------    
    async def evento(name, time):  
        await bot.wait_until_ready()  
        channel = bot.get_channel(824552982728409089)
        msg = f'<@&930481857550778368> {name} em {time} Minutos!'
        await channel.send(msg)

    @bot.event
    async def background_task():
        while True:
            horarios = GetEvents()
            antecedencia = 15
            for i in horarios:
                agora = datetime.utcnow() + timedelta(hours = -3)
                if agora.weekday() == i[4] or i[4] == -1:
                    event_time = datetime.combine(agora.date(), time(i[1],i[2],i[3]))
                    target_time = event_time + timedelta(minutes=-antecedencia)
                    seconds_until_target = (target_time - agora).total_seconds()
                    if seconds_until_target >= 0:
                        name = i[0].capitalize()
                        await asyncio.sleep(seconds_until_target)
                        await evento(name, antecedencia)
            agora = datetime.utcnow() + timedelta(hours = -3)
            amanha = datetime.combine(agora.date() + timedelta(days=1), time(0))
            seconds = (amanha - agora).total_seconds()
            await asyncio.sleep(seconds)
#---------------------------------

    @bot.event
    async def on_message(message):

            if message.channel.name == 'bot_commands':
                await bot.process_commands(message)
            if message.channel.name == 'votação':
                emotes = ['👍','👎']
                for i in emotes:
                    await message.add_reaction(i)


#----------------INICIALIZAÇÃO DO BOT
    bot.loop.create_task(background_task())
    bot.run("Token")

#----------------EXECUÇÃO
main()
