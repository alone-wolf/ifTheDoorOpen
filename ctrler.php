<?php
require './RouterCtrl.php';

$debug = new Debug;

//$_SERVER['SCRIPT_NAME']
//$_SERVER['REQUEST_URI']
if($_SERVER["SCRIPT_NAME"]==$_SERVER["REQUEST_URI"]){
    print('error: wrong url used');
    exit(-1);
}
$routePath=new RouterCtrl.resolvePouter(1);
$operate=$routePath[1];

$allowedOperateArray=array(
    'turnOn'=>array(
        'turnon',
    'turnOn',
    'on',
    'On',
    'opened',
    '1'
    ),
    'turnOff'=>array(
        'turnoff',
    'turnOff',
    'off',
    'Off',
    'closed',
    '0'
    )
    'getStatus'=>array(
        'get',
    '-1',
    'status',
    'getStatus',
    's',
    'S'
    ),
    'switchStatus'=>array(
        'switch'
    )
);

switch($operate){
    case in_array($operate,$allowedOperateArray['turnOn']):{
        $debug->printd('turnOn');
        echo(putDataToFile('1'));
        break;
    }
    case in_array($operate,$allowedOperateArray['turnOff']):{
        $debug->printd('turnOff');
        echo(putDataToFile('0'));
        break;
    }
    case in_array($operate,$allowedOperateArray['getStatus']):{
        $debug->printd('getStatus');
        echo(getStatusFromFile());
        break;
    }
    case in_array($operate,$allowedOperateArray['switchStatus']):{
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

function checkin($open_close){
    $time = getTime();
    $status=$open_close;

}






