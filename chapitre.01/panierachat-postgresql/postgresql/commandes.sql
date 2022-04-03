CREATE TABLE panier (
    panier_id serial primary key,
    client varchar(100) not null UNIQUE
);

CREATE TABLE elementpanier (
    elementpanier_id serial primary key,
    panier_id int not null REFERENCES panier(panier_id),
    produit varchar(100) not null,
    prix NUMERIC(10,2) not null DEFAULT(0),
    quantite int not null CHECK (quantite > 0),
    UNIQUE (panier_id, produit)
);
