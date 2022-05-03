from discord.ext.commands.errors import BadArgument
from lib import *
from discord.ext import commands
import discord
import asyncio
from datetime import datetime, time, timedelta
import io
import json


def main():
    intents = discord.Intents.default()
    intents.members = True


    #bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)
    def get_prefix(bot=None, message=None):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        try:
            prefix = str(message.guild.id)
            return prefixes[prefix]
        except AttributeError:
            return ['defaultPrefix']
    bot = commands.Bot(command_prefix=get_prefix)
    
#----------------EVENTOS
    @bot.event
    async def on_ready():
        print("BOT ONLINE!")
    
    @bot.event
    async def on_guild_join(guild):
        await guild.text_channels[1].send(f"Estou aqui, use {get_prefix}help")

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

    #Prefix (start)
    @bot.event
    async def on_guild_join(guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = 'r!'

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @bot.event
    async def on_guild_remove(guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)


    #Prefix (end)
#----------------COMANDOS

#Prefix (start)
    @bot.command(brief="Modifica o prefixo do bot padrão: !")
    @commands.has_permissions(administrator = True)
    async def prefix(ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f"Prefix now is {prefix}")
    @prefix.error
    async def prefix_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            msg = "Você não tem permissão para isso."
            await ctx.send(msg)

#Prefix (end)

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
                description="Mostra uma tabela de Estrelas.\nTipos:\npower\nprice\nfrags")
    async def stars(ctx, type=''):
        if type.lower() == 'power':
            await ctx.send(file=discord.File('stars/stars_power.png'))
        elif type.lower() == 'price':
            await ctx.send(file=discord.File('stars/stars_price.png'))
        elif type.lower() == 'frags':
            await ctx.send(file=discord.File('stars/stars_frags.png'))
        else:
            await ctx.send(' um tipo: !stars power, !stars price or !stars frags')
#----------------Fim do comando Stars

#----------------Começo do comando Craft
    @bot.command(brief="Mostra a quantidade de itens para craftar", 
                usage="<\"comida\"> <quantidade>", 
                description="Mostra a quantidade de itens necessária para para Craftar algo na quantidade \
                esolhida.\nEX: !craft \"ramen misto\" 10\n**Nomes com espaço precisam estar entre aspas.**")
    async def craft(ctx, *kargs):
        CraftClean()
        if len(kargs) > 3:
            nomes = kargs[::2]
            qtys = kargs[1::2]
        else:
            nomes = [kargs[0]]
            qtys = [kargs[1]]
        for i in range(0,len(nomes)):
            GetCraft(Joiner(nomes[i]),int(qtys[i]))
            if int(qtys[i]) > 100:
                await ctx.send("Quantidade muito alta")
                return
        else:
            image = MontarCraft(nomes,qtys)
            with io.BytesIO() as image_binary:
                image.save(image_binary, 'PNG')
                image_binary.seek(0)
                await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

    """@craft.error
    async def craft_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("Argumentos invalidos. \nPara nomes com espaço, use Aspas (\"sopa mista picante\") \
            \ntente também `!help craft`")"""
#----------------Fim do comando Craft

#----------------Começo do comando Find

    @bot.command(brief="Busca um craft por parte do nome", usage="<texto procurado>")
    async def find(ctx, nome):
        if len(nome) >= 3:
            msg = Find(nome)
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
    @bot.command(brief="Calcula a média de Fragmentos obtidos com X Chaves",
                usage="<chance> <num_keys>",
                description="Retorna a média de fragmentos com X chaves")
    async def keys(ctx, chance: float, keys: int):
        if chance < 13.33:
            await ctx.send("Chance não pode ser menor que 13.33")
            return
        if keys > 500:
            await ctx.send("Chave não pode ser maior que 500")
        info = MediaFrags(chance, keys)
        await ctx.send(f'```Loop: {info[3]}\nMédia de Fragmentos: {info[0]:.2f}\
        \nMinimo: {info[1]}  \nMáximo: {info[2]}```')
#----------------Fim do comando Bau

#----------------Começo do Comando Keys
    @bot.command(brief="Calcula a média de Chaves usadas para obter X Fragmentos",
                usage="<chance> <frags_target>",
                description="Retorna a média de chaves para x fragmentos")
    async def frags(ctx, chance: float, target: int):
        if chance < 13.33:
            await ctx.send("Chance não pode ser menor que 13.33")
            return
        if target > 2000:
            await ctx.send("Alvo de fragmentos não pode ser maior que 2000")
        info = MediaKeys(chance, target)
        await ctx.send(f'```Loop: {info[3]}\nMédia de Chaves: {info[0]:.2f}\
        \nMinimo: {info[1]}  \nMáximo: {info[2]}```')
        
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
        
        if 'bot_commands':
            for guild in bot.guilds:
                # if you want to find the channel by id
                # selectedVcChannel = discord.utils.get(guild.channels, id=voice_channel_id)
                channel = discord.utils.get(guild.channels, name='bot_commands')
                # If you want the first channel found with the name of 'VcChannelName' 
                # you can add this condition with a break statement,
                # you obviously don't need this if you use id
                if channel:
                    try:
                        role = discord.utils.get(guild.roles, name="Evento")
                        msg = f'{role.mention} {name} em {time} Minutos'
                    except AttributeError:
                        msg = f'{name} em {time} Minutos'
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
        if message.author.id == 572493962305077259:
            return

        if 'prefix' == message.content and message.channel.name == 'bot_commands':
            with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)
            prefix = prefixes[str(message.guild.id)]
            await message.channel.send(f'My prefix is: {prefix}')


        if message.channel.name == 'bot_commands':
            await bot.process_commands(message)
        if message.channel.name == 'votação':
            emotes = ['👍','👎']
            for i in emotes:
                await message.add_reaction(i)



#----------------INICIALIZAÇÃO DO BOT
    bot.loop.create_task(background_task())
    bot.run("token")

#----------------EXECUÇÃO
main()
