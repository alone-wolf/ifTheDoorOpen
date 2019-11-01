<?php

if(file_get_contents('status.ini')=='1'){
    file_put_contents('status.ini','0');
}else{
    file_put_contents('status.ini','1');
}
print(file_get_contents('status.ini'));