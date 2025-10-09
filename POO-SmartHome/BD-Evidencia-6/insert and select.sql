INSERT INTO ROLES (NOMBRE, DESCRIPCION) VALUES
('Administrador', 'Rol con todos los permisos'),
('Usuario', 'Rol con permisos limitados');

SELECT * FROM ROLES;
SELECT NOMBRE, DESCRIPCION FROM ROLES ORDER BY NOMBRE ASC;
SELECT * FROM ROLES WHERE NOMBRE = 'Administrador';

INSERT INTO USUARIOS (LOGIN, NOMBRE, CLAVE, ROL, EMAIL) VALUES
('admin', 'Sofía Monje', 'admin123', 1, 'sofia.monje@gmail.com'),
('user1', 'Ana Gómez', 'clave1', 2, 'ana.gomez@gmail.com'),
('user2', 'Carlos Pérez', 'clave2', 2, 'carlos.perez@yahoo.com'),
('user3', 'Lucía Torres', 'clave3', 2, 'lucia.torres@hotmail.com'),
('user4', 'Martín Díaz', 'clave4', 2, 'martin.diaz@gmail.com'),
('user5', 'María López', 'clave5', 2, 'maria.lopez@gmail.com'),
('user6', 'Pedro Fernández', 'clave6', 2, 'pedro.fernandez@gmail.com'),
('user7', 'Laura Castro', 'clave7', 2, 'laura.castro@gmail.com'),
('user8', 'Diego Sánchez', 'clave8', 2, 'diego.sanchez@gmail.com'),
('user9', 'Julia Romero', 'clave9', 2, 'julia.romero@gmail.com'),
('user10', 'Gonzalo Ruiz', 'clave10', 2, 'gonzalo.ruiz@gmail.com'),
('user11', 'Valentina Herrera', 'clave11', 2, 'valentina.herrera@gmail.com'),
('user12', 'Sebastián Gómez', 'clave12', 2, 'sebastian.gomez@gmail.com'),
('user13', 'Camila Vega', 'clave13', 2, 'camila.vega@gmail.com'),
('user14', 'Franco Ortiz', 'clave14', 2, 'franco.ortiz@gmail.com'),
('user15', 'Sol Morales', 'clave15', 2, 'sol.morales@gmail.com'),
('user16', 'Ignacio Silva', 'clave16', 2, 'ignacio.silva@gmail.com'),
('user17', 'Carolina Ruiz', 'clave17', 2, 'carolina.ruiz@gmail.com'),
('user18', 'Pablo Navarro', 'clave18', 2, 'pablo.navarro@gmail.com'),
('user19', 'Brenda Cabrera', 'clave19', 2, 'brenda.cabrera@gmail.com'),
('user20', 'Federico Blanco', 'clave20', 2, 'federico.blanco@gmail.com'),
('user21', 'Romina Paredes', 'clave21', 2, 'romina.paredes@gmail.com'),
('user22', 'Tomás Ibáñez', 'clave22', 2, 'tomas.ibanez@gmail.com'),
('user23', 'Melina Duarte', 'clave23', 2, 'melina.duarte@gmail.com'),
('user24', 'Gabriel Soto', 'clave24', 2, 'gabriel.soto@gmail.com'),
('user25', 'Luz González', 'clave25', 2, 'luz.gonzalez@gmail.com'),
('user26', 'Daniel Rivas', 'clave26', 2, 'daniel.rivas@gmail.com'),
('user27', 'Nicolás Bravo', 'clave27', 2, 'nicolas.bravo@gmail.com'),
('user28', 'Rocío Herrera', 'clave28', 2, 'rocio.herrera@gmail.com'),
('user29', 'Elena Fuentes', 'clave29', 2, 'elena.fuentes@gmail.com');

SELECT * FROM USUARIOS;
SELECT LOGIN, NOMBRE, EMAIL FROM USUARIOS ORDER BY NOMBRE ASC;
SELECT NOMBRE, LOGIN, ROL FROM USUARIOS WHERE ROL = 2;

INSERT INTO UBICACIONES (NOMBRE, DESCRIPCION) VALUES
('Cocina', 'Área de cocina principal'),
('Comedor', 'Zona de comedor'),
('Sala de estar', 'Área de descanso y TV'),
('Dormitorio principal', 'Habitación principal'),
('Dormitorio 2', 'Habitación secundaria'),
('Baño principal', 'Baño completo'),
('Baño de visitas', 'Baño pequeño'),
('Garage', 'Espacio de estacionamiento'),
('Patio', 'Área exterior principal'),
('Lavadero', 'Zona de lavado'),
('Oficina', 'Oficina doméstica'),
('Balcón', 'Espacio con vista al exterior'),
('Terraza', 'Área abierta superior'),
('Pasillo', 'Conexión entre ambientes'),
('Jardín', 'Espacio verde exterior'),
('Sótano', 'Área subterránea'),
('Entrada', 'Ingreso principal'),
('Cuarto de juegos', 'Espacio de entretenimiento'),
('Gimnasio', 'Área de ejercicio'),
('Biblioteca', 'Espacio de lectura'),
('Depósito', 'Zona de almacenamiento'),
('Cuarto técnico', 'Área de mantenimiento'),
('Vestidor', 'Espacio de ropa y accesorios'),
('Comedor diario', 'Zona de desayuno'),
('Altillo', 'Espacio superior'),
('Lavadero exterior', 'Área de lavado al aire libre'),
('Pérgola', 'Área techada exterior'),
('Piscina', 'Zona de natación'),
('Cuarto de invitados', 'Habitación de visitas'),
('Cava', 'Espacio para vinos');

SELECT * FROM UBICACIONES;
SELECT NOMBRE, DESCRIPCION FROM UBICACIONES;
SELECT * FROM UBICACIONES WHERE NOMBRE LIKE '%Sala%';

INSERT INTO TIPOSDISPOSITIVO (NOMBRE_TIPO, DESCRIPCION) VALUES
('Luz', 'Lámparas y luminarias inteligentes'),
('Cámara', 'Cámaras de seguridad IP'),
('Sensor de movimiento', 'Detectores PIR de presencia'),
('Climatización', 'Aires acondicionados o calefactores'),
('Persianas', 'Persianas automáticas'),
('Alarma', 'Sistemas de alarma sonora o silenciosa');

SELECT * FROM TIPOSDISPOSITIVO;
SELECT NOMBRE_TIPO, DESCRIPCION FROM TIPOSDISPOSITIVO ORDER BY NOMBRE_TIPO ASC;
SELECT * FROM TIPOSDISPOSITIVO WHERE NOMBRE_TIPO LIKE '%Luz%';


INSERT INTO DISPOSITIVOS (NOMBRE_DISPOSITIVO, ESTADO_ACTUAL, ID_TIPO_DISPOSITIVO, ID_USUARIO, ID_UBICACION) VALUES
('Luz cocina', 'Encendido', 1, 1, 1),
('Cámara sala', 'Apagado', 2, 1, 3),
('Sensor pasillo', 'Activo', 3, 2, 14),
('Aire dormitorio', 'Encendido', 4, 3, 4),
('Persiana comedor', 'Cerrada', 5, 4, 2),
('Alarma principal', 'Activa', 6, 1, 17),
('Luz garage', 'Apagado', 1, 5, 8),
('Luz jardín', 'Encendido', 1, 6, 15),
('Cámara patio', 'Encendido', 2, 7, 9),
('Sensor terraza', 'Activo', 3, 8, 13),
('Aire living', 'Apagado', 4, 9, 3),
('Luz baño', 'Encendido', 1, 10, 6),
('Persiana dormitorio', 'Abierta', 5, 11, 4),
('Alarma exterior', 'Activa', 6, 12, 9),
('Cámara entrada', 'Encendido', 2, 13, 17),
('Sensor cocina', 'Inactivo', 3, 14, 1),
('Luz pasillo', 'Apagado', 1, 15, 14),
('Aire oficina', 'Encendido', 4, 16, 11),
('Luz patio', 'Encendido', 1, 17, 9),
('Persiana balcón', 'Cerrada', 5, 18, 12),
('Cámara jardín', 'Encendido', 2, 19, 15),
('Luz terraza', 'Encendido', 1, 20, 13),
('Aire comedor', 'Apagado', 4, 21, 2),
('Sensor garage', 'Activo', 3, 22, 8),
('Luz dormitorio 2', 'Apagado', 1, 23, 5),
('Persiana oficina', 'Abierta', 5, 24, 11),
('Cámara gimnasio', 'Encendido', 2, 25, 19),
('Alarma interior', 'Activa', 6, 26, 3),
('Sensor jardín', 'Activo', 3, 27, 15),
('Luz biblioteca', 'Encendido', 1, 28, 20);

SELECT * FROM DISPOSITIVOS;
SELECT NOMBRE_DISPOSITIVO, ESTADO_ACTUAL FROM DISPOSITIVOS WHERE ESTADO_ACTUAL = 'Encendido';
SELECT NOMBRE_DISPOSITIVO, ID_UBICACION FROM DISPOSITIVOS ORDER BY ID_UBICACION ASC;



INSERT INTO ESCENARIOS (NOMBRE_ESCENARIO, DESCRIPCION, ID_USUARIO) VALUES
('Modo Noche', 'Apagar luces y activar alarma', 1),
('Modo Día', 'Encender luces principales', 2),
('Modo Trabajo', 'Apagar TV y luces del living', 3),
('Modo Fiesta', 'Luces de colores y música', 4),
('Modo Vacaciones', 'Activar sensores y alarmas', 5),
('Modo Ahorro', 'Reducir consumo de energía', 6),
('Modo Lectura', 'Encender lámpara de lectura', 7),
('Modo Cine', 'Bajar persianas y apagar luces', 8),
('Modo Cocina', 'Encender luces y extractor', 9),
('Modo Invierno', 'Encender calefacción', 10),
('Modo Verano', 'Encender aire acondicionado', 11),
('Modo Seguridad', 'Activar cámaras y sensores', 12),
('Modo Salida', 'Apagar todo y activar alarma', 13),
('Modo Entrada', 'Encender luces de entrada', 14),
('Modo Limpieza', 'Encender luces y ventilación', 15),
('Modo Jardín', 'Encender luces del jardín', 16),
('Modo Noche Infantil', 'Apagar luces principales', 17),
('Modo Desayuno', 'Encender luces de cocina', 18),
('Modo Ejercicio', 'Encender aire y luces del gym', 19),
('Modo Lectura Nocturna', 'Encender lámpara y apagar TV', 20),
('Modo Estudio', 'Iluminación y silencio', 21),
('Modo Siesta', 'Bajar persianas y apagar luces', 22),
('Modo Reunión', 'Encender luz y cámara', 23),
('Modo Clásico', 'Ambiente cálido y luces suaves', 24),
('Modo Frío', 'Encender aire y luz blanca', 25),
('Modo Gamer', 'Luces RGB y ventiladores activos', 26),
('Modo Nieve', 'Aumentar temperatura ambiente', 27),
('Modo Exterior', 'Encender luces de patio y jardín', 28),
('Modo Cine Familiar', 'Bajar persianas y encender TV', 29),
('Modo Relajación', 'Luz tenue y música suave', 30);


SELECT * FROM ESCENARIOS;
SELECT NOMBRE_ESCENARIO, DESCRIPCION FROM ESCENARIOS;
SELECT * FROM ESCENARIOS WHERE ID_USUARIO = 1;

INSERT INTO ESCENARIOACCIONESDISPOSITVOS (ACCION_DETALLE, ID_ESCENARIO, ID_DISPOSITIVO) VALUES
('Apagar todas las luces', 1, 1),
('Encender luces principales', 2, 3),
('Activar alarma principal', 1, 6),
('Encender aire acondicionado', 11, 4),
('Cerrar persianas del living', 8, 5),
('Encender luces del jardín', 16, 8);


SELECT * FROM ESCENARIOACCIONESDISPOSITVOS;
SELECT ACCION_DETALLE, ID_DISPOSITIVO FROM ESCENARIOACCIONESDISPOSITVOS;
SELECT * FROM ESCENARIOACCIONESDISPOSITVOS WHERE ID_ESCENARIO = 1;

