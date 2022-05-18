SET client_encoding = 'UTF8';

-- 更新処理
CREATE FUNCTION update_updated_at_column()
  RETURNS TRIGGER AS $$
  BEGIN
      NEW.updated_at = now();
      RETURN NEW;
  END;
  $$ language 'plpgsql';

-- users
CREATE TABLE users (
  id SERIAL NOT NULL,
  name varchar(64) NOT NULL DEFAULT '',
  email varchar(64) NOT NULL DEFAULT '',
  pass varchar(200) NOT NULL DEFAULT '',
  created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (id)
);

-- インデックス指定
CREATE UNIQUE INDEX idx_email ON users (email);

-- 更新処理トリガー
CREATE TRIGGER update_user_modtime
  BEFORE UPDATE
  ON users
  FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_column();

-- サンプルユーザー
INSERT INTO users (name, email, pass) VALUES
('sam', 'sample01@example.com', 'sample01')
;

-- photos
CREATE TABLE photos (
  id SERIAL NOT NULL,
  shrine varchar(64) NOT NULL DEFAULT '',
  user_id varchar(64) NOT NULL DEFAULT '',
  url varchar(200) NOT NULL DEFAULT '',
  impression varchar(200) NOT NULL DEFAULT '',
  created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- インデックス指定
CREATE UNIQUE INDEX idx_user_id ON photos (user_id);

-- 更新処理トリガー
CREATE TRIGGER update_photos_modtime
  BEFORE UPDATE
  ON users
  FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_column();

-- サンプルユーザー
INSERT INTO emo (start_time, goal_time, distance, user_id) VALUES
('2021-06-06 18:00:00', '2021-06-06 19:00:00', 10000, 1),
('2021-09-09 19:00:00', '2021-09-09 21:43:00', 25400, 1),
('2021-10-01 18:00:00', '2021-10-01 20:00:00', 18800, 1)
;

-- emo
CREATE TABLE emo (
  id SERIAL NOT NULL,
  photos_id int NOT NULL,
  emo 
  created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (id),
  FOREIGN KEY (photos_id) REFERENCES photos(id)
);

-- インデックス指定
CREATE UNIQUE INDEX idx_user_id ON photos (user_id);

-- 更新処理トリガー
CREATE TRIGGER update_photos_modtime
  BEFORE UPDATE
  ON users
  FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_column();

INSERT INTO emo (start_time, goal_time, distance, user_id) VALUES
('2021-06-06 18:00:00', '2021-06-06 19:00:00', 10000, 1),
('2021-09-09 19:00:00', '2021-09-09 21:43:00', 25400, 1),
('2021-10-01 18:00:00', '2021-10-01 20:00:00', 18800, 1)
;