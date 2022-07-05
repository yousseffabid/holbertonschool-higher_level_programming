--creates a table called first_table
IF NOT EXISTS (CREATE first_table(
    id INT,
    name VARCHAR(256));
);
