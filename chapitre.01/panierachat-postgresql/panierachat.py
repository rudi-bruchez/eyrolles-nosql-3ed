#!/usr/bin/python
# -*- encoding: utf-8 -*-
################################################################################
#
#    2020 Rudi Bruchez <rudi@pachadata.com>.
#    Licence : MIT. Pour livre Eyrolles - les bases de données NoSQL
#
################################################################################

import psycopg2

class ElementPanier(object):
    
    def __init__(self, produit: str, prix: float, quantite: int):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite
                
    def change_quantite(self, nouvelle_quantite: int):
        self.quantite = nouvelle_quantite
        
    @property
    def total(self) -> float:
        return self.prix * self.quantite

class PanierAchat(object):

    def __init__(self, client: str):
        self.client = client
        self.__elements = list()

    def ajoute_element(self, produit: str, prix : float = 0.0, quantite : int = 1):
        if not (quantite or quantite >= 1):
            raise ValueError('la quantité doit être 1 ou plus.', 'quantite')
        
        element_panier = self.cherche_element(produit)
        
        if element_panier:
            element_panier.change_quantite(element_panier.quantite + quantite)
        else:
            element_panier = ElementPanier(produit, prix, quantite)
            self.__elements.append(element_panier)  

    def cherche_element(self, produit: str):
        for element in self.__elements:
            if element.produit == produit:
                return element
            else:
                continue
        return None

    def enregistrer(self):
        try:
            conn = psycopg2.connect("dbname='ecommerce' user='app' host='panier-achat-database' password='secret'")
            print("Connexion à PostgreSQL réussie.")
        except:
            print("Connexion à PostgreSQL échouée.")
            raise

        sql = """
            with cte as (
                INSERT INTO panier (client) VALUES('{0}') ON CONFLICT DO NOTHING RETURNING panier_id
            )
            select panier_id from cte
            union
            select panier_id from panier where client = '{0}'""".format(self.client)

        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit() # <- We MUST commit to reflect the inserted data
        resultat = cursor.fetchone()
        panier_id = int(resultat[0])
        print(panier_id)

        sql = "DELETE FROM elementpanier WHERE panier_id = {0}".format(panier_id)
        cursor.execute(sql)
        conn.commit() # <- We MUST commit to reflect the inserted data

        sql = "INSERT INTO elementpanier (panier_id, produit, prix, quantite) VALUES "

        for element in self.__elements:
            sql += "({0}, '{1}', {2}, {3}), ".format(panier_id, element.produit, element.prix, element.quantite)
        sql = sql[:-2] + " ON CONFLICT DO NOTHING"

        cursor.execute(sql)
        conn.commit() # <- We MUST commit to reflect the inserted data

        cursor.close()
        conn.close()

    def alimenter(self):
        self.__elements.clear()

        try:
            conn = psycopg2.connect("dbname='ecommerce' user='app' host='panier-achat-database' password='secret'")
            print("Connexion à PostgreSQL réussie.")
        except:
            print("Connexion à PostgreSQL échouée.")
            raise

        sql = "select panier_id from panier where client = '{0}'".format(self.client)

        cursor = conn.cursor()
        cursor.execute(sql)
        resultat = cursor.fetchone()
        panier_id = int(resultat[0])
        print(panier_id)

        sql = "SELECT produit, prix, quantite FROM elementpanier WHERE panier_id = {0}".format(panier_id)
        cursor.execute(sql)
        for element in cursor:
            self.__elements.append(ElementPanier(element[0], element[1], element[2]))

        cursor.close()
        conn.close()


    @property
    def total(self) -> float:
        total: float = 0
        for element in self.__elements:
            total += element.total
        return total

    @property
    def panier(self):
        return self.__elements
