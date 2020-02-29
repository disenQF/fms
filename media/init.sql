drop DATABASE if EXISTS fms;

create DATABASE fms CHARSET=utf8;
use fms;


-- 系统管理员表（超级管理员、普通员管理员、合作商超级管理员）

create table t_sys_role(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(20) NOT NULL UNIQUE,
  code VARCHAR(10) UNIQUE
);

INSERT t_sys_role(name, code) values
  ('超级管理员', 'admin'),
  ('普通管理员', 'mgr'),
  ('合作商超级管理员', 'fr_admin');

create table t_sys_user(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(20) UNIQUE NOT NULL ,
  auth_string VARCHAR(32) NOT NULL,
  nick_name  VARCHAR(20),
  role_id    INTEGER REFERENCES t_sys_role(id)
);

INSERT t_sys_user(username, auth_string, nick_name, role_id) VALUES
  ('disen', '43da3eb40a39ddea8d5eb2da915adb09','狄哥', 1),
  ('lili', '8e056ea961370ab19d07993abbb14e73', '小李子', 2);


-- 不同角色有自己的菜单
create table t_sys_menu(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(20),
  parent_id INTEGER REFERENCES t_sys_menu(id),
  ord INT COMMENT '菜单显示的排序',
  url VARCHAR(50) COMMENT '菜单的连接'
);


-- 角色和菜单关系表
CREATE TABLE t_sys_role_menu (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  role_id INTEGER REFERENCES t_sys_role(id),
  menu_id INTEGER REFERENCES t_sys_menu(id)
);


/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/2/19 21:09:12                           */
/*==============================================================*/


drop table if exists t_block_setting;

drop table if exists t_groom;

drop table if exists t_history;

drop table if exists t_image_links;

drop table if exists t_message;

drop table if exists t_share;

drop table if exists t_user;

drop table if exists t_water;

drop table if exists t_file;

/*==============================================================*/
/* Table: t_block_setting                                       */
/*==============================================================*/
create table t_block_setting
(
   block_id             integer not null,
   user_id              integer,
   block_size           int,
   last_time            timestamp,
   note                 text,
   primary key (block_id)
);

/*==============================================================*/
/* Table: t_groom                                               */
/*==============================================================*/
create table t_groom
(
   groom_id             integer,
   user_id              integer,
   friend_id            integer
);

/*==============================================================*/
/* Table: t_history                                             */
/*==============================================================*/
create table t_history
(
   history_id           integer not null auto_increment,
   message_id           integer,
   user_id              integer,
   see_time             timestamp,
   see_cnt              int,
   primary key (history_id)
);

/*==============================================================*/
/* Table: t_image_links                                         */
/*==============================================================*/
create table t_image_links
(
   link_id              integer not null auto_increment,
   water_id             integer,
   file_id              integer,
   token                varchar(50),
   expires              integer,
   create_time          char(10),
   primary key (link_id)
);

/*==============================================================*/
/* Table: t_message                                             */
/*==============================================================*/
create table t_message
(
   message_id           integer not null auto_increment,
   title                varchar(50),
   content              text,
   create_time          timestamp,
   link_url             varchar(100),
   note                 text,
   primary key (message_id)
);

/*==============================================================*/
/* Table: t_share                                               */
/*==============================================================*/
create table t_share
(
   share_id             integer not null auto_increment,
   file_id              integer,
   friend_id            integer,
   expires              int,
   primary key (share_id)
);

/*==============================================================*/
/* Table: t_user                                                */
/*==============================================================*/
create table t_user
(
   user_id              integer not null auto_increment,
   name                 varchar(50),
   auth_string          varchar(50),
   mail                 varchar(50),
   phone                varchar(50),
   head                 varchar(50),
   label             varchar(200),
   create_time          timestamp,
   note                 text,
   primary key (user_id)
);

/*==============================================================*/
/* Table: t_water                                               */
/*==============================================================*/
create table t_water
(
   water_id             integer  auto_increment,
   water_text           VARCHAR(50),
   water_pos            int,
   font_size            int,
   font_name            varchar(20),
   note                 text,
   primary key (water_id)
);

/*==============================================================*/
/* Table: t_file                                                   */
/*==============================================================*/
create table t_file
(
   file_id              integer not null auto_increment,
   user_id              integer,
   file_type            char(1),
   fille_name           varchar(50),
   create_time          timestamp,
   last_time            timestamp,
   file_size            float,
   parent_file_id       int,
   note                 text,
   primary key (file_id)
);

alter table t_block_setting add constraint FK_Reference_5 foreign key (user_id)
      references t_user (user_id) on delete restrict on update restrict;

alter table t_history add constraint FK_Reference_2 foreign key (message_id)
      references t_message (message_id) on delete restrict on update restrict;

alter table t_history add constraint FK_Reference_3 foreign key (user_id)
      references t_user (user_id) on delete restrict on update restrict;

alter table t_image_links add constraint FK_Reference_1 foreign key (water_id)
      references t_water (water_id) on delete restrict on update restrict;

alter table t_image_links add constraint FK_Reference_4 foreign key (file_id)
      references t_file (file_id) on delete restrict on update restrict;

alter table t_share add constraint FK_Reference_7 foreign key (file_id)
      references t_file (file_id) on delete restrict on update restrict;

alter table t_file add constraint FK_Reference_6 foreign key (user_id)
      references t_user (user_id) on delete restrict on update restrict;

