

class SQL(object):
    def Query(self,Query):
        print(Query)
        return 1

def RequestID(table,column,string):
    sql = SQL()
    return sql.Query("SELECT "+table+"_id "+
    " FROM "+table+
    " WHERE "+table+"_name = "+string
    )

def SetNewRow(table,content):
    sql = SQL()
    sql.Query("SELECT "+table+"_id "+
    " FROM "+table+
    " WHERE "+table+"_name = "+string
    )
