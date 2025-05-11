-- Criação da tabela
CREATE TABLE ListaCompras (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Produto VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Quantidade INT NOT NULL
);

-- Procedure: Inserir nova compra
CREATE PROCEDURE sp_INSERIR_COMPRA
    @Produto VARCHAR(100),
    @Preco DECIMAL(10, 2),
    @Quantidade INT
AS
BEGIN
    INSERT INTO ListaCompras (Produto, Preco, Quantidade)
    VALUES (@Produto, @Preco, @Quantidade);
END;

-- Procedure: Atualizar uma compra existente
CREATE PROCEDURE sp_ATUALIZAR_COMPRA
    @ID INT,
    @PRODUTO NVARCHAR(100) = NULL,
    @PRECO DECIMAL(10,2) = NULL,
    @QUANTIDADE INT = NULL
AS
BEGIN
    UPDATE ListaCompras
    SET 
        PRODUTO = COALESCE(@PRODUTO, PRODUTO),
        PRECO = COALESCE(@PRECO, PRECO),
        QUANTIDADE = COALESCE(@QUANTIDADE, QUANTIDADE)
    WHERE ID = @ID
END
;
   
-- Procedure: Excluir uma compra
CREATE PROCEDURE sp_EXCLUIR_COMPRA
    @ID INT
AS
BEGIN
    DELETE FROM ListaCompras WHERE ID = @ID;
END;

--TESTAR PROCEDURES
-- Inserir exemplo
EXEC sp_INSERIR_COMPRA 'Leite', 6.50, 1;

-- Atualizar
EXEC sp_ATUALIZAR_COMPRA 1, 'Arroz Integral', 22.50, 3;

-- Excluir
EXEC sp_EXCLUIR_COMPRA 1;

-- Verificar
SELECT * FROM ListaCompras;



