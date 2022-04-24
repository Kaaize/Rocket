from discord.ext.commands.errors import BadArgument, BadBoolArgument
from lib import *
from discord.ext import commands
import discord
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
        idchannel = 846191030164520970
        msg = f"{member.mention} entrou no Servidor."
        await bot.get_channel(idchannel).send(msg)

    @bot.event
    async def on_member_remove(member):
        idchannel = 846191030164520970
        msg = f"{member.name} deixou o Servidor."
        await bot.get_channel(idchannel).send(msg)
#----------------COMANDOS


#----------------Começo do comando GetPots
    @bot.command(brief="Calcula as Poções Necessárias", 
                usage="<exp atual> <level desejado> <tier>", 
                description="Calcula a quantidade de poções necessárias \
                para atingir o level desejado. \nTIERS: \nDIAMANTE: 0.5 \nOURO: 1 \nPRATA: 2 \nBRONZE: 3")
    async def getpots(ctx, current: int, target: int, tier: float):
        if target < 1000:
                await ctx.send(getPots(current,target,tier))
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
        await ctx.send(getLvl(current,grande, media, pequena, tier))

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
                x = getRecipe(nome.lower(), qty)
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
            if msg == '':
                await ctx.send("Nenhum item encontrado")
            else:
                await ctx.send(f'```{msg}```')
        else:
            await ctx.send("Minimo de 3 letras para procura.")
#----------------Fim do comando Find

#----------------Começo do comando Defense
    @bot.command(brief="Calcula a redução de dano",
                usage="<armor> <def factor>",
                description="Calcula a redução de dano")
    async def defense(ctx, armor: int, deff: int):
        await ctx.send(reduction(armor,deff))

    @defense.error
    async def defense_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("Argumento invalido, tente !help defense")
#----------------Fim do comando Defense

#----------------Começo do comando Effect
    @bot.command(brief="Calcula a vida efetiva",
                usage="<life> <dmg reduction>",
                description="Calcula a vida efetiva")
    async def effect(ctx, life: int, red: float):
        await ctx.send(effectiviness(life, red))

    @effect.error
    async def effect_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("Argumento invalido, tente !help effect")
#----------------Fim do comando Effect

#----------------Começo do Comando InfoChar
    @bot.command(brief="Mostra informações sobre um personagem",
                usage="<char>",
                description="Mostra informações de um personagem.")
    async def infochar(ctx, name):
        await ctx.send(InfoCharacter(name))
        
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
        await ctx.send(f'```Média de Chaves: {keys} \nMinimo: {min}  \nMáximo: {max}```')
        
#----------------Fim do comando Keys

#----------------Começo do Comando Boost
    @bot.command(brief="Mostra a Média de preço para boostar um item de x até y",
                usage="<boost_start> <boost_end> <try_cost> <sky_price> <wise_price> <crimson_price>",
                description="Calcula o preço Médio para boostar um item de X até Y")
    async def boost(ctx, start: int, end: int, try_cost: int, sky: float, wise: float, crimson: float):
            text = Boosts(start, end, try_cost, sky, wise, crimson)
            await ctx.send(f'```Custo Médio: {text}```')
 
    @boost.error
    async def boost_error(ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("Argumento invalido.")
#----------------Fim do comando Boost

    @bot.event
    async def on_message(message):

            if message.channel.name == 'bot_commands':
                await bot.process_commands(message)
            if message.channel.name == 'votação':
                emotes = ['🟢']
                for i in emotes:
                    await message.add_reaction(i)


#----------------INICIALIZAÇÃO DO BOT
    bot.run("bot_key")


#----------------EXECUÇÃO
main()
