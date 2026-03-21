CREATE DATABASE projeto_vendas;
USE projeto_vendas;

CREATE TABLE clientes (
	id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL
    );
    
CREATE TABLE produtos (
	id_produto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(100),
    preco DECIMAL(10,2) NOT NULL
    );
    
CREATE TABLE vendas (
	id_venda INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    data_venda DATE NOT NULL,
    id_cliente INT,
    id_produto INT,
    quantidade FLOAT,
    valor_total DECIMAL(10,2),
    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)  
    );
    
SELECT * FROM vendas;
