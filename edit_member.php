<?php
    include("{$_SERVER['DOCUMENT_ROOT']}/system/main.php");
    if ($_SESSION["role"] != "1") {
        $array = (array) [
            "code" => 300,
            "msg" => "No Permission",
            "data" => "",
        ];
    } else {
        if (!isset($_POST['id']) || empty($_POST['id'])) {
            $res = (array) [
                "code" => 300,
                "msg" => "ข้อมูล ไอดี ผิดพลาด",
            ];
        } else {
            $id = $_POST['id'];
            // $point = trim($_POST["pointw"]);
            // $res = (array) [
            //     "code" => 300,
            //     "msg" => $point,
            // ];
            $stmt = $pdo->prepare("SELECT * FROM `account` WHERE id= ? ");
            $stmt->execute([$id]);
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            $res = (array) [
                "code" => 200,
                "msg" => "Load Form",
                "point" => $row["point"],
                "id" => $row["id"],
            ];
        }
    }
    print_r(json_encode($res));