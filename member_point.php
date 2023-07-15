<?php
    include("{$_SERVER['DOCUMENT_ROOT']}/system/main.php");
    if ($_SESSION["role"] != "1") {
        $array = (array) [
            "code" => 300,
            "msg" => "No Permission",
            "data" => "",
        ];
    } else {
        
        if (!isset($_POST['point']) || !isset($_POST['id'])) {
            $res = (array) [
                "code" => 300,
                "msg" => "กรุณากรอกข้อมูล point",
            ];
        } else {
            // try{
                $id = $_POST['id'];
                $new_point = $_POST['point'];
                $stmt = $pdo->prepare("UPDATE `account` SET point = ? WHERE id = ?");
                $stmt->execute([$new_point, $id]);
                $res = (array) [
                    "code" => 200,
                    "msg" => "อัพเดทสำเร็จ",
                ];
            // }catch(Execption $e){
            //     $res = (array) [
            //         "code" => 300,
            //         "msg" => $e->getmessage(),
            //     ];
            // }
        }
    }
    print_r(json_encode($res));