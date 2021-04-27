CREATE TABLE rent(

	unnamed INT NOT NULL,
    propertyCode INT NOT NULL,
    price INT NOT NULL,
    operation CHAR(5) NOT NULL,
    size FLOAT(4,2) NOT NULL,
    rooms INT NOT NULL,
    bathrooms INT NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    priceByArea FLOAT,
    propertyType CHAR,
    floorNumeric FLOAT,
    PRIMARY KEY (propertyCode)
);

CREATE TABLE sale(

	unnamed INT NOT NULL,
    propertyCode INT NOT NULL,
    price INT NOT NULL,
    operation CHAR(5) NOT NULL,
    size FLOAT(4,2) NOT NULL,
    rooms INT NOT NULL,
    bathrooms INT NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    priceByArea FLOAT,
    propertyType CHAR,
    floorNumeric FLOAT,
    PRIMARY KEY (propertyCode)
);

CREATE TABLE rent_test(

	unnamed INT NOT NULL,
    propertyCode INT NOT NULL,
    price INT NOT NULL,
    operation CHAR(5) NOT NULL,
    size FLOAT(4,2) NOT NULL,
    rooms INT NOT NULL,
    bathrooms INT NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    priceByArea FLOAT,
    propertyType CHAR,
    floorNumeric FLOAT,
    PRIMARY KEY (propertyCode)
);

CREATE TABLE sale_test(

	unnamed INT NOT NULL,
    propertyCode INT NOT NULL,
    price INT NOT NULL,
    operation CHAR(5) NOT NULL,
    size FLOAT(4,2) NOT NULL,
    rooms INT NOT NULL,
    bathrooms INT NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    priceByArea FLOAT,
    propertyType CHAR,
    floorNumeric FLOAT,
    PRIMARY KEY (propertyCode)
);
