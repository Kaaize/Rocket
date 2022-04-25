from datetime import time

locais = {
    'geladeira' : {
        'tomate':10, 'cogumelo':20, 'ovo':10, 'bacon':10, 'folha verde':15, 'leite':10, 'agua':5,
        'queijo':15, 'peixe cru':50, 'bife cru':50, 'limão':10, 'manteiga': 40, 'vinho barato':500
    },

    'armario' : {
        'batata':10, 'cebola':10, 'azeite':15, 'alho':10, 'arroz':10, 'farinha':5, 'shoyu':20, 'sal':10,
        'pimenta':15, 'lata de atum':25
    },

    'tigela' : {'tigela':5},

    'rolo': {'massa':0},

    'corte': {'pasta':0},

    'panela': {
        'ramen':0, 'arroz cozido':0, 'sopa de vegetais':0, "sopa mista picante":0, "ramen de carne":0, "miso ramen":0, 
        "ramen misto":0, "ramen de galinha":0, "ramen de camarão":0, "lagosta prime":0, "caranguejo cozido":0
    },

    'tabua': {
        "onigiri":0, "sushi":0, "nigiri":0, "bento japones":0, "dango":0, "waffles":0
    },

    'forno': {
        "bife prime":0, "carne de porco gourmet":0, "polvo gourmet com ovos":0, "pizza":0, "frango a parmegiana":0, 
        "frango a parmegiana com ovos":0
    },

    'frigideira': {
        "bife frito":0, "ovo frito":0, "espeto de carne":0, "kakuni japones prime":0, "peixe grelhado gourmet":0, 
        "espeto de peixe japones prime":0, "takoyaki":0, "gyoza":0, "peixe apimentado picante":0, "coxa de frango frito":0, 
        "camarão empanado":0
    },

    'cozinha_aliança': {
        "bife e ovo de frigideira": 0,
        "medalhão de carne": 0,
        "salada italiana": 0,
        "espeto de carne gourmet": 0,
        "curry de coelho": 0,
        "camarões salteados": 0,
        "ensopado de ostra": 0,
        "atum grelhado": 0,
        "paella": 0,
    },

    'geladeira_aliança': {
        "bife cru premium": 200, "lagosta crua": 370, "camarão cru": 240, "carne crua de coelho": 186, "ostra": 360, "alface": 20,
        "vinho branco": 700, "trufa branca": 250, "creme de leite": 20, "atum": 86,
    },

    'npc': {
        #Barco
            "tora de madeira":10, "algodão de baixa qualidade":5, "minério de cobre":15, "pólvora":30, "tora de carvalho":100, "algodão":75,
            "minério de ferro":150, "pólvora melhorada":300, "tora de mogno":150, "algodão melhorado":110, "minério de aço":225, 
            "pólvora superior":450,
        #Comida
            "carne de porco": 350, "perna de galinha": 50, "peru": 300, "tomate do deserto": 30,
            "folhas verdes especiais": 40, "açucar rosa": 30,  "carne de caranguejo": 400,
    },

    'refinaria': {
        "prancha de madeira":0, "lingote de cobre":0, "pano de baixa qualidade":0, "corda de baixa qualidade":0, "prego de cobre":0,
        "prancha de carvalho":0, "lingote de ferro":0, "pano":0, "corda":0, "prego de ferro":0, 
        "prancha de mogno":0, "lingote de aço":0, "pano melhorado":0, "corda melhorada":0, "prego de aço":0, 
    },

    'drop': {
        "cola":0, "cano de arma":0, "bala de canhão":0, "bateria":0, "tanque de ar":0, "liquido inflamavel":0, "cogumelo venenoso":0, 
        "lata de óleo":0, "grande cola": 0, "cano de arma superior": 0, "bala de canhão de aço": 0,
    },

    'mesa comum': {
        #barco 1
            "canhão1":0, "vela1":0, "casco1":0,
        #barco 2
            "barco2":0, "canhão2":0, "vela2":0, "casco2":0, "espingarda2":0, "tiro de canhão corrente2":0, "ariete2":0,
        #barco 3
            "barco3":0, "canhão3":0, "vela3":0, "casco3":0, "espingarda3":0, "tiro de canhão corrente3":0, "ariete3":0, 
            "metralhadora3":0, "acelerar3":0, "canhão pesado3":0, 
        #barco 4
            "barco4":0, "canhão4":0, "vela4":0, "casco4":0, 
    },

    'estaleiro': {
        #Nivel 1
            "espingarda4":0, "tiro de canhão corrente4":0, "ariete4":0, "metralhadora4":0, "acelerar4":0, "canhão pesado4":0,
        #Nivel 2 Bronze
            "barril explosivo":0, "barril de óleo":0, "explosão de velocidade":0, "reforçar":0, 
        #Nivel 2 Prata
            "bomba de veneno":0, "lança chamas":0, "bombardeiro":0, "bolha":0, "sonar":0,       
        #Nivel 3
            "barco5":0, "casco5":0, "vela5":0, "canhão5":0,
            "espingarda5":0, "tiro de canhão corrente5":0, "ariete5":0, "metralhadora5":0, "acelerar5":0, "canhão pesado5":0,
    },

    'outro': {"tentaculo de bebe polvo":120, "açucar especial":0, "frango especial":0, "açucar rosa":0}
}

crafts = {
    #Foods
        #Rolo
            "massa": {
                "agua": 1,
                "farinha": 1,
                },

        #Tabua de corte
            "pasta": {
                "massa": 1,
            },
                
        #Panela
            "ramen": {
                "pasta": 5,
                "agua": 2,
                },
            
            "arroz cozido": {
                "tigela": 1,
                "agua": 2,
                "sal": 1,
                "arroz": 2,
                "alho": 1,
                "cebola": 1,
                },
            
            "sopa de vegetais": {
                "tigela": 1,
                "ramen": 1,
                "agua": 2,
                "tomate": 1,
                "cebola": 1,
                "folha verde": 1,
                "sal": 1,
                "batata": 1,
                },
            
            "sopa mista picante": {
                "tigela": 1,
                "ramen": 1,
                "agua": 2,
                "sal": 1,
                "queijo": 1,
                "cebola": 1,
                "bife frito": 1,
                "folha verde": 1,
                "tomate": 1,
                "pimenta": 4,
                },
            
            "ramen de carne": {
                "bife frito": 5,
                "tigela": 1,
                "ramen": 1,
                "agua": 2,
                "folha verde": 1,
                "azeite": 1,
                },
            
            "miso ramen": {
                "bife frito": 5,
                "tigela": 1,
                "ramen": 1,
                "agua": 2,
                "azeite": 1,
                "ovo": 1,
                "shoyu": 1,
                "cebola": 1,
                },
            
            "ramen misto": {
                "bife frito": 1,
                "tigela": 1,
                "ramen": 1,
                "agua": 2,
                "cebola": 1,
                "folha verde": 1,
                "tomate": 1,
                "azeite": 1,
                "batata": 1,
                },
            
            "ramen de galinha": {
                "peru": 1,
                "tigela": 1,
                "ramen": 2,
                "agua": 2,
                "shoyu": 1,
                "pimenta": 1,
                "batata": 1,
                "azeite": 1,
                "folha verde": 1,
                "cebola": 1,
                },
            
            "ramen de camarão": {
                "camarão cru": 1,
                "tigela": 1,
                "ramen": 2,
                "agua": 2,
                "ovo": 1,
                "shoyu": 1,
                "pimenta": 1,
                "azeite": 1,
                "folha verde": 1,
                "cebola": 1,
                },
            
            "lagosta prime": {
                "lagosta cru": 1,
                "agua": 2,
                "sal": 2,
                "pimenta": 2,
                "azeite": 1,
                "limão": 3,
                },
            
            "caranguejo cozido": {
                "carne de caranguejo": 1,
                "agua": 2,
                "sal": 1,
                "pimenta": 1,
                "azeite": 1,
                "folha verde": 1,
                "alho": 2,
                },
            
        #Tabua
            "onigiri": {
                "arroz cozido": 1,
                "sal": 1,
                "folha verde": 1,
                },
            
            "sushi": {
                "arroz cozido": 2,
                "sal": 1,
                "shoyu": 1,
                "azeite": 1,
                "peixe cru": 2,
                "folha verde": 1,
                },
            
            "nigiri": {
                "arroz cozido": 2,
                "shoyu": 1,
                "peixe cru": 2,
                },
            
            "bento japones": {
                "arroz cozido": 3,
                "sal": 1,
                "pimenta": 1,
                "azeite": 1,
                "peixe cru": 2,
                "folha verde": 1,
                "batata": 1,
                },

            "dango": {
                "açucar especial": 1,
                "agua": 2,
                "arroz cozido": 2,
                "farinha": 1,
                "batata": 1,
                "sal": 1,
                "shoyu": 1,
                },
            
            "waffles": {
                "açucar rosa": 1,
                "leite": 1,
                "ovo": 1,
                "farinha": 1,
                "sal": 1,
                "manteiga": 1,
                },
            
        #Forno
            "bife prime": {
                "bife cru": 2,
                "sal": 1,
                "cebola": 1,
                },
            
            "carne de porco gourmet": {
                "bife prime": 1,
                "sal": 1,
                "pimenta": 1,
                "azeite": 1,
                "folha verde": 1,
                "cebola": 1,
                "tomate": 1,
                },
            
            "polvo gourmet com ovos": {
                "tentaculo de bebe polvo": 2,
                "ovo frito": 2,
                "folha verde": 1,
                "azeite": 1,
                "sal": 1,
                "pimenta": 1,
                },
            
            "pizza": {
                "massa": 2,
                "sal": 1,
                "azeite": 1,
                "tomate": 4,
                "queijo": 1,
                "cebola": 1,
                "folha verde": 1,
                "alho": 2,
                },

            "frango a parmegiana": {
                "frango especial":1,
                "pimenta": 1,
                "queijo": 1,
                "farinha": 1,
                "sal": 1,
                "azeite": 1,
                "folha verde": 1,
                "alho": 2,
                "tomate": 2,
                },
                
            "frango a parmegiana com ovos": {
                "peru": 1,
                "pimenta": 1,
                "queijo": 1,
                "farinha": 1,
                "ovo": 1,
                "sal": 1,
                "azeite": 1,
                "folha verde": 1,
                "alho": 2,
                "tomate": 1,
                "ovo": 1,
                },
            
        #Frigideira
            "bife frito":{
                "bife cru": 1,
                "sal": 1,
                },

            "ovo frito": {
                "ovo": 1,
                "sal": 1,
                },
            
            "espeto de carne": {
                "sal": 1,
                "pimenta": 1,
                "azeite": 1,
                "bife frito": 2,
                },

            "kakuni japones prime": {
                "bife prime": 4,
                "sal": 1,
                "pimenta": 1,
                "azeite": 1,
                "folha verde": 1,
                "cebola": 1,
                },
                
            "peixe grelhado gourmet": {
                "sal": 1,
                "shoyu": 1,
                "batata": 1,
                "azeite": 1,
                "peixe cru": 2,
                "alho": 2,
                },	
                
            "espeto de peixe japones prime": {
                "alho": 2,
                "peixe cru": 2,
                "pimenta": 1,
                "sal": 1,
                "bacon": 3,
                "azeite": 1,
                "folha verde": 1,
                "limão": 3,
                },
            
            "takoyaki": {
                "massa": 1,
                "ovo": 1,
                "sal": 1,
                "tentaculo de bebe polvo": 1,
                "cebola": 1,
                "azeite": 1,
                "shoyu": 1,
                },
            
            "gyoza": {
                "sal": 1,
                "farinha": 1,
                "alho": 2,
                "massa": 1,
                "folha verde": 1,
                "carne de porco": 1,
                },
            
            "peixe apimentado picante": {
                "pimenta": 1,
                "batata": 1,
                "atum": 1,
                "azeite": 1,
                "limão": 1,
                "folhas verdes especiais": 1,
                },
            
            "coxa de frango frito": {
                "perna de galinha": 1,
                "sal": 1,
                "pimenta": 1,
                "azeite": 1,
                },
            
            "camarão empanado": {
                "camarão cru": 1,
                "farinha": 1,
                "ovo": 1,
                "sal": 1,
                "pimenta": 1,
                "azeite": 1,
                },	

        #Aliança
            #Nivel 1
                "bife e ovo de frigideira": {  
                    "bife cru premium": 3,
                    "ovo": 2,
                    "pimenta": 2,
                    "azeite": 1,
                    "folha verde": 1,
                    "sal": 4,
                },

                "medalhão de carne": {
                    "bife cru premium": 3,
                    "bacon": 8,
                    "azeite": 3,
                    "folha verde": 1,
                    "alho": 1,
                    "sal": 2,
                    "batata": 4,
                    "agua": 4,
                    "limão": 2, 
                },
            #Nivel 2
                "salada italiana": {
                    "alface": 5,
                    "trufa branca": 5,
                    "folha verde": 1,
                    "tomate": 3,
                    "azeite": 1,
                    "batata": 2,
                    "sal": 1,
                },

                "espeto de carne gourmet": {
                    "bife cru premium": 4,
                    "sal": 2,
                    "pimenta": 3,
                    "azeite": 3,
                    "bacon": 5,
                    "cebola": 4,
                    "folha verde": 3,
                    "vinho branco": 1,
                },

                "curry de coelho": {
                    "carne crua de coelho": 5,
                    "ovo": 1,
                    "azeite": 2,
                    "sal": 2,
                    "pimenta": 2,
                    "alho": 1,
                    "cebola": 1,
                    "tomate": 2,
                },
            #Nivel 3
                "camarões salteados": {
                    "camarão cru": 4,
                    "manteiga": 1,
                    "azeite": 3,
                    "vinho branco": 1,
                    "alho": 4,
                    "pimenta": 2,
                    "limão": 2,
                    "sal": 1,
                    "folha verde": 2,
                    "trufa branca": 1,
                },
                "ensopado de ostra": {
                    "ostra": 3,
                    "creme de leite": 1,
                    "sal": 2,
                    "pimenta": 2,
                    "manteiga": 2,
                    "cebola": 1,
                    "alho": 1,
                },
            #Nivel 4
                "atum grelhado": {
                    "azeite": 2,
                    "limão": 2,
                    "alho": 2,
                    "atum": 5,
                    "pimenta": 2,
                    "folha verde":2,
                    "alface": 4,
                    "vinho branco":1,
                    "manteiga":2,
                },
                "paella": {
                    "camarão cru": 5,
                    "lagosta crua": 3,
                    "arroz": 2,
                    "folha verde": 1,
                    "tomate": 1,
                    "peixe cru": 1,
                    "azeite": 1,
                    "pimenta": 1,
                    "agua": 3,
                    "sal": 1,
                },
            #Nivel 5
        #Baratie
            "baratie": {
                "sushi": 1,
                "nigiri": 1,
                "onigiri": 1,
                "bento japones": 1,
                "sopa de vegetais": 1,
                "ramen misto": 1,
                "sopa mista picante": 2,
                "carne de porco gourmet": 2,
                "pizza": 1,
                "bife prime": 1,
                "vinho barato": 1,
                "ovo frito": 1,
                "bife frito": 1,
                "espeto de carne": 1,
                "kakuni japones prime": 1,
                "espeto de peixe japones prime": 1,
                "peixe grelhado gourmet": 1,
                },	
            
        #Butaman
            "butaman": {
            "tigela": 1,
            "agua": 6,
            "sal": 2,
            "arroz": 6,
            "alho": 4,
            "cebola": 4,
            },
                
    #Ships
        #Refinaria
            "prancha de madeira": {
                "tora de madeira": 10,
            },

            "lingote de cobre": {
                "minério de cobre": 8,
            },

            "pano de baixa qualidade": {
                "algodão de baixa qualidade": 16,
            },

            "corda de baixa qualidade": {
                "pano de baixa qualidade": 2,
            },

            "prego de cobre": {
                "lingote de cobre": 1, 
            },

            "prancha de carvalho": {
                "tora de carvalho": 10,
            },

            "lingote de ferro": {
                "minério de ferro": 8,
            },

            "pano": {
                "algodão": 16,
            },

            "corda": {
                "pano": 2,
            },

            "prego de ferro": {
                "lingote de ferro": 1,
            },

            "prancha de mogno": {
                "tora de mogno": 10,
            },

            "lingote de aço": {
                "minério de aço": 8,
            },

            "pano melhorado": {
                "algodão melhorado": 16,
            },

            "corda melhorada": {
                "pano melhorado": 2,
            },

            "prego de aço": {
                "lingote de aço": 1,
            },

        #Nivel 1
            "barco1": {
                "canhão1": 1,
                "vela1": 1,
                "casco1": 1,
            },

            "canhão1": {
                "lingote de cobre": 2,
                "pólvora":5
                },

            "vela1": {
                "prancha de madeira": 1,
                "pano de baixa qualidade": 2,
            },

            "casco1": {
                "prancha de madeira": 2,
                "lingote de cobre": 1,
            },

        #Nivel 2
            "barco2": {
                "canhão2": 1,
                "vela2": 1,
                "casco2": 1,
            },

            "canhão2":{
                "corda de baixa qualidade": 1,
                "lingote de cobre": 3,
                "prego de cobre": 1,
                "pólvora": 22,
            },

            "vela2": {
                "prancha de madeira": 1,
                "tora de madeira": 20,
                "pano de baixa qualidade": 8,
                "corda de baixa qualidade": 2,
                "prego de cobre": 2,
            },

            "casco2": {
                "prancha de madeira": 8,
                "lingote de cobre": 2,
                "prego de cobre": 2,
            },
        
            "espingarda2": {
                "prancha de madeira": 5,
                "lingote de cobre": 4,
                "prego de cobre": 2,
                "corda de baixa qualidade": 3,
                "pólvora": 33,
                "cola": 2,
            },

            "tiro de canhão corrente2": {
                "prancha de madeira": 2,
                "lingote de cobre": 5,
                "prego de cobre": 2,
                "corda de baixa qualidade": 7,
                "pólvora": 34,
            },

            "ariete2": {
                "prancha de madeira": 13,
                "lingote de cobre": 2,
                "prego de cobre": 2,
                "cola": 6,
            },

        #Nivel 3
            "barco3": {
                "canhão3": 1,
                "vela3": 1,
                "casco3": 1,
            },

            "canhão3":{
                "prancha de madeira": 9,
                "corda de baixa qualidade": 6,
                "lingote de cobre": 25,
                "prego de cobre": 8,
                "pólvora": 135,
                "bala de canhão": 5
            },

            "vela3": {
                "tora de madeira": 160,
                "pano de baixa qualidade": 102,
                "corda de baixa qualidade": 18,
                "prego de cobre": 7,
                "cola": 5,
            },

            "casco3": {
                "prancha de madeira": 90,
                "lingote de cobre": 15,
                "prego de cobre": 25,
            },
        
            "espingarda3": {
                "prancha de madeira": 10,
                "lingote de cobre": 38,
                "prego de cobre": 7,
                "corda de baixa qualidade": 18,
                "pólvora": 223,
                "cola": 10,
            },

            "tiro de canhão corrente3": {
                "prancha de madeira": 12,
                "lingote de cobre": 26,
                "prego de cobre": 12,
                "corda de baixa qualidade": 18,
                "pólvora": 223,
                "bala de canhão": 2,
            },

            "ariete3": {
                "prancha de madeira": 81,
                "lingote de cobre": 10,
                "prego de cobre": 14,
                "cola": 36,
            },

            "metralhadora3": {
                "prancha de madeira": 10,
                "lingote de cobre": 16,
                "pólvora": 167,
                "cano de arma": 28,
            },

            "acelerar3": {
                "prancha de madeira": 10,
                "prego de cobre": 9,
                "pano de baixa qualidade": 75,
                "corda de baixa qualidade": 26,
                "cola": 30,
            },

            "canhão pesado3": {
                "prancha de madeira": 10,
                "lingote de cobre": 21,
                "bala de canhão": 12,
                "corda de baixa qualidade": 7,
                "pólvora": 133, 
            },

        #Nivel 4
            #Mesa
                "barco4": {
                    "canhão4": 1,
                    "vela4": 1,
                    "casco4": 1,
                },

                "canhão4":{
                    "prancha de carvalho": 2,
                    "corda": 1,
                    "lingote de ferro": 2,
                    "prego de ferro": 2,
                    "pólvora melhorada": 20,
                    "bala de canhão": 2,
                },

                "vela4": {
                    "tora de carvalho": 30,
                    "pano": 5,
                    "corda": 2,
                    "prego de ferro": 2,
                    "cola": 5,

                },

                "casco4": {
                    "prancha de carvalho": 8,
                    "lingote de ferro": 3,
                    "prego de ferro": 4,
                },
            
            #Estaleiro 1
                "espingarda4": {
                    "prancha de carvalho": 2,
                    "lingote de ferro": 3,
                    "prego de ferro": 2,
                    "corda": 1,
                    "pólvora melhorada": 20,
                    "cola": 15,
                },

                "tiro de canhão corrente4": {
                    "prancha de carvalho": 2,
                    "lingote de ferro": 4,
                    "prego de ferro": 2,
                    "corda": 1,
                    "pólvora melhorada": 20,
                    "bala de canhão": 2,
                },

                "ariete4": {
                    "prancha de carvalho": 10,
                    "lingote de ferro": 3,
                    "prego de ferro": 4,
                    "cola": 8,
                },

                "metralhadora4": {
                    "prancha de carvalho": 1,
                    "lingote de ferro": 1,
                    "pólvora melhorada": 20,
                    "cano de arma": 33,
                },

                "acelerar4": {
                    "prancha de carvalho": 3,
                    "prego de ferro": 2,
                    "pano": 5,
                    "corda": 1,
                    "cola": 30,
                },

                "canhão pesado4": {
                    "prancha de carvalho": 2,
                    "lingote de ferro": 2,
                    "bala de canhão": 11,
                    "corda": 1,
                    "pólvora melhorada": 15,
                },

            #Estaleiro 2
                "barril explosivo4": {
                    "prancha de carvalho": 2,
                    "pólvora melhorada": 5,
                    "prego de ferro": 2,
                    "corda": 2,
                },

                "barril de óleo4": {
                    "prancha de carvalho": 2,
                    "lata de óleo": 21,
                    "prego de ferro": 2,
                    "corda": 2,
                },

                "explosão de velocidade4": {
                    "prancha de carvalho": 4,
                    "prego de ferro": 2,
                    "pano": 4,
                    "corda": 1,
                    "cola": 30,
                },

                "reforçar4": {
                    "prancha de carvalho": 10,
                    "lingote de ferro": 4,
                    "prego de ferro": 4,
                },

                "bomba de veneno4": {
                    "cogumelo venenoso": 21,
                    "lingote de ferro": 3,
                    "prego de ferro": 2,
                    "cano de arma": 15,
                },

                "lança chamas4": {
                    "liquido inflamavel": 21,
                    "prancha de carvalho": 2,
                    "lingote de ferro": 2,
                    "prego de ferro": 2,
                    "cano de arma": 5,
                    "pólvora melhorada": 10,
                },

                "bombardeiro4": {
                    "lingote de ferro": 4,
                    "prego de ferro": 4,
                    "cano de arma": 10,
                    "pólvora melhorada": 30,
                },

                "bolha4": {
                    "prancha de carvalho": 4,
                    "tanque de ar": 21,
                    "pano": 2,
                    "corda": 2,
                },

                "sonar4": {
                    "bateria": 21,
                    "prancha de carvalho": 4,
                    "prego de ferro": 2,
                    "pano": 4,
                },

        #Nivel 5
            #Estaleiro 3
                "barco5": {
                    "vela5": 1,
                    "casco5": 1,
                    "canhão5": 1,
                },

                "canhão5": {
                    "prancha de carvalho": 2,
                    "corda": 1,
                    "lingote de ferro": 2,
                    "prego de ferro": 2,
                    "pólvora melhorada": 25,
                    "bala de canhão": 4,
                },

                "vela5": {
                    "tora de carvalho": 30,
                    "pano": 7,
                    "corda": 2,
                    "prego de ferro": 2,
                    "cola": 5,
                },

                "casco5": {
                    "prancha de carvalho": 11,
                    "lingote de ferro": 3,
                    "prego de ferro": 4,
                },

                "espingarda5": {
                    "prancha de mogno": 1,
                    "lingote de aço": 2,
                    "prego de aço": 1,
                    "corda melhorada": 1,
                    "pólvora superior": 17,
                    "grande cola": 10,
                },

                "tiro de canhão corrente5": {
                    "prancha de mogno": 1,
                    "lingote de aço": 2,
                    "prego de aço": 2,
                    "corda melhorada": 1,
                    "cano de arma superior": 15,
                    "bala de canhão de aço": 2, 
                },

                "ariete5": {
                    "prancha de mogno": 7,
                    "lingote de aço": 2,
                    "prego de aço": 3,
                    "grande cola": 6, 
                },

                "metralhadora5": {
                    "prancha de mogno": 1,
                    "lingote de aço": 1,
                    "pólvora melhorada": 14,
                    "cano de arma superior": 22,
                },

                "acelerar5": {
                    "prancha de mogno": 2,
                    "prego de aço": 1,
                    "pano melhorado": 4,
                    "corda melhorada": 1,
                    "grande cola": 20,
                },

                "canhão pesado5": {
                    "prancha de mogno": 1,
                    "lingote de aço": 1,
                    "corda melhorada": 1,
                    "pólvora melhorada": 12,
                    "bala de canhão de aço": 8,
                },
}

equips = {
    #level 1 - cabecas
    "bandana de bandido":{
        "level":1,
        "tipo":"cabeca",
        "vit":{"min":2,"max":3},
        "def":{"min":24,"max":30},  
		},      
    "mascara de urso":{
        "level":1,
        "tipo":"cabeca",
        "vit":{"min":5,"max":6},
        "def":{"min":45,"max":60},  
		},    
   
	#level 1 - corpo
    "camisa de bandido":{
        "level":1,
        "tipo":"corpo",
        "vit":{"min":3,"max":4},
        "def":{"min":120,"max":150},  
		},    
    
	#level 1 - perna
    "calça de bandido":{
        "level":1,
        "tipo":"perna",
        "vit":{"min":1,"max":1},
        "def":{"min":96,"max":120},  
		},
    
	#level 1 - emblema
    "emblema do chapeu de palha":{
        "level":1,
        "tipo":"perna",
        "atk":{"min":90,"max":180},
        "pen":{"min":192,"max":240},  
		},    
    
	#level 1 - arma
    "sabre velho":{
        "level":1,
        "tipo":"arma",
        "atk":{"min":225,"max":450},  
		},    
    "arma velha":{
        "level":1,
        "tipo":"arma",
        "atk":{"min":225,"max":450},  
		},        
    "pata de urso":{
        "level":1,
        "tipo":"arma",
        "atk":{"min":450,"max":900},  
		},    
    "clava da alvida":{
        "level":1,
        "tipo":"arma",
        "atk":{"min":675,"max":900},  
		},
    
	#level 1 - acessorio
    "anel antigo":{
        "level":1,
        "tipo":"acessorio",
        "crt":{"min":1,"max":10},  
		},   

    #level 10 - cabeca
    "bone de recruta":{
        "level":10,
        "tipo":"cabeca",
        "vit":{"min":5,"max":6},  
        "def":{"min":48,"max":60},  
		},    
    "mandibula de aco do morgan":{
        "level":10,
        "tipo":"cabeca",
        "vit":{"min":9,"max":10},  
        "def":{"min":81,"max":90},  
		},
    #level 10 - corpo
    "camisa de recruta":{
        "level":10,
        "tipo":"corpo",
        "vit":{"min":6,"max":8},  
        "def":{"min":240,"max":300},  
		},    
    "casaco do morgan":{
        "level":10,
        "tipo":"corpo",
        "vit":{"min":11,"max":12},  
        "def":{"min":405,"max":450},  
		},    
   
	#level 10 - perna 
    "calça de recruta":{
        "level":10,
        "tipo":"perna",
        "vit":{"min":1,"max":2},  
        "def":{"min":192,"max":240},  
		},
    "calça do morgan":{
        "level":10,
        "tipo":"perna",
        "vit":{"min":1,"max":2},  
        "def":{"min":324,"max":360},  
		},    
    
	#level 10 - emblema 
    "emblema da marinha":{
        "level":10,
        "tipo":"emblema",
        "atk":{"min":180,"max":270},  
        "pen":{"min":288,"max":360},  
		},    
    
	#level 10 - arma 
    "sabre":{
        "level":10,
        "tipo":"arma",
        "atk":{"min":450,"max":900},  
		},    
    "rifle":{
        "level":10,
        "tipo":"arma",
        "atk":{"min":450,"max":900},  
		},   
    "livro velho":{
        "level":10,
        "tipo":"arma",
        "atk":{"min":450,"max":900},  
		},
    "luvas de boxe de couro":{
        "level":10,
        "tipo":"arma",
        "atk":{"min":450,"max":900},  
		},    
	"machado de mao do morgan":{
		"level":10,
		"tipo":"arma",
		"atk":{"min":1125,"max":1350},  
		},    
    
	#level 10 - acessorio
	"colar antigo":{
		"level":10,
		"tipo":"acessorio",
		"atk":{"min":360,"max":720},  
		},    
    
    #level 20 - cabeca
    "mascara de urso branco":{
        "level":20,
        "tipo":"cabeca",
        "vit":{"min":8,"max":10},  
        "def":{"min":72,"max":90},  
		},       
    "bandana de novato":{
        "level":20,
        "tipo":"cabeca",
        "vit":{"min":8,"max":10},  
        "def":{"min":72,"max":90},  
		},        
    "cabelo do mohji":{
        "level":20,
        "tipo":"cabeca",
        "vit":{"min":11,"max":13},  
        "def":{"min":108,"max":120},  
		},     
    "cachecol do cabaji":{
        "level":20,
        "tipo":"cabeca",
        "vit":{"min":11,"max":13},  
        "def":{"min":108,"max":120},  
		},        
    "chapeu do buggy":{
        "level":20,
        "tipo":"cabeca",
        "vit":{"min":11,"max":13},  
        "def":{"min":108,"max":120},  
		},      
   
	#level 20 - corpo
    "camisa de novato":{
        "level":20,
        "tipo":"corpo",
        "vit":{"min":10,"max":12},  
        "def":{"min":360,"max":450},  
		},     
    "casaco do mohji":{
        "level":20,
        "tipo":"corpo",
        "vit":{"min":14,"max":16},  
        "def":{"min":540,"max":600},  
		},    
    "colete do cabaji":{
        "level":20,
        "tipo":"corpo",
        "vit":{"min":14,"max":16},  
        "def":{"min":540,"max":600},  
		},    
    "camisa do buggy":{
        "level":20,
        "tipo":"corpo",
        "vit":{"min":14,"max":16},  
        "def":{"min":540,"max":600},  
		},     
   
	#level 20 - perna
    "calça de novato":{
        "level":20,
        "tipo":"perna",
        "vit":{"min":1,"max":2},  
        "def":{"min":288,"max":360},  
		},      
    "calça do mohji":{
        "level":20,
        "tipo":"perna",
        "vit":{"min":2,"max":3},  
        "def":{"min":432,"max":480},  
		},     
    "calça do cabaji":{
        "level":20,
        "tipo":"perna",
        "vit":{"min":2,"max":3},  
        "def":{"min":432,"max":480},  
		},     
    "calça do buggy":{
        "level":20,
        "tipo":"perna",
        "vit":{"min":2,"max":3},  
        "def":{"min":432,"max":480},  
		},  
    
	#level 20 - emblema
    "emblema do buggy":{
        "level":20,
        "tipo":"emblema",
        "atk":{"min":270,"max":360},  
        "pen":{"min":384,"max":480},  
		},          
	
	#level 20 - arma
    "garra":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":900,"max":1350},  
		},
    "livro do conhecimento":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":900,"max":1350},  
		},    
    "soco ingles de bronze":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":900,"max":1350},  
		},
    "arma":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":900,"max":1350},  
		},
    "faca":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":900,"max":1350},  
		},
    "espada de carnaval":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":1575,"max":1800},  
		},
    "chicote de domador":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":1575,"max":1800},  
		},
    "facas de arremesso":{
        "level":20,
        "tipo":"arma",
        "atk":{"min":1575,"max":1800},  
		},
    
	#level 20 - acessorio
    "buggy dama":{
        "level":20,
        "tipo":"acessorio",
        "atk":{"min":720,"max":1080},  
		},    
    "anel de prata":{
        "level":20,
        "tipo":"acessorio",
        "crt":{"min":20,"max":30},  
		},    
    
	#level 30 - cabeca
    "bandana blackcat":{
        "level":30,
        "tipo":"cabeca",
        "vit":{"min":10,"max":13},  
        "def":{"min":92,"max":120},  
		},    
    "chapeu do jango":{
        "level":30,
        "tipo":"cabeca",
        "vit":{"min":14,"max":16},  
        "def":{"min":135,"max":150},  
		},
    "oculos do kuro":{
        "level":30,
        "tipo":"cabeca",
        "vit":{"min":14,"max":16},  
        "def":{"min":135,"max":150},  
		},
    "gorro do buchi":{
        "level":30,
        "tipo":"cabeca",
        "vit":{"min":14,"max":16},  
        "def":{"min":135,"max":150},  
		},   
    
	#level 30 - corpo
    "camisa blackcat":{
        "level":30,
        "tipo":"corpo",
        "vit":{"min":13,"max":16},  
        "def":{"min":480,"max":600},  
		},    
    "jaqueta do jango":{
        "level":30,
        "tipo":"corpo",
        "vit":{"min":18,"max":20},  
        "def":{"min":675,"max":750},  
		},    
    "jaqueta do kuro":{
        "level":30,
        "tipo":"corpo",
        "vit":{"min":18,"max":20},  
        "def":{"min":675,"max":750},   
		},    
    "camisa do sham":{
        "level":30,
        "tipo":"corpo",
        "vit":{"min":18,"max":20},  
        "def":{"min":675,"max":750},    
		},
    "capa do buchi":{
        "level":30,
        "tipo":"corpo",
        "vit":{"min":18,"max":20},  
        "def":{"min":675,"max":750},  
		},    
    
	#level 30 - perna
    "calça blackcat":{
        "level":30,
        "tipo":"perna",
        "vit":{"min":2,"max":3},  
        "def":{"min":384,"max":480},  
		},
    "calça do kuro":{
        "level":30,
        "tipo":"perna",
        "vit":{"min":3,"max":4},  
        "def":{"min":540,"max":600},  
		},
    "calça do buchi":{
        "level":30,
        "tipo":"perna",
        "vit":{"min":3,"max":4},  
        "def":{"min":540,"max":600},  
		},
    "shorts do sham":{
        "level":30,
        "tipo":"perna",
        "vit":{"min":3,"max":4},  
        "def":{"min":540,"max":600},  
		},
    "calça do jango":{
        "level":30,
        "tipo":"perna",
        "vit":{"min":3,"max":4},  
        "def":{"min":540,"max":600},  
		},
    
	#level 30 - emblema
    "emblema blackcat":{
        "level":30,
        "tipo":"emblema",
        "atk":{"min":360,"max":450},  
        "pen":{"min":480,"max":600},  
		},    
    #level 30 - arma
    "livro da irmandade":{
        "level":30,
        "tipo":"arma",
        "atk":{"min":1350,"max":1800},   
		},    
    "arma de gato":{
        "level":30,
        "tipo":"arma",
        "atk":{"min":1350,"max":1800},   
		},
    "sabre de gato":{
        "level":30,
        "tipo":"arma",
        "atk":{"min":1350,"max":1800},   
		},
    "luvas de combate kong":{
        "level":30,
        "tipo":"arma",
        "atk":{"min":1350,"max":1800},   
		},
    "garras nyaban":{
        "level":30,
        "tipo":"arma",
        "atk":{"min":2025,"max":2250},   
		},
    "garras de gato":{
        "level":30,
        "tipo":"arma",
        "atk":{"min":2025,"max":2250},   
		},
    "chakram":{
        "level":30,
        "tipo":"arma",
        "atk":{"min":2025,"max":2250},   
		},    
   
	#level 30 - acessorio
    "colar de ametista":{
        "level":30,
        "tipo":"acessorio",
        "atk":{"min":1080,"max":1440},   
		},    
    "orelha de gato":{
        "level":30,
        "tipo":"acessorio",
        "crt":{"min":30,"max":40},   
		},   
    
	#level 40 - cabeca
    "macara de kobra":{
        "level":40,
        "tipo":"cabeca",
        "vit":{"min":13,"max":16},   
        "def":{"min":120,"max":150},   
		},
    "chapeu do chef":{
        "level":40,
        "tipo":"cabeca",
        "vit":{"min":13,"max":16},   
        "def":{"min":120,"max":150},   
		},
    "bandana do gin":{
        "level":40,
        "tipo":"cabeca",
        "vit":{"min":17,"max":19},   
        "def":{"min":162,"max":180},   
		},
    "bandana do gin":{
        "level":40,
        "tipo":"cabeca",
        "vit":{"min":17,"max":19},   
        "def":{"min":162,"max":180},   
		},
    
	#level 40 - corpo
    "casaco de tigre":{
        "level":40,
        "tipo":"corpo",
        "vit":{"min":16,"max":20},   
        "def":{"min":600,"max":750},   
		},
    "camisa do chef":{
        "level":40,
        "tipo":"corpo",
        "vit":{"min":16,"max":20},   
        "def":{"min":600,"max":750},   
		},
    "jaqueta do gin":{
        "level":40,
        "tipo":"corpo",
        "vit":{"min":21,"max":24},   
        "def":{"min":810,"max":900},   
		},
    "armadura do krieg":{
        "level":40,
        "tipo":"corpo",
        "vit":{"min":21,"max":24},   
        "def":{"min":810,"max":900},   
		},
    "armadura do pearl":{
        "level":40,
        "tipo":"corpo",
        "vit":{"min":21,"max":24},   
        "def":{"min":810,"max":900},   
		},
    
	#level 40 - perna
    "calça do chefe":{
        "level":40,
        "tipo":"perna",
        "vit":{"min":3,"max":4},   
        "def":{"min":480,"max":600},   
		},
    "calça de mergulhador":{
        "level":40,
        "tipo":"perna",
        "vit":{"min":3,"max":4},   
        "def":{"min":480,"max":600},   
		},
    "calça do gin":{
        "level":40,
        "tipo":"perna",
        "vit":{"min":4,"max":5},   
        "def":{"min":648,"max":720},   
		},
    "calça do krieg":{
        "level":40,
        "tipo":"perna",
        "vit":{"min":4,"max":5},   
        "def":{"min":648,"max":720},   
		},
    "calça do pearl":{
        "level":40,
        "tipo":"perna",
        "vit":{"min":4,"max":5},   
        "def":{"min":648,"max":720},   
		},
    
	#level 40 - emblema
    "emblema da armada pirata":{
        "level":40,
        "tipo":"emblema",
        "atk":{"min":450,"max":540},   
        "pen":{"min":576,"max":720},   
		},
    
	#level 40 - arma
    "bastao do rei macaco":{
        "level":40,
        "tipo":"arma",
        "atk":{"min":1800,"max":2250},     
		},
    "garra de tigre":{
        "level":40,
        "tipo":"arma",
        "atk":{"min":1800,"max":2250},     
		},
    "forquilha do baratie":{
        "level":40,
        "tipo":"arma",
        "atk":{"min":1800,"max":2250},     
		},
    "luvas do pearl":{
        "level":40,
        "tipo":"arma",
        "atk":{"min":2475,"max":2700},     
		},
    "tonfa de ferro personalizada":{
        "level":40,
        "tipo":"arma",
        "atk":{"min":2475,"max":2700},     
		},
    "grande lanca de batalha":{
        "level":40,
        "tipo":"arma",
        "atk":{"min":2475,"max":2700},     
		},
    
	#level 40 - acessorio
    "colar de jade":{
        "level":40,
        "tipo":"acessorio",
        "atk":{"min":1440,"max":1800},     
		},
    "anel de jade":{
        "level":40,
        "tipo":"acessorio",
        "crt":{"min":40,"max":50},     
		},
    
	#level 50 - cabeca
    "bandana de tritao":{
        "level":50,
        "tipo":"cabeca",
        "vit":{"min":15,"max":19},     
        "def":{"min":144,"max":180},     
		},
    "capacete de mineracao":{
        "level":50,
        "tipo":"cabeca",
        "vit":{"min":0,"max":0},     
        "def":{"min":720,"max":1000},     
		},
    "coroa kongor":{
        "level":50,
        "tipo":"cabeca",
        "vit":{"min":17,"max":19},     
        "def":{"min":160,"max":180},     
		},
    "toca do arlong":{
        "level":50,
        "tipo":"cabeca",
        "vit":{"min":19,"max":22},     
        "def":{"min":189,"max":210},     
		},
    
	#level 50 - corpo
    "camisa de tritao":{
        "level":50,
        "tipo":"corpo",
        "vit":{"min":19,"max":24},     
        "def":{"min":720,"max":900},     
		},
    "armadura kongor":{
        "level":50,
        "tipo":"corpo",
        "vit":{"min":22,"max":24},     
        "def":{"min":840,"max":900},     
		},
    "kimono do kuroobi":{
        "level":50,
        "tipo":"corpo",
        "vit":{"min":25,"max":28},     
        "def":{"min":945,"max":1050},     
		},
    "colete do chew":{
        "level":50,
        "tipo":"corpo",
        "vit":{"min":25,"max":28},     
        "def":{"min":945,"max":1050},     
		},
    "camisa do hatchan":{
        "level":50,
        "tipo":"corpo",
        "vit":{"min":25,"max":28},     
        "def":{"min":945,"max":1050},     
		},
    "jaqueta do arlong":{
        "level":50,
        "tipo":"corpo",
        "vit":{"min":25,"max":28},     
        "def":{"min":945,"max":1050},     
		},
    
	#level 50 - perna
    "calça de tritao":{
        "level":50,
        "tipo":"perna",
        "vit":{"min":4,"max":5},     
        "def":{"min":576,"max":720},     
		},
    "saia do kongor":{
        "level":50,
        "tipo":"perna",
        "vit":{"min":5,"max":5},     
        "def":{"min":670,"max":720},     
		},
    "shorts do arlong":{
        "level":50,
        "tipo":"perna",
        "vit":{"min":5,"max":6},     
        "def":{"min":756,"max":840},     
		},
    "calça do chew":{
        "level":50,
        "tipo":"perna",
        "vit":{"min":5,"max":6},     
        "def":{"min":756,"max":840},     
		},
    "calça do kuroobi":{
        "level":50,
        "tipo":"perna",
        "vit":{"min":5,"max":6},     
        "def":{"min":756,"max":840},     
		},
    "shorts do hatchan":{
        "level":50,
        "tipo":"perna",
        "vit":{"min":5,"max":6},     
        "def":{"min":756,"max":840},     
		},
    
	#level 50 - emblema
    "emblema do arlong":{
        "level":50,
        "tipo":"emblema",
        "atk":{"min":540,"max":630},     
        "pen":{"min":672,"max":840},     
		},
    
	#level 50 - arma
    "soco ingles de ferro":{
        "level":50,
        "tipo":"arma",
        "atk":{"min":2250,"max":2700},
		},
    "espada dadao":{
        "level":50,
        "tipo":"arma",
        "atk":{"min":2250,"max":2700},
		},
    "arma do tritao":{
        "level":50,
        "tipo":"arma",
        "atk":{"min":2250,"max":2700},
		},
    "livro do morador do mar":{
        "level":50,
        "tipo":"arma",
        "atk":{"min":2250,"max":2700},
		},
    "picareta de mineraçao":{
        "level":50,
        "tipo":"arma",
        "atk":{"min":620,"max":800},
        "vit":{"min":15,"max":20},
        "def":{"min":400,"max":650},
		},
    "ancora":{
        "level":50,
        "tipo":"arma",
        "atk":{"min":2650,"max":2925},
        "def":{"min":300,"max":450},
		},
    "kiribachi":{
        "level":50,
        "tipo":"arma",
        "atk":{"min":2925,"max":3150},
		},
    
	#level 50 - acessorio
    "turbante do mar":{
        "level":50,
        "tipo":"acessorio",
        "atk":{"min":1800,"max":2160},
		},
    "anel do mar":{
        "level":50,
        "tipo":"acessorio",
        "crt":{"min":50,"max":60},
		},
    
	#level 60 - cabeca
    "bone da marinha":{
        "level":60,
        "tipo":"cabeca",
        "vit":{"min":17,"max":22},
        "def":{"min":168,"max":210},
		},
    "oculos da tashigi":{
        "level":60,
        "tipo":"cabeca",
        "vit":{"min":22,"max":25},
        "def":{"min":216,"max":240},
		},
    
	#level 60 - corpo
    "camisa da marinha":{
        "level":60,
        "tipo":"corpo",
        "vit":{"min":22,"max":28},
        "def":{"min":840,"max":1050},
		},
    "jaqueta da tashigi":{
        "level":60,
        "tipo":"corpo",
        "vit":{"min":28,"max":32},
        "def":{"min":1080,"max":1200},
		},
    "jaqueta do smoker":{
        "level":60,
        "tipo":"corpo",
        "vit":{"min":28,"max":32},
        "def":{"min":1080,"max":1200},
		},
    
	#level 60 - perna
    "calça da marinha":{
        "level":60,
        "tipo":"perna",
        "vit":{"min":5,"max":6},
        "def":{"min":672,"max":840},
		},
    "calça do smoker":{
        "level":60,
        "tipo":"perna",
        "vit":{"min":6,"max":7},
        "def":{"min":864,"max":960},
		},
    "calça da tashigi":{
        "level":60,
        "tipo":"perna",
        "vit":{"min":6,"max":7},
        "def":{"min":864,"max":960},
		},
    #level 60 - emblema
    "emblema do smoker":{
        "level":60,
        "tipo":"emblema",
        "atk":{"min":630,"max":720},
        "pen":{"min":768,"max":960},
		},
    
	#level 60 - arma
    "luvas de lutador de rua":{
        "level":60,
        "tipo":"arma",
        "atk":{"min":2700,"max":3150},
		},
    "rifle longo":{
        "level":60,
        "tipo":"arma",
        "atk":{"min":2700,"max":3150},
		},
    "cutlass":{
        "level":60,
        "tipo":"arma",
        "atk":{"min":2700,"max":3150},
		},
    "livro do rei dos piratas":{
        "level":60,
        "tipo":"arma",
        "atk":{"min":2700,"max":3150},
		},
    "nanashaku jitte":{
        "level":60,
        "tipo":"arma",
        "atk":{"min":3375,"max":3600},
		},
    "meito: shigure":{
        "level":60,
        "tipo":"arma",
        "atk":{"min":3375,"max":3600},
		},    
    "talisma da aranha":{
        "level":60,
        "tipo":"arma",
        "atk":{"min":2850,"max":3150},
		},
    
	#level 60 - acessorio
    "colar anti-marinha":{
        "level":60,
        "tipo":"acessorio",
        "atk":{"min":2160,"max":2520},
		},
    "anel da cruz":{
        "level":60,
        "tipo":"acessorio",
        "crt":{"min":60,"max":70},
		},
    
	#level 70 - cabeca
    "bandana do zoro":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    "bandana do usopp":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    "chapeu de palha do luffy":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    "bandana da nojiko":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    
	#level 70 - corpo
    "colete do luffy":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    "camisa da nami":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    "camisa do usopp":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    "camisa do zoro":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":28,"max":32},
        "def":{"min":960,"max":1200},
		},
    "terno do sanji":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    
	#level 70 - perna
    "calça do zoro":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "calça do usopp":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "shorts do luffy":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "calça do sanji":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "saia da nami":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    
	#level 70 - emblema
    "emblema da era pirata":{
        "level":70,
        "tipo":"emblema",
        "atk":{"min":720,"max":810},
        "pen":{"min":864,"max":1080},
		},
    
	#level 70 - arma
    "seringa do doutor":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    "luvas de batedor":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    "a yubashiri":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    "pederneira do daddy":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    
	#level 70 - acessorios
    "colar de conchas":{
        "level":70,
        "tipo":"acessorio",
        "atk":{"min":2520,"max":2880},
		},
    "anel de conchas":{
        "level":70,
        "tipo":"acessorio",
        "crt":{"min":70,"max":80},
		},
    
	#level 70 events - cabeca
    "coroa kongor":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    "fones de ouvido da reiju":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    "fones de ouvido do niji":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    "fones de ouvido do ichiji":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    "fones de ouvido do yonji":{
        "level":70,
        "tipo":"cabeca",
        "vit":{"min":20,"max":25},
        "def":{"min":192,"max":240},
		},
    
	#level 70 events - corpo
    "armadura kongor":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    "armadura do ichiji":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    "armadura do yonji":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    "armadura do niji":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    "armadura da reiju":{
        "level":70,
        "tipo":"corpo",
        "vit":{"min":25,"max":32},
        "def":{"min":960,"max":1200},
		},
    
	#level 70 events - perna
    "saia do kongor":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "saia da reiju":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "calça do ichiji":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "calça do niji":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    "calça do yonji":{
        "level":70,
        "tipo":"perna",
        "vit":{"min":5,"max":7},
        "def":{"min":768,"max":960},
		},
    
	#level 70 events - emblema
    "emblema de saru":{
        "level":70,
        "tipo":"emblema",
        "atk":{"min":720,"max":810},
        "pen":{"min":864,"max":1080},
		},
    
	#level 70 events - arma
    "soco ingles do gorila":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    "lamina escondida":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    "livro da selva":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    "rifle do safari":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3150,"max":3600},
		},
    "raid suit":{
        "level":70,
        "tipo":"arma",
        "atk":{"min":3600,"max":4050},
		},
    
	#level 70 events - acessorios
    "colar de saru":{
        "level":70,
        "tipo":"acessorio",
        "atk":{"min":2520,"max":2880},
		},
	"botas de propulsao a jato":{
		"level":70,
		"tipo":"acessorio",
		"atk":{"min":2520,"max":2880},
		},
}

quests = {
    #Litle
        'brogy':'D D S S A S S A A S S A A W A W W W A W W D D D W W A A W W D D D D W D D S S',

    #Drum
        'kureha':"""
        • Gaze com pomada curativa
        • Pomada para cuidar da pele
        -------------------------
        • Chá de Alecrim
        • Chá de Canela""",

    #Alabasta Leste
        'perfume':"""
        • 10 Caudas de Dugong
        • 2 Topetes de Warusagi
        • 3 Escamas de Gecko
        -------------------------
        • 1 Casco de Crab
        • 5 Ossos Digeridos
        • 5 Mescal Cactus
        -------------------------
        • 3 Frascos de Veneno
        • 4 Jubas de Lion
        • 3 Couros de Rhinoceros""",

        'chaka':"""
        • 18 Escamas de Gecko
        -------------------------
        • 4 Garras de Giant Scorpion
        -------------------------
        • 2 Chifres de Rhinoceros""",

}

chars = {
    #Tank
        #Bronze
        'pearl': {
            'name': 'Pearl',
            'tier': 'Bronze',
            'tags': ['Tank', 'Lutador', 'Especialista'],
            'life': 3000,
            'vit': [252, 262, 273, 287, 301, 325],
            'def': 2800},
        'kuroobi': {
            'name': 'Kuroobi',
            'tier': 'Bronze',
            'tags': ['Tank', 'Lutador', 'Homem-Peixe'],
            'life': 3000,
            'vit': [270, 281, 292, 307, 322, 348],
            'def': 2800},
        #Prata
        'wapol': {
            'name': 'Wapol',
            'tier': 'Prata',
            'tags': ['Tank', 'Atirador', 'Realeza', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [252, 269, 287, 304, 325, 350],
            'def': 2800},
        'mr. 1': {
            'name': 'Mr. 1',
            'tier': 'Prata',
            'tags': ['Tank', 'Cortante', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [270,288,307,326,348,375],
            'def': 3200},
        #Ouro
        'kid': {
            'name': 'Eustass Kid',
            'tier': 'Ouro',
            'tags': ['Tank', 'Atirador', 'Supernova', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [270, 296, 322, 348, 375, 401],
            'def': 2800},
        'yonji': {
            'name': 'Vinsmoke Yonji',
            'tier': 'Ouro',
            'tags': ['Tank', 'Lutador', 'Realeza'],
            'life': 3000,
            'vit': [270, 296, 322, 348, 375, 401],
            'def': 2800},
        'urouge': {
            'name': 'Urouge',
            'tier': 'Ouro',
            'tags': ['Tank', 'Lutador', 'Supernova', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [270, 296, 322, 348, 375, 401],
            'def': 3200},
        'smoker': {
            'name': 'Smoker',
            'tier': 'Ouro',
            'tags': ['Tank', 'Lutador', 'Marinheiro', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [270, 296, 322, 348, 375, 401],
            'def': 3200},
        'bastille': {
            'name': 'Bastille',
            'tier': 'Ouro',
            'tags': ['Tank', 'Cortante', 'Marinheiro'],
            'life': 3000,
            'vit': [270, 296, 322, 348, 375, 401],
            'def': 2800},
        'rebecca': {
            'name': 'Rebecca',
            'tier': 'Ouro',
            'tags': ['Tank', 'Cortante', 'Realeza'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350, 374],
            'def': 3200},
        'burgess': {
            'name': 'Jesus Burgess',
            'tier': 'Ouro',
            'tags': ['Tank', 'Lutador'],
            'life': 3000,
            'vit': [270, 296, 322, 348, 375, 401],
            'def': 3200},
        'crocodile': {
            'name': 'Sir Crocodile',
            'tier': 'Ouro',
            'tags': ['Tank', 'Especialista', 'Shichibukai', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350, 374],
            'def': 3500
        },
        #Diamante
        'kuma':{
            'name': 'Bartholomew Kuma',
            'tier': 'Diamante',
            'tags': ['Tank', 'Especialista', 'Realeza', 'Fruta do Diabo'],
            'life': 2400,
            'vit': [296, 322, 348, 375, 401],
            'def': 2800},
        'jinbe':{
            'name': 'Jinbe',
            'tier': 'Diamante',
            'tags': ['Tank', 'Lutador', 'Shichibukai', 'Homem-Peixe'],
            'life': 3000,
            'vit': [296, 322, 348, 375, 401],
            'def': 2800},
        'franky ts':{
            'name': 'Franky TimeSkip',
            'tier': 'Diamante',
            'tags': ['Tank', 'Atirador', 'Cortante'],
            'life': 3000,
            'vit': [296, 322, 348, 375, 401],
            'def': 2800},
    #Bruiser
        #Bronze
        'mohji': {
            'name': 'Mohji',
            'tier': 'Bronze',
            'tags': ['Bruiser', 'Especialista'],
            'life': 3000,
            'vit': [252, 262, 273, 287, 301, 325],
            'def': 3200},
        'morgan': {
            'name': 'Morgan',
            'tier': 'Bronze',
            'tags': ['Bruiser', 'Cortante', 'Marinheiro'],
            'life': 3000,
            'vit': [252, 262, 273, 287, 301, 325],
            'def': 4000},
        'buchi': {
            'name': 'Buchi & Sham',
            'tier': 'Bronze',
            'tags': ['Bruiser', 'Cortante'],
            'life': 3000,
            'vit': [171, 178, 185, 195, 204, 221],
            'def': 2600},
        'mr. 4': {
            'name': 'Mr. 4 & Miss Merry Christmas',
            'tier': 'Bronze',
            'tags': ['Bruiser', 'Atirador'],
            'life': 3000,
            'vit': [252, 262, 273, 287, 301, 325],
            'def': 3200,
        },
        #Prata
        'arlong': {
            'name': 'Arlong',
            'tier': 'Prata',
            'tags': ['Bruiser', 'Lutador', 'Homem-Peixe'],
            'life': 3000,
            'vit': [252, 269, 287, 304, 325, 350],
            'def': 4000},
        'doublefinger': {
            'name': 'Miss Doublefinger',
            'tier': 'Prata',
            'tags': ['Bruiser', 'Cortante', 'Fruta do Diabo'],
            'life': 2600,
            'vit': [234, 250, 266, 282, 302, 325],
            'def': 4000},
        #Ouro
        'luffy': {
            'name': 'Monkey D. Luffy',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Lutador', 'Supernova', 'Chapéu de Palha', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350],
            'def': 3200},   
        'zoro': {
            'name': 'Roronoa Zoro',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Cortante', 'Supernova', 'Chapéu de Palha'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350],
            'def': 3200},
        'drake': {
            'name': 'X Drake',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Lutador', 'Supernova', 'Marinheiro', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350, 374],
            'def': 4000},       
        'franky': {
            'name': 'Franky',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Atirador', 'Chapéu de Palha'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350],
            'def': 3200},
        'hina': {
            'name': 'Hina',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Lutador', 'Marinheiro', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350, 374],
            'def': 3200},   
        'basil': {
            'name': 'Basil Hawkins',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Especialista', 'Supernova', 'Fruta do Diabo'],
            'life': 700,
            'vit': [36, 39, 43, 46, 50, 53],
            'def': 5000},
        'ichiji': {
            'name': 'Vinsmoke Ichiji',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Lutador', 'Realeza'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350, 374],
            'def': 3200},
        'dalmatian': {
            'name': 'Dalmatian',
            'tier': 'Ouro',
            'tags': ['Bruiser', 'Cortante', 'Marinheiro', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [252, 276, 301, 325, 350, 374],
            'def': 3200},
        #Diamante
        'barba negra': {
            'name': 'Barba Negra',
            'tier': 'Diamante',
            'tags': ['Bruiser', 'Especialista', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [276, 301, 325, 350, 374],
            'def': 3200},
        'shanks': {
            'name': 'Barba Negra',
            'tier': 'Diamante',
            'tags': ['Bruiser', 'Cortante'],
            'life': 3000,
            'vit': [276, 301, 325, 350, 374],
            'def': 3200},
    #DPS
        #Bronze
        'cabaji': {
            'name': 'Cabaji',
            'tier': 'Bronze',
            'tags': ['DPS', 'Cortante'],
            'life': 2600,
            'vit': [234, 243, 253, 266, 279, 302],
            'def': 4000},
        'gin': {
            'name': 'Gin',
            'tier': 'Bronze',
            'tags': ['DPS', 'Lutador', 'Atirador'],
            'life': 2600,
            'vit': [234, 243, 253, 266, 279, 302],
            'def': 4000},
        'chew': {
            'name': 'Chew',
            'tier': 'Bronze',
            'tags': ['DPS', 'Atirador', 'Homem-Peixe'],
            'life': 1900,
            'vit': [171, 178, 185, 195, 204, 221],
            'def': 8800},
        'mr. 5': {
            'name': 'Mr. 5 & Miss Valentine',
            'tier': 'Bronze',
            'tags': ['DPS', 'Atirador', 'Fruta do Diabo'],
            'life': 1900,
            'vit': [171, 178, 185, 195, 204, 221],
            'def': 8800},
        'eric': {
            'name': 'Eric',
            'tier': 'Bronze',
            'tags': ['DPS', 'Atirador', 'Cortante', 'Fruta do Diabo'],
            'life': 1900,
            'vit': [171, 178, 185, 195, 204, 221],
            'def': 8800},
        #Prata
        'bepo': {
            'name': 'Bepo',
            'tier': 'Prata',
            'tags': ['DPS', 'Lutador'],
            'life': 2600,
            'vit': [234, 250, 266, 282, 302, 325],
            'def': 4000},
        'daddy': {
            'name': 'Daddy Masterson',
            'tier': 'Prata',
            'tags': ['DPS', 'Atirador', 'Marinheiro'],
            'life': 1900,
            'vit': [171, 183, 195, 207, 221, 238],
            'def': 8800},
        'buggy': {
            'name': 'Buggy',
            'tier': 'Prata',
            'tags': ['DPS', 'Atirador', 'Fruta do Diabo'],
            'life': 1900,
            'vit': [171, 183, 195, 207, 221, 238, 254],
            'def': 8800},
        'krieg': {
            'name': 'Don Krieg',
            'tier': 'Prata',
            'tags': ['DPS', 'Atirador'],
            'life': 2600,
            'vit': [234, 250, 266, 282, 302, 325],
            'def': 6500},
        'kuro': {
            'name': 'Kuro',
            'tier': 'Prata',
            'tags': ['DPS', 'Cortante'],
            'life': 2600,
            'vit': [234, 250, 266, 282, 302, 325],
            'def': 4000},
        'mr. 2': {
            'name': 'Mr. 2 - Bon Kurei',
            'tags': ['DPS', 'Lutador', 'Fruta do Diabo'],
            'life': 2000,
            'vit': [216, 231, 246, 261, 279, 300],
            'def': 4000},
        #Ouro
        'sanji': {
            'name': 'Vinsmoke Sanji',
            'tier': 'Ouro',
            'tags': ['DPS', 'Lutador', 'Realeza', 'Chapéu de Palha'],
            'life': 2600,
            'vit': [234, 256, 279, 302, 325],
            'def': 4000},
        'koala': {
            'name': 'Koala',
            'tier': 'Ouro',
            'tags': ['DPS', 'Lutador'],
            'life': 2600,
            'vit': [234, 256, 279, 302, 325, 347],
            'def': 4000},
        'law': {
            'name': 'Trafalgar Law',
            'tier': 'Ouro',
            'tags': ['DPS', 'Cortante', 'Especialista', 'Supernova', 'Fruta do Diabo'],
            'life': 2600,
            'vit': [234, 256, 279, 302, 325, 347],
            'def': 4000},
        'capone': {
            'name': 'Capone Gang Bege',
            'tier': 'Ouro',
            'tags': ['DPS', 'Atirador', 'Supernova', 'Fruta do Diabo'],
            'life': 1900,
            'vit': [180, 197, 215, 232, 250, 267],
            'def': 6500},
        'usopp': {
            'name': 'Usopp',
            'tier': 'Ouro',
            'tags': ['DPS', 'Atirador', 'Chapéu de Palha'],
            'life': 1900,
            'vit': [171, 188, 204, 221, 238],
            'def': 8800},
        'tashigi': {
            'name': 'Tashigi',
            'tier': 'Prata',
            'tags': ['DPS', 'Cortante', 'Marinheiro'],
            'life': 2600,
            'vit': [234, 250, 266, 282, 302, 325, 347],
            'def': 4000},
        'nami': {
            'name': 'Nami',
            'tier': 'Ouro',
            'tags': ['DPS', 'Especialista', 'Chapéu de Palha'],
            'life': 2000,
            'vit': [180, 197, 215, 232, 250],
            'def': 6500},
        'killer': {
            'name': 'Killer',
            'tier': 'Ouro',
            'tags': ['DPS', 'Cortante', 'Supernova'],
            'life': 2600,
            'vit': [234, 256, 279, 302, 325, 347],
            'def': 4000},
        'niji': {
            'name': 'Vinsmoke Niji',
            'tier': 'Ouro',
            'tags': ['DPS', 'Atirador', 'Realeza'],
            'life': 2400,
            'vit': [180, 197, 215, 232, 250, 267],
            'def': 6500},
	'van': {
            'name': 'Van Augur',
            'tier': 'Ouro',
            'tags': ['DPS', 'Atirador'],
            'life': 2400,
            'vit': [180, 197, 215, 232, 250, 267],
            'def': 6500},
        'bartolomeo': {
            'name': 'Bartolomeo',
            'tier': 'Ouro',
            'tags': ['DPS', 'Especialista', 'Fruta do Diabo'],
            'life': 2000,
            'vit': [180, 197, 215, 232, 250, 267],
            'def': 6500},
        'robin': {
            'name': 'Nico Robin',
            'tier': 'Ouro',
            'tags': ['DPS', 'Especialista', 'Chapéu de Palha', 'Fruta do Diabo'],
            'life': 2000,
            'vit': [216, 237, 258, 279, 300, 321],
            'def': 6500},
        'ryuma':{ 
            'name': 'Ryuma',
            'tier': 'Ouro',
            'tags': ['DPS', 'Cortante'],
            'life': 2600,
            'vit': [234, 256, 279, 302, 325, 347],
            'def': 4000},
        #Diamante
        'doflamingo': {
            'name': 'Donquixote Doflamingo',
            'tier': 'Diamante',
            'tags': ['DPS', 'Atirador', 'Especialista', 'Realeza', 'Shichibukai', 'Fruta do Diabo'],
            'life': 2400,
            'vit': [237, 258, 279, 300, 321],
            'def': 6500},
        'ace': {
            'name': 'Portgas D. Ace',
            'tier': 'Diamante',
            'tags': ['DPS', 'Atirador', 'Especialista', 'Fruta do Diabo'],
            'life': 2400,
            'vit': [237, 258, 279, 300, 321],
            'def': 6500},
        'hancock': {
            'name': 'Boa Hancock',
            'tier': 'Diamante',
            'tags': ['DPS', 'Lutador', 'Realeza', 'Shichibukai', 'Fruta do Diabo'],
            'life': 2600,
            'vit': [256, 279, 302, 325, 347],
            'def': 4000},
        'mihawk': {
            'name': 'Dracule Mihawk',
            'tier': 'Diamante',
            'tags': ['DPS', 'Cortante', 'Shichibukai'],
            'life': 2600,
            'vit': [234, 256, 279, 302, 325, 347],
            'def': 4000},
        'kizaru': {
            'name': 'Kizaru',
            'tier': 'Diamante',
            'tags': ['DPS', 'Atirador'],
            'life': '2400',
            'vit': [237, 258, 279, 300, 321],
            'def': 6500},
        'sanji ts': {
            'name': 'Sanji TimeSkip',
            'tier': 'Diamante',
            'tags': ['DPS', 'Lutador', 'Realeza', 'Chapéu de Palha'],
            'life': '2600',
            'vit': [256, 279, 302, 325, 347],
            'def': 4000},
        'luffy ts': {
            'name': 'Luffy TimeSkip',
            'tier': 'Diamante',
            'tags': ['DPS', 'Lutador', 'Supernova', 'Chapéu de Palha', 'Fruta do Diabo'],
            'life': '3000',
            'vit': [276, 301, 325, 350, 374],
            'def': 3200},
        'zoro ts': {
            'name': 'Zoro TimeSkip',
            'tier': 'Diamante',
            'tags': ['DPS', 'Cortante', 'Supernova', 'Chapéu de Palha'],
            'life': '2400',
            'vit': [256, 279, 302, 325, 347],
            'def': 4000},
        'nami ts': {
            'name': 'Nami TimeSkip',
            'tier': 'Diamante',
            'tags': ['DPS', 'Especialista', 'Chapéu de Palha'],
            'life': '2000',
            'vit': [197, 215, 232, 250, 267],
            'def': 6500},
        'robin ts': {
            'name': 'Robin TimeSkip',
            'tier': 'Diamante',
            'tags': ['DPS', 'Especialista', 'Fruta do Diabo', 'Chapéu de Palha'],
            'life': '2400',
            'vit': [237, 258, 279, 300, 321],
            'def': 6500},
        'usopp ts': {
            'name': 'Usopp TimeSkip',
            'tier': 'Diamante',
            'tags': ['DPS', 'Atirador', 'Chapéu de Palha'],
            'life': '1900',
            'vit': [188, 204, 221, 238, 254],
            'def': 8800},
    #Suporte
        #Bronze
        'hatchan': {
            'name': 'Hatchan',
            'tier': 'Bronze',
            'tags': ['Suporte', 'Cortante', 'Homem-Peixe'],
            'life': 2600,
            'vit': [234, 243, 253, 266, 279, 302],
            'def': 4000},
        'goldenweek': {
            'name': 'Miss Goldenweek',
            'tier': 'Bronze',
            'tags': ['Suporte', 'Especialista'],
            'life': 2000,
            'vit': [180, 187, 195, 205, 215, 232],
            'def': 6500},
        'alvida': {
            'name': 'Alvida',
            'tier': 'Bronze',
            'tags': ['Suporte', 'Lutador', 'Fruta do Diabo (Skin)'],
            'life': 2400,
            'vit': [216, 225, 234, 245, 258, 279],
            'def': 4000},
        'jango': {
            'name': 'Jango',
            'tier': 'Bronze',
            'tags': ['Suporte', 'Atirador', 'Marinheiro (Skin)'],
            'life': 2000,
            'vit': [180, 187, 195, 205, 215, 232],
            'def': 6500},
        #Prata
        'vivi': {
            'name': 'Vivi',
            'tier': 'Prata',
            'tags': ['Suporte', 'Cortante', 'Realeza'],
            'life': 2400,
            'vit': [180, 192, 205, 217, 232, 250],
            'def': 6500},
        'mr. 3': {
            'name': 'Mr. 3 - Galdino',
            'tier': 'Prata',
            'tags': ['Suporte', 'Especialista', 'Fruta do Diabo'],
            'life': 2000,
            'vit': [180, 192, 205, 217, 232, 250],
            'def': 6500},
        #Ouro
        'leo': {
            'name': 'Léo & Mansherry',
            'tier': 'Ouro',
            'tags': ['Suporte', 'Especialista', 'Realeza', 'Fruta do Diabo'],
            'life': 1900,
            'vit': [171, 188, 204, 221, 238, 254],
            'def': 8800},
        'reiju': {
            'name': 'Vinsmoke Reiju',
            'tier': 'Ouro',
            'tags': ['Suporte', 'Especialista', 'Realeza'],
            'life': 2000,
            'vit': [180, 197, 215, 232, 250, 267],
            'def': 4900},
        'bonney': {
            'name': 'Jewelry Bonney',
            'tier': 'Ouro',
            'tags': ['Suporte', 'Lutador', 'Supernova', 'Fruta do Diabo'],
            'life': 2000,
            'vit': [180, 197, 215, 232, 250, 267],
            'def': 6500},
        'chopper': {
            'name': 'Tony Tony Chopper',
            'tier': 'Ouro',
            'tags': ['Suporte', 'Lutador', 'Chapéu de Palha', 'Fruta do Diabo'],
            'life': 2400,
            'vit': [216, 237, 258, 279, 300],
            'def': 6500},
        'brook': {
            'name': 'Brook',
            'tier': 'Ouro',
            'tags': ['Suporte', 'Cortante', 'Chapéu de Palha', 'Fruta do Diabo'],
            'life': 2400,
            'vit': [216, 237, 258, 279, 300],
            'def': 4900},
        'perona': {
            'name': 'Perona',
            'tier': 'Ouro',
            'tags': ['Suporte', 'Especialista', 'Fruta do Diabo'],
            'life': 1900,
            'vit': [171, 188, 204, 221, 238, 254],
            'def': 6500},
        'apoo': {
            'name': 'Scratchman Apoo',
            'tier': 'Ouro',
            'tags': ['Suporte', 'Atirador', 'Supernova', 'Fruta do Diabo'],
            'life': 2000,
            'vit': [180, 197, 215, 232, 250, 267],
            'def': 6500},
        #Diamante
        'ivankov': {
            'name': 'Emporio Ivankov',
            'tier': 'Diamante',
            'tags': ['Suporte', 'Lutador', 'Fruta do Diabo'],
            'life': 3000,
            'vit': [256, 279, 302, 325, 347],
            'def': 4900},
        'chopper ts': {
            'name': 'Chopper TS',
            'tier': 'Diamante',
            'tags': ['Suporte', 'Lutador', 'Fruta do Diabo'],
            'life': 2400,
            'vit': [237, 258, 279, 300, 321],
            'def': 6500},
        'brook ts': {
            'name': 'Brook TS',
            'tier': 'Diamante',
            'tags': ['Suporte', 'Cortante', 'Fruta do Diabo'],
            'life': 2400,
            'vit': [237, 258, 279, 300, 321],
            'def': 4900},
}

