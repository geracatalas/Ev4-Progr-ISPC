-- Crea la base de datos
CREATE DATABASE maquina_tiro_arco;
USE maquina_tiro_arco;

-- Crea las tablas
CREATE TABLE Arcos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fuerza_tiro FLOAT NOT NULL,
    angulo FLOAT NOT NULL
);

CREATE TABLE Tiros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    arco_id INT,
    distancia FLOAT NOT NULL,
    puntaje INT,
    FOREIGN KEY (arco_id) REFERENCES Arcos(id)
);

-- Una mejor alternativa sería quizas el agregar una tabla extra para ahí almacenar los puntajes, en lugar de guardarlos en la tabla de tiros


-- Insertar arcos
INSERT INTO Arcos (fuerza_tiro, angulo) VALUES (50, 45);
INSERT INTO Arcos (fuerza_tiro, angulo) VALUES (60, 30);
INSERT INTO Arcos (fuerza_tiro, angulo) VALUES (70, 60);
INSERT INTO Arcos (fuerza_tiro, angulo) VALUES (40, 40);
INSERT INTO Arcos (fuerza_tiro, angulo) VALUES (80, 50);

-- Insertar tiros con puntaje
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (1, 120.0, 8);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (1, 125.5, 10);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (2, 140.0, 9);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (3, 150.3, 10);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (4, 110.0, 7);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (5, 160.1, 9);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (2, 135.0, 8);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (3, 155.2, 10);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (1, 115.7, 8);
INSERT INTO Tiros (arco_id, distancia, puntaje) VALUES (4, 130.5, 6);


-- 1. Obtener todos los tiros con puntaje
SELECT * FROM Tiros;

-- 2. Calcular la puntuación total de cada arco
SELECT arco_id, SUM(puntaje) AS puntaje_total
FROM Tiros
GROUP BY arco_id;

-- 3. Obtener el tiro con el mayor puntaje
SELECT * FROM Tiros ORDER BY puntaje DESC LIMIT 1;

-- 4. Obtener la distancia promedio y puntaje promedio de los tiros por arco
SELECT arco_id, AVG(distancia) AS distancia_promedio, AVG(puntaje) AS puntaje_promedio
FROM Tiros
GROUP BY arco_id;

-- 5. Contar cuántos tiros ha realizado cada arco y el puntaje promedio
SELECT arco_id, COUNT(*) AS total_tiros, AVG(puntaje) AS puntaje_promedio
FROM Tiros
GROUP BY arco_id;
