CREATE DATABASE dolphin_swim_school;

USE dolphin_swim_school;

CREATE TABLE teachers (
   lesson_teacher_id INT NOT NULL UNIQUE,
   teacher_name VARCHAR (10),
   PRIMARY KEY (lesson_teacher_id)
);

INSERT INTO teachers VALUES (1, "Becky"), (2, "Amy"), (3, "Alex");

CREATE TABLE messages (
   message_id INT NOT NULL AUTO_INCREMENT,
   lesson_teacher_id INT NOT NULL,
   message VARCHAR(200),
   PRIMARY KEY (message_id),
   FOREIGN KEY (lesson_teacher_id) REFERENCES teachers(lesson_teacher_id)
   );

INSERT INTO messages (lesson_teacher_id, message) VALUES (1, "I will be a bit late for my 10 o'clock lesson, Juila"), (3, "Hi Alex, Can you please give me a ring about our lesson tomorrow, Kacey");

CREATE TABLE lessons_times (
   lesson_time_id INT NOT NULL UNIQUE,
   lesson_time VARCHAR(10),
   PRIMARY KEY (lesson_time_id)
);

INSERT INTO lessons_times VALUES (1, "09-10"), (2, "10-11"), (3, "11-12"), (4, "14-15"), (5, "15-16"), (6, "16-17"); 

CREATE TABLE customers (
   customer_id INT NOT NULL AUTO_INCREMENT,
   customer_first_name VARCHAR(40),
   customer_last_name VARCHAR(40) NOT NULL,
   PRIMARY KEY (customer_id)
);

INSERT INTO customers VALUES (1, "Kacey", "Warwick"), (2, "Colby", "Sherborne"), (3, "Julia", "Chapman"), (4, "Catherine", "Moore"), (5, "Matthew", "Elliot"), (6, "Tiffany", "George"); 

CREATE TABLE lessons (
   lesson_id INT NOT NULL AUTO_INCREMENT,
   lesson_date VARCHAR(20) NOT NULL,
   lesson_time_id INT NOT NULL,
   lesson_teacher_id INT NOT NULL,
   customer_id INT,
   PRIMARY KEY (lesson_id),
   FOREIGN KEY (lesson_teacher_id) REFERENCES teachers(lesson_teacher_id),
   FOREIGN KEY (lesson_time_id) REFERENCES lessons_times(lesson_time_id),
   FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO lessons (lesson_date, lesson_time_id, lesson_teacher_id, customer_id) VALUES 
("2024-05-01", 1, 1, 1), ("2024-05-01", 2, 1, null), ("2024-05-01", 3, 1, 3), ("2024-05-01", 4, 2, null), ("2024-05-01", 5, 2, null), ("2024-05-01", 6, 2, 6),
("2024-05-02", 1, 1, null), ("2024-05-02", 2, 1, 2), ("2024-05-02", 3, 1, null), ("2024-05-02", 4, 2, null), ("2024-05-02", 5, 2, 5), ("2024-05-02", 6, 1, null),
("2024-05-03", 1, 3, null), ("2024-05-03", 2, 3, null), ("2024-05-03", 3, 3, 5), ("2024-05-03", 4, 1, null), ("2024-05-03", 5, 1, null), ("2024-05-03", 6, 1, 2),
("2024-05-06", 1, 3, 4), ("2024-05-06", 2, 3, null), ("2024-05-06", 3, 3, null), ("2024-05-06", 4, 1, 6), ("2024-05-06", 5, 1, null), ("2024-05-06", 6, 1, null),
("2024-05-07", 1, 2, null), ("2024-05-07", 2, 2, 5), ("2024-05-07", 3, 2, null), ("2024-05-07", 4, 1, 1), ("2024-05-07", 5, 1, null), ("2024-05-07", 6, 1, 4),
("2024-05-08", 1, 1, null), ("2024-05-08", 2, 1, null), ("2024-05-08", 3, 1, 3), ("2024-05-08", 4, 2, null), ("2024-05-08", 5, 2, null), ("2024-05-08", 6, 2, 6),
("2024-05-09", 1, 1, null), ("2024-05-09", 2, 1, 2), ("2024-05-09", 3, 1, null), ("2024-05-09", 4, 2, null), ("2024-05-09", 5, 2, 5), ("2024-05-09", 6, 1, null),
("2024-05-10", 1, 3, 3), ("2024-05-10", 2, 3, null), ("2024-05-10", 3, 3, 5), ("2024-05-10", 4, 1, null), ("2024-05-10", 5, 1, null), ("2024-05-10", 6, 1, null),
("2024-05-13", 1, 3, 4), ("2024-05-13", 2, 3, null), ("2024-05-13", 3, 3, null), ("2024-05-13", 4, 1, 6), ("2024-05-13", 5, 1, null), ("2024-05-13", 6, 1, null),
("2024-05-14", 1, 2, null), ("2024-05-14", 2, 2, 1), ("2024-05-14", 3, 2, null), ("2024-05-14", 4, 1, 5), ("2024-05-14", 5, 1, null), ("2024-05-14", 6, 1, 4),
("2024-05-15", 1, 1, 1), ("2024-05-15", 2, 1, null), ("2024-05-15", 3, 1, 3), ("2024-05-15", 4, 2, null), ("2024-05-15", 5, 2, null), ("2024-05-15", 6, 2, 6),
("2024-05-16", 1, 1, null), ("2024-05-16", 2, 1, 2), ("2024-05-16", 3, 1, null), ("2024-05-16", 4, 2, null), ("2024-05-16", 5, 2, 5), ("2024-05-16", 6, 1, null),
("2024-05-17", 1, 3, 6), ("2024-05-17", 2, 3, null), ("2024-05-17", 3, 3, 1), ("2024-05-17", 4, 1, null), ("2024-05-17", 5, 1, null), ("2024-05-17", 6, 1, null);


CREATE VIEW full_lesson_data AS
SELECT a.lesson_id AS ID, a.lesson_date AS "Date", b.lesson_time AS "Time", c.teacher_name AS "Teacher", d.customer_first_name AS "FirstName", d.customer_last_name AS "LastName"
FROM lessons a
JOIN lessons_times b
ON a.lesson_time_id = b.lesson_time_id
JOIN teachers c
ON a.lesson_teacher_id = c.lesson_teacher_id
LEFT JOIN customers d
ON a.customer_id = d.customer_id
ORDER BY "Date";

CREATE VIEW full_available_lesson_data AS
SELECT a.lesson_id AS ID, a.lesson_date AS "Date", b.lesson_time AS "Time", c.teacher_name AS "Teacher", a.customer_id
FROM lessons a
JOIN lessons_times b
ON a.lesson_time_id = b.lesson_time_id
JOIN teachers c
ON a.lesson_teacher_id = c.lesson_teacher_id
WHERE a.customer_id IS NULL
ORDER BY "Date";