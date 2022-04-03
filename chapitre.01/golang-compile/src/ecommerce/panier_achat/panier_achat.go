package panier_achat

type produit struct {
	nom       string
	categorie string
	quantite  int
}

type panierAchat struct {
	panier []produit
}

func New() panierAchat {
	p := panierAchat
	return p
}

func AjouteProduit(p produit) {

}
