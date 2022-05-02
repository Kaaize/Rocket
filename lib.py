from random import random,choice
import xml.etree.ElementTree as ET
from PIL import Image, ImageFont, ImageDraw
import os
import pathlib


PATH = pathlib.Path(__file__).parent.resolve()
#----------------FUNÇÕES

def GetExp(lv):
    lv = lv-1
    return ((50 * lv * lv * lv) - (150 * lv * lv) + (400 * lv)) / 3

def GetLvl(current: int, grande: int, media: int, pequena: int, tier: float):
    level = None
    exp_add = (grande*100000) + (media*10000) + (pequena*1000)
    total_exp = current+(exp_add*tier)
    for i in range(0,1001):
        if total_exp >= GetExp(i) and total_exp <= GetExp(i+1):
            level = i
            exp_to_up = GetExp(i+1) - GetExp(i)
            exceeded = total_exp - GetExp(i)
            percent_lvl = (1 - exceeded / exp_to_up) * 100
            return (f"""```Exp Atingida: {total_exp}
Level Atingido: {level}
Exp P/ Upar: {exp_to_up-exceeded:0.0f}
Porcentagem P/ Upar: {percent_lvl:0.0f}```""")
    return (f"""Level maior que 1000.""")

def GetPots(current: int, target: int, tier: int):
        pots = {'small':1000*tier,'med':10000*tier,'big':100000*tier}
        true_needed = GetExp(target)-current
        needed = true_needed
        big_needed = 0
        med_needed = 0
        small_needed = 0
        while 1:
            if needed > pots['big']:
                big_needed += 1
                needed -= pots['big']
            elif needed > pots['med']:
                med_needed += 1
                needed -= pots['med']
            elif needed > 0:
                small_needed += 1
                needed -= pots['small']
            else:
                break     
        return(f"""```Exp Necessária: {true_needed:0.0f}
Poções Grandes: {big_needed}
Poções Médias: {med_needed}
Poções Pequenas: {small_needed}```""")

#Funções para o comando Craft (Start)
result = {} #variavel responsavel por armazenar todos as informações de craft
def GetInfo(item, qty):
    tree = ET.parse('crafts/items.xml')
    item = Joiner(item)
    root = tree.getroot()
    for i in root:
        if i.get(item):
            x = (i.tag, item, qty, int(i.get(item))*qty)
            return x

def GetPlace(item):
    return GetInfo(item,1)[0]

def Joiner(nome):
    return '_'.join(nome.split(' '))

def Spliter(nome):
    return ' '.join(nome.split('_')).capitalize()

def GetCraft(item, qty: int):
    global result
    info = GetInfo(item,1)
    tree = ET.parse(f"crafts/{info[0]}/{item}.xml")
    root = tree.getroot()
    for k, v in root.attrib.items():
        v = int(v)
        info = GetInfo(k, v)
        if result.get(info[0]):
            if result[info[0]].get(info[1]):
                result[info[0]][info[1]][0] += info[2]*qty
                result[info[0]][info[1]][1] += info[3]*qty
            else:
                result[info[0]][info[1]] = [info[2]*qty,info[3]*qty]
        else:
            result[info[0]] = {info[1]: [info[2]*qty,info[3]*qty]}
        #items com crafts dentro do proprio craft
        nome = Joiner(k)
        try:
            if f'{nome}.xml' in os.listdir(f'{PATH}/crafts/{info[0]}'):
                GetCraft(nome, v*qty)
        except Exception as e:
            print('Erro', e)
    return result

def TryImage(path: str):
    try:
        return Image.open(path).convert('RGBA')
    except FileNotFoundError as e:
        print('Erro', e)
        return Image.open('blank.png').convert('RGBA')

def MontarCraft(nome, qty: int):
    global result
    nome = Joiner(nome)
    GetCraft(nome,qty) #passando as informações pra varival global result, atraves da função GetCraft
    title_font = ImageFont.truetype('crafts/imgs/font.TTF', 15) #fonte usada
    size = 2 #tamanho que a imagem vai ser montada (2 inicial, craft + total)
    line = 0 #posição verical inicial
    total_price = 0 #preço total
    largura = 500 #largura da imagem
    #obtendo a quantidade items para adicionar tamanho vertical a imagem
    for item in result:
        size += 1+len(result[item])
    #criando a imagem e deixando editavel editavel
    text_img = Image.new('RGBA', (largura,size*45), (0,70,100,255))
    image_editable = ImageDraw.Draw(text_img)
    #adicionando nome e quantidade do craft na imagem
    type = TryImage(f'crafts/imgs/{GetPlace(nome)}/{nome}.png')
    text_img.paste(type, (largura//2-16,line), mask=type)
    image_editable.text((largura//2,line+40),str(qty), (255,255,255), font=title_font, anchor="mm")
    line+=10 #espaçamento vertical
    for local, craft in result.items():
        line += 45 #espaçamento vertical
    
        #adicionando Local de Aquisição na imagem
        type = TryImage(f'crafts/imgs/base.png') #tentando carregar imagem do local de aquisição
        text_img.paste(type, (0,line), mask=type)
        image_editable.text((largura//2,line+15),local.upper(), (255,255,255), font=title_font, anchor="mm")
        #passando por cada item para adicionar na imagem
        for key, value in craft.items(): 
            line += 45 #espaçamento vertical
            total_price += value[1] #somando valor total
            type = TryImage(f'crafts/imgs/{GetPlace(key)}/{key}.png') #tentando carregar imagem do item
            text_img.paste(type, (10,line), mask=type) #adicionando imagem do item

            #adicionando texto de nome, quantidade e valor do item
            image_editable.text((45,line+5), Spliter(key), (255,255,255), font=title_font)
            image_editable.text((320,line+5),f'{str(value[0]).upper()}x', (255,255,255), font=title_font)
            image_editable.text((420,line+5),f'${str(value[1]).upper()}', (255,255,255), font=title_font)
    line += 45 #espaçamento pro total
    #total e zerando a variavel para os proximos usos
    image_editable.text((largura//2,line),f'${str(total_price).upper()}', (255,255,255), font=title_font, anchor="mm")
    result = {}
    return text_img

def Find(nome):
    dirs = ['arsenal2','arsenal3','arsenal4','arsenal5','refinaria','cozinheira_aliança']
    items = ''
    for i in dirs:
        for k in os.listdir(f'{PATH}/crafts/{i}'):
            if nome in k:
                items += f'{k}\n'
    return items
#Funções para o comando Craft (End)

def GetEvents():
    tree = ET.parse('eventos.xml')
    root = tree.getroot()
    dias = {'segunda': 0, 'terça':1, 'quarta': 2, 'quinta': 3, 'sexta': 4, 'sabado': 5, 'domingo': 6, 'todos': -1}
    info = []
    for k,v in root.items():
        splited = (v.split(';'))
        for event in splited:
            temp = event.split(',')
            for i in range(1,4):
                temp[i] = int(temp[i])
            temp.append(dias[k])
            info.append(temp)
    sorted_list = sorted(info, key = lambda i: i[1])
    return sorted_list

#Funções do comand Infochar (Start)
def CreateImageInfo(name):
    #Abrindo e obtendo info do XML
    tree = ET.parse(f'personagens/{name}.xml')
    root = tree.getroot()
    infos = root.attrib
    #Imagem base, fonte e cor
    base_image = Image.open('personagens/imgs/base/base.png')
    title_font = ImageFont.truetype('personagens/imgs/base/font.TTF', 18)
    COR = (255,255,255)
    TIERS = {'Bronze':(191,137,112), 'Prata':(178,169,173), 'Ouro':(255,215,0), 'Diamante':(185,242,255)}
    BRANCO = (255,255,255)
    
    #Adição da foto
    portrait = TryImage(f'personagens/imgs/{name.capitalize()}_medal.png')
    #portrait = Image.open(f'personagens/imgs/{name.capitalize()}_medal.png').convert('RGBA')
    text_img = Image.new('RGBA', (340,230), (0,0,0,0))
    text_img.paste(base_image, (0,0))
    text_img.paste(portrait, (13,9), mask=portrait)
     
    #Adição das classes
    icons = infos['tags'].split(";")
    for i in range(0,len(icons)):
        icon = TryImage(f"personagens/imgs/base/{icons[i].lower()}.png")
        #icon = Image.open(f"personagens/imgs/base/{icons[i].lower()}.png").convert('RGBA')
        text_img.paste(icon, (130+(i*30),75), mask=icon)
    
    #colocando base_image de volta como imagem variavel a ser usada
    base_image = text_img

    #Adição do Nome
    nome_separado = infos['name'].split()
    nome = ['','']
    stop = 0
    for i in nome_separado:
        if len(nome[0]) + len(i) < 23 and stop != 1:
            nome[0] += f'{i} '
        else:
            stop = 1
            nome[1] += f'{i} '

    image_editable = ImageDraw.Draw(base_image)
    image_editable.text((130,10),nome[0], TIERS[infos['tier']], font=title_font)
    image_editable.text((130,30),nome[1], TIERS[infos['tier']], font=title_font)
    #Atributos
    image_editable.text((35,127), infos['base_health'], BRANCO, font=title_font)
    image_editable.text((35,152), ', '.join((infos['vitalidade']).split(';')), BRANCO, font=title_font)
    image_editable.text((35,177), infos['speed'], BRANCO, font=title_font)
    image_editable.text((35,202), infos['defense'], BRANCO, font=title_font)
    return base_image
#Funções do comand Infochar (End)

def GetFrags(chance, keys):
    keyn = 0
    chance100 = (10,10,10,10,10,10,10,10,10,10,25,50,75,100)
    total_frags = 0
    for i in range(0,keys):
        keyn += 1
        frags = 20
        if random() <= (chance100[keyn]/100):
            frags = 100
            keyn = 0
        if random() <= (chance/100):
            total_frags += frags
    return total_frags   

def GetKeys(chance, target):
    keyn = 0
    chance100 = (10,10,10,10,10,10,10,10,10,10,25,50,75,100)
    total_frags = 0
    total_keys = 0
    while total_frags < target:
        keyn += 1
        frags = 20
        if random() <= (chance100[keyn]/100):
            frags = 100
            keyn = 0
        if random() <= (chance/100):
            total_frags += frags
        total_keys += 1
    return total_keys

def MediaKeys(chance, target):
    loops = [(500,1000000), (1000,100000), (2000,10000)]
    for i in loops:
        if target > 2000 or target == 0:
            return None
        elif target <= i[0]:
            loop = i[1]
            break
    total_geral = 0
    min = 0
    max = 0
    for i in range(0,loop):
        num_keys = GetKeys(chance, target)
        if num_keys < min or min == 0:
            min = num_keys
        if num_keys > max:
            max = num_keys
        total_geral += num_keys
    return ((total_geral/loop), min, max, loop)

def MediaFrags(chance, keys):
    loops = [(100,1000000), (500,100000), (1000,10000)]
    for i in loops:
        if keys > 1000 or keys == 0:
            return None
        elif keys <= i[0]:
            loop = i[1]
            break
    total_geral = 0
    min = 0
    max = 0
    for i in range(0,loop):
        num_frags = GetFrags(chance,keys)
        if num_frags < min or min == 0:
            min = num_frags
        if num_frags > max:
            max = num_frags
        total_geral += num_frags
    return ((total_geral/loop), min, max, loop)

def Boosts(start,end,try_cost, sky, wise, crimson):
    chances = [35,30,25,20,22,18,14,10,10,9,8,7]
    cap = [3,4,5,6,5,6,8,11,11,12,13,15]
    cristais = [0,0,0]
    cristais_name = ['Céu', 'Sábio', 'Carmesin']
    tipo = try_cost
    custo = 0
    start_boost = start
    final_boost = end
    for i in range(0,10000):
        tent = 0
        boost = start_boost
        while boost < final_boost:
            for j in range(0,cap[boost]):
                sorteio = random()
                if sorteio <= (chances[boost]/100) or j+1 == cap[boost]:
                    tent += 1
                    if boost < 4:
                        custo += tipo*sky
                        cristais[0] += try_cost/10000
                    elif boost < 8:
                        custo += tipo*wise
                        cristais[1] += try_cost/10000
                    else:
                        custo += tipo*crimson
                        cristais[2] += try_cost/10000
                    boost += 1
                    break
                else:
                    tent += 1
                    if boost < 4:
                        custo += tipo*sky
                        cristais[0] += try_cost/10000
                    elif boost < 8:
                        custo += tipo*wise
                        cristais[1] += try_cost/10000
                    else:
                        custo += tipo*crimson
                        cristais[2] += try_cost/10000
    text = f'{int(custo//10000):0,}\n'.replace(',','.')
    for i in range(0,3):
        text += f'{cristais_name[i]}: {cristais[i]:.2f}\n'
    return text


#PXG
def GetStones(increase,target,bonus=False):
    stones = 0
    skip = 0
    for i in range(0,target):
        if skip:
            skip -= 1
            continue
        stones += 1+(i//increase)
        if bonus == True and i < 9:
            skip += bonus
    return stones



def CelebiDecoder(startx, starty, code):
    posx = []
    posy = []
    var = ''
    for i in range(0,len(code)):
        if not code[i].isdigit():
            posx.append(code[i])
            if i != 0:
                posy.append(var)
            var = ''
        else:
            var += code[i]
    posy.append(var)
    code = posx,posy
    text = ''
    for i in range(0,len(code[0])):
        x = ord(code[0][i])-96-1
        y = int(code[1][i])-1
        text += f"{startx+x}, {starty+y}\n"
    return text



