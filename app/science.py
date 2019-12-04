# Status: "available", "purchased", "blocked"

def list_techs():
    return [sc for sc in data.values() if sc["status"] == "available"]


def buy_tech(id):
    data[id]["status"] = "purchased"
    return {"status": "success"}


data = {   
    #NUCLEAR ----------------------------
    'Conhecimento atômico': {
        'title': "Conhecimento atômico",
        'price': "50",
        'type': "is-warning",
        'spec': "Estudos necessários para entender melhor o funcionamento das partículas atômicas e subatômicas e como promover mudanças ambientalmente favoráveis.",
        'type_tech': "nuclear",
        'status': 'available',
        'prog': 0
    },
    'Usinas nucleares': {
        'title': "Usinas nucleares",
        'price': "100",
        'type': "is-warning",
        'spec': "Criação de polos de usinas nucleares para produzirem mais energia com um imacto ambiental menor.",
        'type_tech': "nuclear",
        'status': 'available',
        'prog': 0
    },
    'Geradores nucleares': {
        'title': "Geradores nucleares",
        'price': "150",
        'type': "is-warning",
        'spec': "Diminui a demanda energética de combustíveis fósseis em 40% da população ao produzir um novo gerador de energia elétrica pessoal com elementos radioativos.",
        'type_tech': "nuclear",
        'status': 'available',
        'prog': 0
    },
    'Comida irradiada': {
        'title': "Comida irradiada",
        'price': "200",
        'type': "is-warning",
        'spec': "Produção de alimentos com o uso de irradiação na agricultura a fim de prevenir a proliferação de pragas, diminuindo o uso de agrotóxicos que liberam gases estufa.",
        'type_tech': "nuclear",
        'status': 'available',
        'prog': 0
    },

    # BIOLÓGICO ---------------------
    
    'Conhecimento molecular': {
        'title': "Conhecimento molecular",
        'price': "50",
        'type': "is-success",
        'spec': "Estudos necessários para entender melhor o funcionamento da microbiologia e como promover mudanças ambientalmente favoráveis.",
        'type_tech': "biológico",
        'status': 'available',
        'prog': 0
    },
    'Aumentar o reflorestamento': {
        'title': "Aumentar o reflorestamento",
        'price': "100",
        'type': "is-success",
        'spec': "Aumenta a plantação de árvores no planeta Terra, fazendo com que o sequestro de carbono (CO2) aumente em 25%.",
        'type_tech': "biológico",
        'status': 'available',
        'prog': 0
    },
    'Biofiltro de algas': {
        'title': "Biofiltro de algas",
        'price': "150",
        'type': "is-success",
        'spec': "Biofiltros formados por microalgas aumentam a absorção de CO2 da atmosfera em um nível 100 vezes mais alto que as árvores, podendo melhorar a qualidade de vida na Terra.",
        'type_tech': "biológico",
        'status': 'available',
        'prog': 0
    },
    'Árvores geneticamente modificadas': {
        'title': "Árvores geneticamente modificadas",
        'price': "200",
        'type': "is-success",
        'spec': "Elaboração, em laboratório, de árvores com DNA modificado para terem um rendimento fotossintetizante mais alto que o normal, aumentando a absorção de CO2 na atmosfera.",
        'type_tech': "biológico",
        'status': 'available',
        'prog': 0
    },

    # TRANSPORTE --------------------
    
    'Conhecimento de energias renováveis': {
        'title': "Conhecimento de energias renováveis",
        'price': "50",
        'type': "is-error",
        'spec': "Estudos necessários para fazer meios de transporte serem menos agressivos ambientalmente.",
        'type_tech': "transporte",
        'status': 'available',
        'prog': 0
    },
    'Carro movido a motor de hidrogênio': {
        'title': "Carro movido a motor de hidrogênio",
        'price': "100",
        'type': "is-error",
        'spec': "Liberação do motor movido a hidrogênio a preços acessíveis para a população, reduzindo a produção de CO2.",
        'type_tech': "transporte",
        'status': 'available',
        'prog': 0
    },
    'Uberdrone': {
        'title': "Uberdrone",
        'price': "150",
        'type': "is-error",
        'spec': "Criação do app Uberdrone que permite com que cidadãos realizem corridas econômicas e mais rápidas, diminuindo o uso de carros para a locomoção.",
        'type_tech': "transporte",
        'status': 'available',
        'prog': 0
    },
    'Aerobus': {
        'title': "Aerobus",
        'price': "200",
        'type': "is-error",
        'spec': "Ônibus voadores são desenvolvidos como alternativa para o transporte público. Como possui preço acessível, permitiu o o transporte mais rápido e eficiente entre os locais para a população, diminuindo em massa o uso de ônibus terrestres.",
        'type_tech': "transporte",
        'status': 'available',
        'prog': 0
    },
    
        # ENERGÉTICO ---------------------
    
    'Conhecimentos sobre o fluxo energético': {
        'title': "Conhecimentos sobre o fluxo energético",
        'price': "50",
        'type': "is-primary",
        'spec': "Estudos necessários para promover o uso energético mais eficiente e menos poluente.",
        'type_tech': "energético",
        'status': 'available',
        'prog': 0
    },
    'Usinas eólicas': {
        'title': "Usinas eólicas",
        'price': "100",
        'type': "is-primary",
        'spec': "Instalação de usinas eólicas para maior produção energética.",
        'type_tech': "energético",
        'status': 'available',
        'prog': 0
    },
    'Giroplacas': {
        'title': "Giroplacas",
        'price': "150",
        'type': "is-primary",
        'spec': "Desenvolvimento de placas solares autônomas que giram sua direção para o sol, de forma a garantir que os raios solares ao longo do dia sejam absorvidos pelas placas solares.",
        'type_tech': "energético",
        'status': 'available',
        'prog': 0
    },
    'Fazendas de armazenamento de energia': {
        'title': "Fazendas de armazenamento de energia",
        'price': "150",
        'type': "is-primary",
        'spec': "Armazenamento da produção energética excedente para evitar demanda desigual ao longo do dia.",
        'type_tech': "energético",
        'status': 'available',
        'prog': 0
    },

        # INDUSTRIAL -----------------------
    
    'Conhecimentos industriais': {
        'title': "Conhecimentos industriais",
        'price': "50",
        'type': "industry",
        'spec': "Estudos necessários ara promover uma produção industrial ambientalmente melhor.",
        'type_tech': "industrial",
        'status': 'available',
        'prog': 0
    },
    'Menos produção de lixo': {
        'title': "Menos produção de lixo",
        'price': "100",
        'type': "industry",
        'spec': "Produção industrial mais eficiente, fazendo com que a produção de lixo seja menor e ambientalmente favorável.",
        'type_tech': "industrial",
        'status': 'available',
        'prog': 0
    },
    'Eficiência industrial': {
        'title': "Eficiência industrial",
        'price': "150",
        'type': "industry",
        'spec': "Aumento da eficiência da produção industrial, fazendo com que menos energia seja gasta para produzir os produtos.",
        'type_tech': "industrial",
        'status': 'available',
        'prog': 0
    },
    'Catalisadores inerentes': {
        'title': "Catalisadores inerentes",
        'price': "150",
        'type': "industry",
        'spec': "Veículos utilitários terão catalisadores acoplados de forma obrigatória e gratuita para diminuir a emissão dos gases estufa.",
        'type_tech': "industrial",
        'status': 'available',
        'prog': 0
    },
}