/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : django_backend_wx

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 03/01/2020 15:23:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for apis_app
-- ----------------------------
DROP TABLE IF EXISTS `apis_app`;
CREATE TABLE `apis_app`  (
  `appid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `category` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `application` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `publish_date` date NOT NULL,
  `url` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `desc` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`appid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of apis_app
-- ----------------------------
INSERT INTO `apis_app` VALUES ('549eaaf72cb23716e2b1313acfaed23c', 'life', 'backup-image', '图片备份', '2018-10-02', '/service/image', 'this is a backup image app.');
INSERT INTO `apis_app` VALUES ('7b27422f98f13eb2610f1996ec757be7', 'life', 'stock', '股票', '2018-10-05', '/service/stock', 'this is a stock app.');
INSERT INTO `apis_app` VALUES ('833cfd91bc1ac638ecd3764715b443ef', 'life', 'joke', '每日笑话', '2018-10-06', '/service/joke', 'this is a joke app.');
INSERT INTO `apis_app` VALUES ('a381d410bea99d3618cc6cd431c32b0f', 'life', 'constellation', '星座运势', '2018-10-06', '/service/constellation', 'this is a constellation app.');
INSERT INTO `apis_app` VALUES ('f18ba49825b634f44e8cdfb694ecaa13', 'life', 'weather', '天气', '2018-10-01', '/service/weather', 'this is a weather app.');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add user', 7, 'add_user');
INSERT INTO `auth_permission` VALUES (26, 'Can change user', 7, 'change_user');
INSERT INTO `auth_permission` VALUES (27, 'Can delete user', 7, 'delete_user');
INSERT INTO `auth_permission` VALUES (28, 'Can view user', 7, 'view_user');
INSERT INTO `auth_permission` VALUES (29, 'Can add app', 8, 'add_app');
INSERT INTO `auth_permission` VALUES (30, 'Can change app', 8, 'change_app');
INSERT INTO `auth_permission` VALUES (31, 'Can delete app', 8, 'delete_app');
INSERT INTO `auth_permission` VALUES (32, 'Can view app', 8, 'view_app');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for authorization_user
-- ----------------------------
DROP TABLE IF EXISTS `authorization_user`;
CREATE TABLE `authorization_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `open_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nickname` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `focus_cities` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `focus_constellations` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `focus_stocks` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `open_id`(`open_id`) USING BTREE,
  INDEX `authorizati_open_id_5cfcc1_idx`(`open_id`, `nickname`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of authorization_user
-- ----------------------------
INSERT INTO `authorization_user` VALUES (2, 'oIJUd5NKY3LTjMIcet-PWmKGtm7g', '远辰', '[{\"province\": \"\\u5e7f\\u4e1c\\u7701\", \"city\": \"\\u6df1\\u5733\\u5e02\", \"area\": \"\\u5357\\u5c71\\u533a\"}, {\"province\": \"\\u56db\\u5ddd\\u7701\", \"city\": \"\\u6210\\u90fd\\u5e02\", \"area\": \"\\u9526\\u6c5f\\u533a\"}, {\"province\": \"\\u8d35\\u5dde\\u7701\", \"city\": \"\\u8d35\\u9633\\u5e02\", \"area\": \"\\u5357\\u660e\\u533a\"}]', '[\"\\u53cc\\u5b50\\u5ea7\", \"\\u5929\\u874e\\u5ea7\", \"\\u5929\\u79e4\\u5ea7\", \"\\u6469\\u7faf\\u5ea7\"]', '[{\"code\": \"000001\", \"name\": \"\\u5e73\\u5b89\\u94f6\\u884c\", \"fullInfo\": \"\\u6df1\\u4ea4\\u6240-\\u5e73\\u5b89\\u94f6\\u884c(000001)\", \"market\": \"sz\"}, {\"code\": \"000018\", \"name\": \"\\u795e\\u5dde\\u957f\\u57ce\", \"fullInfo\": \"\\u6df1\\u4ea4\\u6240-\\u795e\\u5dde\\u957f\\u57ce(000018)\", \"market\": \"sz\"}, {\"code\": \"000009\", \"name\": \"\\u4e2d\\u56fd\\u5b9d\\u5b89\", \"fullInfo\": \"\\u6df1\\u4ea4\\u6240-\\u4e2d\\u56fd\\u5b9d\\u5b89(000009)\", \"market\": \"sz\"}]');

-- ----------------------------
-- Table structure for authorization_user_menu
-- ----------------------------
DROP TABLE IF EXISTS `authorization_user_menu`;
CREATE TABLE `authorization_user_menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `app_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `authorization_user_menu_user_id_app_id_4d3d9382_uniq`(`user_id`, `app_id`) USING BTREE,
  INDEX `authorization_user_menu_app_id_13ca5893_fk_apis_app_appid`(`app_id`) USING BTREE,
  CONSTRAINT `authorization_user_m_user_id_b7aaa9f0_fk_authoriza` FOREIGN KEY (`user_id`) REFERENCES `authorization_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `authorization_user_menu_app_id_13ca5893_fk_apis_app_appid` FOREIGN KEY (`app_id`) REFERENCES `apis_app` (`appid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of authorization_user_menu
-- ----------------------------
INSERT INTO `authorization_user_menu` VALUES (1, 2, '549eaaf72cb23716e2b1313acfaed23c');
INSERT INTO `authorization_user_menu` VALUES (2, 2, '7b27422f98f13eb2610f1996ec757be7');
INSERT INTO `authorization_user_menu` VALUES (3, 2, '833cfd91bc1ac638ecd3764715b443ef');
INSERT INTO `authorization_user_menu` VALUES (4, 2, 'a381d410bea99d3618cc6cd431c32b0f');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (8, 'apis', 'app');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (7, 'authorization', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-12-31 08:07:20.648229');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2019-12-31 08:07:21.368351');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2019-12-31 08:07:22.505865');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2019-12-31 08:07:22.514863');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2019-12-31 08:07:22.523816');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2019-12-31 08:07:22.604601');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2019-12-31 08:07:22.645492');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2019-12-31 08:07:22.693363');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2019-12-31 08:07:22.701365');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2019-12-31 08:07:22.743229');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2019-12-31 08:07:22.747219');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2019-12-31 08:07:22.756195');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2019-12-31 08:07:22.806062');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2019-12-31 08:07:22.856926');
INSERT INTO `django_migrations` VALUES (15, 'authorization', '0001_initial', '2019-12-31 08:07:22.880862');
INSERT INTO `django_migrations` VALUES (16, 'authorization', '0002_auto_20191228_1952', '2019-12-31 08:07:22.923747');
INSERT INTO `django_migrations` VALUES (17, 'sessions', '0001_initial', '2019-12-31 08:07:22.956659');
INSERT INTO `django_migrations` VALUES (18, 'authorization', '0003_auto_20191231_1647', '2019-12-31 08:47:14.971246');
INSERT INTO `django_migrations` VALUES (19, 'authorization', '0004_auto_20191231_1658', '2019-12-31 08:58:39.619691');
INSERT INTO `django_migrations` VALUES (20, 'apis', '0001_initial', '2019-12-31 12:27:36.201455');
INSERT INTO `django_migrations` VALUES (21, 'authorization', '0005_auto_20191231_2027', '2019-12-31 12:27:36.331107');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('5vi5xib9c5970iwyfydszyet5tdp1erv', 'NWMwYWY4Mjg5YmEwZDg1NDU3YWMyMWQ5NWExODU2NDFlYjEwYWNjNDp7Im9wZW5faWQiOiJvSUpVZDVOS1kzTFRqTUljZXQtUFdtS0d0bTdnIiwiaXNfYXV0aG9yaXplZCI6dHJ1ZX0=', '2019-12-31 14:13:40.548668');
INSERT INTO `django_session` VALUES ('7v9akoxj7xvxog4q2w5d2h6usw3dybhi', 'NWMwYWY4Mjg5YmEwZDg1NDU3YWMyMWQ5NWExODU2NDFlYjEwYWNjNDp7Im9wZW5faWQiOiJvSUpVZDVOS1kzTFRqTUljZXQtUFdtS0d0bTdnIiwiaXNfYXV0aG9yaXplZCI6dHJ1ZX0=', '2020-01-02 10:55:39.972228');
INSERT INTO `django_session` VALUES ('hezuaclvwxazigdrn6lyuwte0l09gqwt', 'ZGZkMDRiM2E0ZGZjNThkY2NlZTFlYjQ4OThhNmUwOTFhZGMxZDJlNjp7fQ==', '2020-01-02 10:55:38.548925');
INSERT INTO `django_session` VALUES ('zqa29opuoihr3vq04trxenlar2bb70x9', 'ZGZkMDRiM2E0ZGZjNThkY2NlZTFlYjQ4OThhNmUwOTFhZGMxZDJlNjp7fQ==', '2019-12-31 14:13:38.777624');

SET FOREIGN_KEY_CHECKS = 1;
