import cx_Oracle

def insert_to_oracle(df, table_name, conn_str):
    try:
        conn = cx_Oracle.connect(conn_str)
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute(f"""
                INSERT INTO {table_name} (USERNAME, REVIEW, RATING, DATE, VERSION, SENTIMENT)
                VALUES (:1, :2, :3, :4, :5, :6)
            """, (row['userName'], row['content'], row['score'], row['at'], row['reviewCreatedVersion'], row['sentiment']))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"DB insert error: {e}")
