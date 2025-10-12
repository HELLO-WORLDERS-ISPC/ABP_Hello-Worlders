USE smart_home;

INSERT INTO ROLES (NOMBRE, DESCRIPCION) VALUES
('Administrador', 'Acceso total al sistema'),
('Usuario', 'Acceso limitado a sus dispositivos');


INSERT INTO USUARIOS (LOGIN, NOMBRE, CLAVE, ROL, EMAIL) VALUES
('admin', 'Sofía Monje', 'admin123', 1, 'sofia.monje@gmail.com'),
('user02', 'Carlos Pérez', 'clave02', 2, 'carlos.perez@gmail.com'),
('user03', 'Lucía Torres', 'clave03', 2, 'lucia.torres@hotmail.com'),
('user04', 'Martín Díaz', 'clave04', 2, 'martin.diaz@gmail.com'),
('user05', 'Ana Gómez', 'clave05', 2, 'ana.gomez@gmail.com'),
('user06', 'Mariano López', 'clave06', 2, 'mariano.lopez@gmail.com'),
('user07', 'Julia Romero', 'clave07', 2, 'julia.romero@gmail.com'),
('user08', 'Tomás Herrera', 'clave08', 2, 'tomas.herrera@gmail.com'),
('user09', 'Valentina Silva', 'clave09', 2, 'valentina.silva@gmail.com'),
('user10', 'Ignacio Vega', 'clave10', 2, 'ignacio.vega@gmail.com'),
('user11', 'Camila Cabrera', 'clave11', 2, 'camila.cabrera@gmail.com'),
('user12', 'Franco Morales', 'clave12', 2, 'franco.morales@gmail.com'),
('user13', 'Rocío Duarte', 'clave13', 2, 'rocio.duarte@gmail.com'),
('user14', 'Ezequiel Soto', 'clave14', 2, 'ezequiel.soto@gmail.com'),
('user15', 'Sol Fernández', 'clave15', 2, 'sol.fernandez@gmail.com'),
('user16', 'Pablo Ortiz', 'clave16', 2, 'pablo.ortiz@gmail.com'),
('user17', 'Marina Ruiz', 'clave17', 2, 'marina.ruiz@gmail.com'),
('user18', 'Gastón Bravo', 'clave18', 2, 'gaston.bravo@gmail.com'),
('user19', 'Carolina Ibáñez', 'clave19', 2, 'carolina.ibanez@gmail.com'),
('user20', 'Lautaro Blanco', 'clave20', 2, 'lautaro.blanco@gmail.com'),
('user21', 'Brenda Rivas', 'clave21', 2, 'brenda.rivas@gmail.com'),
('user22', 'Nicolás Paredes', 'clave22', 2, 'nicolas.paredes@gmail.com'),
('user23', 'Luz Gutiérrez', 'clave23', 2, 'luz.gutierrez@gmail.com'),
('user24', 'Gabriel Soto', 'clave24', 2, 'gabriel.soto@gmail.com'),
('user25', 'Melina Duarte', 'clave25', 2, 'melina.duarte@gmail.com'),
('user26', 'Romina Vega', 'clave26', 2, 'romina.vega@gmail.com'),
('user27', 'Daniel Rivas', 'clave27', 2, 'daniel.rivas@gmail.com'),
('user28', 'Federico Gómez', 'clave28', 2, 'federico.gomez@gmail.com'),
('user29', 'Laura Fernández', 'clave29', 2, 'laura.fernandez@gmail.com'),
('user30', 'Elena Fuentes', 'clave30', 2, 'elena.fuentes@gmail.com');


INSERT INTO UBICACIONES (NOMBRE, DESCRIPCION) VALUES
('Cocina', 'Espacio principal para cocinar'),
('Comedor', 'Zona para comer'),
('Living', 'Sala principal de estar'),
('Dormitorio 1', 'Habitación principal'),
('Dormitorio 2', 'Habitación secundaria'),
('Baño Principal', 'Baño completo con ducha'),
('Baño Visitas', 'Baño pequeño para invitados'),
('Garage', 'Espacio de estacionamiento'),
('Patio', 'Zona exterior al aire libre'),
('Terraza', 'Espacio exterior superior'),
('Oficina', 'Área de trabajo'),
('Lavadero', 'Zona para lavar y secar'),
('Balcón', 'Espacio con vista al exterior'),
('Jardín', 'Zona verde con plantas'),
('Cuarto de Juegos', 'Área recreativa'),
('Sótano', 'Espacio de almacenamiento'),
('Biblioteca', 'Lugar de lectura'),
('Vestidor', 'Zona de vestimenta'),
('Depósito', 'Almacén doméstico'),
('Entrada', 'Ingreso principal de la casa'),
('Pasillo', 'Conexión entre ambientes'),
('Altillo', 'Espacio superior reducido'),
('Cava', 'Almacenamiento de vinos'),
('Piscina', 'Zona de natación'),
('Pérgola', 'Espacio techado al aire libre'),
('Cuarto de Invitados', 'Habitación de visitas'),
('Gimnasio', 'Área de entrenamiento'),
('Cine Hogareño', 'Sala multimedia'),
('Sala de Reunión', 'Espacio de encuentro'),
('Taller', 'Área para bricolaje');


INSERT INTO TIPOSDISPOSITIVO (NOMBRE_TIPO, DESCRIPCION) VALUES
('Luz', 'Luminaria o foco inteligente'),
('Cámara', 'Cámara de seguridad IP'),
('Sensor de movimiento', 'Detector PIR de presencia'),
('Climatización', 'Aire acondicionado o calefactor'),
('Alarma', 'Sistema de alerta o sirena'),
('Persiana', 'Persiana eléctrica automatizada');


INSERT INTO ESTADODISPOSITIVO (ACCION_DETALLE) VALUES
('Apagar'),
('Encender');


INSERT INTO ESCENARIOS (NOMBRE_ESCENARIO, ID_TIPO_DISPOSITIVO, ID_UBICACION, ID_ACCION) VALUES
('Modo Dormir', 1, 3, 1),    
('Modo Noche', 1, 1, 2),     
('Modo Seguridad', 2, 4, 2), 
('Modo Descanso', 4, 3, 1), 
('Modo Trabajo', 4, 5, 2),
('Modo Ahorro Energético', 4, 1, 1);

INSERT INTO DISPOSITIVOS (NOMBRE_DISPOSITIVO, ID_ACCION, ID_TIPO_DISPOSITIVO, ID_USUARIO, ID_UBICACION) VALUES
('Luz Cocina', 2, 1, 1, 1),
('Luz Comedor', 2, 1, 2, 2),
('Luz Living', 2, 1, 3, 3),
('Cámara Entrada', 2, 2, 4, 20),
('Cámara Patio', 2, 2, 5, 9),
('Cámara Garage', 2, 2, 6, 8),
('Sensor Movimiento Pasillo', 1, 3, 7, 21),
('Sensor Dormitorio', 1, 3, 8, 4),
('Sensor Cocina', 1, 3, 9, 1),
('Sensor Baño', 1, 3, 10, 6),
('Aire Dormitorio', 2, 4, 11, 4),
('Aire Living', 2, 4, 12, 3),
('Aire Oficina', 2, 4, 13, 11),
('Aire Gimnasio', 2, 4, 14, 27),
('Persiana Dormitorio', 1, 6, 15, 4),
('Persiana Oficina', 1, 6, 16, 11),
('Persiana Living', 1, 6, 17, 3),
('Persiana Comedor', 1, 6, 18, 2),
('Alarma General', 2, 5, 19, 20),
('Alarma Patio', 2, 5, 20, 9),
('Luz Baño', 2, 1, 21, 6),
('Luz Terraza', 2, 1, 22, 10),
('Luz Piscina', 2, 1, 23, 24),
('Luz Jardín', 2, 1, 24, 14),
('Cámara Oficina', 1, 2, 25, 11),
('Cámara Gimnasio', 1, 2, 26, 27),
('Sensor Garage', 1, 3, 27, 8),
('Sensor Jardín', 1, 3, 28, 14),
('Aire Comedor', 2, 4, 29, 2),
('Luz Cine', 2, 1, 30, 28);

-- ROLES
SELECT * FROM ROLES;
SELECT ID_ROL, NOMBRE FROM ROLES;
SELECT NOMBRE FROM ROLES WHERE NOMBRE = 'Administrador';

-- USUARIOS
SELECT * FROM USUARIOS;
SELECT NOMBRE, EMAIL FROM USUARIOS ORDER BY NOMBRE;
SELECT NOMBRE FROM USUARIOS WHERE ROL = 2;

-- UBICACIONES
SELECT * FROM UBICACIONES;
SELECT NOMBRE  FROM UBICACIONES ORDER BY ID_UBICACION;
SELECT NOMBRE, DESCRIPCION FROM UBICACIONES WHERE NOMBRE LIKE '%Sala%';

-- TIPOSDISPOSITIVO
SELECT * FROM TIPOSDISPOSITIVO;
SELECT NOMBRE_TIPO FROM TIPOSDISPOSITIVO;
SELECT NOMBRE_TIPO FROM TIPOSDISPOSITIVO WHERE NOMBRE_TIPO LIKE '%Luz%';

-- ESTADODISPOSITIVO
SELECT * FROM ESTADODISPOSITIVO;
SELECT ACCION_DETALLE FROM ESTADODISPOSITIVO;
SELECT * FROM ESTADODISPOSITIVO WHERE ACCION_DETALLE = 'Encender';

-- ESCENARIOS
SELECT * FROM ESCENARIOS;
SELECT NOMBRE_ESCENARIO, ID_TIPO_DISPOSITIVO FROM ESCENARIOS;
SELECT NOMBRE_ESCENARIO FROM ESCENARIOS WHERE ID_ACCION = 2;

-- DISPOSITIVOS
SELECT * FROM DISPOSITIVOS;
SELECT NOMBRE_DISPOSITIVO, ID_ACCION FROM DISPOSITIVOS;
SELECT NOMBRE_DISPOSITIVO FROM DISPOSITIVOS WHERE ID_ACCION = 2;

-- CONSULTAS, SUBCONSULTAS Y FILTROS
SELECT 
  d.NOMBRE_DISPOSITIVO,
  a.ACCION_DETALLE AS ACCION
FROM DISPOSITIVOS d
JOIN ESTADODISPOSITIVO a 
  ON d.ID_ACCION = a.ID_ACCION;

SELECT 
  e.NOMBRE_ESCENARIO,
  t.NOMBRE_TIPO AS TIPO_DISPOSITIVO,
  u.NOMBRE AS UBICACION,
  a.ACCION_DETALLE AS ACCION
FROM ESCENARIOS e 
JOIN TIPOSDISPOSITIVO t ON e.ID_TIPO_DISPOSITIVO = t.ID_TIPO_DISPOSITIVO
JOIN UBICACIONES u ON e.ID_UBICACION = u.ID_UBICACION
JOIN ESTADODISPOSITIVO a ON e.ID_ACCION = a.ID_ACCION;


SELECT 
  e.NOMBRE_ESCENARIO,
  t.NOMBRE_TIPO AS TIPO_DISPOSITIVO,
  u.NOMBRE AS UBICACION,
  a.ACCION_DETALLE AS ACCION
FROM ESCENARIOS e
JOIN TIPOSDISPOSITIVO t ON e.ID_TIPO_DISPOSITIVO = t.ID_TIPO_DISPOSITIVO
JOIN UBICACIONES u ON e.ID_UBICACION = u.ID_UBICACION
JOIN ESTADODISPOSITIVO a ON e.ID_ACCION = a.ID_ACCION
WHERE t.NOMBRE_TIPO = 'Luz';


SELECT 
  d.NOMBRE_DISPOSITIVO,
  t.NOMBRE_TIPO AS TIPO_DISPOSITIVO,
  u.NOMBRE AS UBICACION,
  a.ACCION_DETALLE AS ACCION,
  us.NOMBRE AS USUARIO
FROM DISPOSITIVOS d
JOIN TIPOSDISPOSITIVO t ON d.ID_TIPO_DISPOSITIVO = t.ID_TIPO_DISPOSITIVO
JOIN UBICACIONES u ON d.ID_UBICACION = u.ID_UBICACION
JOIN ESTADODISPOSITIVO a ON d.ID_ACCION = a.ID_ACCION
JOIN USUARIOS us ON d.ID_USUARIO = us.ID_USUARIO
WHERE t.NOMBRE_TIPO = 'Luz';