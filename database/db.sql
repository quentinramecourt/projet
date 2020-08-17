USE utilisateurs;
CREATE TABLE users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255), 
    naissance DATE NOT NULL,
    email VARCHAR(50) NOT NULL,
    login VARCHAR(16),
    mot_de_passe VARCHAR(30) NOT NULL,
    done TINYINT(1)
); 