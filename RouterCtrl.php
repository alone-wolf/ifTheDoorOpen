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

    public function __construct($SCRIPT_NAME, $REQUEST_URI)
    {
        $this->setSCRIPTNAME($SCRIPT_NAME);
        $this->setREQUESTURI($REQUEST_URI);
    }
    public function resolveRouter($routerLimit = 0)
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
        // if ($routerLimit == 0) {
        //     return array_slice($routePath,0,NULL);
        // } else {
        //     //echo($routerLimit);
        //     return array_slice($routePath,0,$routerLimit);
        // }
    }
}


// $routerCtrl = new RouterCtrl($_SERVER['SCRIPT_NAME'],$_SERVER['REQUEST_URI']);
// $bbb = $routerCtrl->resolveRouter(2);
// print_r($bbb);

//usage:
// $routerCtrl = new RouterCtrl($_SERVER['SCRIPT_NAME'],$_SERVER['REQUEST_URI']);
// $routePath = $routerCtrl->resolveRouter(); //argc is int, default is 0

//将类实例化，构造函数输入$_SEREVER的SCRIPT_NAME 和 REQUEST_URI
//调用 resolveRouter()返回routePath数组
//其中resolveRouter()函数能够输入对数组长度的限制
//返回的数组从0开始