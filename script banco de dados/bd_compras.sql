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

--ALTERAÇÃO 13/05/2025
-- adicionar tabela de usuários
CREATE TABLE Usuarios (
    id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(100) UNIQUE NOT NULL,
    senha_hash NVARCHAR(255) NOT NULL
);
-- incluir vinculo da tabela de usuario com a tabela listaCompras
ALTER TABLE ListaCompras
ADD usuario_id INT;

ALTER TABLE ListaCompras
ADD CONSTRAINT FK_ListaCompras_Usuarios FOREIGN KEY (usuario_id)
REFERENCES Usuarios(id);
-- incluir usuario na tabela de usuarios
INSERT INTO Usuarios(username,senha_hash)
VALUES('adm','adm')



