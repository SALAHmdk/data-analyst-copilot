def generate_sql(table_name, columns, intention):
    cols_str = ", ".join(columns)
    sql = f"-- Intention: {intention}\n"
    sql += f"SELECT {cols_str}\nFROM {table_name}\n"
    
    intention_lower = intention.lower()
    if "filtrer" in intention_lower or "où" in intention_lower:
        sql += "WHERE [condition]\n"
    if "grouper" in intention_lower or "par" in intention_lower:
        sql += f"GROUP BY {columns[0]}\n"
    if "trier" in intention_lower or "ordre" in intention_lower:
        sql += f"ORDER BY {columns[0]} DESC\n"
        
    sql += "LIMIT 100;"
    return sql
