<?php
//�t�H�[�}�b�g
//http://localhost/sensor/sensor.php?date=20150801&time=00:00:00&tmp=23.88&lux=300&atm=1025.3
// ��M�����l��ۊǂ���ϐ�
$strDateVal = $_GET['date'];
$strTimeVal = $_GET['time'];
$strTmpVal = $_GET['tmp'];
$strLuxVal = $_GET['lux'];
$strAtmVal = $_GET['atm'];
// �ۑ����镶������쐬+ ���s�R�[�h
$strData = $strTimeVal . ',' 
. $strTmpVal . ',' 
. $strLuxVal . ',' 
. $strAtmVal . "\n";

// �f�[�^��ۑ�����e�L�X�g�t�@�C���̑��΃p�X
$strDataFilePath = 'data/' . $strDateVal . '.txt';
// �f�[�^��ۑ�����e�L�X�g�t�@�C����ǋL���[�h�ŃI�[�v��
$fp = fopen($strDataFilePath, "a");
// ���M���ꂽ�l���e�L�X�g�t�@�C���ɏ�������
fwrite($fp, $strData);
// �t�@�C���|�C���^���N���[�Y
fclose($fp);

// �f�[�^�̋L�^(���݃f�[�^)
// �f�[�^��ۑ�����e�L�X�g�t�@�C���̑��΃p�X
$strFilePath = 'now.txt';
// �f�[�^��ۑ�����e�L�X�g�t�@�C�����������݃��[�h�ŃI�[�v��
$fp2 = fopen($strFilePath, "w");
//���݂̃T�[�o�̎����擾���t�@�C���ɏ�������
$now = date('Y/m/d (D) H:i:s');

// ���M���ꂽ�l���e�L�X�g�t�@�C���ɏ�������
fwrite($fp2, "�ŏI�X�V�F");
fwrite($fp2, $now);
fwrite($fp2, "\n\n");

$strData2 = "�擾����:" . $strDateVal . $strTimeVal . "\n";
fwrite($fp2, $strData2);
$strData2 = "����:" . $strTmpVal . "\n";
fwrite($fp2, $strData2);
$strData2 = "�Ɠx:" . $strLuxVal . "\n";
fwrite($fp2, $strData2);
$strData2 = "�C��:" . $strAtmVal . "\n";
fwrite($fp2, $strData2);
// �t�@�C���|�C���^���N���[�Y
fclose($fp2);

//Windows�ɃC���X�g�[������php.ini�̈ʒu��Apache httpd.conf�ɋL�q
//PHPIniDir "D:\program2\php"
//���ݓ����̎擾��php.ini��TimeZone�̐ݒ��ύX
//date.timezone = "Asia/Tokyo"
?>
