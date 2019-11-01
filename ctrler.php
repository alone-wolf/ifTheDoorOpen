<?php

$debug = new Debug;

//$_SERVER['SCRIPT_NAME']
//$_SERVER['REQUEST_URI']
if($_SERVER["SCRIPT_NAME"]==$_SERVER["REQUEST_URI"]){
    print('error: wrong url used');
    exit(-1);
}
$routePath=explode($_SERVER["SCRIPT_NAME"],$_SERVER["REQUEST_URI"]);
$routePath=$routePath[1];
$routePath=explode('/',$routePath);
if(sizeof($routePath)!=2){
    print('error: wrong number of args');
    exit(-1);
}
// print_r($routePath);
$operate=$routePath[1];

$allowedOperateArray1=array(
    'turnon',
    'turnOn',
    'on',
    'On',
    'opened',
    '1'
);
$allowedOperateArray0=array(
    'turnoff',
    'turnOff',
    'off',
    'Off',
    'closed',
    '0'
);
$allowedOperateArray_1=array(
    'get',
    '-1',
    'status',
    'getStatus',
    's',
    'S'
);
$allowedOperateArray_2=array(
    'switch'
);

switch($operate){
    case in_array($operate,$allowedOperateArray1):{
        $debug->printd('turnOn');
        echo(putDataToFile('1'));
        break;
    }
    case in_array($operate,$allowedOperateArray0):{
        $debug->printd('turnOff');
        echo(putDataToFile('0'));
        break;
    }
    case in_array($operate,$allowedOperateArray_1):{
        $debug->printd('getStatus');
        echo(getStatusFromFile());
        break;
    }
    case in_array($operate,$allowedOperateArray_2):{
        $debug->printd('switchStatus');
        $echoStr=NULL;
        getStatusFromFile()=='1'?$echoStr=putDataToFile('0'):$echoStr=putDataToFile('1');
        echo($echoStr);
        break;
    }
    default:{
        print('error: wrong args');
        break;
        exit(-1);
    }
}

function putDataToFile($data){
    file_put_contents('status.ini',$data);
    return getStatusFromFile();
}

function getStatusFromFile(){
    if(file_exists('status.ini')){
        return file_get_contents('status.ini');
    }
}

class FileCtrl{
    private $filePath;
    private $file;
    public function setFilePath($filePath){
        $this->filePath=$filePath;
    }
    public function getFilePath(){
        return $this->filePath;
    }
    public function openFileRead(){
        $this->file=fopen($this->getFilePath(),'r');
        flock($this->getFile(),LOCK_SH);
    }
    public function getFile(){
        return $this->file;
    }
    public function openFileWrite(){
        $this->file=fopen($this->getFilePath,'w');
    }

    public function __destruct(){
        fclose($this->getFile());
    }

}

class Debug{
    private $debugStatus=0;
    public function printd($str){
        if($this->debugStatus){
            print($str.'<br>');
        }
    }
}
