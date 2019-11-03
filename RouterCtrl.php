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
        $routePath = explode('/', $routePath);
        print_r(sizeof($routePath));
        //array_shift($routePath);
        if ($routerLimit == 0) {
            return $routePath;
        } else {
            if (sizeof($routePath != $routerLimit)) {
                echo ('error: wrong number of args');
                return '-1';
            }
        }
        return $routePath;
    }
}


$routerCtrl = new RouterCtrl('http://a.com/', 'http://a.com/cnaa');
$bbb = $routerCtrl->resolveRouter();
print_r($bbb);
