# -*- coding: utf-8 -*-
"""
Script mestre atualizado para gerar os 179 sites demonstrativos do Nexo Studio
com imagens Full HD curadas, fotografia real por segmento, módulos interativos de alta conversão
e catálogo mestre com visual premium.
"""
import os
import json
from scripts.photos_db import get_niche_images

# Lista com as 14 categorias e 179 nichos completos
CATEGORIES = [
    {
        "id": "saude",
        "name": "Saúde",
        "icon": "🩺",
        "desc": "Clínicas, consultórios e laboratórios médicos e terapêuticos",
        "niches": [
            ("clinica-odontologica", "Clínica Odontológica", "Sorriso & Arte Odontologia", "Implantes, ortodontia e estética dental com tecnologia digital e acolhimento.", "#0E9384", "#083338", "#14B8A6", "#F2FAF8", "booking"),
            ("clinica-fisioterapia", "Clínica de Fisioterapia", "Aura Fisio & Reabilitação", "Fisioterapia ortopédica, RPG e reabilitação funcional para sua qualidade de vida.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "booking"),
            ("clinica-psicologia", "Clínica de Psicologia", "Espaço Mente & Equilíbrio", "Psicoterapia presencial e online para adultos, casais e adolescentes.", "#6366F1", "#1E1B4B", "#818CF8", "#F5F3FF", "booking"),
            ("clinica-nutricao", "Clínica de Nutrição", "NutriVida Consultoria Nutricional", "Emagrecimento sustentável, nutrição esportiva e reeducação alimentar sem dietas radicais.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "booking"),
            ("clinica-medica", "Clínica Médica", "Centro Médico Vitta Plus", "Consultas com médicos especialistas, check-ups e exames preventivos no mesmo lugar.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "booking"),
            ("clinica-estetica", "Clínica de Estética", "Dermallis Estética & Harmonização", "Harmonização facial, bioestimuladores de colágeno e tratamentos corporais avançados.", "#BE185D", "#4C0519", "#F43F5E", "#FFF1F2", "booking"),
            ("clinica-depilacao-laser", "Clínica de Depilação a Laser", "PelliLaser Tecnologia & Conforto", "Depilação a laser definitiva sem dor com ponteira resfriada e resultado garantido.", "#7C3AED", "#2E1065", "#A78BFA", "#F5F3FF", "booking"),
            ("laboratorio-analises-clinicas", "Laboratório de Análises Clínicas", "BioDiagnóstico Laboratório", "Exames laboratoriais precisos, coleta domiciliar e resultados rápidos online.", "#0369A1", "#082F49", "#0EA5E9", "#F0F9FF", "quote"),
            ("clinica-fonoaudiologia", "Clínica de Fonoaudiologia", "Voz & Sentidos Fonoaudiologia", "Terapia fonoaudiológica para crianças e adultos, motricidade orofacial e voz.", "#D97706", "#451A03", "#F59E0B", "#FFFBEB", "booking"),
            ("clinica-acupuntura", "Clínica de Acupuntura", "Harmonia Shen Medicina Chinesa", "Alívio de dores crônicas, ansiedade e enxaqueca através da acupuntura tradicional.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "booking"),
            ("clinica-podologia", "Clínica de Podologia", "Pés & Cuidado Podologia Avançada", "Tratamento de unhas encravadas, calosidades e cuidados para pés diabéticos.", "#0D9488", "#134E4A", "#14B8A6", "#F0FDFA", "booking"),
            ("otica", "Ótica", "Ótica Visão Cristal", "Armações exclusivas, lentes de alta definição e exame de vista computadorizado.", "#2563EB", "#1E293B", "#60A5FA", "#F8FAFC", "catalog"),
            ("farmacia-manipulacao", "Farmácia de Manipulação", "Oficina das Fórmulas Manipulação", "Fórmulas personalizadas, suplementos e dermocosméticos sob rigoroso controle de qualidade.", "#059669", "#064E3B", "#34D399", "#ECFDF5", "quote"),
            ("casa-repouso", "Casa de Repouso", "Residencial Viver Bem Sênior", "Cuidado humanizado 24h, fisioterapia diária e recreação em um ambiente acolhedor.", "#C026D3", "#4A044E", "#E879F9", "#FDF4FF", "quote"),
            ("clinica-vacinacao", "Clínica de Vacinação", "ImunoVida Centro de Imunização", "Vacinas para todas as idades, imunizações infantis e corporativas com atendimento humanizado.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "booking"),
            ("consultorio-quiropraxia", "Consultório de Quiropraxia", "Coluna Viva Quiropraxia", "Ajuste vertebral e alívio imediato de dores na coluna, ciático e postura corporal.", "#D97706", "#451A03", "#FBBF24", "#FFFBEB", "booking")
        ]
    },
    {
        "id": "beleza-estetica",
        "name": "Beleza e Estética",
        "icon": "✨",
        "desc": "Salões, barbearias, estúdios de olhar, unhas, tatuagem e spas",
        "niches": [
            ("salao-beleza", "Salão de Beleza", "Atelier Silken Cabelos & Make", "Cortes visagistas, mechas luxuosas e tratamentos capilares de alta performance.", "#C89585", "#2C201C", "#D3A294", "#FAF7F2", "booking"),
            ("barbearia", "Barbearia", "Cavalera & Co. Barbearia Vintage", "Cortes clássicos, barba na toalha quente e cerveja gelada em ambiente masculino premium.", "#D97706", "#18181B", "#F59E0B", "#18181B", "booking"),
            ("estudio-sobrancelhas", "Estúdio de Sobrancelhas", "Design & Linhas Eyebrows", "Design estratégico, micropigmentação fio a fio e reconstrução de sobrancelhas.", "#BE185D", "#3B0718", "#FB7185", "#FFF1F2", "booking"),
            ("extensao-cilios", "Extensão de Cílios", "Lash Studio Olhar Magnífico", "Volume russo, efeito molhado e extensão clássica com retenção de até 30 dias.", "#9333EA", "#2E1065", "#C084FC", "#FAF5FF", "booking"),
            ("esmalteria", "Esmalteria", "Laqua Esmalteria & Lounge", "Unhas impecáveis, spa dos pés e mais de 400 cores de esmaltes nacionais e importados.", "#E11D48", "#4C0519", "#FB7185", "#FFF1F2", "booking"),
            ("nail-designer", "Nail Designer", "Glam Nails Alongamentos", "Alongamento em fibra de vidro, gel moldado e nail arts exclusivas com durabilidade extrema.", "#DB2777", "#500724", "#F472B6", "#FDF2F8", "booking"),
            ("estudio-maquiagem", "Estúdio de Maquiagem", "Bella Visage Makeup & Beauty", "Produções sociais para formaturas, noivas e ensaios com maquiagem blindada à prova d'água.", "#B45309", "#291804", "#F59E0B", "#FFFBEB", "booking"),
            ("espaco-depilacao", "Espaço de Depilação", "Pele & Cera Depilação Especializada", "Depilação suave com ceras exclusivas hipoalergênicas e cuidados pós-depilatórios.", "#D97706", "#451A03", "#FBBF24", "#FFFBEB", "booking"),
            ("bronzeamento-artificial", "Bronzeamento Artificial", "Sol Dourado Bronze Express", "Bronzeamento por vaporização saudável e bronze na fita com marquinha perfeita.", "#D97706", "#3E1E02", "#F59E0B", "#FFFBEB", "booking"),
            ("estudio-tatuagem", "Estúdio de Tatuagem", "Black Ink Tattoo Studio", "Tatuagens autorais em blackwork, fineline e realismo com biossegurança certificada.", "#E2E8F0", "#09090B", "#38BDF8", "#09090B", "booking"),
            ("body-piercing", "Body Piercing", "Aura Piercing & Joalheria", "Perfurações corporais assépticas e joalheria nobre em titânio e ouro 18k.", "#6366F1", "#0F172A", "#818CF8", "#F8FAFC", "booking"),
            ("spa", "Spa & Bem-Estar", "Zenith Spa Urbano", "Massagens relaxantes, pedras quentes, banhos de imersão e rituais antiestresse.", "#0D9488", "#112D29", "#2DD4BF", "#F0FDFA", "booking"),
            ("terapias-holisticas", "Terapias Holísticas", "Espaço Alvorecer Holístico", "Reiki, alinhamento dos chakras, aromaterapia e florais para equilíbrio integral.", "#7C3AED", "#241042", "#A78BFA", "#FAF5FF", "booking")
        ]
    },
    {
        "id": "alimentacao",
        "name": "Alimentação",
        "icon": "🍽️",
        "desc": "Restaurantes, pizzarias, hamburguerias, confeitarias e deliveries",
        "niches": [
            ("restaurante", "Restaurante", "Origens Bistrô Contemporâneo", "Gastronomia autoral, ingredientes frescos de produtores locais e carta de vinhos selecionada.", "#D97706", "#1F1206", "#F59E0B", "#FDFBF7", "catalog"),
            ("pizzaria", "Pizzaria", "Forneria San Gennaro", "Pizzas de longa fermentação assadas a 450°C no forno a lenha com queijos artesanais.", "#B91C1C", "#1C0A0A", "#EF4444", "#FEF2F2", "catalog"),
            ("hamburgueria", "Hamburgueria", "Smash & Smoke Burger House", "Burgers suculentos prensados na chapa, bacon caramelizado e pão brioche amanteigado.", "#EA580C", "#1C0D05", "#F97316", "#FFF7ED", "catalog"),
            ("cafeteria", "Cafeteria", "Grão & Prosa Cafés Especiais", "Cafés filtrados por baristas, espressos de grãos 100% arábica e quitutes caseiros.", "#854D0E", "#271707", "#CA8A04", "#FEFCE8", "catalog"),
            ("confeitaria", "Confeitaria", "Doce Requinte Confeitaria Fina", "Bolos decorados para festas, tortas clássicas e doces gourmet feitos com afeto.", "#DB2777", "#3B0721", "#F472B6", "#FDF2F8", "catalog"),
            ("doceria", "Doceria", "Amor em Pedaços Doceria", "Brigadeiros gourmet, fatias generosas de bolo e sobremesas que abraçam o paladar.", "#E11D48", "#3B0716", "#FB7185", "#FFF1F2", "catalog"),
            ("padaria", "Padaria Artesanal", "Golden Crust Fermentação Natural", "Pães sourdough assados na primeira hora da manhã, croissants crocantes e cafés.", "#D97706", "#1E1208", "#F59E0B", "#FBF8F2", "catalog"),
            ("acaiteria", "Açaiteria", "Açaí Prime Bowl & Smoothies", "Açaí puro e cremoso do Pará com mais de 35 opções de frutas e acompanhamentos à vontade.", "#7E22CE", "#1E0533", "#A855F7", "#FAF5FF", "catalog"),
            ("sorveteria", "Sorveteria", "Gelateria Dolcezza Italiana", "Gelatos artesanais feitos diariamente com frutas frescas e bases italianas legítimas.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "catalog"),
            ("churrascaria", "Churrascaria", "Boi de Fogo Cortes Nobres", "Picanha na brasa, costela assada em fogo de chão e buffet completo com cortes premium.", "#991B1B", "#1C0505", "#DC2626", "#FEF2F2", "catalog"),
            ("restaurante-japones", "Restaurante Japonês", "Satori Sushi & Lounge", "Sushis, sashimis frescos de salmão e atum e combinados contemporâneos de alta gastronomia.", "#DC2626", "#121212", "#EF4444", "#121212", "catalog"),
            ("marmitaria", "Marmitaria", "Sabor da Terra Marmitas & Fit", "Marmitas caseiras balanceadas, comida com sabor de vó e planos semanais de almoço corporativo.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "catalog"),
            ("pastelaria", "Pastelaria", "Pastel de Ouro Massas Artesanais", "Pastéis crocantes e sequinhos com mais de 40 recheios transbordando e caldo de cana gelado.", "#D97706", "#2E1503", "#F59E0B", "#FFFBEB", "catalog"),
            ("casa-sucos", "Casa de Sucos", "Vitamina & Cia Green Bar", "Sucos naturais prensados a frio, açaí, sanduíches integrais e lanches pós-treino.", "#65A30D", "#1A2E05", "#84CC16", "#F7FEE7", "catalog"),
            ("emporio-produtos-naturais", "Empório de Produtos Naturais", "Grão da Terra Empório", "Castanhas, cereais a granel, farinhas especiais, temperos e alimentos funcionais.", "#B45309", "#271202", "#D97706", "#FFFBEB", "catalog"),
            ("adega", "Adega", "Cave Imperial Adega Selecionada", "Rótulos premiados do mundo inteiro, sommeliers especializados e entrega climatizada expressa.", "#7E22CE", "#1E0B30", "#A855F7", "#FAF5FF", "catalog"),
            ("distribuidora-bebidas", "Distribuidora de Bebidas", "Ponto Gelado Bebidas Express", "Cervejas trincando de geladas, destilados, gelo e carvão para o seu churrasco e festa.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "catalog")
        ]
    },
    {
        "id": "fitness-bem-estar",
        "name": "Fitness e Bem-Estar",
        "icon": "⚡",
        "desc": "Academias, pilates, crossfit, yoga e estúdios esportivos",
        "niches": [
            ("academia", "Academia", "Força & Performance Fitness", "Musculação completa, equipamentos biomecânicos e acompanhamento de professores dedicados.", "#DC2626", "#09090B", "#EF4444", "#09090B", "booking"),
            ("estudio-pilates", "Estúdio de Pilates", "Equilibrium Pilates & Fisio", "Aulas personalizadas com no máximo 3 alunos por horário em aparelhos modernos.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "booking"),
            ("box-crossfit", "Box de CrossFit", "IronBox Cross Training", "Superação diária com treinos de alta intensidade, comunidade unida e coaches certificados.", "#EA580C", "#0C0A09", "#F97316", "#0C0A09", "booking"),
            ("estudio-yoga", "Estúdio de Yoga", "Shanti Yoga Shala", "Hatha, Vinyasa e meditação guiada para respirar com calma e reencontrar o equilíbrio.", "#D97706", "#291804", "#F59E0B", "#FFFBEB", "booking"),
            ("personal-trainer", "Personal Trainer", "Lucas Prado Personal", "Consultoria de treino individualizada com prescrição de exercícios com base científica.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "booking"),
            ("escola-natacao", "Escola de Natação", "Acqua Mar Natação & Hidro", "Piscinas aquecidas e salinizadas para bebês, crianças e hidroginástica adulta.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "booking"),
            ("estudio-danca", "Estúdio de Dança", "Passos & Ritmos Dança", "Ballet, jazz, dança de salão e ritmos para se movimentar, queimar calorias e sorrir.", "#DB2777", "#4C0526", "#F472B6", "#FDF2F8", "booking"),
            ("academia-artes-marciais", "Academia de Artes Marciais", "Gracie Legacy Jiu-Jitsu & Muay Thai", "Disciplina, defesa pessoal e condicionamento físico para crianças, mulheres e adultos.", "#B91C1C", "#141414", "#EF4444", "#141414", "booking"),
            ("quadra-beach-tennis", "Arena de Beach Tennis", "Praia & Areia Beach Club", "Quadras de areia oficiais, aulas para iniciantes, torneios e bar com petiscos.", "#EA580C", "#1C1917", "#F97316", "#FFF7ED", "booking"),
            ("estudio-treinamento-funcional", "Estúdio Funcional", "Action Treino Funcional", "Queima de gordura e fortalecimento com circuitos dinâmicos sem a rotina da musculação.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "booking")
        ]
    },
    {
        "id": "servicos-profissionais",
        "name": "Serviços Profissionais",
        "icon": "⚖️",
        "desc": "Advocacia, contabilidade, arquitetura, engenharia e consultorias",
        "niches": [
            ("escritorio-advocacia", "Escritório de Advocacia", "Moraes & Associados Advocacia", "Defesa combativa e assessoria jurídica em Direito Trabalhista, Civil e Empresarial.", "#D97706", "#0F172A", "#F59E0B", "#F8FAFC", "quote"),
            ("escritorio-contabilidade", "Escritório de Contabilidade", "Exata Gestão Contábil & Fiscal", "Abertura de empresas grátis, planejamento tributário e assessoria contábil completa.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("escritorio-arquitetura", "Escritório de Arquitetura", "Studio Vértice Arquitetura", "Projetos arquitetônicos residenciais e comerciais que unem funcionalidade, luz e sofisticação.", "#2563EB", "#0B0F15", "#38BDF8", "#0B0F15", "quote"),
            ("escritorio-engenharia", "Escritório de Engenharia", "Estrutura & Obra Engenharia Civil", "Cálculo estrutural, laudos periciais, reformas prediais e gerenciamento de obras civis.", "#D97706", "#1C1917", "#F59E0B", "#FFFBEB", "quote"),
            ("imobiliaria", "Imobiliária", "Horizonte Imóveis Nobres", "Venda e locação de imóveis residenciais e comerciais nas melhores regiões da cidade.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "catalog"),
            ("corretor-imoveis", "Corretor de Imóveis", "Carlos Mendes Consultor Imobiliário", "Atendimento consultivo personalizado para compra de lançamentos e imóveis de alto padrão.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "booking"),
            ("corretora-seguros", "Corretora de Seguros", "Garantia Total Seguros & Vida", "Seguro auto, residencial, empresarial e planos de saúde com as maiores seguradoras do país.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "quote"),
            ("consultoria-financeira", "Consultoria Financeira", "Valor & Prosperidade Consultoria", "Gestão de fluxo de caixa, reestruturação de dívidas e planejamento de lucro para PMEs.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "quote"),
            ("assessoria-investimentos", "Assessoria de Investimentos", "Apex Wealth Assessoria", "Alocação patrimonial inteligente, previdência privada e renda fixa com suporte credenciado.", "#D97706", "#1E1B4B", "#F59E0B", "#F8FAFC", "booking"),
            ("despachante", "Despachante Documentalista", "Ágil Despachante Documentos", "Emissão rápida de certidões, regularização de escrituras e assessoria burocrática sem filas.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "quote"),
            ("empresa-topografia", "Empresa de Topografia", "GeoMedições Topografia & Drone", "Levantamento planialtimétrico, georreferenciamento de imóveis e mapeamento por drone.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "quote"),
            ("perito-avaliador-imoveis", "Perito Avaliador de Imóveis", "Avalia Perícias & Laudos", "Laudos técnicos de avaliação imobiliária para partilhas judiciais, garantias e financiamento.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "quote"),
            ("tradutor-juramentado", "Tradutor Juramentado", "Poliglota Traduções Oficiais", "Traduções juramentadas em inglês, espanhol, italiano e alemão reconhecidas internacionalmente.", "#7C3AED", "#2E1065", "#A78BFA", "#FAF5FF", "quote")
        ]
    },
    {
        "id": "casa-reforma",
        "name": "Casa e Reforma",
        "icon": "🔨",
        "desc": "Marcenarias, empreiteiras, eletricistas, pintores e instalações",
        "niches": [
            ("marcenaria", "Marcenaria", "Arte & Madeira Marcenaria Fina", "Móveis sob medida com ferragens italianas, acabamento de alto padrão e garantia de 5 anos.", "#B45309", "#1E1208", "#D97706", "#FDFBF7", "quote"),
            ("moveis-planejados", "Móveis Planejados", "Inspira Ambientes Planejados", "Cozinhas modernas, dormitórios funcionais e closets com projeto 3D gratuito sem compromisso.", "#D97706", "#1C1917", "#F59E0B", "#FFFBEB", "quote"),
            ("eletricista", "Eletricista Residencial & Comercial", "Volts & Cia Elétrica Rápida", "Instalação de quadros de força, fiação completa, tomadas e iluminação LED com total segurança.", "#EAB308", "#18181B", "#FACC15", "#18181B", "quote"),
            ("encanador", "Encanador Especializado", "HidroSoluções Encanamentos", "Caça-vazamentos com geofone, desentupimentos, instalação de torneiras e registros em geral.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("pintura-predial", "Pintor & Pintura Predial", "Cores Vivas Pinturas & Texturas", "Pintura residencial, aplicação de texturas, cimento queimado e fachadas comerciais.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "quote"),
            ("gesso-drywall", "Gesso e Drywall", "Forma & Forro Drywall", "Sancas de gesso com LED embutido, paredes divisórias acústicas e forros modulares.", "#64748B", "#0F172A", "#94A3B8", "#F8FAFC", "quote"),
            ("serralheria", "Serralheria", "Aço Forte Serralheria & Portões", "Portões basculantes, grades de proteção, corrimãos em inox e mezaninos industriais.", "#D97706", "#18181B", "#F59E0B", "#18181B", "quote"),
            ("vidracaria", "Vidraçaria", "Cristal Box Vidros Temperados", "Box para banheiro elegance, espelhos lapidados, fachadas em pele de vidro e guarda-corpo.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "quote"),
            ("esquadrias-aluminio", "Esquadrias de Alumínio", "Linha Nobre Esquadrias", "Portas balcão, janelas acústicas e esquadrias de alumínio preto fosco sob medida.", "#475569", "#09090B", "#94A3B8", "#09090B", "quote"),
            ("marmoraria", "Marmoraria", "Granitos & Mármores Aliança", "Bancadas de cozinha em quartzo, ilhas em granito e pias esculpidas com corte milimétrico.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "quote"),
            ("piscinas", "Construção de Piscinas", "Acqua Azul Piscinas & Spas", "Construção de piscinas de alvenaria armada, vinil, cascatas de pedra e aquecimento solar.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("jardinagem", "Jardinagem & Manutenção Verde", "Verde Vida Jardins", "Poda de árvores, corte de grama, adubação orgânica e manutenção periódica de condomínios.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "quote"),
            ("paisagismo", "Paisagismo", "Terra Verde Projetos Paisagísticos", "Criação de jardins tropicais, muros verdes verticais e vasos ornamentais com plantas nobres.", "#15803D", "#022C22", "#4ADE80", "#F0FDF4", "quote"),
            ("ar-condicionado", "Instalação de Ar-Condicionado", "Clima Puro Ar-Condicionado", "Instalação de split inverter, higienização química profunda e recarga de gás ecológica.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("energia-solar", "Energia Solar Fotovoltaica", "Solarex Energia Sustentável", "Reduza até 95% da sua conta de luz com painéis solares financiados com economia imediata.", "#EAB308", "#1C1917", "#FACC15", "#FFFBEB", "quote"),
            ("seguranca-eletronica", "Segurança Eletrônica", "Vigilant Câmeras & Alarmes", "Instalação de CFTV HD com acesso no celular, cerca elétrica, interfonia e controle de acesso.", "#DC2626", "#0F172A", "#EF4444", "#F8FAFC", "quote"),
            ("portoes-automaticos", "Portões Automáticos", "Speed Motor Portões", "Automatização de portões rápidos de 3 segundos, travas elétricas e manutenção preventiva.", "#D97706", "#18181B", "#F59E0B", "#18181B", "quote"),
            ("chaveiro", "Chaveiro 24 Horas", "Chave de Ouro Chaveiro Express", "Aberturas residenciais e automotivas de emergência 24h, cópia de chaves codificadas.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "quote"),
            ("desentupidora", "Desentupidora 24h", "Desentope Já Hidrojateamento", "Desentupimento rápido de pias, ralos, vasos sanitários e esgotos com equipamento rotativo.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("dedetizadora", "Dedetizadora", "BioPragas Controle de Pragas", "Dedetização contra baratas, formigas, cupins e desratização com laudo e garantia certificada.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "quote"),
            ("impermeabilizacao", "Impermeabilização", "Selaflex Impermeabilizações", "Elimine infiltrações em lajes, baldrames, piscinas e calhas com manta asfáltica garantida.", "#0284C7", "#0F172A", "#38BDF8", "#F8FAFC", "quote"),
            ("calhas-telhados", "Calhas e Telhados", "Calheiro do Vale Rufos & Telhas", "Fabricação de calhas sem emenda, rufos em alumínio, limpeza e reforma completa de telhados.", "#D97706", "#18181B", "#F59E0B", "#18181B", "quote"),
            ("construtora", "Construtora & Obras", "Vanguard Engenharia & Obras", "Construção de casas do alicerce à pintura com cronograma pontual e prestação de contas clara.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "quote"),
            ("decoracao-interiores", "Decoração de Interiores", "Harmonia Home Decorações", "Cortinas sob medida, papéis de parede importados, persianas motorizadas e iluminação.", "#BE185D", "#3B0718", "#FB7185", "#FFF1F2", "quote")
        ]
    },
    {
        "id": "automotivo",
        "name": "Automotivo",
        "icon": "🚗",
        "desc": "Oficinas mecânicas, estética automotiva, autoescolas e socorro",
        "niches": [
            ("oficina-mecanica", "Oficina Mecânica", "AutoTech Mecânica Especializada", "Revisão geral, injeção eletrônica, freios, suspensão e troca de óleo com scanner digital.", "#D97706", "#111827", "#F59E0B", "#111827", "quote"),
            ("estetica-automotiva", "Estética Automotiva", "Detailer Pro Polimento & Vitrificação", "Vitrificação cerâmica de pintura 9H, polimento técnico e higienização interna profunda.", "#2563EB", "#0B0F15", "#38BDF8", "#0B0F15", "booking"),
            ("funilaria-pintura", "Funilaria e Pintura", "Marmoraria & Funilaria Express", "Recuperação de para-choques, martelinho de ouro sem danificar a pintura e cabine pressurizada.", "#DC2626", "#111827", "#EF4444", "#111827", "quote"),
            ("lava-rapido", "Lava Rápido", "Acqua Wash Lavação & Cera", "Lavagem detalhada com snow foam, aspiração minuciosa e aplicação de cera protetora de carnaúba.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "booking"),
            ("autoescola", "Autoescola", "CFC Primeira Linha Habilitação", "Primeira habilitação A e B, adição de categoria e simulador com alta taxa de aprovação.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "booking"),
            ("borracharia", "Borracharia & Pneus", "Ponto do Pneu Borracharia 24h", "Conserto de pneus na hora, balanceamento computadorizado, alinhamento e pneus novos.", "#D97706", "#18181B", "#F59E0B", "#18181B", "quote"),
            ("auto-pecas", "Auto Peças", "Central das Peças Automotivas", "Amplo estoque de suspensão, embreagem, correias e filtros com pronta entrega na sua oficina.", "#EA580C", "#1C1917", "#F97316", "#FFF7ED", "catalog"),
            ("moto-pecas-oficina", "Moto Peças & Oficina", "Duas Rodas Oficina & Peças", "Revisão de motos, troca de relação, pneus, escapamentos e acessórios para motociclistas.", "#DC2626", "#18181B", "#EF4444", "#18181B", "quote"),
            ("som-automotivo", "Som e Acessórios Automotivos", "Extreme Som & Acessórios", "Instalação de centrais multimídia Apple CarPlay, caixas de som sob medida e alarmes.", "#7C3AED", "#18181B", "#A78BFA", "#18181B", "quote"),
            ("insulfilm-peliculas", "Insulfilm & Películas Automotivas", "Black Glass Películas Solares", "Películas térmicas nanocerâmicas com redução de calor de 90%, segurança antivandalismo.", "#2563EB", "#0B0F15", "#38BDF8", "#0B0F15", "quote"),
            ("vidros-automotivos", "Vidros Automotivos", "Autoglass Reparo de Para-brisas", "Troca rápida de para-brisas, vidros laterais e reparo de trincas com garantia de fábrica.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("guincho", "Guincho e Auto Socorro", "SOS Resgate Guincho Plataforma", "Atendimento emergencial 24 horas para carros, motos e vans com chegada em até 30 minutos.", "#D97706", "#111827", "#F59E0B", "#111827", "quote"),
            ("locadora-veiculos", "Locadora de Veículos", "Mobilidade Rent a Car", "Locação diária e mensal para motoristas de aplicativo e empresas sem burocracia.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "catalog"),
            ("despachante-veicular", "Despachante Veicular", "Rápido Transferências Veiculares", "Transferência de veículos, licenciamento online e primeiro emplacamento sem perder tempo.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "quote")
        ]
    },
    {
        "id": "pets",
        "name": "Pets",
        "icon": "🐾",
        "desc": "Pet shops, clínicas veterinárias, banho e tosa e hospedagem animal",
        "niches": [
            ("pet-shop", "Pet Shop", "Pet Charm Acessórios & Rações", "Rações premium e super premium, caminhas, brinquedos e farmácia veterinária completa.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "catalog"),
            ("clinica-veterinaria", "Clínica Veterinária", "VetCare Hospital Veterinário", "Consultas, vacinas importadas, exames laboratoriais e cirurgias com plantão 24 horas.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "booking"),
            ("banho-tosa", "Banho e Tosa", "Espaço Peludos Banho & Estética", "Banhos relaxantes com hidratação de ozônio, tosa bebê, tosa na tesoura e táxi dog com ar.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "booking"),
            ("hotel-cachorro", "Hotel para Cachorro", "Colônia Pet Hospedagem Familiar", "Hospedagem segura sem gaiolas, quartos climatizados, gramado amplo e fotos no WhatsApp.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "booking"),
            ("creche-cachorro", "Creche Canina (Day Care)", "Happy Dogs Creche & Recreação", "Socialização, enriquecimento ambiental, piscina e recreação supervisionada o dia inteiro.", "#EA580C", "#1C0D05", "#F97316", "#FFF7ED", "booking"),
            ("adestrador-caes", "Adestrador de Cães", "Comportamento Canino Adestramento", "Educação de filhotes, controle de ansiedade de separação e obediência por reforço positivo.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "booking")
        ]
    },
    {
        "id": "educacao",
        "name": "Educação",
        "icon": "🎓",
        "desc": "Escolas de idiomas, música, infantil, reforço e cursos livres",
        "niches": [
            ("escola-idiomas", "Escola de Idiomas", "Talk & Go Inglês para Comunicação", "Inglês fluente em até 18 meses com foco 100% em conversação e metodologia imersiva.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "curriculum"),
            ("escola-infantil", "Escola Infantil & Berçário", "Pequenos Passos Educação Infantil", "Educação socioemocional, nutrição balanceada e pedagogia afetiva para crianças de 0 a 5 anos.", "#E11D48", "#4C0519", "#FB7185", "#FFF1F2", "booking"),
            ("reforco-escolar", "Reforço Escolar", "Aprender Mais Apoio Pedagógico", "Acompanhamento diário em matemática, redação e física para o seu filho tirar nota 10.", "#D97706", "#1E1208", "#F59E0B", "#FFFBEB", "booking"),
            ("escola-musica", "Escola de Música", "Sonata Academia Musical", "Aulas de piano, canto, teclado, bateria e violino para crianças, jovens e adultos.", "#7C3AED", "#18181B", "#A78BFA", "#FAF5FF", "curriculum"),
            ("aulas-violao", "Aulas de Violão e Guitarra", "Cordas & Som Estúdio Musical", "Toque suas músicas favoritas desde a primeira aula com método prático e descomplicado.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "booking"),
            ("aulas-canto", "Aulas de Canto e Técnica Vocal", "Voz em Foco Escola de Canto", "Afinação, extensão vocal, respiração diafragmática e presença de palco sem esforço.", "#DB2777", "#3B0721", "#F472B6", "#FDF2F8", "booking"),
            ("curso-profissionalizante", "Cursos Profissionalizantes", "Capacita Brasil Centro de Formação", "Cursos práticos e rápidos para você entrar no mercado de trabalho com certificado válido.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "curriculum"),
            ("escola-gastronomia", "Escola de Gastronomia", "Chef & Sabor Culinária Prática", "Cursos de confeitaria, panificação artesanal e culinária contemporânea com chefs renomados.", "#B45309", "#1E1208", "#D97706", "#FDFBF7", "curriculum"),
            ("escola-informatica", "Escola de Informática", "TechStart Cursos de Tecnologia", "Excel avançado para negócios, Power BI, programação e pacote Office completo.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "curriculum"),
            ("robotica-criancas", "Robótica para Crianças", "RoboKids Inovação Infantil", "Programação, robótica e pensamento lógico para crianças e adolescentes através do lúdico.", "#7C3AED", "#1E1B4B", "#A78BFA", "#F8FAFC", "curriculum")
        ]
    },
    {
        "id": "comercio-local",
        "name": "Comércio Local",
        "icon": "🏪",
        "desc": "Lojas de roupas, calçados, materiais, floriculturas e óticas",
        "niches": [
            ("floricultura", "Floricultura", "Florescer Floricultura & Afeto", "Buquês de rosas nobres, orquídeas raras, arranjos para presentes e entrega expressa no mesmo dia.", "#DB2777", "#3B0721", "#F472B6", "#FDF2F8", "catalog"),
            ("loja-roupas", "Loja de Roupas Femininas", "Moda Elegance Closet", "Looks contemporâneos do casual ao chique com tecidos nobres e caimento impecável.", "#BE185D", "#3B0718", "#FB7185", "#FFF1F2", "catalog"),
            ("boutique", "Boutique Exclusiva", "Maison Chic Boutique", "Coleções limitadas de peças exclusivas, alfaiataria fina e atendimento com personal stylist.", "#9333EA", "#1E1B4B", "#C084FC", "#FAF5FF", "catalog"),
            ("loja-calcados", "Loja de Calçados", "Passo Firme Calçados & Tênis", "Sapatos confortáveis, sandálias e tênis casuais para todas as ocasiões com numerações especiais.", "#D97706", "#1C1917", "#F59E0B", "#FFFBEB", "catalog"),
            ("joalheria", "Joalheria & Alianças", "Aurum Joias Finas", "Alianças de casamento em ouro 18k, anéis solitários com diamantes e joias personalizadas.", "#D97706", "#0B0F15", "#F59E0B", "#0B0F15", "catalog"),
            ("relojoaria", "Relojoaria e Consertos", "Cronos Relógios & Restaurações", "Venda de relógios automáticos, pulseiras nobres e manutenção de mecanismos suíços.", "#0284C7", "#0F172A", "#38BDF8", "#F8FAFC", "catalog"),
            ("perfumaria", "Perfumaria & Cosméticos", "Essência Rara Perfumes Importados", "Perfumes importados 100% originais com selo ADIPEC e hidratantes corporais de luxo.", "#BE185D", "#4C0519", "#F43F5E", "#FFF1F2", "catalog"),
            ("loja-cosmeticos", "Loja de Cosméticos", "Beleza & Pele Cosméticos", "Skincare dermatológico, maquiagens profissionais e produtos para cronograma capilar.", "#E11D48", "#3B0716", "#FB7185", "#FFF1F2", "catalog"),
            ("papelaria", "Papelaria & Presentes", "Papel & Letras Papelaria Criativa", "Cadernos inteligentes, canetas importadas, planners e artigos de escritório encantadores.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "catalog"),
            ("loja-brinquedos", "Loja de Brinquedos", "Brinque Bem Brinquedos Educativos", "Jogos de tabuleiro familiares, quebra-cabeças e brinquedos de madeira para todas as idades.", "#EA580C", "#1C0D05", "#F97316", "#FFF7ED", "catalog"),
            ("loja-moveis", "Loja de Móveis", "Conforto Prime Estofados & Salas", "Sofás retráteis com molas ensacadas, poltronas confortáveis e mesas de jantar em madeira maciça.", "#B45309", "#1E1208", "#D97706", "#FDFBF7", "catalog"),
            ("loja-colchoes", "Loja de Colchões", "Sono dos Sonhos Colchões", "Colchões magnéticos, molas ensacadas individuais e travesseiros de látex natural para seu sono.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "catalog"),
            ("loja-iluminacao", "Loja de Iluminação", "Lustres & Luz Design Luminotécnico", "Pendentes modernos, perfis de LED de sobrepor e lustres de cristal com projeto de iluminação.", "#D97706", "#0B0F15", "#F59E0B", "#0B0F15", "catalog"),
            ("loja-materiais-construcao", "Loja de Materiais de Construção", "Construmais Materiais Básicos", "Do cimento ao acabamento, entrega rápida na obra com condições especiais para empreiteiros.", "#D97706", "#18181B", "#F59E0B", "#18181B", "catalog"),
            ("loja-tintas", "Loja de Tintas", "Mundo das Tintas & Vernizes", "Máquina tintométrica com mais de 5.000 cores, esmaltes sintéticos e complementos para pintura.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "catalog"),
            ("armarinho", "Armarinho e Aviamentos", "Linhas & Nós Armarinho", "Fios para crochê, lãs, botões especiais, zíperes e tudo para costura criativa e artesanato.", "#DB2777", "#3B0721", "#F472B6", "#FDF2F8", "catalog"),
            ("loja-tecidos", "Loja de Tecidos", "Tecelagem Nobre Tecidos Finos", "Sedas puras, linhos, rendas francesas e tecidos para decoração e cortinas a pronta entrega.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "catalog"),
            ("loja-presentes", "Loja de Presentes Criativos", "Surpreenda Presentes & Decor", "Canecas personalizadas, luminárias divertidas, porta-retratos e kits temáticos para datas especiais.", "#E11D48", "#3B0716", "#FB7185", "#FFF1F2", "catalog"),
            ("loja-produtos-naturais", "Loja de Produtos Naturais", "Raízes Saúde & Granel", "Castanhas nobres a granel, chás terapêuticos, farinhas funcionais e suplementação natural.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "catalog"),
            ("tabacaria", "Tabacaria", "Charutaria & Tabacos Dom Pedro", "Charutos cubanos e baianos legítimos, cachimbos esculpidos e isqueiros de precisão.", "#B45309", "#111827", "#D97706", "#111827", "catalog")
        ]
    },
    {
        "id": "eventos-festas",
        "name": "Eventos e Festas",
        "icon": "🎉",
        "desc": "Buffets, salões de festas, fotógrafos, DJs e decoração",
        "niches": [
            ("buffet-festas", "Buffet para Festas", "Celebrar Gastronomia & Eventos", "Cardápios completos para casamentos, aniversários de 15 anos e eventos corporativos de sucesso.", "#D97706", "#1C1917", "#F59E0B", "#FFFBEB", "quote"),
            ("espaco-eventos", "Espaço de Eventos", "Mansão das Palmeiras Eventos", "Salão nobre climatizado com área externa verdejante para até 350 convidados com estacionamento.", "#2563EB", "#0B0F15", "#38BDF8", "#0B0F15", "booking"),
            ("decoracao-festas", "Decoração de Festas", "Festa Encantada Cenografia", "Projetos cenográficos exclusivos, painéis de LED, flores nobres e mesa temática impecável.", "#DB2777", "#3B0721", "#F472B6", "#FDF2F8", "quote"),
            ("doces-festas", "Doces Finos para Festas", "Dulce Amore Doces Finos", "Brigadeiros belgas gourmet, camafeus de nozes e doces personalizados para mesa de noivos.", "#E11D48", "#3B0716", "#FB7185", "#FFF1F2", "catalog"),
            ("fotografo", "Fotógrafo de Casamentos e Família", "Rodrigo Lima Fotografia", "Registros emocionantes e espontâneos com olhar cinematográfico e álbuns encadernados de luxo.", "#2563EB", "#0B0F15", "#38BDF8", "#0B0F15", "booking"),
            ("produtora-video", "Produtora de Vídeo e Drone", "Cinemateca Filmes & Eventos", "Cobertura em vídeo 4K com imagens de drone, teaser para redes sociais e filme completo.", "#7C3AED", "#0B0F15", "#A78BFA", "#0B0F15", "quote"),
            ("dj-festas", "DJ para Festas e Casamentos", "Soundtrack DJ & Iluminação", "Pista de dança cheia a noite toda com repertório personalizado e estrutura de som e laser.", "#EA580C", "#09090B", "#F97316", "#09090B", "booking"),
            ("cerimonialista", "Cerimonialista de Casamento", "Aliança Perfeita Assessoria", "Planejamento minucioso, cronograma no dia e coordenação geral para um evento sem imprevistos.", "#D97706", "#1E1208", "#F59E0B", "#FDFBF7", "quote"),
            ("aluguel-mesas-cadeiras", "Aluguel de Mesas e Cadeiras", "LocFest Mesas & Mobiliário", "Cadeiras Tiffany, mesas redondas, toalhas adamascadas e louças com entrega e recolhimento.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("aluguel-brinquedos-festas", "Aluguel de Brinquedos", "Alegria Kids Brinquedos Infláveis", "Pula-pula gigante, piscina de bolinhas, tobogã inflável com monitores treinados.", "#EAB308", "#1C1917", "#FACC15", "#FFFBEB", "booking"),
            ("banda-eventos", "Banda para Eventos", "Banda Viva Som & Baile", "Show ao vivo com os maiores sucessos do pop, sertanejo e axé que contagiam todos os convidados.", "#DC2626", "#09090B", "#EF4444", "#09090B", "booking")
        ]
    },
    {
        "id": "turismo-hospedagem",
        "name": "Turismo e Hospedagem",
        "icon": "🏖️",
        "desc": "Pousadas, hotéis, agências de viagem e casas de temporada",
        "niches": [
            ("pousada", "Pousada", "Pousada Recanto das Águas", "Chalés aconchegantes com hidromassagem, café da manhã colonial com vista para as montanhas.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "booking"),
            ("hotel", "Hotel Urbano & Executivo", "Grand Plaza Hotel & Suítes", "Quartos confortáveis com isolamento acústico, business center e localização estratégica.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "booking"),
            ("hostel", "Hostel", "Vagabundo Hostel & Bar", "Acomodações compartilhadas e privativas com área de convivência acolhedora e bar descolado.", "#EA580C", "#1C0D05", "#F97316", "#FFF7ED", "booking"),
            ("agencia-turismo", "Agência de Turismo", "Destinos & Sonhos Viagens", "Pacotes completos com passagens, hospedagem e passeios para os destinos mais cobiçados do mundo.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "quote"),
            ("casa-temporada", "Casa de Temporada", "Vila Sol Casa de Praia & Piscina", "Imóvel completo para até 12 pessoas com piscina aquecida, churrasqueira e a 200m da praia.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "booking"),
            ("chacara-eventos", "Chácara para Eventos e Lazer", "Chácara Paraíso dos Eucaliptos", "Área de lazer com campo de futebol, salão de jogos, piscina e churrasqueira para finais de semana.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "booking")
        ]
    },
    {
        "id": "tecnologia-assistencia",
        "name": "Tecnologia e Assistência",
        "icon": "📱",
        "desc": "Assistência técnica de celulares, computadores, gráficas e câmeras",
        "niches": [
            ("assistencia-celular", "Assistência Técnica de Celular", "SmartFix Reparo Express de Celulares", "Troca de tela na hora, troca de bateria, reparo de conector e placas com garantia de 90 dias.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "quote"),
            ("assistencia-informatica", "Assistência Técnica em Informática", "PC Master Manutenção de Computadores", "Formatação, remoção de vírus, upgrade de SSD e reparo de placas de notebooks e computadores.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("conserto-videogame", "Conserto de Videogames", "GameZone Reparo de Consoles", "Manutenção preventiva com troca de pasta térmica de prata, reparo de controles e fontes de PS5 e Xbox.", "#7C3AED", "#18181B", "#A78BFA", "#18181B", "quote"),
            ("assistencia-eletrodomesticos", "Assistência de Eletrodomésticos", "Frio & Calor Consertos", "Conserto no mesmo dia de geladeiras, máquinas de lavar roupa, micro-ondas e fogões em domicílio.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "quote"),
            ("instalacao-cameras", "Instalação de Câmeras CFTV", "Olho Vivo Segurança Integrada", "Câmeras IP com visualização remota em alta definição no seu smartphone e gravação em nuvem.", "#DC2626", "#0F172A", "#EF4444", "#F8FAFC", "quote"),
            ("comunicacao-visual", "Comunicação Visual", "Visual Art Letreiros & Fachadas", "Letras caixa em ACM e acrílico iluminadas com LED, envelopamento de frotas e totens externos.", "#EA580C", "#1C1917", "#F97316", "#FFF7ED", "quote"),
            ("grafica", "Gráfica Rápida", "PrintMais Gráfica & Offset", "Cartões de visita com verniz localizado, panfletos, pastas corporativas e banners em lona.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "quote"),
            ("loja-informatica", "Loja de Informática & Peças", "TechStore Peças & Periféricos", "Monitores gamer, teclados mecânicos, mouses de alta precisão e roteadores Wi-Fi 6 de alta velocidade.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "catalog")
        ]
    },
    {
        "id": "outros-servicos",
        "name": "Outros Serviços",
        "icon": "📦",
        "desc": "Lavanderias, mudanças, limpezas pós-obra, cuidadores e costura",
        "niches": [
            ("lavanderia", "Lavanderia", "Lava Bem Lavanderia Têxtil", "Lavagem por quilo, higienização de ternos, vestidos de festa e cobertores com entrega embalada.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "catalog"),
            ("lavagem-sofa", "Higienização de Sofás e Estofados", "Clean Max Limpeza de Estofados", "Limpeza e impermeabilização profunda de sofás, colchões e tapetes a seco com eliminação de ácaros.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "quote"),
            ("empresa-limpeza", "Empresa de Limpeza", "Brilho Forte Limpeza Pós-Obra", "Limpeza pós-obra pesada, faxinas corporativas e terceirização de limpeza com nota fiscal e segurança.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("empresa-mudancas", "Empresa de Mudanças", "TransPorto Mudanças Residenciais", "Embalagem completa de louças e móveis, içamentos seguros e transporte interestadual ágil.", "#D97706", "#111827", "#F59E0B", "#111827", "quote"),
            ("cuidador-idosos", "Cuidador de Idosos", "Aconchego Cuidadores de Idosos", "Acompanhamento domiciliar e hospitalar humanizado 24h por profissionais de enfermagem credenciados.", "#BE185D", "#4C0519", "#F43F5E", "#FFF1F2", "booking"),
            ("organizadora-armarios", "Personal Organizer", "Harmonia Closet Organização", "Otimização inteligente de closets, cozinhas e despensas para economizar seu tempo no dia a dia.", "#9333EA", "#1E1B4B", "#C084FC", "#FAF5FF", "booking"),
            ("atelier-costura", "Atelier de Costura e Ajustes", "Ponto de Ouro Atelier de Costura", "Ajuste de vestidos de festa, bainhas originais, consertos de zíper e confecção de peças sob medida.", "#D97706", "#1E1208", "#F59E0B", "#FDFBF7", "booking"),
            ("sapataria", "Sapataria e Restaurações", "Sapataria Mestre Artesão", "Troca de solados, hidratação de couro legítimo, tingimento e recuperação de sapatos e bolsas de luxo.", "#B45309", "#111827", "#D97706", "#111827", "quote"),
            ("transportadora", "Transportadora de Cargas", "RodoCargas Encomendas Expressas", "Fretes e entregas rápidas ponto a ponto para e-commerce e empresas com rastreamento em tempo real.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "quote"),
            ("coworking", "Espaço de Coworking", "Hub Nexo Coworking & Salas", "Estações de trabalho compartilhadas, salas de reunião com TV 4K e endereço fiscal para sua empresa.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "booking")
        ]
    }
]

def get_service_data(title, brand, feat):
    return [
        {
            "name": f"Atendimento Primário / Avaliação",
            "desc": f"Diagnóstico inicial completo, análise das necessidades do cliente e plano de ação transparente.",
            "price": "R$ 150,00"
        },
        {
            "name": f"Serviço Especializado de {title}",
            "desc": f"Execução com os melhores materiais do mercado, pontualidade rigorosa e suporte de profissionais experientes.",
            "price": "R$ 290,00"
        },
        {
            "name": f"Manutenção / Suporte Periódico",
            "desc": f"Acompanhamento preventivo para garantir durabilidade, economia e evitar gastos inesperados.",
            "price": "R$ 210,00"
        },
        {
            "name": f"Plano Premium & Exclusivo",
            "desc": f"Solução completa para clientes que buscam a máxima performance, materiais nobres e prioridade no atendimento.",
            "price": "R$ 480,00"
        }
    ]

def render_case_html(cat, niche):
    slug, title, brand, slogan, primary, dark, accent, bg, feat = niche
    services = get_service_data(title, brand, feat)
    images = get_niche_images(cat['id'], slug)

    hero_img = images["hero"]
    srv_imgs = images["services"]
    gal_imgs = images["gallery"]
    avatars = images["avatars"]

    # Módulos Interativos Funcionais
    feature_markup = ""
    if feat == "booking":
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Agendamento Online</span>
            <h3>Escolha o melhor dia e horário para seu atendimento</h3>
            <p>Atendimento prioritário sem filas com confirmação instantânea no WhatsApp.</p>
          </div>
          <div class="date-chips">
            <button class="chip is-active" type="button" onclick="selectDate(this, 'Hoje, 28 Out')"><b>Hoje</b><span>28 Out</span></button>
            <button class="chip" type="button" onclick="selectDate(this, 'Amanhã, 29 Out')"><b>Amanhã</b><span>29 Out</span></button>
            <button class="chip" type="button" onclick="selectDate(this, 'Quinta, 30 Out')"><b>Quinta</b><span>30 Out</span></button>
            <button class="chip" type="button" onclick="selectDate(this, 'Sexta, 31 Out')"><b>Sexta</b><span>31 Out</span></button>
            <button class="chip" type="button" onclick="selectDate(this, 'Sábado, 01 Nov')"><b>Sábado</b><span>01 Nov</span></button>
          </div>
          <div class="time-chips">
            <button class="time-tag is-active" type="button" onclick="selectTime(this, '09:00')">09:00</button>
            <button class="time-tag" type="button" onclick="selectTime(this, '10:30')">10:30</button>
            <button class="time-tag" type="button" onclick="selectTime(this, '14:00')">14:00</button>
            <button class="time-tag" type="button" onclick="selectTime(this, '15:30')">15:30</button>
            <button class="time-tag" type="button" onclick="selectTime(this, '17:00')">17:00</button>
          </div>
          <div class="box-action">
            <a id="btn-booking" href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+agendar+um+hor%C3%A1rio+para+Hoje,+28+Out+às+09:00+na+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary btn-block">Confirmar Agendamento no WhatsApp →</a>
          </div>
        </div>
        """
    elif feat == "catalog":
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Cardápio &amp; Vitrine Digital</span>
            <h3>Selecione os itens e peça direto pelo WhatsApp</h3>
            <p>Entrega expressa ou retirada no balcão com atendimento imediato.</p>
          </div>
          <div class="catalog-grid">
            <div class="cat-item">
              <img src="{srv_imgs[0]}" alt="Opção da Casa" class="cat-img" />
              <div class="cat-info">
                <span class="cat-badge">Mais Pedido</span>
                <h4>Opção Especial da Casa</h4>
                <p>Receita clássica artesanal com ingredientes frescos selecionados.</p>
                <div class="cat-foot">
                  <b>R$ 38,00</b>
                  <div class="qty-control">
                    <button type="button" onclick="updateQty('q1', -1, 38)">-</button>
                    <span id="q1">1</span>
                    <button type="button" onclick="updateQty('q1', 1, 38)">+</button>
                  </div>
                </div>
              </div>
            </div>
            <div class="cat-item">
              <img src="{srv_imgs[1]}" alt="Combo Premium" class="cat-img" />
              <div class="cat-info">
                <span class="cat-badge">Especial</span>
                <h4>Combo Premium &amp; Acompanhamentos</h4>
                <p>A combinação perfeita para compartilhar com a família ou amigos.</p>
                <div class="cat-foot">
                  <b>R$ 65,00</b>
                  <div class="qty-control">
                    <button type="button" onclick="updateQty('q2', -1, 65)">-</button>
                    <span id="q2">0</span>
                    <button type="button" onclick="updateQty('q2', 1, 65)">+</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="box-action">
            <a id="btn-catalog" href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+fazer+o+pedido:+1x+Opcao+Especial+(R$+38,00)+na+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary btn-block">Pedir no WhatsApp · Total: <span id="cart-total">R$ 38,00</span> →</a>
          </div>
        </div>
        """
    elif feat == "curriculum":
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Turmas &amp; Matrículas Abertas</span>
            <h3>Aulas Práticas com Vagas Limitadas</h3>
            <p>Garanta sua vaga ou agende uma aula experimental gratuita hoje mesmo.</p>
          </div>
          <div class="curriculum-list">
            <div class="curr-card">
              <span class="curr-tag">Turma Regular</span>
              <h4>Módulo Fundamental — Do Zero ao Avançado</h4>
              <p>Metodologia prática, material didático incluso e suporte com professores dedicados.</p>
              <small>📅 Início: Próxima Segunda-feira • 3 vagas restantes</small>
            </div>
            <div class="curr-card">
              <span class="curr-tag">Intensivo</span>
              <h4>Workshop Especial de Aperfeiçoamento</h4>
              <p>Técnicas modernas para quem deseja evoluir rápido com imersão completa.</p>
              <small>📅 Sábados das 09h às 13h • Turmas reduzidas</small>
            </div>
          </div>
          <div class="box-action">
            <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+garantir+uma+vaga+na+turma+da+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary btn-block">Agendar Aula Experimental Gratuita no WhatsApp →</a>
          </div>
        </div>
        """
    else: # quote
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Orçamento Instantâneo</span>
            <h3>Simule seu orçamento em menos de 1 minuto</h3>
            <p>Selecione as opções desejadas e receba a proposta detalhada no WhatsApp.</p>
          </div>
          <div class="quote-calculator">
            <label class="calc-check">
              <input type="checkbox" checked onchange="calcQuote()" value="180" class="chk-item" />
              <span>{services[0]['name']} (Avaliação / Diagnóstico)</span>
              <b>+R$ 180</b>
            </label>
            <label class="calc-check">
              <input type="checkbox" checked onchange="calcQuote()" value="290" class="chk-item" />
              <span>{services[1]['name']} (Execução Padrão)</span>
              <b>+R$ 290</b>
            </label>
            <label class="calc-check">
              <input type="checkbox" onchange="calcQuote()" value="150" class="chk-item" />
              <span>Garantia Estendida &amp; Suporte Prioritário</span>
              <b>+R$ 150</b>
            </label>
            <div class="quote-subtotal">
              <span>Estimativa Preliminar:</span>
              <b id="quote-val">R$ 470,00</b>
            </div>
          </div>
          <div class="box-action">
            <a id="btn-quote" href="https://wa.me/5519996331656?text=Ol%C3%A1!+Simulei+um+or%C3%A7amento+no+valor+de+R$+470,00+para+{title.replace(' ', '+')}+na+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary btn-block">Receber Orçamento Oficial no WhatsApp →</a>
          </div>
        </div>
        """

    # 4 Cards de Serviços com Fotos Full HD
    services_html = "".join([f"""
      <article class="service-card">
        <div class="srv-img-wrap">
          <img src="{srv_imgs[i % len(srv_imgs)]}" alt="{s['name']}" class="srv-img" loading="lazy" />
          <span class="srv-badge">Especialidade</span>
        </div>
        <div class="srv-body">
          <h4>{s['name']}</h4>
          <p>{s['desc']}</p>
          <div class="srv-price">
            <small>Investimento</small>
            <b>{s['price']}</b>
          </div>
          <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Tenho+interesse+no+servi%C3%A7o+{s['name'].replace(' ', '+')}+da+{brand.replace(' ', '+')}." target="_blank" class="srv-btn">
            Solicitar no WhatsApp <span>→</span>
          </a>
        </div>
      </article>
    """ for i, s in enumerate(services)])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{brand} — {title}</title>
  <meta name="description" content="{slogan}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --primary: {primary};
      --dark: {dark};
      --accent: {accent};
      --bg: {bg};
      --paper: #FFFFFF;
      --text: #1E293B;
      --muted: #64748B;
      --line: rgba(15, 23, 42, 0.08);
      --font-head: 'Plus Jakarta Sans', system-ui, sans-serif;
      --font-body: 'Plus Jakarta Sans', system-ui, sans-serif;
      --radius: 16px;
      --shadow: 0 12px 36px -12px rgba(15, 23, 42, 0.12);
    }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 70px;
    }}
    /* Top Ribbon Nexo */
    .nexo-bar {{
      background: #0B0F14;
      color: #94A3B8;
      font-size: 12px;
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      position: relative; z-index: 60;
    }}
    .nexo-bar a {{ color: #38BDF8; font-weight: 700; text-decoration: none; }}
    .nexo-bar a:hover {{ text-decoration: underline; }}
    
    /* Top Info Bar */
    .top-info {{
      background: var(--dark);
      color: #CBD5E1;
      font-size: 12.5px;
      padding: 8px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .top-info b {{ color: #fff; font-weight: 600; }}

    /* Header */
    .header {{
      background: rgba(255,255,255,0.95);
      backdrop-filter: blur(12px);
      padding: 16px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--line);
      position: sticky; top: 0; z-index: 50;
      box-shadow: 0 4px 20px -10px rgba(0,0,0,0.05);
    }}
    .logo {{
      display: flex; align-items: center; gap: 12px; text-decoration: none; color: var(--dark);
    }}
    .logo-badge {{
      width: 44px; height: 44px; border-radius: 12px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #fff; display: grid; place-items: center; font-size: 20px; font-weight: 800;
      box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    }}
    .logo-info b {{ display: block; font-size: 17.5px; font-weight: 800; letter-spacing: -0.02em; line-height: 1.1; }}
    .logo-info small {{ font-size: 11px; color: var(--muted); letter-spacing: 0.08em; text-transform: uppercase; font-weight: 700; }}
    
    .nav {{ display: flex; align-items: center; gap: 24px; list-style: none; }}
    .nav a {{ color: var(--muted); text-decoration: none; font-size: 13.5px; font-weight: 600; transition: color .2s; }}
    .nav a:hover {{ color: var(--primary); }}

    .btn {{
      display: inline-flex; align-items: center; justify-content: center; gap: 8px;
      padding: 13px 26px; border-radius: 999px;
      font-size: 14px; font-weight: 700; text-decoration: none;
      transition: all .25s ease; cursor: pointer; border: none; font-family: inherit;
    }}
    .btn-icon {{ width: 18px; height: 18px; }}
    .btn-primary {{
      background: var(--primary); color: #fff;
      box-shadow: 0 6px 20px -4px rgba(0,0,0,0.2);
    }}
    .btn-primary:hover {{ transform: translateY(-2px); filter: brightness(1.08); box-shadow: 0 10px 28px -4px rgba(0,0,0,0.3); }}
    .btn-outline {{
      background: #FFFFFF; color: var(--dark); border: 1.5px solid var(--line);
    }}
    .btn-outline:hover {{ border-color: var(--primary); color: var(--primary); background: #fff; transform: translateY(-2px); }}
    .btn-block {{ width: 100%; }}
    .btn-sm {{
      background: var(--primary); color: #fff; font-size: 12px; font-weight: 700;
      padding: 7px 16px; border-radius: 999px; text-decoration: none;
    }}

    /* HERO */
    .hero {{
      padding: 56px 32px 64px;
      max-width: 1240px; margin: 0 auto;
      display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 48px;
      align-items: center;
    }}
    .rating-pill {{
      display: inline-flex; align-items: center; gap: 8px;
      background: #FFFFFF; border: 1px solid var(--line);
      padding: 6px 14px; border-radius: 999px; font-size: 12.5px; font-weight: 700;
      color: var(--dark); margin-bottom: 20px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}
    .rating-pill span {{ color: #F59E0B; }}
    .hero h1 {{
      font-size: clamp(34px, 4vw, 50px);
      font-weight: 800; letter-spacing: -0.03em; line-height: 1.14;
      color: var(--dark);
    }}
    .hero h1 em {{ font-style: normal; color: var(--primary); }}
    .hero-desc {{
      margin-top: 16px; font-size: 16.5px; color: var(--muted);
      max-width: 540px; line-height: 1.6;
    }}
    .hero-actions {{ display: flex; gap: 14px; margin-top: 28px; flex-wrap: wrap; }}
    .trust-row {{
      display: flex; gap: 18px; flex-wrap: wrap; margin-top: 32px;
      padding-top: 24px; border-top: 1px solid var(--line);
      font-size: 12.5px; font-weight: 600; color: var(--muted);
    }}
    .trust-row span {{ display: flex; align-items: center; gap: 6px; }}

    /* HERO IMAGE SHOWCASE */
    .hero-visual {{ position: relative; }}
    .hero-image-wrap {{
      position: relative; border-radius: 24px; overflow: hidden;
      box-shadow: 0 24px 50px -12px rgba(0,0,0,0.25);
      border: 1px solid rgba(255,255,255,0.8);
      background: #000;
    }}
    .hero-img {{
      width: 100%; height: 420px; object-fit: cover; display: block;
      transition: transform .6s ease;
    }}
    .hero-image-wrap:hover .hero-img {{ transform: scale(1.03); }}
    .hero-float {{
      position: absolute; background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px); border-radius: 14px;
      padding: 12px 18px; display: flex; align-items: center; gap: 12px;
      box-shadow: 0 16px 32px -8px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.6);
    }}
    .hero-float--top {{ top: 20px; right: 20px; }}
    .hero-float--bottom {{ bottom: 20px; left: 20px; }}
    .float-star {{ background: #FEF3C7; color: #D97706; font-weight: 800; font-size: 13px; padding: 6px 10px; border-radius: 8px; }}
    .float-dot {{ width: 10px; height: 10px; border-radius: 50%; background: #10B981; box-shadow: 0 0 10px #10B981; }}
    .hero-float b {{ display: block; font-size: 13px; font-weight: 800; color: #0F172A; }}
    .hero-float small {{ font-size: 11px; color: #64748B; }}

    /* INTERACTIVE CONVERSION MODULE */
    .interactive-section {{
      padding: 24px 32px 56px; max-width: 1240px; margin: 0 auto;
    }}
    .interactive-box {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 36px 32px; box-shadow: var(--shadow);
    }}
    .box-head {{ text-align: center; max-width: 680px; margin: 0 auto 28px; }}
    .box-badge {{
      display: inline-block; font-size: 11px; font-weight: 800;
      letter-spacing: 0.1em; text-transform: uppercase;
      color: var(--primary); background: var(--bg); padding: 4px 12px;
      border-radius: 999px; margin-bottom: 8px;
    }}
    .box-head h3 {{ font-size: 24px; font-weight: 800; color: var(--dark); }}
    .box-head p {{ font-size: 14px; color: var(--muted); margin-top: 6px; }}

    /* Booking chips */
    .date-chips {{ display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 16px; }}
    .chip {{
      background: var(--bg); border: 1.5px solid var(--line); border-radius: 12px;
      padding: 10px 18px; text-align: center; cursor: pointer; transition: all .2s;
      font-family: inherit;
    }}
    .chip b {{ display: block; font-size: 13px; color: var(--dark); }}
    .chip span {{ font-size: 11px; color: var(--muted); }}
    .chip.is-active, .chip:hover {{
      background: var(--primary); border-color: var(--primary);
    }}
    .chip.is-active b, .chip.is-active span, .chip:hover b, .chip:hover span {{ color: #fff; }}
    
    .time-chips {{ display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-bottom: 24px; }}
    .time-tag {{
      background: var(--bg); border: 1px solid var(--line); border-radius: 8px;
      padding: 8px 16px; font-size: 13px; font-weight: 700; color: var(--dark);
      cursor: pointer; transition: all .2s; font-family: inherit;
    }}
    .time-tag.is-active, .time-tag:hover {{ background: var(--primary); color: #fff; border-color: var(--primary); }}

    /* Catalog items with photo */
    .catalog-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 900px; margin: 0 auto 24px; }}
    .cat-item {{
      background: var(--bg); border: 1px solid var(--line); border-radius: 12px;
      padding: 16px; display: flex; gap: 16px; align-items: center;
    }}
    .cat-img {{ width: 90px; height: 90px; border-radius: 10px; object-fit: cover; flex-shrink: 0; }}
    .cat-info {{ flex: 1; }}
    .cat-badge {{ font-size: 10.5px; font-weight: 800; color: var(--primary); text-transform: uppercase; }}
    .cat-info h4 {{ font-size: 15.5px; font-weight: 800; color: var(--dark); margin: 2px 0 4px; }}
    .cat-info p {{ font-size: 12.5px; color: var(--muted); line-height: 1.4; }}
    .cat-foot {{ display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }}
    .cat-foot b {{ font-size: 16px; color: var(--dark); font-weight: 800; }}
    .qty-control {{ display: inline-flex; align-items: center; gap: 8px; background: #fff; padding: 4px 10px; border-radius: 999px; border: 1px solid var(--line); }}
    .qty-control button {{ border: none; background: transparent; font-size: 16px; font-weight: 800; cursor: pointer; color: var(--primary); }}
    .qty-control span {{ font-size: 13px; font-weight: 700; width: 16px; text-align: center; }}

    /* Quote calculator */
    .quote-calculator {{ max-width: 640px; margin: 0 auto 24px; display: flex; flex-direction: column; gap: 12px; }}
    .calc-check {{
      display: flex; justify-content: space-between; align-items: center; gap: 12px;
      background: var(--bg); border: 1px solid var(--line); border-radius: 10px;
      padding: 14px 18px; cursor: pointer; font-size: 14px; font-weight: 600;
    }}
    .calc-check input {{ width: 18px; height: 18px; accent-color: var(--primary); }}
    .calc-check span {{ flex: 1; margin-left: 10px; }}
    .calc-check b {{ color: var(--primary); }}
    .quote-subtotal {{
      display: flex; justify-content: space-between; align-items: center;
      padding: 14px 18px; background: #FEF3C7; border-radius: 10px; color: #92400E; font-size: 14px; font-weight: 700;
    }}
    .quote-subtotal b {{ font-size: 18px; color: #B45309; }}

    /* Curriculum */
    .curriculum-list {{ max-width: 800px; margin: 0 auto 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
    .curr-card {{ background: var(--bg); border: 1px solid var(--line); border-radius: 12px; padding: 20px; }}
    .curr-tag {{ font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--primary); }}
    .curr-card h4 {{ font-size: 16px; font-weight: 800; color: var(--dark); margin: 6px 0; }}
    .curr-card p {{ font-size: 13px; color: var(--muted); }}
    .curr-card small {{ display: block; margin-top: 10px; font-size: 11.5px; font-weight: 700; color: var(--dark); }}

    .box-action {{ max-width: 480px; margin: 0 auto; }}

    /* SERVICES SECTION WITH FULL HD IMAGES */
    .services-sec {{ padding: 64px 32px; }}
    .sec-container {{ max-width: 1240px; margin: 0 auto; }}
    .sec-head {{ text-align: center; margin-bottom: 48px; }}
    .sec-head small {{
      display: inline-block; font-size: 11.5px; font-weight: 800;
      letter-spacing: 0.12em; text-transform: uppercase;
      color: var(--primary); margin-bottom: 6px;
    }}
    .sec-head h2 {{ font-size: clamp(28px, 3.2vw, 40px); font-weight: 800; color: var(--dark); letter-spacing: -0.02em; }}
    .sec-head p {{ font-size: 15.5px; color: var(--muted); margin-top: 8px; max-width: 620px; margin-inline: auto; }}

    .services-grid {{
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;
    }}
    .service-card {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      overflow: hidden; display: flex; flex-direction: column;
      transition: transform .3s ease, box-shadow .3s ease, border-color .3s;
    }}
    .service-card:hover {{
      transform: translateY(-6px); box-shadow: var(--shadow);
      border-color: var(--primary);
    }}
    .srv-img-wrap {{ position: relative; height: 190px; overflow: hidden; background: #1E293B; }}
    .srv-img {{
      width: 100%; height: 100%; object-fit: cover; display: block;
      transition: transform .5s ease;
    }}
    .service-card:hover .srv-img {{ transform: scale(1.08); }}
    .srv-badge {{
      position: absolute; top: 12px; left: 12px;
      font-size: 10.5px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase;
      background: rgba(0,0,0,0.65); backdrop-filter: blur(4px); color: #fff;
      padding: 4px 10px; border-radius: 6px;
    }}
    .srv-body {{ padding: 22px 20px; flex: 1; display: flex; flex-direction: column; }}
    .srv-body h4 {{ font-size: 17px; font-weight: 800; color: var(--dark); line-height: 1.3; }}
    .srv-body p {{ font-size: 13.5px; color: var(--muted); margin-top: 8px; line-height: 1.5; flex: 1; }}
    .srv-price {{ margin: 16px 0 14px; padding-top: 14px; border-top: 1px dashed var(--line); }}
    .srv-price small {{ display: block; font-size: 11px; text-transform: uppercase; color: var(--muted); }}
    .srv-price b {{ font-size: 18px; font-weight: 800; color: var(--dark); }}
    .srv-btn {{
      background: var(--bg); color: var(--dark); border: 1px solid var(--line);
      text-decoration: none; font-size: 12.5px; font-weight: 700; padding: 10px 14px;
      border-radius: 8px; text-align: center; transition: all .2s;
    }}
    .srv-btn:hover {{ background: var(--primary); color: #fff; border-color: var(--primary); }}

    /* FULL HD SPACE & RESULTS GALLERY */
    .gallery-sec {{ background: var(--paper); padding: 72px 32px; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }}
    .gallery-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }}
    .gallery-item {{
      position: relative; border-radius: 14px; overflow: hidden; height: 260px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    }}
    .gallery-item img {{
      width: 100%; height: 100%; object-fit: cover; display: block;
      transition: transform .5s ease;
    }}
    .gallery-item:hover img {{ transform: scale(1.08); }}
    .gallery-label {{
      position: absolute; bottom: 0; left: 0; right: 0;
      padding: 24px 14px 12px; background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.85) 100%);
      color: #fff; font-size: 12.5px; font-weight: 700;
    }}

    /* Pillars */
    .pillars-sec {{ padding: 72px 32px; max-width: 1240px; margin: 0 auto; }}
    .pillars-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
    .pillar-card {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 32px 28px; box-shadow: 0 4px 16px rgba(0,0,0,0.02);
    }}
    .pillar-icon {{
      width: 48px; height: 48px; border-radius: 12px;
      background: var(--bg); color: var(--primary); display: grid; place-items: center;
      font-size: 22px; margin-bottom: 18px;
    }}
    .pillar-card h3 {{ font-size: 18px; font-weight: 800; color: var(--dark); margin-bottom: 8px; }}
    .pillar-card p {{ font-size: 14px; color: var(--muted); }}

    /* Testimonials with real photos */
    .testi-sec {{ background: var(--bg); padding: 72px 32px; border-top: 1px solid var(--line); }}
    .testi-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1240px; margin: 0 auto; }}
    .testi-card {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 28px 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }}
    .testi-stars {{ color: #F59E0B; margin-bottom: 12px; font-size: 14px; }}
    .testi-card p {{ font-size: 13.5px; color: var(--text); font-style: italic; line-height: 1.6; }}
    .testi-user {{ display: flex; align-items: center; gap: 12px; margin-top: 20px; }}
    .user-avatar-img {{
      width: 44px; height: 44px; border-radius: 50%; object-fit: cover;
      border: 2px solid var(--primary);
    }}
    .user-info b {{ display: block; font-size: 14px; font-weight: 700; color: var(--dark); }}
    .user-info small {{ font-size: 11.5px; color: var(--muted); }}

    /* FAQ */
    .faq-sec {{ padding: 72px 32px; max-width: 860px; margin: 0 auto; }}
    .faq-item {{
      background: var(--paper); border: 1px solid var(--line); border-radius: 12px;
      margin-bottom: 12px; overflow: hidden;
    }}
    .faq-item summary {{
      padding: 18px 22px; font-size: 15px; font-weight: 700; color: var(--dark);
      cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;
    }}
    .faq-item summary::-webkit-details-marker {{ display: none; }}
    .faq-item summary::after {{ content: "+"; font-size: 18px; color: var(--primary); font-weight: 800; }}
    .faq-item[open] summary::after {{ content: "−"; }}
    .faq-content {{ padding: 0 22px 20px; font-size: 14px; color: var(--muted); line-height: 1.6; }}

    /* Footer */
    .footer {{
      background: var(--dark); color: #94A3B8; padding: 64px 32px 36px; font-size: 13.5px;
    }}
    .footer-inner {{
      max-width: 1240px; margin: 0 auto; display: grid;
      grid-template-columns: 1.5fr 1fr 1fr; gap: 40px; padding-bottom: 40px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}
    .footer h5 {{ color: #fff; font-size: 16px; font-weight: 700; margin-bottom: 14px; }}
    .footer p {{ font-size: 13.5px; color: #94A3B8; line-height: 1.6; }}
    .footer-bottom {{
      max-width: 1240px; margin: 24px auto 0; display: flex;
      justify-content: space-between; align-items: center; font-size: 12px; color: #64748B;
    }}
    .footer-bottom a {{ color: #38BDF8; text-decoration: none; }}

    /* Floating WhatsApp Button */
    .wa-float {{
      position: fixed; right: 24px; bottom: 84px; width: 56px; height: 56px;
      border-radius: 50%; background: #25D366; color: #fff;
      display: grid; place-items: center; text-decoration: none;
      box-shadow: 0 8px 24px rgba(37, 211, 102, 0.4);
      z-index: 90; transition: transform .25s ease;
      animation: pulseWa 2s infinite;
    }}
    .wa-float:hover {{ transform: scale(1.1); }}
    .wa-float svg {{ width: 30px; height: 30px; }}
    @keyframes pulseWa {{
      0% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.5); }}
      70% {{ box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }}
    }}

    /* Mobile Sticky Conversion Bar */
    .mobile-sticky-bar {{
      position: fixed; bottom: 0; left: 0; right: 0;
      background: #0B0F14; border-top: 1px solid rgba(255,255,255,0.1);
      padding: 12px 20px; display: none; justify-content: space-between; align-items: center;
      z-index: 100;
    }}
    .mobile-sticky-bar small {{ display: block; font-size: 11px; color: #94A3B8; }}
    .mobile-sticky-bar b {{ color: #fff; font-size: 14px; font-weight: 700; }}
    .mobile-sticky-btn {{
      background: #25D366; color: #fff; font-size: 12.5px; font-weight: 800;
      padding: 8px 16px; border-radius: 999px; text-decoration: none;
    }}

    @media (max-width: 1024px) {{
      .hero {{ grid-template-columns: 1fr; gap: 36px; padding: 40px 24px; }}
      .hero-img {{ height: 320px; }}
      .services-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .gallery-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .testi-grid, .pillars-grid {{ grid-template-columns: 1fr; }}
      .catalog-grid, .curriculum-list {{ grid-template-columns: 1fr; }}
      .footer-inner {{ grid-template-columns: 1fr; gap: 28px; }}
    }}
    @media (max-width: 640px) {{
      .nav {{ display: none; }}
      .services-grid {{ grid-template-columns: 1fr; }}
      .gallery-grid {{ grid-template-columns: 1fr; }}
      .mobile-sticky-bar {{ display: flex; }}
      .wa-float {{ bottom: 76px; right: 16px; width: 48px; height: 48px; }}
      .wa-float svg {{ width: 24px; height: 24px; }}
    }}
  </style>
</head>
<body>

  <!-- Top Ribbon Nexo Studio -->
  <div class="nexo-bar">
    <div>
      <span>Exemplo de demonstração real desenvolvido por <b>Nexo Studio</b></span>
    </div>
    <div>
      <a href="../../index.html">← Voltar ao Catálogo de +170 Demonstrações</a>
    </div>
  </div>

  <!-- Top Info Bar -->
  <div class="top-info">
    <div>
      <span>📍 Atendimento em <b>Campinas, SP</b> e região metropolitana</span>
    </div>
    <div>
      <span>Horário: <b>Seg a Sex 08h-19h • Sáb 08h-14h</b></span>
    </div>
  </div>

  <!-- Header -->
  <header class="header">
    <a href="#inicio" class="logo">
      <div class="logo-badge">{title[:1]}</div>
      <div class="logo-info">
        <b>{brand}</b>
        <small>{title}</small>
      </div>
    </a>
    <ul class="nav">
      <li><a href="#inicio">Início</a></li>
      <li><a href="#interativo">Agendamento &amp; Orçamento</a></li>
      <li><a href="#servicos">Especialidades</a></li>
      <li><a href="#galeria">Nosso Espaço</a></li>
      <li><a href="#avaliacoes">Depoimentos</a></li>
    </ul>
    <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Vim+pelo+site+da+{brand.replace(' ', '+')}+e+gostaria+de+um+atendimento." target="_blank" class="btn btn-primary">
      <svg viewBox="0 0 24 24" class="btn-icon"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24"/></svg>
      Falar no WhatsApp
    </a>
  </header>

  <main id="inicio">
    <!-- Hero com Imagem Full HD -->
    <section class="hero">
      <div class="hero-copy">
        <div class="rating-pill">
          <span>★★★★★</span> 4.9 no Google · +1.800 atendimentos realizados
        </div>
        <h1>Excelência, confiança e cuidado para <em>{title.lower()}</em>.</h1>
        <p class="hero-desc">{slogan} Atendimento com hora marcada, garantia e facilidade de pagamento em Campinas e região.</p>
        <div class="hero-actions">
          <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+solicitar+um+atendimento+na+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary">
            <svg viewBox="0 0 24 24" class="btn-icon"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24"/></svg>
            Agendar pelo WhatsApp
          </a>
          <a href="#servicos" class="btn btn-outline">Ver Especialidades &amp; Valores</a>
        </div>
        <div class="trust-row">
          <span>✓ Profissionais Certificados</span>
          <span>✓ Garantia &amp; Nota Fiscal</span>
          <span>✓ Parcelamento em até 12x</span>
        </div>
      </div>

      <!-- Hero Visual Showcase -->
      <div class="hero-visual">
        <div class="hero-image-wrap">
          <img src="{hero_img}" alt="{brand} — {title}" class="hero-img" loading="eager" />
          <div class="hero-float hero-float--top">
            <span class="float-star">★ 4.9</span>
            <div>
              <b>Avaliação 5 Estrelas</b>
              <small>+450 reviews no Google</small>
            </div>
          </div>
          <div class="hero-float hero-float--bottom">
            <span class="float-dot"></span>
            <div>
              <b>Atendimento Ativo</b>
              <small>Resposta em menos de 5 min</small>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Módulo Interativo de Alta Conversão -->
    <section class="interactive-section" id="interativo">
      <div class="sec-container">
        {feature_markup}
      </div>
    </section>

    <!-- Especialidades & Serviços com Fotos Full HD -->
    <section class="services-sec" id="servicos">
      <div class="sec-container">
        <div class="sec-head">
          <small>Nossas Soluções</small>
          <h2>Especialidades &amp; Serviços</h2>
          <p>Conheça os procedimentos e soluções desenvolvidos com padrão de excelência, tecnologia e materiais de primeira linha.</p>
        </div>
        <div class="services-grid">
          {services_html}
        </div>
      </div>
    </section>

    <!-- Conheça Nosso Espaço & Resultados com Fotos Full HD -->
    <section class="gallery-sec" id="galeria">
      <div class="sec-container">
        <div class="sec-head">
          <small>Estrutura &amp; Resultados</small>
          <h2>Conheça Nosso Espaço &amp; Atendimento</h2>
          <p>Ambiente climatizado, biossegurança rigorosa e tecnologia de última geração para receber você com conforto.</p>
        </div>
        <div class="gallery-grid">
          <div class="gallery-item">
            <img src="{gal_imgs[0]}" alt="Ambiente e recepção" loading="lazy" />
            <span class="gallery-label">Recepção Acolhedora</span>
          </div>
          <div class="gallery-item">
            <img src="{gal_imgs[1]}" alt="Equipamentos modernos" loading="lazy" />
            <span class="gallery-label">Equipamentos de Ponta</span>
          </div>
          <div class="gallery-item">
            <img src="{gal_imgs[2]}" alt="Procedimentos de precisão" loading="lazy" />
            <span class="gallery-label">Atendimento Especializado</span>
          </div>
          <div class="gallery-item">
            <img src="{gal_imgs[3]}" alt="Resultados de excelência" loading="lazy" />
            <span class="gallery-label">Padrão de Excelência</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Pilares de Confiança -->
    <section class="pillars-sec" id="diferenciais">
      <div class="sec-head">
        <small>Por que nos escolher</small>
        <h2>Diferenciais que Fazem a Diferença</h2>
      </div>
      <div class="pillars-grid">
        <div class="pillar-card">
          <div class="pillar-icon">★</div>
          <h3>Experiência Comprovada</h3>
          <p>Equipe qualificada com anos de atuação no mercado, constante atualização e compromisso com o resultado.</p>
        </div>
        <div class="pillar-card">
          <div class="pillar-icon">⏱</div>
          <h3>Pontualidade &amp; Agilidade</h3>
          <p>Respeito rigoroso ao seu tempo, agendamento organizado e respostas imediatas pelo WhatsApp.</p>
        </div>
        <div class="pillar-card">
          <div class="pillar-icon">🛡</div>
          <h3>Garantia &amp; Segurança</h3>
          <p>Materiais de primeira linha, ambiente higienizado e total clareza em todas as etapas do serviço.</p>
        </div>
      </div>
    </section>

    <!-- Depoimentos com Avatares Reais -->
    <section class="testi-sec" id="avaliacoes">
      <div class="sec-head">
        <small>Depoimentos</small>
        <h2>O que Dizem Nossos Clientes no Google</h2>
      </div>
      <div class="testi-grid">
        <div class="testi-card">
          <div class="testi-stars">★★★★★</div>
          <p>"Atendimento impecável do início ao fim! Fui super bem acolhida e o resultado superou todas as minhas expectativas. Recomendo de olhos fechados!"</p>
          <div class="testi-user">
            <img src="{avatars[0]}" alt="Mariana Costa" class="user-avatar-img" />
            <div class="user-info">
              <b>Mariana Costa</b>
              <small>Cliente Verificada • Google Reviews</small>
            </div>
          </div>
        </div>
        <div class="testi-card">
          <div class="testi-stars">★★★★★</div>
          <p>"Profissionalismo raro de encontrar hoje em dia. Preço transparente, pontualidade britânica e um cuidado que faz toda a diferença."</p>
          <div class="testi-user">
            <img src="{avatars[1]}" alt="Rodrigo Almeida" class="user-avatar-img" />
            <div class="user-info">
              <b>Rodrigo Almeida</b>
              <small>Cliente Verificado • Google Reviews</small>
            </div>
          </div>
        </div>
        <div class="testi-card">
          <div class="testi-stars">★★★★★</div>
          <p>"Ambiente acolhedor, comunicação clara pelo WhatsApp e serviço nota dez. Já sou cliente fiel há mais de um ano!"</p>
          <div class="testi-user">
            <img src="{avatars[2]}" alt="Camila Ferreira" class="user-avatar-img" />
            <div class="user-info">
              <b>Camila Ferreira</b>
              <small>Cliente Verificada • Google Reviews</small>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Accordion -->
    <section class="faq-sec" id="duvidas">
      <div class="sec-head">
        <small>Tire suas dúvidas</small>
        <h2>Perguntas Frequentes</h2>
      </div>
      <details class="faq-item" open>
        <summary>Como funciona o agendamento de horários ou pedidos?</summary>
        <div class="faq-content">
          Você pode clicar em qualquer botão do site para falar diretamente com nossa equipe no WhatsApp. O atendimento é rápido e confirmamos sua solicitação na hora com hora marcada.
        </div>
      </details>
      <details class="faq-item">
        <summary>Quais são as formas de pagamento aceitas?</summary>
        <div class="faq-content">
          Aceitamos Pix com desconto, cartões de crédito em até 12x, débito e transferência bancária com emissão de nota fiscal para todos os serviços.
        </div>
      </details>
      <details class="faq-item">
        <summary>Onde fica o local de atendimento?</summary>
        <div class="faq-content">
          Estamos localizados em região nobre com fácil acesso, estacionamento conveniado e infraestrutura completa para seu conforto em Campinas/SP.
        </div>
      </details>
    </section>
  </main>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-inner">
      <div>
        <h5>{brand}</h5>
        <p>{slogan}</p>
        <p style="margin-top: 12px; font-size: 12px; color: #64748B;">Atendimento em Campinas, SP e cidades vizinhas com suporte via WhatsApp.</p>
      </div>
      <div>
        <h5>Horários de Funcionamento</h5>
        <p>Segunda a Sexta: 08:00 às 19:00</p>
        <p>Sábados: 08:00 às 14:00</p>
        <p>Domingos e Feriados: Fechado</p>
      </div>
      <div>
        <h5>Contato &amp; Localização</h5>
        <p>WhatsApp: <b>(19) 99633-1656</b></p>
        <p>Campinas — SP</p>
        <p style="margin-top: 10px;"><a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+um+atendimento+na+{brand.replace(' ', '+')}." target="_blank" style="color: #38BDF8; font-weight: 700; text-decoration: none;">Chamar no WhatsApp ↗</a></p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 {brand}. Todos os direitos reservados.</span>
      <span>Desenvolvido com excelência por <a href="../../index.html" target="_blank"><b>Nexo Studio</b></a></span>
    </div>
  </footer>

  <!-- WhatsApp Flutuante com Pulso -->
  <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Vim+pelo+site+da+{brand.replace(' ', '+')}+e+gostaria+de+um+atendimento." target="_blank" class="wa-float" title="Falar no WhatsApp">
    <svg viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24"/></svg>
  </a>

  <!-- Mobile Sticky Bar -->
  <div class="mobile-sticky-bar">
    <div>
      <small>Atendimento Rápido</small>
      <b>Fale no WhatsApp</b>
    </div>
    <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Vim+pelo+site+da+{brand.replace(' ', '+')}+e+gostaria+de+um+atendimento." target="_blank" class="mobile-sticky-btn">
      Conversar no WhatsApp ↗
    </a>
  </div>

  <script>
    // Interatividade de Agendamento
    let selectedDate = 'Hoje, 28 Out';
    let selectedTime = '09:00';
    const brandName = '{brand}';

    function selectDate(el, val) {{
      document.querySelectorAll('.date-chips .chip').forEach(c => c.classList.remove('is-active'));
      el.classList.add('is-active');
      selectedDate = val;
      updateBookingLink();
    }}

    function selectTime(el, val) {{
      document.querySelectorAll('.time-chips .time-tag').forEach(c => c.classList.remove('is-active'));
      el.classList.add('is-active');
      selectedTime = val;
      updateBookingLink();
    }}

    function updateBookingLink() {{
      const btn = document.getElementById('btn-booking');
      if (btn) {{
        const msg = encodeURIComponent(`Olá! Gostaria de agendar um horário para ${{selectedDate}} às ${{selectedTime}} na ${{brandName}}.`);
        btn.href = `https://wa.me/5519996331656?text=${{msg}}`;
      }}
    }}

    // Interatividade de Cardápio / Catálogo
    let q1 = 1;
    let q2 = 0;
    function updateQty(id, delta, price) {{
      if (id === 'q1') {{
        q1 = Math.max(0, q1 + delta);
        document.getElementById('q1').innerText = q1;
      }} else {{
        q2 = Math.max(0, q2 + delta);
        document.getElementById('q2').innerText = q2;
      }}
      const total = (q1 * 38) + (q2 * 65);
      const totalEl = document.getElementById('cart-total');
      if (totalEl) totalEl.innerText = `R$ ${{total}},00`;

      const btn = document.getElementById('btn-catalog');
      if (btn) {{
        const msg = encodeURIComponent(`Olá! Gostaria de fazer o pedido na ${{brandName}}: ${{q1}}x Opção Especial e ${{q2}}x Combo Premium. Total: R$ ${{total}},00.`);
        btn.href = `https://wa.me/5519996331656?text=${{msg}}`;
      }}
    }}

    // Interatividade de Orçamento
    function calcQuote() {{
      const checks = document.querySelectorAll('.quote-calculator .chk-item');
      let sum = 0;
      checks.forEach(c => {{
        if (c.checked) sum += parseInt(c.value);
      }});
      const valEl = document.getElementById('quote-val');
      if (valEl) valEl.innerText = `R$ ${{sum}},00`;
      
      const btn = document.getElementById('btn-quote');
      if (btn) {{
        const msg = encodeURIComponent(`Olá! Simulei um orçamento no valor de R$ ${{sum}},00 para {title} na ${{brandName}}.`);
        btn.href = `https://wa.me/5519996331656?text=${{msg}}`;
      }}
    }}
  </script>
</body>
</html>"""

def render_master_hub_html(categories):
    total_niches = sum(len(c["niches"]) for c in categories)

    tabs_html = [
        f'<button class="hub-tab is-active" data-cat="all">Todos <span class="badge">{total_niches}</span></button>'
    ]
    for c in categories:
        count = len(c["niches"])
        tabs_html.append(
            f'<button class="hub-tab" data-cat="{c["id"]}">{c["icon"]} {c["name"]} <span class="badge">{count}</span></button>'
        )
    tabs_str = "\n".join(tabs_html)

    cards_html = []
    for c in categories:
        cat_id = c["id"]
        cat_name = c["name"]
        for n in c["niches"]:
            slug, title, brand, slogan, primary, dark, accent, bg, feat = n
            images = get_niche_images(cat_id, slug)
            hero_thumb = images["hero"]
            feat_label = {
                "booking": "Agendamento Online",
                "catalog": "Cardápio / Pedidos",
                "quote": "Orçamento Rápido",
                "curriculum": "Matrículas Abertas"
            }.get(feat, "Demonstração Ativa")

            search_terms = f"{title.lower()} {brand.lower()} {slogan.lower()} {cat_name.lower()} {slug}".replace('"', '')

            cards_html.append(f"""
            <article class="hub-card" data-cat="{cat_id}" data-search="{search_terms}">
              <div class="hub-card-header" style="background: linear-gradient(180deg, rgba(11,15,21,0.2) 0%, rgba(11,15,21,0.85) 100%), url('{hero_thumb}') center/cover no-repeat;">
                <span class="hub-cat-tag">{cat_name}</span>
                <span class="hub-feat-tag">{feat_label}</span>
              </div>
              <div class="hub-card-body">
                <h3>{brand}</h3>
                <small class="hub-niche-label">{title}</small>
                <p>{slogan}</p>
                <div class="hub-card-foot">
                  <a href="{cat_id}/{slug}/index.html" target="_blank" class="hub-btn-view">Ver Site Ao Vivo ↗</a>
                  <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Tenho+interesse+em+um+site+para+{title.replace(' ', '+')}+como+o+da+{brand.replace(' ', '+')}." target="_blank" class="hub-btn-wa" title="Pedir um site assim no WhatsApp">
                    <svg viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24"/></svg>
                  </a>
                </div>
              </div>
            </article>
            """)

    cards_str = "\n".join(cards_html)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Catálogo de Demonstrações Comerciais Full HD — Nexo Studio</title>
  <meta name="description" content="Explore mais de 170 sites demonstrativos animados com fotografia Full HD para diferentes tipos de comércio e empresas locais." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #0B0F15; color: #F8FAFC;
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    .hub-header {{
      padding: 20px 32px;
      display: flex; justify-content: space-between; align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      background: rgba(11, 15, 21, 0.95);
      position: sticky; top: 0; z-index: 50;
      backdrop-filter: blur(16px);
    }}
    .hub-logo {{
      display: flex; align-items: center; gap: 12px; text-decoration: none; color: #fff;
    }}
    .hub-logo b {{ font-size: 19px; font-weight: 800; letter-spacing: -0.02em; }}
    .hub-logo span {{ color: #38BDF8; }}
    .hub-back-btn {{
      color: #94A3B8; font-size: 13.5px; font-weight: 600; text-decoration: none;
      display: inline-flex; align-items: center; gap: 6px;
      transition: color .2s;
    }}
    .hub-back-btn:hover {{ color: #38BDF8; }}

    .hub-hero {{
      padding: 72px 24px 36px;
      text-align: center; max-width: 900px; margin: 0 auto;
    }}
    .hub-badge {{
      display: inline-flex; align-items: center; gap: 8px;
      padding: 6px 14px; border-radius: 999px;
      background: rgba(37, 99, 235, 0.12); border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38BDF8; font-size: 12px; font-weight: 700;
      letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 20px;
    }}
    .hub-hero h1 {{
      font-size: clamp(34px, 4.4vw, 54px); font-weight: 800; letter-spacing: -0.03em;
      line-height: 1.15;
    }}
    .hub-hero h1 span {{
      background: linear-gradient(135deg, #38BDF8, #60A5FA, #818CF8);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hub-hero p {{
      margin-top: 16px; font-size: 17px; color: #94A3B8; max-width: 680px; margin-inline: auto;
    }}

    /* Search Bar */
    .hub-search-wrap {{
      max-width: 640px; margin: 32px auto 0; position: relative;
    }}
    .hub-search-input {{
      width: 100%; padding: 18px 24px 18px 52px; border-radius: 999px;
      background: #131A24; border: 1px solid rgba(255,255,255,0.12);
      color: #fff; font-size: 15px; font-family: inherit;
      outline: none; transition: border-color .2s, box-shadow .2s;
    }}
    .hub-search-input:focus {{
      border-color: #38BDF8; box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.15);
    }}
    .hub-search-icon {{
      position: absolute; left: 20px; top: 50%; transform: translateY(-50%);
      color: #64748B; width: 20px; height: 20px; pointer-events: none;
    }}

    /* Tabs */
    .hub-tabs-container {{
      max-width: 1320px; margin: 40px auto 0; padding: 0 24px;
    }}
    .hub-tabs {{
      display: flex; gap: 8px; flex-wrap: wrap; justify-content: center;
    }}
    .hub-tab {{
      background: #131A24; border: 1px solid rgba(255,255,255,0.08);
      color: #94A3B8; padding: 9px 16px; border-radius: 999px;
      font-size: 13px; font-weight: 600; cursor: pointer;
      display: inline-flex; align-items: center; gap: 8px;
      transition: all .2s; font-family: inherit;
    }}
    .hub-tab:hover, .hub-tab.is-active {{
      background: #2563EB; color: #fff; border-color: #2563EB;
    }}
    .hub-tab .badge {{
      background: rgba(255,255,255,0.15); padding: 2px 7px; border-radius: 999px;
      font-size: 11px;
    }}

    /* Grid */
    .hub-grid {{
      max-width: 1320px; margin: 48px auto 96px; padding: 0 24px;
      display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
    }}
    .hub-card {{
      background: #111722; border: 1px solid rgba(255,255,255,0.07);
      border-radius: 16px; overflow: hidden;
      display: flex; flex-direction: column;
      transition: transform .3s ease, border-color .3s, box-shadow .3s;
    }}
    .hub-card:hover {{
      transform: translateY(-5px); border-color: rgba(56, 189, 248, 0.4);
      box-shadow: 0 20px 40px -15px rgba(0,0,0,0.5);
    }}
    .hub-card-header {{
      height: 160px; padding: 16px 20px; display: flex;
      justify-content: space-between; align-items: flex-start;
      position: relative;
    }}
    .hub-cat-tag {{
      font-size: 11px; font-weight: 800; letter-spacing: 0.08em;
      text-transform: uppercase; color: #fff; background: rgba(0,0,0,0.65);
      padding: 4px 10px; border-radius: 6px; backdrop-filter: blur(4px);
    }}
    .hub-feat-tag {{
      font-size: 10.5px; font-weight: 800; color: #E2E8F0;
      background: rgba(37, 99, 235, 0.85); padding: 4px 10px; border-radius: 999px;
      backdrop-filter: blur(4px);
    }}
    .hub-card-body {{
      padding: 22px 20px 20px; flex: 1; display: flex; flex-direction: column;
    }}
    .hub-card-body h3 {{ font-size: 18.5px; font-weight: 800; color: #fff; }}
    .hub-niche-label {{ font-size: 12px; color: #38BDF8; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; display: block; }}
    .hub-card-body p {{ font-size: 13.5px; color: #94A3B8; line-height: 1.5; flex: 1; }}

    .hub-card-foot {{
      margin-top: 20px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.08);
      display: flex; gap: 10px; align-items: center;
    }}
    .hub-btn-view {{
      flex: 1; background: #1E293B; color: #fff; text-decoration: none;
      font-size: 12.5px; font-weight: 700; padding: 11px 16px; border-radius: 8px;
      text-align: center; transition: background .2s;
    }}
    .hub-btn-view:hover {{ background: #2563EB; }}
    .hub-btn-wa {{
      width: 42px; height: 42px; border-radius: 8px; background: #25D366;
      color: #fff; display: grid; place-items: center; text-decoration: none;
      transition: filter .2s;
    }}
    .hub-btn-wa:hover {{ filter: brightness(1.1); }}
    .hub-btn-wa svg {{ width: 22px; height: 22px; }}

    .hub-no-results {{
      grid-column: 1 / -1; text-align: center; padding: 60px 20px; color: #64748B;
      font-size: 16px; display: none;
    }}

    @media (max-width: 768px) {{
      .hub-grid {{ grid-template-columns: 1fr; }}
      .hub-header {{ padding: 16px 20px; }}
    }}
  </style>
</head>
<body>
  <header class="hub-header">
    <a href="../index.html" class="hub-logo">
      <b>NEXO<span>STUDIO</span></b>
    </a>
    <a href="../index.html" class="hub-back-btn">← Voltar ao Site Principal</a>
  </header>

  <main>
    <section class="hub-hero">
      <div class="hub-badge">Galeria Comercial Full HD · 179 Demonstrações</div>
      <h1>Modelos de Alta Conversão para <span>Todos os Tipos de Negócio</span></h1>
      <p>Explore sites demonstrativos completos desenvolvidos com fotografia Full HD, agendamento interativo, cardápio digital e integração direta ao WhatsApp.</p>
      
      <div class="hub-search-wrap">
        <svg class="hub-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text" id="hub-search" class="hub-search-input" placeholder="Buscar por nicho, serviço ou comércio (ex.: odontologia, pizzaria, mecânica, pet shop)..." />
      </div>
    </section>

    <div class="hub-tabs-container">
      <div class="hub-tabs">
        {tabs_str}
      </div>
    </div>

    <section class="hub-grid" id="hub-grid">
      {cards_str}
      <div class="hub-no-results" id="no-results">
        Nenhum modelo encontrado para este termo. Tente buscar por outro serviço ou categoria!
      </div>
    </section>
  </main>

  <script>
    const searchInput = document.getElementById('hub-search');
    const tabs = document.querySelectorAll('.hub-tab');
    const cards = document.querySelectorAll('.hub-card');
    const noResults = document.getElementById('no-results');

    let currentCat = 'all';

    function filterGrid() {{
      const query = searchInput.value.toLowerCase().trim();
      let visible = 0;

      cards.forEach(card => {{
        const cat = card.getAttribute('data-cat');
        const searchData = card.getAttribute('data-search');
        
        const matchesCat = (currentCat === 'all' || cat === currentCat);
        const matchesQuery = (!query || searchData.includes(query));

        if (matchesCat && matchesQuery) {{
          card.style.display = 'flex';
          visible++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      noResults.style.display = visible === 0 ? 'block' : 'none';
    }}

    tabs.forEach(tab => {{
      tab.addEventListener('click', () => {{
        tabs.forEach(t => t.classList.remove('is-active'));
        tab.classList.add('is-active');
        currentCat = tab.getAttribute('data-cat');
        filterGrid();
      }});
    }});

    searchInput.addEventListener('input', filterGrid);
  </script>
</body>
</html>"""

def build_all():
    print("Iniciando gerador de cases do Nexo Studio com fotografia Full HD...")
    base_dir = r"c:\Projetos\nexo\cases"
    os.makedirs(base_dir, exist_ok=True)
    
    generated_count = 0
    for cat in CATEGORIES:
        cat_id = cat["id"]
        for niche in cat["niches"]:
            slug = niche[0]
            niche_dir = os.path.join(base_dir, cat_id, slug)
            os.makedirs(niche_dir, exist_ok=True)
            
            html_content = render_case_html(cat, niche)
            file_path = os.path.join(niche_dir, "index.html")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            
            generated_count += 1

    # Gerar Master Hub
    hub_html = render_master_hub_html(CATEGORIES)
    hub_file = os.path.join(base_dir, "index.html")
    with open(hub_file, "w", encoding="utf-8") as f:
        f.write(hub_html)

    print(f"Sucesso! {generated_count} sites Full HD gerados com sucesso!")
    print(f"Master Showcase Hub gerado em: {hub_file}")

if __name__ == "__main__":
    build_all()
