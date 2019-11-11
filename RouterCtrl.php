<?php

class RouterCtrl
{
    private $SCRIPT_NAME = NULL;
    private $REQUEST_URI = NULL;
    protected function setSCRIPTNAME($SCRIPT_NAME)
    {
        $this->SCRIPT_NAME = $SCRIPT_NAME;
    }
    protected function getSCRIPTNAME()
    {
        return $this->SCRIPT_NAME;
    }
    protected function setREQUESTURI($REQUEST_URI)
    {
        $this->REQUEST_URI = $REQUEST_URI;
    }
    protected function getREQUESTURI()
    {
        return $this->REQUEST_URI;
    }

    public function __construct($path)
    {
        $head=explode($path['DOCUMENT_ROOT'],$path['SCRIPT_FILENAME'])[1];
        $this->setSCRIPTNAME($head);
        $this->setREQUESTURI($path['REQUEST_URI']);
    }
    public function getRoutePath($routerLimit = 0)
    {
        $routePath = explode($this->getSCRIPTNAME(), $this->getREQUESTURI());
        $routePath = $routePath[1];

        //delete the get method of request on url
        $routePath = explode('?',$routePath)[0];
        $routePath = explode('/', $routePath);
        $routePath = array_diff($routePath,['']);

        //ensure the routerLimit less than the sizeof(routerPath)
        $routerLimit<sizeof($routePath)?$routerLimit=$routerLimit:$routerLimit=sizeof($routePath);
        //echo($routerLimit);
        //array_shift($routePath);//used to del the blank head of the array, but we can del it with array_diff val = [''];
        if($routerLimit==0){
            $routerLimit=NULL;
        }
        return array_slice($routePath,0,$routerLimit);
    }

}


//usage:
// $routerCtrl = new RouterCtrl($_SERVER);
// $routePath = $routerCtrl->getRoutePath(int argc);
//argc is int, default is 0

//将类实例化，构造函数输入$_SERVER
//调用 getRoutePath()返回routePath数组
//getRoutePath()函数能够输入对数组长度的限制
//返回的数组从0开始 限制默认关闭