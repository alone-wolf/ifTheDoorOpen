<?php

class DataTime{
    function getTime($format='ymdhis',$TZ='UTC'){
        date_default_timezone_set($TZ);
        $datetime = new DateTime();
        switch($format){
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
            case 'his':{
                $format='H:i:s';
                break;
            }
            default:{
                break;
            }
        }
        return $datetime->format($format);
    }
}

// $aaa = new DataTime;
// print($aaa->getTime());