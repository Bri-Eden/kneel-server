CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Order`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metal`(`id`),
	FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`)
);

CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` TEXT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

INSERT INTO `Metal` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metal` VALUES (null, "14K Gold", 736.4);
INSERT INTO `Metal` VALUES (null, "24K Gold", 1258.9);
INSERT INTO `Metal` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metal` VALUES (null, "Palladium", 1241);

INSERT INTO `Size` VALUES (null, "0.5", 405);
INSERT INTO `Size` VALUES (null, "0.75", 782);
INSERT INTO `Size` VALUES (null, "1", 1470);
INSERT INTO `Size` VALUES (null, "1.5", 1997);
INSERT INTO `Size` VALUES (null, "2", 3638);

INSERT INTO `Style` VALUES (null, "Classic", 500);
INSERT INTO `Style` VALUES (null, "Modern", 710);
INSERT INTO `Style` VALUES (null, "Vintage", 965);

INSERT INTO `Order` VALUES (null, 2, 5, 1);
INSERT INTO `Order` VALUES (null, 5, 5, 2);
INSERT INTO `Order` VALUES (null, 1, 3, 3);
INSERT INTO `Order` VALUES (null, 3, 5, 2);
INSERT INTO `Order` VALUES (null, 4, 3, 3);
INSERT INTO `Order` VALUES (null, 2, 4, 1);
INSERT INTO `Order` VALUES (null, 1, 2, 1);

SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    m.metal metal_name,
    m.price metal_price,
    z.carets size_carets,
    z.price size_price,
    s.style style_name,
    s.price style_price     
FROM `Order` o
JOIN Metal m 
    ON m.id = o.metal_id
JOIN Size z
    ON z.id = o.size_id
JOIN Style s
    ON s.id = o.style_id

