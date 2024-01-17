SELECT 
	C.login, 
	COUNT(O.*) 
FROM 
	"Orders" AS O 
INNER JOIN 
	"Couriers" AS C ON O."courierId" = C."id" 
WHERE 
	O."inDelivery" = true 
GROUP BY 
	C.login;
