CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT,
    DataEntrada DATE,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

SELECT 
    e.EstoqueID,
    p.NomeProduto,
    f.NomeFornecedor,
    e.Quantidade
FROM Estoque e
FULL OUTER JOIN Produtos p 
    ON e.ProdutoID = p.ProdutoID
FULL OUTER JOIN Fornecedores f 
    ON e.FornecedorID = f.FornecedorID;

SELECT 
    ProdutoID,
    SUM(Quantidade) AS TotalEstoque
FROM Estoque
GROUP BY ProdutoID;

ALTER TABLE Estoque
ADD Localizacao VARCHAR(100);

