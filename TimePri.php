<?php

class DataTime{
    function getTime($format='YmdHis'){
        date_default_timezone_set('UTC');
        $datetime = new DateTime();
        switch($fomat){
            case 'ymdhis':{
                $format='Y-m-d H:i:s';
                break;
            }
            case 'ymdhi':{
                $format='Y-m-d H:i';
                break;
            }
            case 'ymd':{
                $format='Y-m-d';
                break;
            }
        }
        return $datetime->format($format);
    }
}

$aaa = new DataTime;