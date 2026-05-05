\COPY users(id, name, email, password) FROM '/data/user_data.csv' DELIMITER ',' CSV HEADER;
\COPY projects(id, name, owner_id) FROM '/data/project_data.csv' DELIMITER ',' CSV HEADER;
\COPY tasks(id, title, description, status, project_id, assigned_to) FROM '/data/task_data.csv' DELIMITER ',' CSV HEADER;
\COPY comments(id, content, task_id, user_id) FROM '/data/comment_data.csv' DELIMITER ',' CSV HEADER;
