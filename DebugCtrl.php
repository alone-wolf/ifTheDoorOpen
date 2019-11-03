<?php

class Debug{
    private $debugStatus=0;
    public function printd($str){
        if($this->debugStatus){
            print($str.'<br>');
        }
    }
}