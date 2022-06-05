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
    reprobadas INT NOT NULL,
    /*creditos_total float(5,2) NOT NULL,
    creditos_pend float(5,2) NOT NULL,
    creditos_repr float(5,2) NOT NULL,*/
    creditos_total NUMERIC(5,2) NOT NULL,
    creditos_pend NUMERIC(5,2) NOT NULL,
    creditos_repr NUMERIC(5,2) NOT NULL,
    periodos_cursados INT NOT NULL,
    periodos_disponibles INT NOT NULL,
    carga_auth char(3) NOT NULL,
    
    FOREIGN KEY (alumno_id) REFERENCES alumno (username)
);

/* Test queries, must be removed */
INSERT INTO alumno (username,passwrd) VALUES (
    '2019630387',
    'JackRourke343'
);

INSERT INTO alumno (username,passwrd) VALUES (
    '2015630007',
    'password'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C105',
    'Programacion orientada a objetos',
    '2CM14'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C107',
    'Probabilidad y estadistica',
    '2CM14'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C117',
    'Ecuaciones diferenciales',
    '1CM12'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C200',
    'Estructuras de datos',
    '1CM11'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C404',
    'Algebra lineal',
    '1CM14'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C101',
    'Fundamentos economicos',
    '2CM06'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C286',
    'Calculo vectorial',
    '1CM01'
);

INSERT INTO materia (id,nombre,grupo) VALUES (
    'C210',
    'Trabajo Terminal I',
    '5CMX'
);

INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C105',
        '2CM14',
        'Lun',
        '1200'
    );
    
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C105',
        '2CM14',
        'Mie',
        '1330'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C105',
        '2CM14',
        'Jue',
        '1200'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C117',
        '1CM12',
        'Lun',
        '1030'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C117',
        '1CM12',
        'Mie',
        '0800'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C117',
        '1CM12',
        'Jue',
        '1030'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C107',
        '2CM14',
        'Mar',
        '1030'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C107',
        '2CM14',
        'Mie',
        '1030'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2019630387',
        'C107',
        '2CM14',
        'Vie',
        '1030'
    );
INSERT INTO materia_actual (
    alumno_id,
    materia_id,
    grupo,
    dia,
    hora
    ) VALUES (
        '2015630007',
        'C210',
        '5CMX',
        'Jue',
        '0830'
    );
INSERT INTO materia_cursada (
    alumno_id,
    materia_id,
    grupo,
    periodo,
    calif,
    eval
    ) VALUES (
        '2019630387',
        'C210',
        '5CMX',
        '22-1',
        9,
        'ord'
    );
INSERT INTO materia_cursada (
    alumno_id,
    materia_id,
    grupo,
    periodo,
    calif,
    eval
    ) VALUES (
        '2015630007',
        'C107',
        '2CM14',
        '19-2',
        6,
        'ext'
    );
INSERT INTO materia_cursada (
    alumno_id,
    materia_id,
    grupo,
    periodo,
    calif,
    eval
    ) VALUES (
        '2019630387',
        'C404',
        '1CM14',
        '20-1',
        9,
        'ord'
    );
INSERT INTO materia_cursada (
    alumno_id,
    materia_id,
    grupo,
    periodo,
    calif,
    eval
    ) VALUES (
        '2015630007',
        'C200',
        '1CM11',
        '16-2',
        10,
        'ets'
    );
INSERT INTO materia_cursada (
    alumno_id,
    materia_id,
    grupo,
    periodo,
    calif,
    eval
    ) VALUES (
        '2019630387',
        'C286',
        '1CM01',
        '19-1',
        6,
        'ord'
    );
INSERT INTO materia_cursada (
    alumno_id,
    materia_id,
    grupo,
    periodo,
    calif,
    eval
    ) VALUES (
        '2019630387',
        'C101',
        '2CM06',
        '20-1',
        8,
        'ord'
    );

INSERT INTO carrera (
    alumno_id,
    reprobadas,
    creditos_total,
    creditos_pend,
    creditos_repr,
    periodos_cursados,
    periodos_disponibles,
    carga_auth
) VALUES (
    '2019630387',
    0,
    196.03,
    33.57,
    0,
    7,
    7,
    'max'
);

INSERT INTO carrera (
    alumno_id,
    reprobadas,
    creditos_total,
    creditos_pend,
    creditos_repr,
    periodos_cursados,
    periodos_disponibles,
    carga_auth
) VALUES (
    '2015630007',
    5,
    96.03,
    133.57,
    61.00,
    8,
    2,
    'min'
);