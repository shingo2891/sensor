<?php
//フォーマット
//http://localhost/sensor/sensor.php?date=20150801&time=00:00:00&tmp=23.88&lux=300&atm=1025.3
// 受信した値を保管する変数
$strDateVal = $_GET['date'];
$strTimeVal = $_GET['time'];
$strTmpVal = $_GET['tmp'];
$strLuxVal = $_GET['lux'];
$strAtmVal = $_GET['atm'];
// 保存する文字列を作成+ 改行コード
$strData = $strTimeVal . ',' 
. $strTmpVal . ',' 
. $strLuxVal . ',' 
. $strAtmVal . "\n";

// データを保存するテキストファイルの相対パス
$strDataFilePath = 'data/' . $strDateVal . '.txt';
// データを保存するテキストファイルを追記モードでオープン
$fp = fopen($strDataFilePath, "a");
// 送信された値をテキストファイルに書き込み
fwrite($fp, $strData);
// ファイルポインタをクローズ
fclose($fp);

// データの記録(現在データ)
// データを保存するテキストファイルの相対パス
$strFilePath = 'now.txt';
// データを保存するテキストファイルを書き込みモードでオープン
$fp2 = fopen($strFilePath, "w");
//現在のサーバの時刻取得しファイルに書き込み
$now = date('Y/m/d (D) H:i:s');

// 送信された値をテキストファイルに書き込み
fwrite($fp2, "最終更新：");
fwrite($fp2, $now);
fwrite($fp2, "\n\n");

$strData2 = "取得日時:" . $strDateVal . $strTimeVal . "\n";
fwrite($fp2, $strData2);
$strData2 = "室温:" . $strTmpVal . "\n";
fwrite($fp2, $strData2);
$strData2 = "照度:" . $strLuxVal . "\n";
fwrite($fp2, $strData2);
$strData2 = "気圧:" . $strAtmVal . "\n";
fwrite($fp2, $strData2);
// ファイルポインタをクローズ
fclose($fp2);

//Windowsにインストールしたphp.iniの位置をApache httpd.confに記述
//PHPIniDir "D:\program2\php"
//現在日時の取得でphp.iniのTimeZoneの設定を変更
//date.timezone = "Asia/Tokyo"
?>
