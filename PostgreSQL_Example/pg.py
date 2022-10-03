import psycopg # Python操作PostgreSQL

# 操作PostgreSQL資料庫
class PgData():
    # 資料連接設定
    def __init__(self, DatabaseName, UserName, Password, Host, Port, table_name=None, DataName=None, DataValues=None):
        self.dbname = DatabaseName # 資料庫名稱
        self.user = UserName # 使用者名稱
        self.ps = Password # 密碼
        self.host = Host # 主機名稱
        self.Port = Port # 連接埠
        self.table = table_name # 表格名稱
        self.DName = DataName # 資料名稱
        self.DValue = DataValues # 資料值

    # 新增表格table
    def create(self, Table_name, Name, Name_type, Values, Values_type):
        with psycopg.connect("dbname={} user={} password={} host={} port={}".format(self.dbname, self.user, self.ps, self.host, self.Port)) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE {} (
                        id serial PRIMARY KEY,
                        {} {},
                        {} {})
                    """.format(str(Table_name), Name, Name_type, Values, Values_type),
                )

                conn.commit()

    # 新增資料
    def add(self, Table_name=None, Data_Name=None, Data_Values=None):
        with psycopg.connect("dbname={} user={} password={} host={} port={}".format(self.dbname, self.user, self.ps, self.host, self.Port)) as conn:
            with conn.cursor() as cur:

                cur.execute(
                    "INSERT INTO {} (name, data) VALUES (%s, %s)".format(self.table or Table_name),
                    (Data_Name or self.DName, Data_Values or self.DValue)
                )

                conn.commit()

    # 新增多項資料
    def add_many(self, Data_list:list):
        with psycopg.connect("dbname={} user={} password={} host={} port={}".format(self.dbname, self.user, self.ps, self.host, self.Port)) as conn:
            with conn.cursor() as cur:

                cur.executemany(
                    "INSERT INTO {} (name, data) VALUES (%s)".format(self.table),
                    (Data_list)
                )

                conn.commit()

    # 取得資料
    def get(self):
        with psycopg.connect("dbname={} user={} password={} host={} port={}".format(self.dbname, self.user, self.ps, self.host, self.Port)) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM {}".format(self.table))
                return cur.fetchone()

                #cur.fetchone()
                #cur.fetchmany()

    # 取得多筆資料
    def get_many(self, numbers:int):
        with psycopg.connect("dbname={} user={} password={} host={} port={}".format(self.dbname, self.user, self.ps, self.host, self.Port)) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM {}".format(self.table))
                if numbers != -1:
                    rows = cur.fetchmany(int(numbers))
                else:
                    rows = cur.fetchall()

                return rows

    # 更新資料
    def up(self, Data_Name=None, Data_Values=None):
        with psycopg.connect("dbname={} user={} password={} host={} port={}".format(self.dbname, self.user, self.ps, self.host, self.Port)) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE {} SET data = %s WHERE name = %s;".format(self.table),
                    ((Data_Values or self.DValue), (Data_Name or self.DName))
                )

                conn.commit()

    # 刪除資料
    def delete(self, Data_Name=None):
        with psycopg.connect("dbname={} user={} password={} host={} port={}".format(self.dbname, self.user, self.ps, self.host, self.Port)) as conn:
            with conn.cursor() as cur:
                if str(Data_Name) == 'all':
                    cur.execute(
                        "DROP TABLE {};".format(self.table)
                    )
                else:
                    cur.execute(
                        "DELETE FROM {} WHERE name = %s;".format(self.table),
                        ((Data_Name or self.DName))
                    )

                conn.commit()