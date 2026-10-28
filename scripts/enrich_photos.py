# -*- coding: utf-8 -*-
"""
Gerador do banco de fotos Full HD curadas para todos os 179 nichos do Nexo Studio.
"""

# Biblioteca de fotos curadas em alta definição por palavras-chave e categorias
CURATED_POOLS = {
    # SAUDE
    "odontologia": {
        "hero": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1598256989800-fe5f95da9787?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1629909615184-74f495363b67?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "medica": {
        "hero": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "fisioterapia": {
        "hero": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "psicologia": {
        "hero": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1527689368864-3a821dbccc34?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "nutricao": {
        "hero": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1505576399279-565b52d4ac71?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "estetica": {
        "hero": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1512290900672-1f55a11be074?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1560750588-73207b1ef5b8?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1512290900672-1f55a11be074?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "laboratorio": {
        "hero": "https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "otica": {
        "hero": "https://images.unsplash.com/photo-1574258495973-f010dfbb5371?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1591076482161-42ce6da69f67?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1574258495973-f010dfbb5371?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1591076482161-42ce6da69f67?auto=format&fit=crop&w=800&q=80"
        ]
    },

    # BELEZA
    "salao": {
        "hero": "https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1562322140-8baeececf3df?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1562322140-8baeececf3df?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "barbearia": {
        "hero": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1621605815971-fbc98d665033?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1622286342621-4bd786c2447c?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1599351431202-1e0f0137899a?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1534778356534-d3d45b6df1da?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1585747860715-2ba37e788b70?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1593702295094-aea22597af65?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1512690459411-b9245aed614b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1605497788044-5a32c7078486?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "unhas": {
        "hero": "https://images.unsplash.com/photo-1604654894610-df63bc536371?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1519014816548-bf5fe059798b?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1632345031435-8727f6897d53?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1599839575945-a9e5af0c3fa5?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1604654894610-df63bc536371?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1519014816548-bf5fe059798b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1632345031435-8727f6897d53?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "tatuagem": {
        "hero": "https://images.unsplash.com/photo-1598371839696-5c5bb00bdc28?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1568515045052-f9a854d70bfd?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1611501275019-9b5cda994e8d?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1590246814883-578336465f24?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1542385151-efd9000785a0?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1598371839696-5c5bb00bdc28?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1568515045052-f9a854d70bfd?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1611501275019-9b5cda994e8d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1590246814883-578336465f24?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "spa": {
        "hero": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=800&q=80"
        ]
    },

    # ALIMENTACAO
    "restaurante": {
        "hero": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "pizzaria": {
        "hero": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1541745537411-b8046dc6d66c?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1541745537411-b8046dc6d66c?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "hamburgueria": {
        "hero": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1576107232684-1279f3908594?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1576107232684-1279f3908594?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "cafe": {
        "hero": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1509785307050-d4066910ec1e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "padaria": {
        "hero": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1549931319-a545dcf3bc73?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1549931319-a545dcf3bc73?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "japones": {
        "hero": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1611143669185-af224c5e3252?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1553621042-f6e147245754?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1611143669185-af224c5e3252?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1553621042-f6e147245754?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "doces": {
        "hero": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1550617931-e17a7b70dce2?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1550617931-e17a7b70dce2?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=800&q=80"
        ]
    },

    # FITNESS
    "academia": {
        "hero": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "crossfit": {
        "hero": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80"
        ]
    },

    # AUTOMOTIVO
    "mecanica": {
        "hero": "https://images.unsplash.com/photo-1486006920555-c77dce18193b?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1607860108855-64acf2078ed9?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1486006920555-c77dce18193b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1607860108855-64acf2078ed9?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=800&q=80"
        ]
    },

    # CASA E REFORMA
    "reforma": {
        "hero": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1541888946425-d0fbb186156f?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1541888946425-d0fbb186156f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "marcenaria": {
        "hero": "https://images.unsplash.com/photo-1538688525198-9b88f6f53126?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1538688525198-9b88f6f53126?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=800&q=80"
        ]
    },

    # PETS
    "pets": {
        "hero": "https://images.unsplash.com/photo-1587300003388-59208cc962cb?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1587300003388-59208cc962cb?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=800&q=80"
        ]
    },

    # PROFISSIONAL
    "advocacia": {
        "hero": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "arquitetura": {
        "hero": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "comercio": {
        "hero": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1472851294608-062f824d29cc?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1445205170230-053b83016050?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1472851294608-062f824d29cc?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "eventos": {
        "hero": "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=800&q=80"
        ]
    },
    "tecnologia": {
        "hero": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1200&q=85",
        "s": [
            "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1550009158-9ebf69173e03?auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1581092335397-9583fe92d232?auto=format&fit=crop&w=600&q=80"
        ],
        "g": [
            "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1550009158-9ebf69173e03?auto=format&fit=crop&w=800&q=80"
        ]
    }
}

# Mapa de palavras-chave para associar ao melhor pool visual
def pick_pool(cat_id, slug):
    s = slug.lower()
    c = cat_id.lower()
    if "odonto" in s: return "odontologia"
    if "fisio" in s or "quiro" in s: return "fisioterapia"
    if "psico" in s or "terapia" in s: return "psicologia"
    if "nutri" in s: return "nutricao"
    if "estetic" in s or "depil" in s or "sobrancelh" in s or "cilio" in s: return "estetica"
    if "lab" in s or "vacin" in s or "farmac" in s: return "laboratorio"
    if "otica" in s: return "otica"
    if "barbear" in s: return "barbearia"
    if "unha" in s or "esmalte" in s or "nail" in s: return "unhas"
    if "tatu" in s or "piercing" in s: return "tatuagem"
    if "spa" in s or "relax" in s or "massag" in s: return "spa"
    if "pizza" in s: return "pizzaria"
    if "burger" in s or "hamburg" in s: return "hamburgueria"
    if "cafe" in s: return "cafe"
    if "pao" in s or "padar" in s: return "padaria"
    if "japon" in s or "sushi" in s: return "japones"
    if "doce" in s or "confeit" in s or "acai" in s or "sorvet" in s: return "doces"
    if "crossfit" in s or "funcional" in s: return "crossfit"
    if "academia" in s or "personal" in s or "luta" in s or "treino" in s: return "academia"
    if "auto" in s or "mecanic" in s or "carro" in s or "guincho" in s or "lava" in s or "borracha" in s: return "mecanica"
    if "marcenar" in s or "moveis" in s: return "marcenaria"
    if "constru" in s or "eletric" in s or "pintur" in s or "reforma" in s or "gesso" in s or "solar" in s: return "reforma"
    if "pet" in s or "veterin" in s or "cachorr" in s or "adestra" in s or "tosa" in s: return "pets"
    if "advoc" in s or "contab" in s or "perito" in s or "finan" in s or "seguro" in s: return "advocacia"
    if "arquit" in s or "imobil" in s or "decor" in s or "paisag" in s or "imove" in s: return "arquitetura"
    if "comercio" in c or "loja" in s or "boutique" in s: return "comercio"
    if "evento" in c or "festa" in s or "buffet" in s or "dj" in s or "foto" in s: return "eventos"
    if "tecno" in c or "comput" in s or "celular" in s or "game" in s or "camera" in s: return "tecnologia"
    
    # Fallbacks por categoria
    if c == "saude": return "medica"
    if c == "beleza-estetica": return "salao"
    if c == "alimentacao": return "restaurante"
    if c == "fitness-bem-estar": return "academia"
    if c == "automotivo": return "mecanica"
    if c == "casa-reforma": return "reforma"
    if c == "pets": return "pets"
    if c == "servicos-profissionais": return "advocacia"
    if c == "eventos-festas": return "eventos"
    if c == "tecnologia-assistencia": return "tecnologia"
    
    return "comercio"
