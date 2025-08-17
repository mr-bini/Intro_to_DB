-- task_3.sql

-- Check if the correct database is selected
SELECT DATABASE() AS current_database;
IF current_database != 'alx_book_store' THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Incorrect database selected. Please use alx_book_store.';
END IF;

-- List all tables in the alx_book_store database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';
