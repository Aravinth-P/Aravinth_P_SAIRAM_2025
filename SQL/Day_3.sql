Build an OLX like data modelling having features to purchase and buy any product across the city and 
the customer can choose any transportation mode like  (porter app) connected to it and system should recommend vehicle based on the product choosed.

Admin:
    Attributes: adminID, adminname, Email, Password, Address, Phone Number
User:
    Attributes: UserID, Username, Email, Password, Address, Phone Number
Product:
    Attributes: ProductID, Name, Description, Price, SellerID, Location, Category
Order:
    Attributes: OrderID, UserID, ProductID, Quantity, Total Price, Order Date, Status (e.g., pending, delivered)
Transportation Mode:
    Attributes: ModeID, ModeName, Description
Vehicle:
    Attributes: VehicleID, ModeID, VehicleType, Capacity, Availability, Location
Porter:
    Attributes: PorterID, UserID, VehicleID, Availability, Location
