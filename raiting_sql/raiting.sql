CREATE TABLE `auth_user` (
    `id` int PRIMARY KEY AUTO_INCREMENT,
    `password` varchar(128),
    `last_login` datetime,
    `is_superuser` bool,
    `username` varchar(150),
    `first_name` varchar(150),
    `last_name` varchar(150),
    `email` varchar(254),
    `is_staff` bool,
    `is_active` bool,
    `date_joined` datetime
);

CREATE TABLE `property` (
    `id` int PRIMARY KEY AUTO_INCREMENT,
    `address` varchar(120),
    `city` varchar(32),
    `price` bigint(20),
    `description` text,
    `year` int(4)
);

CREATE TABLE `raiting` (
    `id` int PRIMARY KEY AUTO_INCREMENT,
    `raiting` int(5)
);

CREATE TABLE `raiting_history` (
    `id` int PRIMARY KEY AUTO_INCREMENT,
    `user_id` int,
    `property_id` int,
    `raiting_id` int,
    `update_date` datetime
);

ALTER TABLE `raiting_history` ADD FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `raiting_history` ADD FOREIGN KEY (`property_id`) REFERENCES `property` (`id`);

ALTER TABLE `raiting_history` ADD FOREIGN KEY (`raiting_id`) REFERENCES `raiting` (`id`);
