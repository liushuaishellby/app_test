import pymysql


class GetMysql:
    # 创建sql数据库链接
    def __init__(self,
                 user='root',
                 pwd='123456',
                 host='localhost',
                 port=3306
                 ):
        self.db = pymysql.connect(user=user, password=pwd, host=host, port=port)
        # 创建游标
        self.cursor = self.db.cursor()

    # 查询sql数据库，
    def select_mysql(self, sql, num=1):
        # 创建游标

        # 使用execute方法 使用sql语句
        self.cursor.execute(sql)
        # 获取查询的数据

        if num:  # 如果num为true则返回一条数据，否则返回所有的数据
            data = self.cursor.fetchone()
            return data
        return self.cursor.fetchall()

    # 插入数据
    def insert_mysql(self):
        pass

    # 删除数据
    def update_mysql(self):
        pass

    # 关闭数据库链接
    def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    mysql = GetMysql()
    print(mysql.select_mysql("select * from my_databases.people", num=False))
