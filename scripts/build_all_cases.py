# -*- coding: utf-8 -*-
"""
Script mestre para gerar os 179 sites demonstrativos do Nexo Studio
cobrindo todos os nichos de comércio local divididos em 14 categorias.
"""
import os
import json

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
        "desc": "Advocacia, contabilidade, imobiliárias, seguros e consultorias",
        "niches": [
            ("escritorio-advocacia", "Escritório de Advocacia", "Moraes & Albuquerque Advogados", "Atuação estratégica e ética em Direito Civil, Trabalhista, Previdenciário e Empresarial.", "#1E3A8A", "#0F172A", "#60A5FA", "#F8FAFC", "quote"),
            ("escritorio-contabilidade", "Escritório de Contabilidade", "Nexus Gestão Contábil & Fiscal", "Abertura de empresas, assessoria tributária inteligente e folha de pagamento sem complicação.", "#0369A1", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("imobiliaria", "Imobiliária", "Vanguard Imóveis Premium", "Venda e locação de imóveis residenciais e comerciais nos melhores bairros da cidade.", "#047857", "#064E3B", "#10B981", "#ECFDF5", "catalog"),
            ("corretor-imoveis", "Corretor de Imóveis", "Carlos Eduardo Corretor Exclusivo", "Assessoria imobiliária personalizada para você encontrar o imóvel dos seus sonhos.", "#B45309", "#1F1206", "#F59E0B", "#FFFBEB", "quote"),
            ("corretora-seguros", "Corretora de Seguros", "Garantia Forte Seguros", "Seguro auto, residencial, de vida e empresarial com a melhor cobertura e suporte 24h.", "#1D4ED8", "#0F172A", "#3B82F6", "#EFF6FF", "quote"),
            ("escritorio-arquitetura", "Escritório de Arquitetura", "Studio Vértice Arquitetura", "Projetos arquitetônicos residenciais e comerciais com design contemporâneo e funcional.", "#334155", "#0F172A", "#94A3B8", "#F8FAFC", "quote"),
            ("escritorio-engenharia", "Escritório de Engenharia", "Eixo Engenharia & Estruturas", "Cálculo estrutural, laudos periciais, aprovação de projetos e acompanhamento de obras.", "#0369A1", "#082F49", "#0EA5E9", "#F0F9FF", "quote"),
            ("consultoria-financeira", "Consultoria Financeira", "Apex Consultoria Empresarial", "Planejamento financeiro corporativo, redução de custos e valuation para pequenas e médias empresas.", "#0F766E", "#134E4A", "#14B8A6", "#F0FDFA", "quote"),
            ("despachante", "Despachante", "Ágil Despachante Documentalista", "Licenciamento, transferência de veículos, regularização de CNH e certidões expressas.", "#C2410C", "#431407", "#FB923C", "#FFF7ED", "quote"),
            ("assessoria-investimentos", "Assessoria de Investimentos", "Capital Alpha Wealth", "Estratégias de alocação de patrimônio e investimentos com assessores certificados.", "#1E3A8A", "#0F172A", "#3B82F6", "#EFF6FF", "quote"),
            ("empresa-topografia", "Empresa de Topografia", "GeoMedir Engenharia & Topografia", "Levantamento topográfico planialtimétrico, georreferenciamento de imóveis e drones.", "#047857", "#064E3B", "#10B981", "#ECFDF5", "quote"),
            ("perito-avaliador-imoveis", "Perito Avaliador de Imóveis", "AvaliaTech Perícias Judiciais", "Laudos técnicos de avaliação imobiliária de acordo com as normas da ABNT para processos e vendas.", "#4338CA", "#1E1B4B", "#6366F1", "#EEF2FF", "quote"),
            ("tradutor-juramentado", "Tradutor Juramentado", "Língua Franca Traduções", "Traduções juramentadas oficiais de documentos para imigração, estudos e negócios internacionais.", "#0F766E", "#134E4A", "#2DD4BF", "#F0FDFA", "quote")
        ]
    },
    {
        "id": "casa-reforma",
        "name": "Casa e Reforma",
        "icon": "🔨",
        "desc": "Marcenaria, vidraçaria, eletricistas, construtoras e reparos residenciais",
        "niches": [
            ("marcenaria", "Marcenaria", "Madeira Nobre Marcenaria Fina", "Móveis planejados sob medida com ferragens italianas e acabamento impecável.", "#B45309", "#2E1503", "#D97706", "#FFFBEB", "quote"),
            ("marmoraria", "Marmoraria", "Pedras Raras Granitos & Quartzos", "Bancadas de cozinha, lavatórios e pisos em mármores nacionais e importados.", "#475569", "#0F172A", "#94A3B8", "#F8FAFC", "quote"),
            ("vidracaria", "Vidraçaria", "Cristal Glass Vidros & Box", "Box para banheiro, espelhos lapidados, guarda-corpos e fechamentos de sacada.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("serralheria", "Serralheria", "Ferro & Arte Serralheria", "Portões de ferro, corrimãos, grades de proteção e estruturas metálicas duráveis.", "#334155", "#0F172A", "#64748B", "#F1F5F9", "quote"),
            ("eletricista", "Eletricista", "Volts Express Serviços Elétricos", "Instalação de quadros elétricos, tomadas, iluminação LED e laudos de segurança residencial.", "#D97706", "#1E1B4B", "#F59E0B", "#FFFBEB", "quote"),
            ("desentupidora", "Desentupidora 24h", "HidroDesentope Emergência 24h", "Atendimento rápido sem quebrar pisos em pias, ralos, vasos e esgotos residenciais.", "#0369A1", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("pintura-predial", "Pintura Predial", "Cores & Fachadas Pintura Técnica", "Restauração de fachadas prediais, pintura residencial e aplicação de textura projetada.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "quote"),
            ("gesso-drywall", "Gesso e Drywall", "Plena Drywall & Forros Acústicos", "Rebaixamento de teto com sancas iluminadas, paredes em drywall e isolamento acústico.", "#475569", "#1E293B", "#94A3B8", "#F8FAFC", "quote"),
            ("paisagismo", "Paisagismo", "Flora & Arte Paisagismo", "Criação e implantação de projetos paisagísticos para jardins residenciais e corporativos.", "#15803D", "#052E16", "#22C55E", "#F0FDF4", "quote"),
            ("jardinagem", "Jardinagem", "Verde Limpo Cuidados de Jardim", "Corte de grama, podas de árvores, adubação e controle de ervas daninhas para seu quintal.", "#16A34A", "#052E16", "#4ADE80", "#F0FDF4", "quote"),
            ("dedetizadora", "Dedetizadora", "PragaZero Controle de Pragas", "Eliminação segura de baratas, cupins, formigas e roedores com produtos sem cheiro.", "#B91C1C", "#1C0A0A", "#EF4444", "#FEF2F2", "quote"),
            ("ar-condicionado", "Ar Condicionado", "ClimaTech Refrigeração", "Instalação, higienização completa e manutenção preventiva de ar condicionado split e inverter.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("energia-solar", "Energia Solar", "Solarium Energia Fotovoltaica", "Reduza até 95% da sua conta de luz com placas solares de última geração e homologação rápida.", "#EA580C", "#1C0D05", "#F97316", "#FFF7ED", "quote"),
            ("moveis-planejados", "Móveis Planejados", "Forma & Espaço Ambientes Planejados", "Cozinhas, dormitórios e salas planejadas com projeto 3D gratuito e 5 anos de garantia.", "#B45309", "#291804", "#F59E0B", "#FFFBEB", "quote"),
            ("esquadrias-aluminio", "Esquadrias de Alumínio", "AluminiTech Esquadrias", "Portas balcão, janelas acústicas e persianas integradas com vedação perfeita.", "#334155", "#0F172A", "#64748B", "#F8FAFC", "quote"),
            ("construtora", "Construtora", "Aliança Construções & Obras", "Construção de casas de alto padrão do projeto à entrega da chave sem atrasos.", "#B45309", "#1F1206", "#D97706", "#FFFBEB", "quote"),
            ("empreiteira", "Empreiteira de Reformas", "Master Reformas Residenciais", "Equipe completa de pedreiros, encanadores e pintores para reformar sua casa sem estresse.", "#D97706", "#1E293B", "#F59E0B", "#FFFBEB", "quote"),
            ("piscinas", "Piscinas", "AquaLazer Piscinas & Decks", "Construção de piscinas de alvenaria e vinil, aquecimento solar e decks de madeira.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("impermeabilizacao", "Impermeabilização", "DryTech Impermeabilizações", "Proteção definitiva contra infiltrações e umidade em lajes, piscinas e baldrames.", "#0F766E", "#134E4A", "#14B8A6", "#F0FDFA", "quote"),
            ("calhas-telhados", "Calhas e Telhados", "TelhaForte Coberturas & Calhas", "Fabricação própria de calhas sem emenda, rufos e reforma completa de telhados.", "#C2410C", "#431407", "#FB923C", "#FFF7ED", "quote"),
            ("portoes-automaticos", "Portões Automáticos", "Automatiza Motores & Portões", "Instalação e conserto de motores rápidos para portões deslizantes e basculantes.", "#1D4ED8", "#0F172A", "#3B82F6", "#EFF6FF", "quote"),
            ("seguranca-eletronica", "Segurança Eletrônica", "Sentinela Alarmes & Câmeras", "Monitoramento 24h, alarmes com sensor de presença e visualização pelo celular.", "#B91C1C", "#0F172A", "#EF4444", "#FEF2F2", "quote"),
            ("chaveiro", "Chaveiro 24 Horas", "Chaveiro Central 24h", "Aberturas residenciais e automotivas, confecção de chaves codificadas e cópias na hora.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "quote"),
            ("decoracao-interiores", "Decoração de Interiores", "Harmonie Ambientes & Design", "Consultoria de decoração, escolha de paleta de cores, cortinas e iluminação personalizada.", "#BE185D", "#4C0519", "#F43F5E", "#FFF1F2", "quote")
        ]
    },
    {
        "id": "automotivo",
        "name": "Automotivo",
        "icon": "🚗",
        "desc": "Oficinas mecânicas, estética automotiva, funilaria e serviços de veículos",
        "niches": [
            ("oficina-mecanica", "Oficina Mecânica", "AutoCentro Precision Mecânica", "Revisão preventiva, injeção eletrônica, suspensão e freios com scanner automotivo de precisão.", "#DC2626", "#18181B", "#EF4444", "#18181B", "quote"),
            ("auto-eletrica", "Auto Elétrica", "EletroCar Baterias & Elétrica", "Diagnóstico elétrico, troca de bateria com socorro rápido e reparo em motor de arranque e alternador.", "#D97706", "#1E293B", "#F59E0B", "#FFFBEB", "quote"),
            ("funilaria-pintura", "Funilaria e Pintura", "ColorTech Martelinho de Ouro", "Recuperação de amassados sem danificar a pintura original e pintura em cabine pressurizada.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "quote"),
            ("estetica-automotiva", "Estética Automotiva", "Veloce Detail Studio", "Vitrificação de pintura, polimento técnico, higienização interna e proteção cerâmica de alto nível.", "#E11D48", "#09090B", "#FB7185", "#09090B", "booking"),
            ("lava-rapido", "Lava Rápido", "Brilho Car Estética Express", "Lavagem detalhada, aplicação de cera protetora e aspiração completa sem fila com agendamento.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "booking"),
            ("borracharia", "Borracharia", "PneuFácil Borracharia & Socorro", "Conserto de pneus, alinhamento, balanceamento e venda de pneus novos e seminovos.", "#EA580C", "#1C1917", "#F97316", "#FFF7ED", "quote"),
            ("auto-pecas", "Auto Peças", "Peça Certa Distribuidora", "Peças originais e de reposição para veículos nacionais e importados com entrega rápida.", "#1D4ED8", "#0F172A", "#60A5FA", "#EFF6FF", "catalog"),
            ("som-automotivo", "Som Automotivo", "BassAudio Som & Acessórios", "Centrais multimídia com Apple CarPlay, caixas de som sob medida e alarmes automotivos.", "#7C3AED", "#18181B", "#A78BFA", "#18181B", "catalog"),
            ("insulfilm-peliculas", "Insulfilm e Películas", "FilmTech Películas Térmicas", "Películas de alta redução térmica com nanocerâmica, privacidade e proteção UV com garantia.", "#334155", "#0F172A", "#64748B", "#F8FAFC", "quote"),
            ("vidros-automotivos", "Vidros Automotivos", "Parabrisa Express Troca Rápida", "Substituição e reparo de parabrisas trincados, palhetas e vidros laterais homologados.", "#0369A1", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("despachante-veicular", "Despachante Veicular", "Rápido Car Despachante Detran", "Transferência rápida de veículo, primeiro emplacamento e parcelamento de débitos em até 12x.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "quote"),
            ("autoescola", "Autoescola", "CFC Piloto Centro de Condutores", "Habilitação categoria A e B com frota nova de carros com ar-condicionado e instrutores pacientes.", "#D97706", "#1E1B4B", "#F59E0B", "#FFFBEB", "curriculum"),
            ("locadora-veiculos", "Locadora de Veículos", "DriveWay Aluguel de Carros", "Locação de carros econômicos e executivos para viagens, negócios e motoristas de aplicativo.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "booking"),
            ("guincho", "Guincho 24 Horas", "SOS Estrada Auto Socorro 24h", "Guincho plataforma para carros e motos com resposta ágil em toda a região a qualquer hora.", "#DC2626", "#1C0A0A", "#EF4444", "#FEF2F2", "quote"),
            ("moto-pecas-oficina", "Moto Peças e Oficina", "Rota Duas Rodas Moto Center", "Revisão de motos, troca de óleo, pneus e escapamentos para motociclistas exigentes.", "#EA580C", "#18181B", "#F97316", "#18181B", "quote")
        ]
    },
    {
        "id": "pets",
        "name": "Pets",
        "icon": "🐾",
        "desc": "Pet shops, banho e tosa, clínicas veterinárias e hospedagem animal",
        "niches": [
            ("pet-shop", "Pet Shop", "Mundo Pet Rações & Mimos", "Rações premium, brinquedos, roupinhas e petiscos selecionados para cães e gatos.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "catalog"),
            ("banho-tosa", "Banho e Tosa", "Groomer Pet Spa & Estética Animal", "Banho com água morna, tosa na tesoura, hidratação e transporte com leva e traz com ar-condicionado.", "#D97706", "#291804", "#F59E0B", "#FFFBEB", "booking"),
            ("clinica-veterinaria", "Clínica Veterinária", "Vida Animal Hospital Veterinário", "Consultas, vacinas importadas, cirurgias e atendimento de emergência com carinho.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "booking"),
            ("hotel-cachorro", "Hotel para Cachorro", "Villa Pet Resort & Hospedagem", "Hospedagem com quartos climatizados, gramado amplo para correr e monitoramento por câmeras para os tutores.", "#7C3AED", "#241042", "#A78BFA", "#FAF5FF", "booking"),
            ("adestrador-caes", "Adestrador de Cães", "Cão Obediente Treinamento Canino", "Adestramento positivo para resolver ansiedade, puxões na coleira e xixi fora do lugar.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "booking"),
            ("creche-cachorro", "Creche para Cachorro", "Patas & Cia Daycare Canino", "Socialização, piscina de bolinhas, recreação e gasto de energia para o seu cachorro não ficar sozinho.", "#16A34A", "#052E16", "#22C55E", "#F0FDF4", "booking")
        ]
    },
    {
        "id": "educacao",
        "name": "Educação",
        "icon": "🎓",
        "desc": "Escolas de idiomas, infantil, música, gastronomia e profissionalizantes",
        "niches": [
            ("escola-idiomas", "Escola de Idiomas", "Global Speak Idiomas & Cultura", "Inglês e espanhol fluentes com metodologia prática e conversação ativa desde a primeira aula.", "#1D4ED8", "#0F172A", "#38BDF8", "#EFF6FF", "curriculum"),
            ("escola-infantil", "Escola Infantil", "Pequenos Passos Educação Infantil", "Educação afetiva, bilinguismo, psicomotricidade e nutrição balanceada para crianças de 0 a 5 anos.", "#EA580C", "#291804", "#F97316", "#FFF7ED", "curriculum"),
            ("reforco-escolar", "Reforço Escolar", "Aprender Mais Apoio Pedagógico", "Aulas de reforço em matemática, português e ciências com planos de estudo individualizados.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "curriculum"),
            ("escola-musica", "Escola de Música", "Harmonia Instituto Musical", "Aulas de piano, violão, bateria e canto para todas as idades com apresentações semestrais.", "#B45309", "#1F1206", "#D97706", "#FFFBEB", "curriculum"),
            ("aulas-violao", "Aulas de Violão", "Cordas & Acordes Estúdio", "Toque suas músicas favoritas no violão e na guitarra em poucas semanas com método sem enrolação.", "#D97706", "#1E1208", "#F59E0B", "#FDF8F2", "curriculum"),
            ("escola-informatica", "Escola de Informática", "TecnoFuturo Cursos Digitais", "Cursos práticos de Pacote Office, design gráfico, programação e informática para a terceira idade.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "curriculum"),
            ("curso-profissionalizante", "Curso Profissionalizante", "Qualifica Brasil Carreiras", "Cursos rápidos com certificado para o mercado de trabalho: auxiliar administrativo, farmácia e estética.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "curriculum"),
            ("escola-gastronomia", "Escola de Gastronomia", "Chef Gourmet Escola de Culinária", "Workshops de confeitaria, panificação artesanal e técnicas clássicas de cozinha com chefs profissionais.", "#991B1B", "#1C0505", "#DC2626", "#FEF2F2", "curriculum"),
            ("aulas-canto", "Aulas de Canto", "Voz em Pauta Academia Vocal", "Desenvolva sua voz, respiração e afinação com acompanhamento fonoaudiológico e gravações em estúdio.", "#7C3AED", "#1E1238", "#A78BFA", "#FAF5FF", "curriculum"),
            ("robotica-criancas", "Robótica para Crianças", "RoboMaker Tech Kids", "Programação, robótica e pensamento lógico com Lego e circuitos para crianças e adolescentes.", "#0284C7", "#0B1A28", "#38BDF8", "#F0F9FF", "curriculum")
        ]
    },
    {
        "id": "comercio-local",
        "name": "Comércio Local",
        "icon": "🛍️",
        "desc": "Lojas de roupas, calçados, joias, presentes, tintas e decoração",
        "niches": [
            ("loja-roupas", "Loja de Roupas", "Estilo Urbano Moda Masculina & Feminina", "Looks versáteis, roupas confortáveis de alta qualidade e as maiores tendências da estação.", "#1E293B", "#0F172A", "#64748B", "#F8FAFC", "catalog"),
            ("boutique", "Boutique", "Atelier D'Or Boutique Conceito", "Peças de alfaiataria fina, vestidos sofisticados e curadoria exclusiva de moda feminina.", "#BE185D", "#3B0718", "#FB7185", "#FFF1F2", "catalog"),
            ("loja-calcados", "Loja de Calçados", "Passo Nobre Calçados & Bolsas", "Sapatos confortáveis em couro legítimo, tênis casuais e bolsas elegantes.", "#B45309", "#2E1503", "#D97706", "#FFFBEB", "catalog"),
            ("joalheria", "Joalheria", "Aura Joias & Alianças Finas", "Alianças de casamento em ouro 18k, anéis solitários e joias eternas para marcar momentos.", "#CA8A04", "#1E1805", "#EAB308", "#FEFCE8", "catalog"),
            ("relojoaria", "Relojoaria", "Chronos Relojoaria & Ótica", "Relógios de pulso das melhores marcas internacionais e manutenção técnica com peças originais.", "#334155", "#0F172A", "#64748B", "#F8FAFC", "catalog"),
            ("loja-moveis", "Loja de Móveis", "Casarão Móveis & Ambientes", "Sofás confortáveis, mesas de jantar de madeira maciça e móveis para transformar seu lar.", "#B45309", "#291804", "#D97706", "#FFFBEB", "catalog"),
            ("loja-colchoes", "Loja de Colchões", "Sono Perfeito Colchões & Sommiers", "Colchões de molas ensacadas, espuma ortopédica e travesseiros com suporte postural anatômico.", "#1D4ED8", "#0F172A", "#3B82F6", "#EFF6FF", "catalog"),
            ("papelaria", "Papelaria", "Ponto de Tinta Papelaria Criativa", "Cadernos inteligentes, canetas importadas, materiais escolares e presentes fofos para o dia a dia.", "#EC4899", "#500724", "#F472B6", "#FDF2F8", "catalog"),
            ("floricultura", "Floricultura", "Florescer Arranjos & Buquês", "Buquês de rosas frescas, orquídeas para presente e arranjos florais para datas especiais.", "#15803D", "#052E16", "#22C55E", "#F0FDF4", "catalog"),
            ("loja-presentes", "Loja de Presentes", "Encanto & Mimos Presentes", "Presentes criativos, canecas personalizadas, porta-retratos e kits temáticos para encantar.", "#D97706", "#2E1503", "#F59E0B", "#FFFBEB", "catalog"),
            ("loja-cosmeticos", "Loja de Cosméticos", "Bella Donna Cosméticos & Make", "Maquiagens, produtos para skincare, tônicos e linhas de tratamento capilar profissionais.", "#DB2777", "#4C0519", "#F472B6", "#FDF2F8", "catalog"),
            ("perfumaria", "Perfumaria", "Essence Privée Perfumaria Fina", "Perfumes importados originais das marcas mais cobiçadas com fixação duradoura garantida.", "#7E22CE", "#1E0B30", "#A855F7", "#FAF5FF", "catalog"),
            ("loja-tecidos", "Loja de Tecidos", "Trama & Fio Tecidos Exclusivos", "Linho, sedas, tricolines 100% algodão e tecidos para decoração e vestuário sob medida.", "#B45309", "#271202", "#D97706", "#FFFBEB", "catalog"),
            ("armarinho", "Armarinho", "Ponto & Nó Armarinho Completo", "Linhas de crochê, lãs, botões, rendas e aviamentos para quem ama costura e artesanato.", "#EA580C", "#291804", "#F97316", "#FFF7ED", "catalog"),
            ("loja-brinquedos", "Loja de Brinquedos", "BrinqLúdica Brinquedos & Jogos", "Brinquedos educativos de madeira, quebra-cabeças e jogos de tabuleiro para a família toda.", "#0284C7", "#0C4A6E", "#38BDF8", "#F0F9FF", "catalog"),
            ("loja-materiais-construcao", "Materiais de Construção", "Obra Forte Materiais Básicos ao Acabamento", "Cimento, argamassa, tubos, conexões e materiais de acabamento com entrega expressa na obra.", "#C2410C", "#431407", "#FB923C", "#FFF7ED", "catalog"),
            ("loja-tintas", "Loja de Tintas", "Mundo das Cores Tintas", "Tinta acrílica, esmaltes sintéticos, vernizes e sistema tintométrico computadorizado na hora.", "#2563EB", "#0F172A", "#60A5FA", "#F8FAFC", "catalog"),
            ("loja-iluminacao", "Loja de Iluminação", "Lúmen Lustres & Iluminação Técnica", "Perfis de LED, pendentes modernos, trilhos e lâmpadas econômicas para valorizar qualquer ambiente.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "catalog"),
            ("loja-produtos-naturais", "Loja de Produtos Naturais", "Origem da Terra Cereais & Chás", "Alimentos a granel, temperos sem sódio, colágeno hidrolisado e suplementos limpos.", "#15803D", "#052E16", "#4ADE80", "#F0FDF4", "catalog"),
            ("tabacaria", "Tabacaria", "Imperium Tabacaria & Charutos", "Charutos cubanos conservados em umidor de cedro, cachimbos e presentes finos para apreciadores.", "#78350F", "#1E0D03", "#B45309", "#FEF3C7", "catalog")
        ]
    },
    {
        "id": "eventos-festas",
        "name": "Eventos e Festas",
        "icon": "🎉",
        "desc": "Buffets, fotógrafos, espaços para festas, DJs e cerimonialistas",
        "niches": [
            ("buffet-festas", "Buffet de Festas", "Celebrar Gastronomia & Festas", "Cardápio farto com salgados assados, empratados quentes, doces e serviço impecável de garçons.", "#B45309", "#291804", "#D97706", "#FFFBEB", "quote"),
            ("espaco-eventos", "Espaço para Eventos", "Mansão das Palmeiras Eventos", "Salão climatizado com área verde, iluminação paisagística e infraestrutura para até 350 convidados.", "#047857", "#064E3B", "#10B981", "#ECFDF5", "booking"),
            ("fotografo", "Fotógrafo", "Luz & Alma Fotografia de Emoções", "Ensaios de família, casamentos e aniversários registrados com emoção autêntica e luz natural.", "#1E293B", "#0F172A", "#64748B", "#F8FAFC", "booking"),
            ("produtora-video", "Produtora de Vídeo", "CineVision Filmes & Coberturas", "Filmes cinematográficos com câmeras 4K e drones para casamentos e vídeos institucionais.", "#DC2626", "#141414", "#EF4444", "#141414", "quote"),
            ("decoracao-festas", "Decoração de Festas", "Festa dos Sonhos Cenografia", "Mesas cenográficas temáticas, arcos orgânicos de balões e flores naturais personalizadas.", "#DB2777", "#4C0519", "#F472B6", "#FDF2F8", "quote"),
            ("aluguel-brinquedos-festas", "Aluguel de Brinquedos", "Pula-Pula Alegria Brinquedos & Pipoca", "Cama elástica, tobogã inflável, piscina de bolinhas higienizada e monitores atenciosos.", "#EA580C", "#291804", "#F97316", "#FFF7ED", "quote"),
            ("cerimonialista", "Cerimonialista", "Elegance Cerimonial & Eventos", "Organização do cronograma, assessoria completa aos noivos e tranquilidade total no grande dia.", "#C026D3", "#4A044E", "#E879F9", "#FDF4FF", "booking"),
            ("doces-festas", "Doces para Festas", "Confeitaria D’Arte Doces Finos", "Doces finos, bem-casados macios e bolos com acabamento impecável em pasta e ganache.", "#BE185D", "#3B0718", "#FB7185", "#FFF1F2", "catalog"),
            ("aluguel-mesas-cadeiras", "Aluguel de Mesas e Cadeiras", "Festa Pronta Locações", "Mesas redondas, cadeiras Tiffany, toalhas adamascadas e tendas resistentes para eventos.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("dj-festas", "DJ para Festas", "DJ Rodrigo Live Som & Luz", "Pista de dança animada com os melhores hits, iluminação moving head e estrutura de som profissional.", "#7C3AED", "#18181B", "#A78BFA", "#18181B", "booking"),
            ("banda-eventos", "Banda para Eventos", "SoulPop Banda Show ao Vivo", "Música ao vivo de alta energia com repertório de pop, rock, sertanejo e MPB para animar a noite.", "#D97706", "#1E1208", "#F59E0B", "#FDF8F2", "booking")
        ]
    },
    {
        "id": "turismo-hospedagem",
        "name": "Turismo e Hospedagem",
        "icon": "🌴",
        "desc": "Pousadas, hotéis, agências de turismo e casas de temporada",
        "niches": [
            ("pousada", "Pousada", "Pousada Vila da Serra Refúgio", "Chalés aconchegantes com banheira de hidromassagem, lareira e café da manhã colonial incluso.", "#047857", "#064E3B", "#10B981", "#ECFDF5", "booking"),
            ("hotel", "Hotel", "Grand Palace Hotel & Suítes", "Hospedagem executiva no centro financeiro, suítes com cama king size, piscina e sala de reuniões.", "#1E3A8A", "#0F172A", "#3B82F6", "#EFF6FF", "booking"),
            ("hostel", "Hostel", "Mochileiros Roots Hostel & Bar", "Quartos compartilhados e privativos limpos, cozinha compartilhada, cervejas locais e boa conversa.", "#D97706", "#291804", "#F59E0B", "#FFFBEB", "booking"),
            ("agencia-turismo", "Agência de Turismo", "Passaporte Aberto Viagens", "Pacotes turísticos completos com passagens aéreas, passeios e suporte integral durante a viagem.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "catalog"),
            ("casa-temporada", "Casa de Temporada", "Casa do Mar Refúgio de Praia", "Casa beira-mar com 4 suítes, piscina privativa, churrasqueira e a 50 metros da areia.", "#0D9488", "#112D29", "#14B8A6", "#F0FDFA", "booking"),
            ("chacara-eventos", "Chácara para Eventos", "Recanto dos Ipês Chácara", "Área de lazer com piscina semiolímpica, campo de futebol, salão de jogos e churrasqueira para finais de semana.", "#15803D", "#052E16", "#22C55E", "#F0FDF4", "booking")
        ]
    },
    {
        "id": "tecnologia-assistencia",
        "name": "Tecnologia e Assistência",
        "icon": "💻",
        "desc": "Assistências de celulares, computadores, consoles, gráficas e câmeras",
        "niches": [
            ("assistencia-celular", "Assistência de Celular", "iFix Smartphone Express", "Troca de tela na hora, troca de bateria com garantia de 6 meses e reparos em placas iPhone e Android.", "#2563EB", "#0F172A", "#38BDF8", "#F8FAFC", "quote"),
            ("assistencia-informatica", "Assistência de Informática", "PC Master Manutenção & Redes", "Formatação rápida com backup seguro, upgrade de SSD para acelerar o PC e conserto de notebooks.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("assistencia-eletrodomesticos", "Assistência de Eletrodomésticos", "EletroFix Assistência Técnica", "Conserto de geladeiras, máquinas de lavar roupa, micro-ondas e lava-louças com visita técnica rápida.", "#D97706", "#1F1206", "#F59E0B", "#FFFBEB", "quote"),
            ("grafica", "Gráfica Rápida", "PrintArte Gráfica & Brindes", "Cartões de visita, panfletos com verniz localizado, crachás e brindes corporativos expressos.", "#7C3AED", "#18181B", "#A78BFA", "#F8FAFC", "quote"),
            ("comunicacao-visual", "Comunicação Visual", "VisualSign Fachadas em ACM", "Fachadas comerciais em ACM, letras caixa iluminadas, adesivação de frotas e totens externos.", "#EA580C", "#1C1917", "#F97316", "#FFF7ED", "quote"),
            ("loja-informatica", "Loja de Informática", "ChipSet Hardware & PC Gamer", "Montagem de PCs gamers personalizados, placas de vídeo, memórias e periféricos de alta performance.", "#7C3AED", "#09090B", "#C084FC", "#09090B", "catalog"),
            ("conserto-videogame", "Conserto de Videogame", "GameZone Assistência Técnica", "Limpeza preventiva com troca de pasta térmica, reparo de HDMI e controles de PS5, Xbox e Nintendo Switch.", "#2563EB", "#09090B", "#60A5FA", "#09090B", "quote"),
            ("instalacao-cameras", "Instalação de Câmeras", "Visão Segura Câmeras HD & CFTV", "Instalação de câmeras com visualização colorida noturna e gravação em nuvem para casas e comércios.", "#0369A1", "#0F172A", "#38BDF8", "#F0F9FF", "quote")
        ]
    },
    {
        "id": "outros-servicos",
        "name": "Outros Serviços",
        "icon": "📦",
        "desc": "Lavanderias, mudanças, costura, limpezas, cuidadores e coworking",
        "niches": [
            ("lavanderia", "Lavanderia", "LavaClean Lavanderia Têxtil", "Lavagem e passadoria de ternos, vestidos de festa, cobertores pesados e planos mensais de roupas do dia a dia.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("atelier-costura", "Atelier de Costura", "Linha de Ouro Ajustes de Roupas", "Bainhas originais, ajustes de cintura em vestidos e ternos e customização de roupas com perfeição.", "#B45309", "#271202", "#D97706", "#FFFBEB", "quote"),
            ("sapataria", "Sapataria", "O Mestre Sapateiro Restauração", "Troca de solados, hidratação de calçados de couro, conserto de zíperes e restauração de tênis esportivos.", "#78350F", "#1E0D03", "#B45309", "#FEF3C7", "quote"),
            ("empresa-mudancas", "Empresa de Mudanças", "TransFácil Mudanças & Içamentos", "Mudanças residenciais com embalagem completa de caixas, plástico bolha e montagem de móveis.", "#1D4ED8", "#0F172A", "#3B82F6", "#EFF6FF", "quote"),
            ("transportadora", "Transportadora", "Rápido Brasil Cargas Express", "Transporte seguro de cargas fracionadas e encomendas com rastreamento em tempo real.", "#C2410C", "#431407", "#FB923C", "#FFF7ED", "quote"),
            ("coworking", "Coworking", "HubSpace Escritórios Compartilhados", "Estações de trabalho com internet de fibra veloz, salas privativas e endereço fiscal para sua empresa.", "#0F766E", "#134E4A", "#14B8A6", "#F0FDFA", "booking"),
            ("lavagem-sofa", "Lavagem de Sofá", "Estofado Limpo Higienização", "Lavagem a seco e desinfecção profunda de sofás, colchões e tapetes que remove ácaros e odores.", "#0369A1", "#082F49", "#38BDF8", "#F0F9FF", "quote"),
            ("organizadora-armarios", "Organizadora de Armários", "Harmonia & Ordem Personal Organizer", "Organização profissional de closets, dispensas e cozinhas para trazer praticidade à sua rotina.", "#C026D3", "#4A044E", "#E879F9", "#FDF4FF", "booking"),
            ("cuidador-idosos", "Cuidador de Idosos", "Cuidado & Amor Acompanhantes", "Profissionais de saúde selecionados para acompanhamento de idosos com medicação, banho e carinho.", "#059669", "#064E3B", "#10B981", "#ECFDF5", "booking"),
            ("empresa-limpeza", "Empresa de Limpeza", "Brilho Forte Limpeza Pós-Obra", "Limpeza pós-obra pesada, faxinas corporativas e terceirização de limpeza com nota fiscal e segurança.", "#0284C7", "#082F49", "#38BDF8", "#F0F9FF", "quote")
        ]
    }
]

def get_service_data(niche_title, brand, feature_type):
    """Gera 4 serviços realistas e preços para cada nicho específico."""
    return [
        {
            "name": f"Atendimento Padrão & Avaliação",
            "desc": f"Diagnóstico inicial completo, planejamento detalhado e atendimento prioritário com nossa equipe.",
            "price": "R$ 120,00" if feature_type == "booking" else ("R$ 45,00" if feature_type == "catalog" else "Sob Consulta")
        },
        {
            "name": f"Procedimento Especializado",
            "desc": f"Execução de serviços avançados com equipamentos de ponta, materiais certificados e garantia de satisfação.",
            "price": "R$ 280,00" if feature_type == "booking" else ("R$ 78,00" if feature_type == "catalog" else "Sob Consulta")
        },
        {
            "name": f"Pacote Completo / Manutenção",
            "desc": f"Acompanhamento contínuo, revisões periódicas e condições facilitadas em planos mensais ou parcelados.",
            "price": "R$ 490,00" if feature_type == "booking" else ("R$ 130,00" if feature_type == "catalog" else "Sob Consulta")
        },
        {
            "name": f"Plano Personalizado / Premium",
            "desc": f"Solução sob medida para clientes exigentes que buscam a máxima qualidade, exclusividade e suporte total.",
            "price": "Sob Consulta"
        }
    ]

def render_case_html(cat, niche):
    slug, title, brand, slogan, primary, dark, accent, bg, feat = niche
    services = get_service_data(title, brand, feat)
    
    # Detalhes específicos de interatividade
    feature_markup = ""
    if feat == "booking":
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Agendamento Online</span>
            <h3>Escolha o melhor dia e horário para seu atendimento</h3>
            <p>Selecione uma data para ser atendido sem filas e com horário reservado.</p>
          </div>
          <div class="date-chips">
            <button class="chip is-active" type="button"><b>Hoje</b><span>28 Out</span></button>
            <button class="chip" type="button"><b>Amanhã</b><span>29 Out</span></button>
            <button class="chip" type="button"><b>Quinta</b><span>30 Out</span></button>
            <button class="chip" type="button"><b>Sexta</b><span>31 Out</span></button>
            <button class="chip" type="button"><b>Sábado</b><span>01 Nov</span></button>
          </div>
          <div class="time-chips">
            <span class="time-tag is-active">08:30</span>
            <span class="time-tag">10:00</span>
            <span class="time-tag">11:30</span>
            <span class="time-tag">14:00</span>
            <span class="time-tag">15:30</span>
            <span class="time-tag">17:00</span>
            <span class="time-tag">18:30</span>
          </div>
          <div class="box-action">
            <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+agendar+um+hor%C3%A1rio+na+{brand.replace(' ', '+')}+para+{title.replace(' ', '+')}." target="_blank" class="btn btn-primary">Confirmar Agendamento no WhatsApp →</a>
          </div>
        </div>
        """
    elif feat == "catalog":
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Catálogo Digital &amp; Pedidos</span>
            <h3>Cardápio &amp; Produtos em Destaque</h3>
            <p>Faça seu pedido diretamente pelo WhatsApp com entrega rápida e atendimento imediato.</p>
          </div>
          <div class="catalog-grid">
            <div class="cat-item">
              <div class="cat-badge">Mais Pedido</div>
              <h4>Opção Tradicional da Casa</h4>
              <p>Receita clássica artesanal preparada com ingredientes frescos selecionados.</p>
              <div class="cat-foot">
                <b>R$ 38,00</b>
                <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+pedir+a+Opcao+Tradicional+na+{brand.replace(' ', '+')}." target="_blank" class="btn-sm">Pedir Agora</a>
              </div>
            </div>
            <div class="cat-item">
              <div class="cat-badge">Especial</div>
              <h4>Combo Especial &amp; Acompanhamentos</h4>
              <p>A combinação perfeita para compartilhar com a família ou amigos hoje mesmo.</p>
              <div class="cat-foot">
                <b>R$ 65,00</b>
                <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+pedir+o+Combo+Especial+na+{brand.replace(' ', '+')}." target="_blank" class="btn-sm">Pedir Agora</a>
              </div>
            </div>
          </div>
          <div class="box-action">
            <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+ver+o+card%C3%A1pio+completo+da+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary">Pedir Cardápio Completo no WhatsApp →</a>
          </div>
        </div>
        """
    elif feat == "curriculum":
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Matrículas &amp; Turmas</span>
            <h3>Aulas Práticas com Vagas Limitadas</h3>
            <p>Agende uma aula experimental gratuita e conheça nossa metodologia de perto.</p>
          </div>
          <div class="curriculum-list">
            <div class="curr-card">
              <span class="curr-tag">Turma Iniciante</span>
              <h4>Módulo Fundamental — Do Zero à Prática</h4>
              <p>Aprenda os fundamentos essenciais com exercícios práticos e acompanhamento próximo.</p>
              <small>Duração: 8 semanas • Certificado incluso</small>
            </div>
            <div class="curr-card">
              <span class="curr-tag">Avançado</span>
              <h4>Módulo Master — Aperfeiçoamento &amp; Performance</h4>
              <p>Técnicas aprofundadas para quem quer atingir o próximo nível profissional.</p>
              <small>Duração: 12 semanas • Aulas em pequenos grupos</small>
            </div>
          </div>
          <div class="box-action">
            <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+agendar+uma+aula+experimental+na+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary">Agendar Aula Experimental Gratuita →</a>
          </div>
        </div>
        """
    else: # quote
        feature_markup = f"""
        <div class="interactive-box">
          <div class="box-head">
            <span class="box-badge">Orçamento Rápido</span>
            <h3>Simule seu Orçamento sem Compromisso</h3>
            <p>Envie os detalhes do seu projeto e nossa equipe responderá em até 1 hora no WhatsApp.</p>
          </div>
          <form class="quote-form" onsubmit="return false;">
            <div class="form-row">
              <input type="text" placeholder="Seu Nome Completo *" required />
              <input type="tel" placeholder="WhatsApp / Telefone *" required />
            </div>
            <div class="form-row">
              <select required>
                <option value="">Selecione o Serviço Desejado *</option>
                <option>{services[0]['name']}</option>
                <option>{services[1]['name']}</option>
                <option>{services[2]['name']}</option>
                <option>{services[3]['name']}</option>
              </select>
              <input type="text" placeholder="Bairro / Cidade" value="Campinas e Região" />
            </div>
            <textarea placeholder="Conte brevemente o que você precisa resolver..." rows="2"></textarea>
            <div class="box-action">
              <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+solicitar+um+or%C3%A7amento+para+{title.replace(' ', '+')}+na+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary btn-block">Enviar Pedido de Orçamento no WhatsApp →</a>
            </div>
          </form>
        </div>
        """

    services_html = "".join([f"""
      <article class="service-card">
        <div class="srv-badge">Especialidade</div>
        <h4>{s['name']}</h4>
        <p>{s['desc']}</p>
        <div class="srv-price">
          <small>Investimento</small>
          <b>{s['price']}</b>
        </div>
        <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Tenho+interesse+no+servi%C3%A7o+{s['name'].replace(' ', '+')}+da+{brand.replace(' ', '+')}." target="_blank" class="srv-link">Solicitar este serviço <span>→</span></a>
      </article>
    """ for s in services])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{brand} — {title}</title>
  <meta name="description" content="{slogan}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap" rel="stylesheet" />
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
      --radius: 14px;
      --shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.08);
    }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    /* Top Ribbon Nexo */
    .nexo-bar {{
      background: #0B0F14;
      color: #94A3B8;
      font-size: 12px;
      padding: 8px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}
    .nexo-bar a {{ color: #38BDF8; font-weight: 600; text-decoration: none; }}
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
      background: var(--paper);
      padding: 18px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--line);
      position: sticky; top: 0; z-index: 50;
      box-shadow: 0 4px 20px -10px rgba(0,0,0,0.05);
    }}
    .logo {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--dark);
    }}
    .logo-badge {{
      width: 42px; height: 42px; border-radius: 10px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #fff; display: grid; place-items: center; font-size: 20px; font-weight: 800;
      box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    }}
    .logo-info b {{ display: block; font-size: 17px; font-weight: 800; letter-spacing: -0.02em; line-height: 1.1; }}
    .logo-info small {{ font-size: 11px; color: var(--muted); letter-spacing: 0.08em; text-transform: uppercase; font-weight: 600; }}
    
    .nav {{ display: flex; align-items: center; gap: 28px; list-style: none; }}
    .nav a {{ color: var(--muted); text-decoration: none; font-size: 14px; font-weight: 600; transition: color .2s; }}
    .nav a:hover {{ color: var(--primary); }}

    .btn {{
      display: inline-flex; align-items: center; justify-content: center; gap: 8px;
      padding: 12px 24px; border-radius: 999px;
      font-size: 13.5px; font-weight: 700; text-decoration: none;
      transition: all .25s ease;
    }}
    .btn-primary {{
      background: var(--primary); color: #fff;
      box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    }}
    .btn-primary:hover {{ transform: translateY(-2px); filter: brightness(1.08); box-shadow: 0 8px 24px rgba(0,0,0,0.2); }}
    .btn-outline {{
      background: transparent; color: var(--text); border: 1.5px solid var(--line);
    }}
    .btn-outline:hover {{ border-color: var(--primary); color: var(--primary); background: #fff; }}
    .btn-block {{ width: 100%; }}
    .btn-sm {{
      background: var(--primary); color: #fff; font-size: 12px; font-weight: 700;
      padding: 7px 16px; border-radius: 999px; text-decoration: none;
    }}

    /* Hero */
    .hero {{
      padding: 64px 32px 72px;
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
      font-size: clamp(34px, 4.2vw, 52px);
      font-weight: 800; letter-spacing: -0.03em; line-height: 1.14;
      color: var(--dark);
    }}
    .hero h1 em {{ font-style: normal; color: var(--primary); }}
    .hero p {{
      margin-top: 18px; font-size: 16.5px; color: var(--muted);
      max-width: 540px; line-height: 1.65;
    }}
    .hero-actions {{ display: flex; gap: 14px; margin-top: 32px; flex-wrap: wrap; }}
    .trust-row {{
      display: flex; gap: 20px; margin-top: 36px;
      font-size: 12.5px; color: var(--muted); font-weight: 600; flex-wrap: wrap;
    }}
    .trust-row span {{ display: flex; align-items: center; gap: 6px; color: var(--dark); }}

    /* Interactive Box */
    .interactive-box {{
      background: var(--paper); border: 1px solid var(--line);
      border-radius: var(--radius); padding: 32px;
      box-shadow: var(--shadow);
    }}
    .box-badge {{
      display: inline-block; font-size: 11px; font-weight: 800;
      letter-spacing: 0.12em; text-transform: uppercase;
      color: var(--primary); background: rgba(0,0,0,0.03);
      padding: 4px 10px; border-radius: 6px; margin-bottom: 8px;
    }}
    .box-head h3 {{ font-size: 20px; font-weight: 800; color: var(--dark); }}
    .box-head p {{ font-size: 13.5px; color: var(--muted); margin-top: 4px; }}
    
    /* Chips */
    .date-chips {{ display: flex; gap: 10px; margin: 20px 0 16px; overflow-x: auto; padding-bottom: 6px; }}
    .chip {{
      background: var(--bg); border: 1px solid var(--line); border-radius: 10px;
      padding: 10px 16px; text-align: center; cursor: pointer; min-width: 80px;
      transition: all .2s; font-family: inherit;
    }}
    .chip.is-active, .chip:hover {{ background: var(--primary); color: #fff; border-color: var(--primary); }}
    .chip b {{ display: block; font-size: 13px; }}
    .chip span {{ font-size: 11px; opacity: .85; }}
    .time-chips {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px; }}
    .time-tag {{
      background: var(--bg); border: 1px solid var(--line); border-radius: 6px;
      padding: 6px 12px; font-size: 12px; font-weight: 700; cursor: pointer;
    }}
    .time-tag.is-active, .time-tag:hover {{ background: var(--dark); color: #fff; }}
    .box-action {{ margin-top: 16px; }}

    /* Form */
    .quote-form {{ margin-top: 20px; display: flex; flex-direction: column; gap: 12px; }}
    .form-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
    .quote-form input, .quote-form select, .quote-form textarea {{
      width: 100%; padding: 12px 14px; border-radius: 8px;
      border: 1px solid var(--line); background: var(--bg);
      font-family: inherit; font-size: 13.5px; color: var(--text);
    }}

    /* Catalog Grid */
    .catalog-grid {{ display: flex; flex-direction: column; gap: 12px; margin: 18px 0; }}
    .cat-item {{
      background: var(--bg); border: 1px solid var(--line);
      border-radius: 10px; padding: 14px 16px;
    }}
    .cat-badge {{ font-size: 10.5px; font-weight: 800; color: var(--primary); text-transform: uppercase; }}
    .cat-item h4 {{ font-size: 15px; font-weight: 700; color: var(--dark); margin-top: 2px; }}
    .cat-item p {{ font-size: 12px; color: var(--muted); }}
    .cat-foot {{ display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }}
    .cat-foot b {{ font-size: 16px; color: var(--dark); font-weight: 800; }}

    /* Curriculum Cards */
    .curriculum-list {{ display: flex; flex-direction: column; gap: 12px; margin: 18px 0; }}
    .curr-card {{ background: var(--bg); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; }}
    .curr-tag {{ font-size: 10.5px; font-weight: 800; color: var(--primary); text-transform: uppercase; }}
    .curr-card h4 {{ font-size: 14.5px; font-weight: 700; color: var(--dark); }}
    .curr-card p {{ font-size: 12px; color: var(--muted); margin-top: 2px; }}
    .curr-card small {{ font-size: 11px; color: var(--primary); font-weight: 600; display: block; margin-top: 6px; }}

    /* Services Section */
    .services-sec {{
      background: var(--paper); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);
      padding: 72px 32px;
    }}
    .sec-container {{ max-width: 1240px; margin: 0 auto; }}
    .sec-head {{ text-align: center; margin-bottom: 48px; }}
    .sec-head small {{
      display: inline-block; font-size: 11.5px; font-weight: 800;
      letter-spacing: 0.12em; text-transform: uppercase;
      color: var(--primary); margin-bottom: 6px;
    }}
    .sec-head h2 {{ font-size: clamp(28px, 3.2vw, 38px); font-weight: 800; color: var(--dark); letter-spacing: -0.02em; }}
    .sec-head p {{ font-size: 15px; color: var(--muted); margin-top: 8px; max-width: 600px; margin-inline: auto; }}

    .services-grid {{
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px;
    }}
    .service-card {{
      background: var(--bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 28px 22px; display: flex; flex-direction: column;
      transition: transform .3s ease, box-shadow .3s ease, border-color .3s;
    }}
    .service-card:hover {{
      transform: translateY(-4px); box-shadow: var(--shadow);
      border-color: var(--primary);
    }}
    .srv-badge {{
      font-size: 11px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase;
      color: var(--primary); margin-bottom: 8px;
    }}
    .service-card h4 {{ font-size: 17px; font-weight: 700; color: var(--dark); line-height: 1.3; }}
    .service-card p {{ font-size: 13.5px; color: var(--muted); margin-top: 8px; line-height: 1.5; flex: 1; }}
    .srv-price {{ margin: 18px 0 14px; padding-top: 14px; border-top: 1px dashed var(--line); }}
    .srv-price small {{ display: block; font-size: 11px; text-transform: uppercase; color: var(--muted); }}
    .srv-price b {{ font-size: 18px; font-weight: 800; color: var(--dark); }}
    .srv-link {{
      font-size: 12.5px; font-weight: 700; color: var(--primary); text-decoration: none;
      display: inline-flex; align-items: center; gap: 4px;
    }}

    /* Pillars */
    .pillars-sec {{ padding: 72px 32px; max-width: 1240px; margin: 0 auto; }}
    .pillars-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
    .pillar-card {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 32px 28px; box-shadow: 0 4px 16px rgba(0,0,0,0.02);
    }}
    .pillar-icon {{
      width: 44px; height: 44px; border-radius: 10px;
      background: var(--bg); color: var(--primary); display: grid; place-items: center;
      font-size: 22px; margin-bottom: 18px;
    }}
    .pillar-card h3 {{ font-size: 18px; font-weight: 800; color: var(--dark); margin-bottom: 8px; }}
    .pillar-card p {{ font-size: 14px; color: var(--muted); }}

    /* Testimonials */
    .testi-sec {{ background: var(--paper); padding: 72px 32px; border-top: 1px solid var(--line); }}
    .testi-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1240px; margin: 0 auto; }}
    .testi-card {{
      background: var(--bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 28px 24px;
    }}
    .testi-stars {{ color: #F59E0B; margin-bottom: 12px; font-size: 14px; }}
    .testi-card p {{ font-size: 13.5px; color: var(--text); font-style: italic; line-height: 1.6; }}
    .testi-user {{ display: flex; align-items: center; gap: 12px; margin-top: 18px; }}
    .user-avatar {{
      width: 38px; height: 38px; border-radius: 50%; background: var(--primary);
      color: #fff; font-weight: 700; font-size: 14px; display: grid; place-items: center;
    }}
    .user-info b {{ display: block; font-size: 13.5px; font-weight: 700; color: var(--dark); }}
    .user-info small {{ font-size: 11.5px; color: var(--muted); }}

    /* FAQ */
    .faq-sec {{ padding: 72px 32px; max-width: 860px; margin: 0 auto; }}
    .faq-item {{
      background: var(--paper); border: 1px solid var(--line); border-radius: 10px;
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
      background: var(--dark); color: #94A3B8; padding: 60px 32px 32px; font-size: 13px;
    }}
    .footer-inner {{
      max-width: 1240px; margin: 0 auto; display: grid;
      grid-template-columns: 1.5fr 1fr 1fr; gap: 40px; padding-bottom: 40px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}
    .footer h5 {{ color: #fff; font-size: 15px; font-weight: 700; margin-bottom: 14px; }}
    .footer p {{ line-height: 1.6; max-width: 320px; }}
    .footer-bottom {{
      max-width: 1240px; margin: 24px auto 0; display: flex;
      justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;
      font-size: 12px;
    }}
    .footer-bottom a {{ color: var(--accent); text-decoration: none; }}

    /* WhatsApp Float */
    .wa-float {{
      position: fixed; right: 24px; bottom: 24px; z-index: 99;
      width: 58px; height: 58px; border-radius: 50%;
      background: #25D366; color: #fff; display: grid; place-items: center;
      box-shadow: 0 6px 24px rgba(37, 211, 102, 0.4);
      transition: transform .3s ease; text-decoration: none;
    }}
    .wa-float:hover {{ transform: scale(1.1); }}
    .wa-float svg {{ width: 32px; height: 32px; fill: currentColor; }}

    @media (max-width: 1024px) {{
      .hero {{ grid-template-columns: 1fr; padding: 40px 20px; }}
      .services-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .pillars-grid, .testi-grid {{ grid-template-columns: 1fr; }}
      .footer-inner {{ grid-template-columns: 1fr; }}
      .nav {{ display: none; }}
    }}
    @media (max-width: 640px) {{
      .services-grid {{ grid-template-columns: 1fr; }}
      .form-row {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <!-- Top Ribbon Nexo -->
  <aside class="nexo-bar">
    <span>✦ Modelo Demonstrativo Comercial · <b>{title}</b></span>
    <a href="../../../index.html">Criado por Nexo Studio — Solicite um site igual para sua empresa →</a>
  </aside>

  <!-- Top Info -->
  <div class="top-info">
    <span>Seg-Sáb: 08:00 - 19:00 &nbsp;•&nbsp; Campinas e Região Metropolitana - SP</span>
    <span>Atendimento WhatsApp: <b>(19) 99633-1656</b></span>
  </div>

  <!-- Header -->
  <header class="header">
    <a href="#" class="logo">
      <div class="logo-badge">{title[0]}</div>
      <div class="logo-info">
        <b>{brand}</b>
        <small>{title}</small>
      </div>
    </a>
    <ul class="nav">
      <li><a href="#">Início</a></li>
      <li><a href="#servicos">Serviços</a></li>
      <li><a href="#diferenciais">Diferenciais</a></li>
      <li><a href="#avaliacoes">Avaliações</a></li>
      <li><a href="#duvidas">Dúvidas</a></li>
    </ul>
    <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Tenho+interesse+nos+servi%C3%A7os+da+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary">Fale Conosco</a>
  </header>

  <main>
    <!-- Hero -->
    <section class="hero">
      <div class="hero-copy">
        <div class="rating-pill">
          <span>★★★★★</span> 4.9 no Google · +180 clientes satisfeitos
        </div>
        <h1>Excelência e cuidado para <em>{title.lower()}</em> que você confia.</h1>
        <p>{slogan}</p>
        <div class="hero-actions">
          <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Gostaria+de+solicitar+um+atendimento+na+{brand.replace(' ', '+')}." target="_blank" class="btn btn-primary">Agendar pelo WhatsApp</a>
          <a href="#servicos" class="btn btn-outline">Ver Especialidades</a>
        </div>
        <div class="trust-row">
          <span>✓ Profissionais Certificados</span>
          <span>✓ Atendimento Humanizado</span>
          <span>✓ Orçamento Transparente</span>
        </div>
      </div>

      <!-- Interactive Module -->
      {feature_markup}
    </section>

    <!-- Services -->
    <section class="services-sec" id="servicos">
      <div class="sec-container">
        <div class="sec-head">
          <small>Nossas Soluções</small>
          <h2>Especialidades &amp; Serviços</h2>
          <p>Conheça os principais procedimentos e serviços desenvolvidos com padrão de excelência e tecnologia.</p>
        </div>
        <div class="services-grid">
          {services_html}
        </div>
      </div>
    </section>

    <!-- Pillars -->
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

    <!-- Testimonials -->
    <section class="testi-sec" id="avaliacoes">
      <div class="sec-head">
        <small>Depoimentos</small>
        <h2>O que Dizem Nossos Clientes</h2>
      </div>
      <div class="testi-grid">
        <div class="testi-card">
          <div class="testi-stars">★★★★★</div>
          <p>"Atendimento impecável do início ao fim! Fui super bem atendida e o resultado superou minhas expectativas. Recomendo de olhos fechados!"</p>
          <div class="testi-user">
            <div class="user-avatar">MC</div>
            <div class="user-info">
              <b>Mariana Costa</b>
              <small>Cliente Verificada • Google</small>
            </div>
          </div>
        </div>
        <div class="testi-card">
          <div class="testi-stars">★★★★★</div>
          <p>"Profissionalismo raro de encontrar hoje em dia. Preço justo, pontualidade britânica e um cuidado que faz toda a diferença."</p>
          <div class="testi-user">
            <div class="user-avatar">RA</div>
            <div class="user-info">
              <b>Rodrigo Almeida</b>
              <small>Cliente Verificado • Google</small>
            </div>
          </div>
        </div>
        <div class="testi-card">
          <div class="testi-stars">★★★★★</div>
          <p>"Ambiente acolhedor, comunicação clara pelo WhatsApp e serviço nota dez. Já sou cliente fiel há mais de um ano!"</p>
          <div class="testi-user">
            <div class="user-avatar">CF</div>
            <div class="user-info">
              <b>Camila Ferreira</b>
              <small>Cliente Verificada • Google</small>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="faq-sec" id="duvidas">
      <div class="sec-head">
        <small>Tire suas dúvidas</small>
        <h2>Perguntas Frequentes</h2>
      </div>
      <details class="faq-item" open>
        <summary>Como funciona o agendamento de horários ou pedidos?</summary>
        <div class="faq-content">
          Você pode clicar em qualquer botão do site para falar diretamente com nossa equipe no WhatsApp. O atendimento é rápido e confirmamos sua solicitação na hora.
        </div>
      </details>
      <details class="faq-item">
        <summary>Quais são as formas de pagamento aceitas?</summary>
        <div class="faq-content">
          Aceitamos Pix com desconto, cartões de crédito em até 12x, débito e transferência bancária com emissão de nota fiscal.
        </div>
      </details>
      <details class="faq-item">
        <summary>Onde fica o local de atendimento?</summary>
        <div class="faq-content">
          Estamos localizados em região nobre com fácil acesso, estacionamento no local e infraestrutura completa para seu conforto.
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
        <p style="margin-top: 12px; font-size: 12px; color: #64748B;">Atendimento em Campinas, SP e cidades vizinhas.</p>
      </div>
      <div>
        <h5>Horários de Funcionamento</h5>
        <p>Segunda a Sexta: 08:00 às 19:00<br />Sábados: 08:00 às 14:00<br />Domingos e Feriados: Fechado</p>
      </div>
      <div>
        <h5>Contato &amp; WhatsApp</h5>
        <p>WhatsApp: (19) 99633-1656<br />E-mail: contato@{slug}.com.br<br />Campinas - SP</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 {brand}. Todos os direitos reservados.</span>
      <span>Site demonstrativo desenvolvido por <a href="../../../index.html">Nexo Studio</a></span>
    </div>
  </footer>

  <!-- WhatsApp Float -->
  <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Vi+o+site+da+{brand.replace(' ', '+')}+e+gostaria+de+um+atendimento." target="_blank" class="wa-float" aria-label="Fale conosco pelo WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.39-1.72-.14-.25-.02-.39.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.24.9 2.44 1.03 2.61.13.17 1.77 2.7 4.29 3.79.6.26 1.07.41 1.43.53.6.19 1.15.16 1.58.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.11-.23-.17-.48-.3"/></svg>
  </a>
</body>
</html>"""

def render_master_hub_html(categories):
    total = sum(len(c["niches"]) for c in categories)
    
    # Gerar os botões de abas
    tabs_html = '<button class="hub-tab is-active" data-cat="all">Todos os Nichos <span class="badge">' + str(total) + '</span></button>'
    for c in categories:
        tabs_html += f'<button class="hub-tab" data-cat="{c["id"]}">{c["icon"]} {c["name"]} <span class="badge">{len(c["niches"])}</span></button>'
    
    # Gerar os cards dos 179 nichos
    cards_html = ""
    for c in categories:
        for niche in c["niches"]:
            slug, title, brand, slogan, primary, dark, accent, bg, feat = niche
            feat_label = "Agendamento Online" if feat == "booking" else ("Catálogo Digital" if feat == "catalog" else ("Matrículas" if feat == "curriculum" else "Orçamento Rápido"))
            cards_html += f"""
            <article class="hub-card" data-cat="{c['id']}" data-search="{title.lower()} {brand.lower()} {c['name'].lower()} {slug}">
              <div class="hub-card-header" style="background: linear-gradient(135deg, {dark}, {primary});">
                <span class="hub-cat-tag">{c['name']}</span>
                <span class="hub-feat-tag">{feat_label}</span>
              </div>
              <div class="hub-card-body">
                <h3>{brand}</h3>
                <small class="hub-niche-label">{title}</small>
                <p>{slogan}</p>
                <div class="hub-card-foot">
                  <a href="{c['id']}/{slug}/index.html" target="_blank" class="hub-btn-view">Ver Site Ao Vivo ↗</a>
                  <a href="https://wa.me/5519996331656?text=Ol%C3%A1!+Tenho+interesse+em+um+site+para+{title.replace(' ', '+')}+como+o+da+{brand.replace(' ', '+')}." target="_blank" class="hub-btn-wa" title="Pedir um site assim no WhatsApp">
                    <svg viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24"/></svg>
                  </a>
                </div>
              </div>
            </article>
            """

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Catálogo de Demonstrações Comerciais — Nexo Studio</title>
  <meta name="description" content="Explore mais de 170 sites demonstrativos animados para diferentes tipos de comércio e empresas locais." />
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
      padding: 24px 32px;
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
      padding: 72px 24px 40px;
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
      transform: translateY(-4px); border-color: rgba(56, 189, 248, 0.4);
      box-shadow: 0 20px 40px -15px rgba(0,0,0,0.5);
    }}
    .hub-card-header {{
      height: 90px; padding: 16px 20px; display: flex;
      justify-content: space-between; align-items: flex-start;
      position: relative;
    }}
    .hub-cat-tag {{
      font-size: 11px; font-weight: 700; letter-spacing: 0.08em;
      text-transform: uppercase; color: #fff; background: rgba(0,0,0,0.35);
      padding: 4px 10px; border-radius: 6px; backdrop-filter: blur(4px);
    }}
    .hub-feat-tag {{
      font-size: 10.5px; font-weight: 700; color: #E2E8F0;
      background: rgba(255,255,255,0.15); padding: 4px 10px; border-radius: 999px;
    }}
    .hub-card-body {{
      padding: 24px 20px 20px; flex: 1; display: flex; flex-direction: column;
    }}
    .hub-card-body h3 {{ font-size: 18px; font-weight: 800; color: #fff; }}
    .hub-niche-label {{ font-size: 12px; color: #38BDF8; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; display: block; }}
    .hub-card-body p {{ font-size: 13.5px; color: #94A3B8; line-height: 1.5; flex: 1; }}

    .hub-card-foot {{
      margin-top: 20px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.08);
      display: flex; gap: 10px; align-items: center;
    }}
    .hub-btn-view {{
      flex: 1; background: #1E293B; color: #fff; text-decoration: none;
      font-size: 12.5px; font-weight: 700; padding: 10px 16px; border-radius: 8px;
      text-align: center; transition: background .2s;
    }}
    .hub-btn-view:hover {{ background: #2563EB; }}
    .hub-btn-wa {{
      width: 40px; height: 40px; border-radius: 8px; background: #25D366;
      color: #fff; display: grid; place-items: center; text-decoration: none;
      transition: filter .2s;
    }}
    .hub-btn-wa:hover {{ filter: brightness(1.1); }}
    .hub-btn-wa svg {{ width: 20px; height: 20px; }}

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
      <span class="hub-badge">✦ Portfólio Comercial Completo</span>
      <h1><span>{total} Sites Demonstrativos</span><br />Prontos para seu Negócio.</h1>
      <p>Demonstrações com design exclusivo, microinterações, paleta estratégica e dados reais em português para cada segmento do mercado.</p>

      <div class="hub-search-wrap">
        <svg class="hub-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
        <input type="text" id="hub-search" class="hub-search-input" placeholder="Pesquise seu nicho: dentista, barbearia, pizzaria, mecânica, pilates..." />
      </div>
    </section>

    <div class="hub-tabs-container">
      <div class="hub-tabs" id="hub-tabs">
        {tabs_html}
      </div>
    </div>

    <section class="hub-grid" id="hub-grid">
      {cards_html}
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
    print("Iniciando gerador de cases do Nexo Studio...")
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

    print(f"Sucesso! {generated_count} sites gerados com sucesso!")
    print(f"Master Showcase Hub gerado em: {hub_file}")

if __name__ == "__main__":
    build_all()

