\COPY users(name, email, password) FROM '/data/user_data.csv' DELIMITER ',' CSV HEADER;
\COPY projects(name, owner_id) FROM '/data/project_data.csv' DELIMITER ',' CSV HEADER;
\COPY tasks(title, description, status, project_id, assigned_to) FROM '/data/task_data.csv' DELIMITER ',' CSV HEADER;
\COPY comments(content, task_id, user_id) FROM '/data/comment_data.csv' DELIMITER ',' CSV HEADER;
