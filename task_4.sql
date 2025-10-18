-- Print the full description of the table 'Books' without using DESCRIBE or EXPLAIN.
-- Queries the Information Schema, explicitly targeting the 'alx_book_store' database.
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store'
AND
    TABLE_NAME = 'Books';
