INSERT INTO ROLES (NOMBRE, DESCRIPCION) VALUES
('Administrador', 'Rol con todos los permisos'),
('Usuario', 'Rol con permisos limitados');

INSERT INTO USUARIOS (LOGIN, NOMBRE, CLAVE, ROL, EMAIL) VALUES
('admin', 'Sofia Monje', 'admin123', 1, 'sofia_monje@gmail.com'),
('usuario1', 'Ana Gomez', 'clave123', 2, 'ana.gomez@yahoo.com.ar');

SELECT * FROM ROLES;

SELECT u.ID_USUARIO, u.NOMBRE, u.LOGIN, r.NOMBRE AS ROL
FROM USUARIOS u
JOIN ROLES r ON u.ROL = r.ID_ROL;

INSERT INTO UBICACIONES (NOMBRE, DESCRIPCION) VALUES
('Cocina', 'Ubicación de la cocina A'),
('Sala de living', 'Sala del living'),
('Dormitorio Central', 'Ubicación del dormitorio principal');

INSERT INTO TIPOSDISPOSITIVO (NOMBRE_TIPO, DESCRIPCION) VALUES
('Luz', 'Luces de la casa'),
('Camara', 'Camaras de seguridad');

SELECT * FROM UBICACIONES;
SELECT * FROM TIPOSDISPOSITIVO;