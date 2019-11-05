<?php

class FileCtrl{
    private $filePath=NULL;
    public function setFilePath($filePath){
        $this->filePath=$filePath;
    }
    public function getFilePath(){
        return $this->filePath;
    }
    public function __construct($filePath)
    {
        $this->setFilePath($filePath);
    }
    public function getFileCon(){
        if(file_exists($this->getFilePath())){
            return file_get_contents($this->getFilePath());
        }else{
            return '-1';
        }
    }
}

//usage
// $fileCtrl=new FileCtrl('status.ini');
// print($fileCtrl->getFileCon());