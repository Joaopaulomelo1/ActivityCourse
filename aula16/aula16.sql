CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10, 2)
);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco) VALUES
(1, 'Notebook', 10, 3500.00),
(2, 'Mouse', 50, 45.90),
(3, 'Teclado', 30, 120.00);


