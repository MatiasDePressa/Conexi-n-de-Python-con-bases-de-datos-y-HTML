CREATE DATABASE IF NOT EXISTS escuela;

USE escuela;

CREATE TABLE alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    edad INT NOT NULL,
    carrera VARCHAR(255) NOT NULL,
    nota DECIMAL(4,2) NOT NULL
);