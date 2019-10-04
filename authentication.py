DROP TABLE IF EXISTS auth

CREATE TABLE auth
(
    username text NOT NULL,
    pass text NOT NULL,
    role text NOT NULL
)

INSERT INTO auth VALUES
('investor', 'passw', 'User')


SELECT * FROM auth
COMMIT
