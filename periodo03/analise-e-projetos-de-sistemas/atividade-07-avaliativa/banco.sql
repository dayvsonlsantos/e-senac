create database dbtabajara;

use dbtabajara;

CREATE TABLE Conta  (    
    codigo int PRIMARY KEY AUTO_INCREMENT,     
    nome VARCHAR(50) NOT NULL,
    saldo DECIMAL(9,2)  NOT NULL);

INSERT INTO Conta (codigo, nome, saldo) VALUES ( 1, "Orlando José da Silva", 23000);

SELECT * FROM Conta;

CREATE TABLE Users (
	codigoUser INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    senha VARCHAR(50)  NOT NULL 
);

SELECT * FROM Users;