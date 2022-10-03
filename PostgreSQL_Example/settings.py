from .pg import PgData

# pg資料庫設定
def pg_config(TableName=None, DataName=None, DataValues=None):
    pg_set = PgData(
            DatabaseName = "",
            UserName = "",
            Password = "",
            Host = "",
            Port = "",
            table_name = TableName,
            DataName = DataName,
            DataValues = DataValues
        )
    return pg_set