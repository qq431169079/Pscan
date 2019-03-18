##### 项目名称

Pscan

##### 项目描述

* 探测端口: 端口信息 banner
* 敏感信息泄漏扫描

##### 项目使用

* 端口扫描

  * 扫B段

    ```
    python pscan.py --mode port --host 114.116.50-60 --port 80,8080 --thread 50
    ```

  * 扫C段

    ```
    python pscan.py --mode port --host 114.116.50.1-60 --port 80,8080 --thread 50
    ```

  ![](https://ws2.sinaimg.cn/large/006tKfTcly1g167ed78hbj321i0tm4qp.jpg)

* 敏感信息扫描

  ```
  python pscan.py --mode sens --host 114.116.44.126 --thread 50
  ```

  ![](https://ws2.sinaimg.cn/large/006tKfTcly1g1675yil5zj30ty0bs42a.jpg)



