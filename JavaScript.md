# JavaScript

脚本语言

## 在HTML中使用js

``` js
<script type="text/javascript">
xxx;
</script>
```

或直接引用.js文件

``` js
<script src="xx.js"></script>
```

## 打印

``` js
var a = 5;
document.write(a+"123"+"<br>")
```

## 弹出框

``` js
alert("123");//弹窗

var message=confirm("123");//选择
if (message=true){}
else{}

var message=prompt("123");//填空
if (message!=null){}
else{}

window.open('http://www.xxxx.com', '_blank', 'width=100px, height=200px');//新浏览器标签
```

## 函数

``` js
<head>
<script type="text/javascript">
    funtion a(){
        alert("");
    }
</script>
</head>
<body>
    <input type="button" value="xxx" onclick="a()"/>
</body>
```

## 查找变量

``` js
<p id="id1">hello</p>
<script type="text/javascript>
    var message=document.getElementById('id1').innerHTML;
    document.write(message);
</script>
```

## 更改属性

``` js
var mychar=document.getElementById('id1');
mychar.style.font='14';
mychar.style.display='none';
mychar.style.display='block';
```
