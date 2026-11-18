-- ====================================================================
-- SCRIPT DE BASE DE DATOS: SISTEMA VETERINARIO - REGISTRO DE ANIMALES
-- Motor: MySQL 8.4.11 LTS
-- ====================================================================

-- 1. Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS veterinaria_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 2. Seleccionar la base de datos
USE veterinaria_db;

-- 3. Crear la tabla para el registro de animales para sus citas
DROP TABLE IF EXISTS registro_citas_animales;

CREATE TABLE IF NOT EXISTS registro_citas_animales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_mascota VARCHAR(80) NOT NULL COMMENT 'Nombre del animal / mascota',
    especie VARCHAR(50) NOT NULL COMMENT 'Especie (Canino, Felino, Ave, Roedor, etc.)',
    raza VARCHAR(80) NOT NULL COMMENT 'Raza de la mascota',
    edad VARCHAR(30) NOT NULL COMMENT 'Edad estimada (ej. 2 años, 6 meses)',
    sexo ENUM('Macho', 'Hembra') NOT NULL COMMENT 'Sexo de la mascota',
    nombre_propietario VARCHAR(120) NOT NULL COMMENT 'Nombre completo del propietario',
    telefono_propietario VARCHAR(25) NOT NULL COMMENT 'Número telefónico de contacto',
    fecha_cita DATE NOT NULL COMMENT 'Fecha asignada para la cita médica',
    hora_cita TIME NOT NULL COMMENT 'Hora asignada para la cita',
    motivo_cita VARCHAR(255) NOT NULL COMMENT 'Razón de la cita médica veterinaria',
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de registro en el sistema',
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Fecha de última actualización'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Inserción de registros iniciales de prueba (Opcional para pruebas inmediatas)
INSERT INTO registro_citas_animales 
(nombre_mascota, especie, raza, edad, sexo, nombre_propietario, telefono_propietario, fecha_cita, hora_cita, motivo_cita)
VALUES
('Max', 'Canino', 'Golden Retriever', '3 años', 'Macho', 'Carlos Mendoza', '555-123-4567', CURDATE(), '10:00:00', 'Vacunación anual y desparasitación'),
('Luna', 'Felino', 'Siamés', '1 año y 4 meses', 'Hembra', 'Andrea Morales', '555-987-6543', CURDATE(), '11:30:00', 'Revisión general por falta de apetito'),
('Rocky', 'Canino', 'Bulldog Francés', '2 años', 'Macho', 'Roberto Gómez', '555-456-7890', DATE_ADD(CURDATE(), INTERVAL 1 DAY), '16:00:00', 'Limpieza dental y corte de uñas');
