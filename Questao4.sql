SELECT 
    c.nome,
    p.assunto,
    p.data_abertura,
    c.estado 
FROM 
    clientes c 
INNER JOIN 
    processos p ON c.id_cliente = p.id_cliente 
WHERE 
    YEAR(p.data_abertura) > 2023 
    AND c.estado = 'SP';