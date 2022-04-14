from math import e
from sqlite3.dbapi2 import Cursor
from data import *
from random import random,choice
import sqlite3
#----------------FUNÇÕES
def map(x, in_min, in_max, out_min, out_max):
    return float((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def getExp(lv):
    lv = lv-1
    return ((50 * lv * lv * lv) - (150 * lv * lv) + (400 * lv)) / 3

def getLvl(current: int, grande: int, media: int, pequena: int, tier: float):
    level = None
    exp_add = (grande*100000) + (media*10000) + (pequena*1000)
    total_exp = current+(exp_add*tier)
    for i in range(0,1001):
        if total_exp >= getExp(i) and total_exp <= getExp(i+1):
            level = i
            exp_to_up = getExp(i+1) - getExp(i)
            exceeded = total_exp - getExp(i)
            percent_lvl = (1 - exceeded / exp_to_up) * 100
            return (f"""```Exp Atingida: {total_exp}
Level Atingido: {level}
Exp P/ Upar: {exp_to_up-exceeded:0.0f}
Porcentagem P/ Upar: {percent_lvl:0.0f}```""")
    return (f"""Level maior que 1000.""")

def getPots(current: int, target: int, tier: int):
        pots = {'small':1000*tier,'med':10000*tier,'big':100000*tier}
        true_needed = getExp(target)-current
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

def getRecipe(nome, main_qty):
    items = {
            #cozinha
            'geladeira': {
                'tomate':[0,0], 'cogumelo':[0,0], 'ovo':[0,0], 'bacon':[0,0], 'folha verde':[0,0], 'leite':[0,0], 'agua':[0,0],
				'queijo':[0,0], 'peixe cru':[0,0], 'bife cru':[0,0], 'limão':[0,0], 'vinho barato':[0,0], 'manteiga':[0,0],
            },
			 
			'armario': {
                'batata':[0,0], 'cebola':[0,0], 'azeite':[0,0], 'alho':[0,0], 'arroz':[0,0], 'farinha':[0,0], 'shoyu':[0,0], 'sal':[0,0],
				'pimenta':[0,0], 'lata de atum':[0,0],
            },
			 
			'tigela': {'tigela':[0,0]},
			 
			'rolo': {'massa':[0,0]},
			 
			'corte': {'pasta':[0,0]},
			 
			'panela': {
                'ramen':[0,0], 'arroz cozido':[0,0], 'sopa de vegetais':[0,0], "sopa mista picante":[0,0], "ramen de carne":[0,0], "miso ramen":[0,0], "ramen misto":[0,0],
				"ramen de galinha":[0,0], "ramen de camarão":[0,0], "lagosta prime":[0,0], "caranguejo cozido":[0,0]
            },
				
			'tabua': {
                "onigiri":[0,0], "sushi":[0,0], "nigiri":[0,0], "bento japones":[0,0], "dango":[0,0], "waffles":[0,0]
            },
			 
			'forno':{
                "bife prime":[0,0], "carne de porco gourmet":[0,0], "polvo gourmet com ovos":[0,0], "pizza":[0,0], "frango a parmegiana":[0,0], 
				"frango a parmegiana com ovos":[0,0]
            },
                
		    'frigideira':{
                "bife frito":[0,0], "ovo frito":[0,0], "espeto de carne":[0,0], "kakuni japones prime":[0,0], "peixe grelhado gourmet":[0,0],
				"espeto de peixe japones prime":[0,0], "takoyaki":[0,0], "gyoza":[0,0], "peixe apimentado picante":[0,0],
                "coxa de frango frito":[0,0], "camarão empanado":[0,0]
            },

            'geladeira_aliança': {
                "bife cru premium": [0,0], "lagosta crua": [0,0], "camarão cru": [0,0], "carne crua de coelho": [0,0], "ostra": [0,0], "alface": [0,0],
                "vinho branco": [0,0], "trufa branca": [0,0], "creme de leite": [0,0], "atum":[0,0]
            },

            'menu_aliança': {
                "bife e ovo de frigideira": [0,0], "medalhão de carne":  [0,0],
                "salada italiana":  [0,0], "espeto de carne gourmet":  [0,0], "curry de coelho":  [0,0],
                "camarões salteados": [0,0], "ensopado de ostra": [0,0],
            },
			 
            #navio
            
            'npc': {
                #Barco
                    "tora de madeira":[0,0], "algodão de baixa qualidade":[0,0], "minério de cobre":[0,0], "pólvora":[0,0],
                    "tora de carvalho": [0,0], "algodão": [0,0], "minério de ferro": [0,0], "pólvora melhorada": [0,0],
                    "tora de mogno": [0,0], "algodão melhorado": [0,0], "minério de aço": [0,0], "pólvora superior": [0,0],
                #Cozinha
                    "carne de porco": [0,0], "perna de galinha": [0,0], "peru": [0,0], "tomate do deserto": [0,0],
                    "folhas verdes especiais": [0,0], "açucar rosa": [0,0],  "carne de caranguejo": [0,0],
            },

            'refinaria': {
                "prancha de madeira":[0,0], "lingote de cobre":[0,0], "pano de baixa qualidade":[0,0], "corda de baixa qualidade":[0,0], "prego de cobre":[0,0],
                "prancha de carvalho":[0,0], "lingote de ferro":[0,0], "pano":[0,0], "corda":[0,0], "prego de ferro":[0,0],
                "prancha de mogno":[0,0], "lingote de aço":[0,0], "pano melhorado":[0,0], "corda melhorada":[0,0], "prego de aço":[0,0],
            },

            'drop': {
                "cola":[0,0], "cano de arma": [0,0], "bala de canhão": [0,0],
                "bateria":[0,0], "tanque de ar": [0,0], "liquido inflamavel": [0,0], "cogumelo venenoso": [0,0], "lata de óleo": [0,0],
                "grande cola": [0,0], "cano de arma superior": [0,0], "bala de canhão de aço": [0,0],
            },

            'mesa comum': {
                #barco 1
                    "canhão1":[0,0], "vela1":[0,0], "casco1":[0,0],
                #barco 2
                    "barco2":[0,0], "canhão2":[0,0], "vela2":[0,0], "casco2":[0,0], "espingarda2":[0,0], "tiro de canhão corrente2":[0,0],
                     "ariete2":[0,0],
                #barco 3
                    "barco3":[0,0], "canhão3":[0,0], "vela3":[0,0], "casco3":[0,0], "espingarda3":[0,0], "tiro de canhão corrente3":[0,0], "ariete3":[0,0], 
                    "metralhadora3":[0,0], "acelerar3":[0,0], "canhão pesado3":[0,0], 
                #barco 4
                    "barco4":[0,0], "canhão4":[0,0], "vela4":[0,0], "casco4":[0,0], 
            },

            'estaleiro': {
                #Nivel 1
                    "espingarda4":[0,0], "tiro de canhão corrente4":[0,0], "ariete4":[0,0], "metralhadora4":[0,0], "acelerar4":[0,0], 
                    "canhão pesado4":[0,0],
                #Nivel 2 Bronze
                    "barril explosivo4":[0,0], "barril de óleo4":[0,0], "explosão de velocidade4":[0,0], "reforçar4":[0,0], 
                #Nivel 2 Prata
                    "bomba de veneno4":[0,0], "lança chamas4":[0,0], "bombardeiro4":[0,0], "bolha4":[0,0], "sonar4":[0,0], 
                #Nivel 3     
                    "barco5":[0,0], "canhão5":[0,0], "vela5":[0,0], "casco5":[0,0], 
                    "espingarda5":[0,0], "tiro de canhão corrente5":[0,0], "ariete5":[0,0], "metralhadora5":[0,0], "acelerar5":[0,0], 
                    "canhão pesado5":[0,0],
            },

			'outro': {
                "tentaculo de bebe polvo":[0,0], "açucar especial":[0,0], "frango especial":[0,0], "açucar rosa":[0,0],
                },             
    }
    for ing, qty in crafts[nome].items():
        local = getLocal(ing)[0]
        price = getLocal(ing)[1]
        if ing in items[local]:
            items[local][ing][0] += qty*main_qty
            items[local][ing][1] += price*qty*main_qty
        else:
            items[local][ing][0] = qty*main_qty
            items[local][ing][1] = price*qty*main_qty
        if ing in crafts:
            for place, recipe in getRecipe(ing, qty*main_qty).items():
                for subing, subqty in recipe.items():
                    if subing in items[place]:
                        items[place][subing][0] += subqty[0]
                        items[place][subing][1] += subqty[1]
                    else:
                        items[place][subing][0] = subqty[0]
                        items[place][subing][1] = subqty[1]

    return items

def getLocal(nome):
    for k, v in locais.items():
        if nome.lower() in v:
            return(k, v[nome])
    return ('outro', '?')

def reduction(arm, valor):
    reduct = arm/(valor+arm)
    return f"```Redução de dano: {reduct*100}%```"

def effectiviness(life: int, red: float):
    red = 1-(red/100)
    efet = round(life/(life*red), 5)
    efet_life = life*efet
    return f"```Efetividade da Vida: {efet:.2f} \nVida Efetiva: {int(efet_life)}```"
 
def InfoCharacter(name):
    char = chars[name]
    text = f"""```
Nome: {char['name']}
Tier: {char['tier']}
Tags: {char['tags']}
Vida Base: {char['life']}
Vida/Vit: {char['vit']}
Fator de Defesa: {char['def']}```"""
    return text

def BauRot(char1, char2, char3, keys):
    keyn = 0
    chance100 = (10,10,10,10,10,10,10,10,10,10,25,50,75,100)
    chars = {char1: 0, char2: 0, char3: 0, 'others': 0}
    for i in range(0,keys):
        frags = 20
        if random() <= chance100[keyn]/100:
            frags = 100
            keyn = 13
        chance = random()
        if chance <= 0.40:
            choosen = choice([char1,char2,char3])
            chars[choosen] += frags
        else:
            chars['others'] += frags
        keyn += 1
        if keyn >= 13:
            keyn = 0
    return chars


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
                sorteio = random
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
