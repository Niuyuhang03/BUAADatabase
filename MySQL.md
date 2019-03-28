# MySQL

不区分大小写，习惯性将保留字全部大写，列和表名全部小写

第一行为0行

MySQL无撤销指令

1. 启动服务：

    ``` MySQL
    net start mysql//启动服务
    
    mysql -u root -p//登陆
    
    SHOW databases;//选择数据库
    USE crashcourse;
    
    CREATE database xxx;//创建数据库
    DROP database xxx;//删除数据库
    
    SHOW tables;//选择表
    
    select host,user,authentication_string from mysql.user;//查询所有用户
    create user "username"@"host" identified by "password";//新建用户
    ```

2. 创建表、删除表

    ```MySQL
    CREATE TABLE
    CREATE TABLE table_name(column1_name int NOT NULL AUTO_INCREMENT, column2_name char(50) NULL DEFAULT 1, PRIMARY KEY(column1_name))ENGINE=InnoDB;

    DROP TABLE
    DROP TABLE table_name;

    RENAME TABLE
    RENAME TEBLE table1_name TO table2_name;
    ```

3. 按列检索SELECT

    顺序：SELECT+FROM+WHERE+GROUP BY+HAVING+ORDER BY+LIMIT

    ``` MySQL
    FROM
    SELECT * FROM table_name;//展示整个table
    SELECT column1_name, column2_name FROM table_name;//展示table中某几列

    ORDER BY排序
    SELECT * FROM table_name ORDER BY column1_name, column2_name;//以某几列为顺序展示table
    SELECT * FROM table_name ORDER BY column1_name DESC,column2_name;//以某几列为倒序展示table

    DISTINCT去重
    SELECT DISTINCT column1_name FROM table_name;//对某列去重后输出

    LIMIT限制特定行
    SELECT * FROM table_name (ORDER BY column1_name) LIMIT a, b;//排序后展示第a+1行开始的b行

    WHERE、IN、NOT IN
    SELECCT * FROM table_name WHERE column1_name=a AND (column2_name<=3 OR column3_name IN (3,4,5));//查找第一列为a，第二列小于等于3或第三列为3或4或5的词

    LIKE
    %任意数目字符
    SELECT column1_name FROM table_name WHERE column1_name LIKE 'xyz%';//某列中以xyz开头词

    _一个字符
    SELECT column1_name FROM table_name WHERE column1_name LIKE 'xyz_';//某列中以xyz开头+1个字符的词

    REGEXP正则
    SELECT column1_name FROM table_name WHERE column1_name REGEXP '.000';//REGEXP后加正则
    ```

4. 计算字段

    ```MySQL
    Concnt()拼接
    SELECT Concnt(column1_name, '(', column2_name, ')') FROM table_name ORDER BY column1_name;//拼接a(b)的形式

    RTrim()删除最右边所有空格，LTrim()删除最左边所有空格
    SELECT Concnt(column1_name, '(', RTrim(column2_name), ')') FROM table_name ORDER BY column1_name;

    AS别名
    SELECT Concnt(column1_name, '(', RTrim(column2_name), ')') AS new FROM table_name ORDER BY column1_name;
    ```

5. 数据处理

    ```MySQL
    Upper()全部大写
    SELECT Concnt(column1_name, '(', Upper(column2_name), ')') FROM table_name ORDER BY column1_name;
    ```

6. 数据汇总

    ```MySQL
    AVG()获取一列平均值
    SELECT AVG(column1_name) FROM table_name AS name;

    COUNT()统计行数
    SELECT COUNT(*) FORM table_name;

    MAX() MIN() SUM()
    SELECT AVG(column1_name) AS name1, MIN(column2_name) AS name2 FROM table_name;
    ```

7. 数据分组

    ```MySQL
    GROUP BY分组
    SELECT COUNT(column1_name) AS name1 FROM table_name GROUP BY column2_name;

    HAVING代替WHERE以用于过滤分组
    SELECT COUNT(column1_name) AS name1 FROM table_name GROUP BY column2_name HAVING COUNT(column1_name) > 2;
    ```

8. 子查询

    ```MYSQL
    ANY

    ALL

    IN

    NOT IN

    EXISTS

    NOT EXISTS

    UNION并

    MINUS差

    INTERSECT交
    ```

9. 联接表

    ```MySQL
    从两个表中查询笛卡尔乘积
    SELECT column1_name, column2_name, column3_name FROM table1_name, table2_name WHERE table1_name.column1_name = table2_name.column1_name';
    或
    SELECT column1_name, column2_name, column3_name FROM table1_name INNER JOIN table2_name ON table1_name.column1_name = table2_name.column1_name';
    后者更佳

    OUTER JOIN联接行
    ```

10. 组合查询

    ```MySQL
    UNION一起输出并去重
    SELECT……UNION SELECT……;

    UNION ALL一起输出不去重
    SELECT……UNION SELECT……;
    ```

11. 插入更新

    ```MySQL
    INSERT INTO插入行
    INSERT INTO table_name[(column1_name, column2_name…… )] VALUES(1,2……),(3,4……);
    INSERT INTO table_name(column1_name, column2_name……) SELECT column3_name, column4_name…… FROM table2_name;

    ALTER TABLE ADD增加列
    ALTER TABLE table_name ADD column1_name int;

    ALTER TABLE DROP删除列
    ALTER TABLE table_name DROP COLUMN column1_name;

    UPDATE
    UPDATE table_name SET column1_name=word, column2_name=word WHERE column3_name=word;

    DELETE删除行
    DELETE FROM table_name WHRER column1_name = word;

    TRUNCATE清空
    TRUNCATE table_name;
    ```

12. 索引

    ``` MySQL
        创建索引
        CREATE [UNIQUE][CLUSTER] INDEX index_name ON talbe_name(column1_name ASC, column2_name DESC);

        删除索引
        DROP INDEX index_name;
    ```

13. 视图

    ``` MySQL
    创建视图
    CREATE VIEW view_name AS SELECT * FROM table_name WHERE what;

    删除视图
    DROP VIEW view_name;
    ```
