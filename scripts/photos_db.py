# -*- coding: utf-8 -*-
"""
Banco de dados de imagens Full HD curadas via Unsplash para os 179 nichos do Nexo Studio.
"""
from scripts.enrich_photos import CURATED_POOLS, pick_pool

AVATARS = [
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&h=150&q=80",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&h=150&q=80",
    "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=150&h=150&q=80"
]

def get_niche_images(cat_id, niche_slug):
    """
    Retorna o dicionário com hero, 4 services, 4 gallery e 3 avatars para o nicho informado.
    Garante cobertura 100% de imagens Full HD curadas.
    """
    pool_key = pick_pool(cat_id, niche_slug)
    pool = CURATED_POOLS.get(pool_key, CURATED_POOLS["comercio"])

    return {
        "hero": pool["hero"],
        "services": pool["s"],
        "gallery": pool["g"],
        "avatars": AVATARS
    }
