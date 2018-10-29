-- 需要执行的脚本
create database rupeng;
use rupeng;

-- 建表
CREATE TABLE stu (
    s_id INT(11) NOT NULL AUTO_INCREMENT,
    s_name VARCHAR(50) NOT NULL,
    s_address VARCHAR(60) DEFAULT '北京昌平',
    PRIMARY KEY (s_id)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;

-- 插入数据
INSERT INTO stu (s_name,s_address)
VALUES('李萍', '北京海淀'),('刘华', '上海黄浦区'),
( '黄骅', '深圳皇岗'),
('李娟', '中国西藏');