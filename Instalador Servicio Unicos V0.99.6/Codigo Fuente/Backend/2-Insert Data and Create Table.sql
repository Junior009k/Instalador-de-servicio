CREATE TABLE "Frame" (
	"id"	INTEGER,
	"Descripcion"	TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE "Color" (
	"id"	INTEGER,
	"color"	INTEGER,
	"descripcion"	INTEGER,
	PRIMARY KEY("id")
);

CREATE TABLE "estadoColor" (
	"id"	INTEGER,
	"Descripcion"	INTEGER,
	"Estado"	TEXT,
	"Color"	INTEGER,
	"Frame"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("Color") REFERENCES Color(id),
	FOREIGN KEY("Frame") REFERENCES Frame(id)
);

Insert into Frame 
Values 
(1, "Instalador de Servicio"),
(2, "Creador de aplicaciones en el IIS"),
(3, "Instalador de Servicio");



Insert into estadoColor 
Values 
(1, "Activo",1,1,1),
(2, "Activo",1,2,2),
(3, "Activo",1,2,2);

