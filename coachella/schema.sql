DROP TABLE IF EXISTS carrera;
DROP TABLE IF EXISTS materia_actual;
DROP TABLE IF EXISTS materia_cursada;
DROP TABLE IF EXISTS materia;
DROP TABLE IF EXISTS alumno;

CREATE TABLE alumno (
    username char(10) PRIMARY KEY NOT NULL,
    passwrd char(16) NOT NULL
);

CREATE TABLE materia (
    id char(4) NOT NULL,
    nombre char(128) NOT NULL,
    grupo char(8) NOT NULL,
    primary key (id, grupo)
);

CREATE TABLE materia_cursada (
    alumno_id char(10) NOT NULL,
    materia_id char(4) NOT NULL,
    grupo char(8) NOT NULL,
    periodo TEXT NOT NULL,
    calif INT NOT NULL,
    eval TEXT NOT NULL,
    FOREIGN KEY (alumno_id) REFERENCES alumno(username),
    FOREIGN KEY (materia_id, grupo) REFERENCES materia(id, grupo)
);

CREATE TABLE materia_actual (
    alumno_id char(10) NOT NULL,
    materia_id char(4) NOT NULL,
    grupo char(8) NOT NULL,
    dia char(3) NOT NULL,
    hora char(4) NOT NULL,
    FOREIGN KEY (alumno_id) REFERENCES alumno (username),
    FOREIGN KEY (materia_id, grupo) REFERENCES materia(id, grupo),
    PRIMARY KEY (dia, hora)
);

CREATE TABLE carrera (
    alumno_id char(10) NOT NULL,
    
    FOREIGN KEY (alumno_id) REFERENCES alumno (username)
);

INSERT INTO alumno (username,passwrd) VALUES (
    "2019630387",
    "JackRourke343"
);
INSERT INTO materia (id,nombre,grupo) VALUES (
    "C105",
    "Programacion orientada a objetos",
    "2CM14"
);
INSERT INTO materia (id,nombre,grupo) VALUES (
    "C107",
    "Probabilidad y estadistica",
    "2CM14"
);
INSERT INTO materia (id,nombre,grupo) VALUES (
    "C117",
    "Ecuaciones diferenciales",
    "1CM12"
);
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C105",
        "2CM14",
        "Lun",
        "1200"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C105",
        "2CM14",
        "Mie",
        "1330"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C105",
        "2CM14",
        "Jue",
        "1200"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C117",
        "1CM12",
        "Lun",
        "1030"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C117",
        "1CM12",
        "Mie",
        "0800"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C117",
        "1CM12",
        "Jue",
        "1030"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C107",
        "2CM14",
        "Mar",
        "1030"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C107",
        "2CM14",
        "Mie",
        "1030"
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        "2019630387",
        "C107",
        "2CM14",
        "Vie",
        "1030"
    );