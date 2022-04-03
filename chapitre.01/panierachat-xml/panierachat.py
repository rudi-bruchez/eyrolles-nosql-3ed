#!/usr/bin/python
# -*- encoding: utf-8 -*-
################################################################################
#
#    2020 Rudi Bruchez <rudi@pachadata.com>.
#    Licence : MIT. Pour livre Eyrolles - les bases de données NoSQL
#
################################################################################

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

    @property
    def to_xml_element(self) -> str:
        return "<element><produit>{}</produit><prix>{}</prix><quantite>{}</quantite></element>" \
            .format(self.produit, self.prix, self.quantite)
            

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

    @property
    def total(self) -> float:
        total: float = 0
        for element in self.__elements:
            total += element.total
        return total

    @property
    def panier(self):
        return self.__elements

    @property
    def to_xml(self) -> str:
        xml: str = "<panier>"
        for element in self.__elements:
            xml += element.to_xml_element
        xml += "</panier>"
        return xml


    