<?php
    date_default_timezone_set("Asia/Bangkok");
    try {
        $pdo = new PDO(
            "mysql:host=localhost;dbname=jaonaish_dewfwefwef;charset=utf8",
            "jaonaish_dewfwefwef",
            "@dewfwefwef_jaonaish"
        );
    } catch(PDOException $e) {
        print $e->getmessage();
    }