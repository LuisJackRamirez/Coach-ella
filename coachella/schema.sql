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