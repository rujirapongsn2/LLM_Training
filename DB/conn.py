import psycopg2
from psycopg2.extras import RealDictCursor

# Connection string สำหรับ Neon database
CONNECTION_STRING = "postgresql://neondb_owner:npg_pO7oQiMzwxJ2@ep-raspy-rice-a1rij5tx-pooler.ap-southeast-1.aws.neon.tech/library?sslmode=require"

def connect_to_neon():
    """เชื่อมต่อกับ Neon database แบบง่าย"""
    try:
        conn = psycopg2.connect(CONNECTION_STRING, cursor_factory=RealDictCursor)
        print("✅ เชื่อมต่อสำเร็จ!")
        return conn
    except Exception as e:
        print(f"❌ เชื่อมต่อไม่สำเร็จ: {e}")
        return None

def execute_query(query, params=None):
    """รัน SQL query และ return ผลลัพธ์"""
    conn = connect_to_neon()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        
        # ถ้าเป็น SELECT statement
        if query.strip().upper().startswith('SELECT'):
            result = cursor.fetchall()
        else:
            # ถ้าเป็น INSERT/UPDATE/DELETE
            conn.commit()
            result = cursor.rowcount
            
        cursor.close()
        conn.close()
        return result
        
    except Exception as e:
        print(f"❌ Query ไม่สำเร็จ: {e}")
        conn.rollback()
        conn.close()
        return None

def get_books():
    """ดึงข้อมูลหนังสือทั้งหมด"""
    return execute_query("SELECT * FROM books ORDER BY bookid")

def get_borrowers():
    """ดึงข้อมูลผู้ยืมทั้งหมด"""
    return execute_query("SELECT * FROM borrowers ORDER BY return_date")

def add_book(title, description, quantity, reviews=""):
    """เพิ่มหนังสือใหม่"""
    query = "INSERT INTO books (title, description, quantity, reviews) VALUES (%s, %s, %s, %s)"
    result = execute_query(query, (title, description, quantity, reviews))
    if result:
        print(f"✅ เพิ่มหนังสือ '{title}' สำเร็จ")
    return result

def add_borrower(borrower_name, bookid, quantity_borrowed, return_date):
    """เพิ่มผู้ยืมใหม่"""
    query = "INSERT INTO borrowers (borrower_name, bookid, quantity_borrowed, return_date) VALUES (%s, %s, %s, %s)"
    result = execute_query(query, (borrower_name, bookid, quantity_borrowed, return_date))
    if result:
        print(f"✅ เพิ่มผู้ยืม '{borrower_name}' สำเร็จ")
    return result

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    print("🚀 ทดสอบการเชื่อมต่อแบบง่าย")
    
    # ทดสอบดึงข้อมูลหนังสือ
    books = get_books()
    if books:
        print(f"📚 มีหนังสือ {len(books)} เล่ม:")
        for book in books:
            print(f"  - {book['title']}")
    
    # ทดสอบดึงข้อมูลผู้ยืม
    borrowers = get_borrowers()
    if borrowers:
        print(f"👥 มีผู้ยืม {len(borrowers)} คน:")
        for borrower in borrowers:
            print(f"  - {borrower['borrower_name']}")
    
    # ทดสอบเพิ่มหนังสือใหม่
    add_book("หนังสือทดสอบ", "สำหรับทดสอบระบบ", 5, "ดีมาก")
    
    print("✅ ทดสอบเสร็จสิ้น!")
