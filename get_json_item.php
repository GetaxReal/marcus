<?php
    include("{$_SERVER['DOCUMENT_ROOT']}/system/main.php");
    
    $stmt = $pdo->prepare("SELECT * FROM `backend` ");
    $stmt->execute();
    $config =  $stmt->fetch(PDO::FETCH_ASSOC);
    if (!isset($_SESSION["logging"])) {
        $array = (array) [
            "code" => 300,
            "msg" => "กรุณาเข้าสู่ระบบก่อนทำรายการ",
            "data" => "",
        ];
        print_r(json_encode($array));
        return;
    } else {
        $stmt = $pdo->prepare("SELECT * FROM `item`");
        $stmt->execute();
        $count = $stmt->rowCount();
        $items = $stmt->fetchAll(PDO::FETCH_ASSOC);

        $_items = array();

        for ($x = 0; $x < count($items); $x++) {
            $obj = $items[$x];
            $stmt3 = $pdo->prepare('SELECT * FROM `stock` WHERE `type` = "none" AND `itemid` = ?');
            $stmt3->execute([$obj["name"]]);
            $stock = $stmt3->rowCount();
            $obj["stock"] = $stock;

            array_push($_items, $obj);
        }

        if ($count >= 1) {
            $array = (array) [
                "count" => $count,
                "code" => 200,
                "data" => $_items,
            ];
        } else {
            $array = (array) [
                "count" => $count,
                "code" => 404,
                "data" => "",
            ];
        }
    }
    print_r(json_encode($array));