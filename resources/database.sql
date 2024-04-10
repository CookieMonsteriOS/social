CREATE TABLE users (
    ID int NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (ID)  -- Defining ID as the primary key
);

CREATE TABLE posts (
    ID int NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    user_id int NOT NULL,
    PRIMARY KEY (ID),  -- Defining ID as the primary key
    FOREIGN KEY (user_id) REFERENCES users(ID)
);

DELIMITER //

CREATE PROCEDURE SeedTables()
BEGIN
    -- Insert sample data into the users table
    INSERT INTO users (name, email) VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com'),
    ('Michael Johnson', 'michael@example.com');

    -- Insert sample data into the posts table
    INSERT INTO posts (title, content, user_id) VALUES
    ('First Post', 'This is the content of the first post.', 1),
    ('Second Post', 'This is the content of the second post.', 2),
    ('Third Post', 'This is the content of the third post.', 3);
END //

DELIMITER ;

CALL SeedTables();

