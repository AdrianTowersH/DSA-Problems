SELECT 
    protocol, -- Select the protocol column
    SUM(traffic_in) AS traffic_in, -- Calculate the total incoming traffic for each protocol
    SUM(traffic_out) AS traffic_out -- Calculate the total outgoing traffic for each protocol
FROM 
    traffic -- Specify the table to query
GROUP BY 
    protocol -- Group the results by protocol to aggregate traffic data
HAVING 
    traffic_in > traffic_out -- Filter to include only protocols where incoming traffic is greater than outgoing traffic
ORDER BY 
    protocol ASC; -- Order the results alphabetically by protocol name

/*

Si quisieras saber cuántas unidades se vendieron por tipo de fruta: 
SELECT producto, SUM(cantidad) AS total 
FROM ventas 
GROUP BY producto;

*/