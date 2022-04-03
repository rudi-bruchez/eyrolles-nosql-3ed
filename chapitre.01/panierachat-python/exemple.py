#!/usr/bin/python
# -*- encoding: utf-8 -*-
################################################################################
#
#    2020 Rudi Bruchez <rudi@pachadata.com>.
#    Licence : MIT. Pour livre Eyrolles - les bases de données NoSQL
#
################################################################################

from panierachat import PanierAchat

# --------------------------------------------------
# --                  exemple 01                  --
# --------------------------------------------------

panier = PanierAchat("rudi@pachadata.com")
panier.ajoute_element("Les Bases de Données NoSQL", 35.50, 1)
panier.ajoute_element("Arrosage automatique pour les vacances", 99.50, 1)
print("le total du panier est : ", panier.total)