from code import interact
from logging import PlaceHolder
from discord.ext.commands.errors import BadArgument
from lib import *
from discord.ext import commands
import discord
import asyncio
from datetime import datetime, time, timedelta
import io
import json
from dropdowns import *

host = ''
db = ''
user = ''
password = ''

def main():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    #Função para obter o prefixo do servidor em questão
    def get_prefix(bot=None, message=None):
        con=Conexao(host, db, user, password)
        try:
            sql = f"SELECT prefix FROM prefixes WHERE guild = '{message.guild.id}'"
            x = con.consultar(sql)
            con.fechar()
            return x[0][0]
        except:
            return 'r!'

    #adicionando o prefixo ao bot, do servidor em questão
    bot = commands.Bot(command_prefix=get_prefix, case_insensitive=False, intents=intents)

    #Função para obter o canal que o servidor usa para o bot
    def get_chan(guild):
        con=Conexao(host, db, user, password)
        try:
            sql = f"SELECT channel FROM channels WHERE guild = '{guild.id}'"
            x = con.consultar(sql)
            con.fechar()
            return int(x[0][0])
        except:
            return None
    
    #Função para obter os canais que recebem reação do bot
    def get_react(channel):
        con=Conexao(host, db, user, password)
        try:
            sql = f"SELECT emote FROM emotes WHERE channel = '{channel.id}'"
            x = con.consultar(sql)
            con.fechar()
            return x
        except Exception as e:
            return print(e)
   

    
#----------------EVENTOS
    @bot.event
    async def setup_hook() -> None:
        bot.bg_task = bot.loop.create_task(background_task())

    @bot.event
    async def on_ready():
        print("BOT ONLINE!")
        for i in bot.guilds: print("Server >> ",i.name)
    
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
        con=Conexao(host, db, user, password)
        try:
            sql = f"INSERT INTO prefixes VALUES ('{guild.id}', 'r!')"
            x = con.manipular(sql)
            con.fechar()
        except:
            print(f'Não foi possivel adicionar {guild} ({guild.id}) no banco de dados')

    @bot.event
    async def on_guild_remove(guild):
        con=Conexao(host,db,user,password)
        try:
            sql = f"DELETE FROM prefixes WHERE guild = '{guild.id}'"
            x = con.manipular(sql)
            con.fechar()
        except:
            print(f'Não foi possivel remover {guild} ({guild.id}) do banco de dados')

    #Prefix (end)
#----------------COMANDOS

#----------------Começo do comando Prefix
    @bot.command(brief="Modifica o prefixo do bot. Padrão: r!",
                usage="<new_prefix>",
                description="troca o prefixo atual do bot para o escolhido.")
    @commands.has_permissions(administrator = True)
    async def prefix(ctx, prefix):
        con = Conexao(host,db,user,password)
        try:
            #Adicionar se não existir
            sql =f"""INSERT INTO prefixes (guild, prefix)
                SELECT '{ctx.guild.id}','{prefix}'
                WHERE
                    NOT EXISTS (
                        SELECT guild FROM prefixes WHERE guild = '{ctx.guild.id}'
                    );"""
            con.manipular(sql)

            #Atualizar se existir
            sql = f"""UPDATE prefixes
            SET prefix = '{prefix}'
            WHERE guild = '{ctx.guild.id}'"""
            con.manipular(sql)
            con.fechar()
            await ctx.send(f"Seu prefixo agora é {prefix}")
        except Exception as e:
            print(e)

    @prefix.error
    async def prefix_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            msg = "Você não tem permissão para isso."
            await ctx.send(msg)

#----------------Começo do comando Prefix

#----------------Começo do comando Channel
    @bot.command(brief="Modifica o canal do bot (ADM)",
                usage="",
                description="Adiciona o canal atual como unico que o bot vai responder \
                    (usar no canal já selecionado remove a exclusividade)")
    @commands.has_permissions(administrator = True)
    async def channel(ctx):
        con = Conexao(host, db, user, password)
        chan = get_chan(ctx.guild)
        if chan == None:
            sql = f"INSERT INTO channels VALUES ('{ctx.guild.id}','{ctx.channel.id}');"
            con.manipular(sql)
            await ctx.send("Agora seu canal de comandos é esse")
        elif chan != ctx.channel.id:
            sql = f"UPDATE channels SET channel = '{ctx.channel.id}' WHERE guild = '{ctx.guild.id}'"
            con.manipular(sql)
            await ctx.send("Agora seu canal de comandos é esse")
        else:
            sql = f"DELETE FROM channels WHERE guild = '{ctx.guild.id}'"
            con.manipular(sql)
            await ctx.send("Agora você não tem nenhum canal especifico")
        con.fechar()
            
    @channel.error
    async def channel_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            msg = "Você não tem permissão para isso."
            await ctx.send(msg)
#----------------Fim do comando Channel         
# 
# #----------------Começo do comando React
    @bot.command(brief="Adiciona ou Remove um canal para reações (ADM)",
                usage="",
                description="Use o comando no chat que deseja ativar as reações de :thumbsup: e :thumbsdown:")
    @commands.has_permissions(administrator = True)
    async def react(ctx, *args):
        con = Conexao(host, db, user, password)
        if len(args) > 0:
            for i in args:
                sql = f"INSERT INTO emotes VALUES ('{ctx.channel.id}','{i}')"
                con.manipular(sql)
            await ctx.send(f"Reações adicionadas a esse canal, para remover digite {get_prefix(0,ctx)}react")
        else:
            sql = f"DELETE FROM emotes WHERE channel = '{ctx.channel.id}'"
            con.manipular(sql)
            await ctx.send("Reações removidas desse canal.")


    @react.error
    async def react_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            msg = "Você não tem permissão para isso."
            await ctx.send(msg)
#----------------Fim do comando React      

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
        if isinstance(error, BadArgument):
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
        if isinstance(error, BadArgument):
            await ctx.send("Argumentos invalidos, tente `!help getlvl`")
#----------------Fim do comando GetLvl

#----------------
    @bot.command(brief="Menu")
    async def menu(ctx):
        await ctx.send("Menu Principal: ", view=ViewMainMenu(ctx), delete_after=180)
#----------------

#----------------Começo do comando Stars
    @bot.command(brief="Informação de Estrelas", usage="")
    async def stars(ctx):
        await ctx.send("Info de Estrelas: ",view=ViewStars(ctx), delete_after=180)
#----------------Fim do comando Stars

#----------------Começo do comando Infos
    @bot.command(brief="Informação dos personagens", usage="")
    async def infos(ctx):
        await ctx.send("Info dos Personagens: ",view=ViewChar(ctx), delete_after=180)
#----------------Fim do comando Infos


#----------------Começo do comando Craft
    @bot.command(brief="Mostra a quantidade de itens para craftar", 
                usage="<\"craft\"> <quantidade> <craft2> <quantidade2>...", 
                description="Mostra a quantidade de itens necessária para para Craftar algo na quantidade \
                esolhida.\nEX: !craft \"atum grelhado\" 10\n**Nomes com espaço precisam estar entre aspas.**")
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

    @craft.error
    async def craft_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send(f"Argumentos invalidos. \nPara nomes com espaço, use Aspas (\"sopa mista picante\") \
            \ntente também `{get_prefix(0,ctx)}help craft`")
#----------------Fim do comando Craft

#----------------Começo do comando Find

    @bot.command(brief="Busca um craft por parte do nome", usage="<texto procurado>")
    async def find(ctx, nome):
        if len(nome) >= 3:
            msg = Find(nome)
            if msg == '':
                await ctx.send("Nenhum item encontrado")
            else:
                await ctx.send(f'```\n{msg}```')
        else:
            await ctx.send("Minimo de 3 letras para procura.")
#----------------Fim do comando Find

#----------------Começo do Comando InfoChar
    @bot.command(brief="Mostra informações sobre um personagem", usage="<char>")
    async def infochar(ctx, name):
        image = CreateImageInfo(name)
        if isinstance(image,str):
            await ctx.send(image)
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
                usage="<chance> <num_keys> <frags_to_get>",
                description="Retorna a média de fragmentos com X chaves")
    async def keys(ctx, chance: float, keys: int, frags_target: int = 0):
        if chance < 13.33:
            await ctx.send("Chance não pode ser menor que 13.33")
            return
        if keys > 500:
            await ctx.send("Chave não pode ser maior que 500")
            return
        info = MediaFrags(chance, keys, frags_target)
        msg = f'```Simulações: {info[1]} | Chance: {chance}% | Chaves Usadas: {keys}.\n\
Média de Fragmentos: {info[0]:.2f}```'
        if frags_target != 0:
            msg = f"""```Simulações: {info[1]} | Chance: {chance}% | Chaves Disponiveis: {keys}.\n
Média de Fragmentos: {info[0]:.2f}
Probabilidade de pegar {frags_target} fragmentos com {keys} chaves: {info[2]*100:.2f}%```"""
        await ctx.send(msg)
    
    @keys.error
    async def keys_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send(f"Argumento invalido, tente {get_prefix(0,ctx)}help keys")
        else:
            await ctx.send(f"Erro: {error}")
#----------------Fim do comando Bau

#----------------Começo do Comando Keys
    @bot.command(brief="Calcula a média de Chaves usadas para obter X Fragmentos",
                usage="<chance> <frags_target> <keys_to_use>",
                description="Retorna a média de chaves para x fragmentos")
    async def frags(ctx, chance: float, target: int, keys_target: int = 0):
        if chance < 13.33:
            await ctx.send("Chance não pode ser menor que 13.33")
            return
        if target > 2000:
            await ctx.send("Alvo de fragmentos não pode ser maior que 2000")
            return
        info = MediaKeys(chance, target, keys_target)
        msg = f'```Simulações: {info[1]} | Chance: {chance}% | Fragmentos Alvo: {target}.\n\
Média de Chaves: {info[0]:.2f}```'
        if keys_target != 0:
            msg = f"""```Simulações: {info[1]} | Chance: {chance}% | Fragmentos Alvo: {target}.\n
Média de Chaves: {info[0]:.2f}
Probabilidade de pegar {target} fragmentos com {keys_target} chaves: {info[2]*100:.2f}%```"""
        await ctx.send(msg)
            
    @frags.error
    async def frags_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send(f"Argumento invalido, tente {get_prefix(0,ctx)}help frags")
        else:
            await ctx.send(f"Erro: {error}")
        
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
            await ctx.send(f"Argumento invalido, tente {get_prefix(0,ctx)}help frags")
#----------------Fim do comando Boost

#----------------Fim do comando Cargo
    @bot.command(brief='Cargo `Evento`', usage="", description="Adiciona/Remove o cargo Evento.")
    @commands.bot_has_permissions(manage_roles=True)
    async def cargo(ctx):
        role = discord.utils.find(lambda r: r.name == 'Evento', ctx.message.guild.roles)

        user = ctx.message.author
        if role not in ctx.author.roles:
            await user.add_roles(role)
            await ctx.send(f'{user.mention} Cargo Adicionado')
        else:
            await user.remove_roles(role)
            await ctx.send(f'{user.mention} Cargo Removido')
        
    @cargo.error
    async def cargo_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Não tenho permissão para adicionar o cargo.")
        else:
            await ctx.send(f"Cargo `Evento` não encontrado")
#----------------Fim do comando Cargo

#---------------------------------PxG Start
#---------------------------------Quantidade/Preço Boost
    @bot.command(brief='Stones necessárias', usage='<boost_cost> <boost_now> <boost_target> <price>')
    async def stones(ctx,boost: int, now: int, target: int, price: int, bonus=False):
        result = GetStones(boost,target,bonus)-GetStones(boost,now,bonus)
        await ctx.send(f'Stones: {result} | Preço: {result*price//1000}K')
    
    @stones.error
    async def stones_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send(f"Argumento invalido, tente {get_prefix(0,ctx)}help stones")

#---------------------------------Celebi Decoder
    @bot.command(brief='Decodificador Celebi', usage="<pilar_pox> <pilar_posy> <code>")
    async def celebi(ctx, posx: int, posy: int, code):
        await ctx.send(CelebiDecoder(posx,posy,code))

    @celebi.error
    async def celebi_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send(f"Argumento invalido, tente {get_prefix(0,ctx)}help celebi")

#---------------------------------PxG End

#---------------------------------    
    async def evento(name, time):  
        await bot.wait_until_ready()
        for guild in bot.guilds:
            channel = bot.get_channel(get_chan(guild))
            if channel != None:
                try:
                    role = discord.utils.get(guild.roles, name="Evento")
                    msg = f'{role.mention} {name} em {time} Minutos'
                except AttributeError:
                    msg = f'{name} em {time} Minutos. (Aviso: Cargo `Evento` não encontrado)'
                await channel.send(msg)
            else:
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).send_messages:
                        try:
                            role = discord.utils.get(guild.roles, name="Evento")
                            msg = f'{role.mention} {name} em {time} Minutos'
                        except AttributeError:
                            msg = f'{name} em {time} Minutos. (Aviso: Cargo `Evento` não encontrado)'
                        await channel.send(msg)
                        break

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

        if message.author.bot:
            return
        pref = get_prefix(0, message)
        if pref in message.content:
            print(f'{message.guild.name} | {message.author} | {message.channel.name} >> {message.content}')

        if f'{pref}channel' in message.content or f'{pref}react' in message.content:
            await bot.process_commands(message)
            return

        if get_chan(message.guild) == message.channel.id or get_chan(message.guild) == None:
            await bot.process_commands(message)


        if 'prefix' == message.content:
            prefix = get_prefix(0, message)
            await message.channel.send(f'Meu prefixo é {prefix}')
            print(f'{message.guild.name} | {message.author} | {message.channel.name} >> {message.content}')


        channels_react = get_react(message.channel)
        if channels_react:
            for i in channels_react:
                await message.add_reaction(i[0])



#----------------INICIALIZAÇÃO DO BOT
    #bot.loop.create_task(background_task())
    with open('token.json', 'r') as f:
        info = json.load(f)
    bot.run(info['token'])

#----------------EXECUÇÃO
main()
