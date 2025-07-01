import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime

class LibraryDatabase:
    def __init__(self):
        # Neon database connection string
        self.connection_string = "postgresql://neondb_owner:npg_pO7oQiMzwxJ2@ep-raspy-rice-a1rij5tx-pooler.ap-southeast-1.aws.neon.tech/library?sslmode=require"
        self.connection = None
        
    def connect(self):
        """เชื่อมต่อกับ Neon database"""
        try:
            self.connection = psycopg2.connect(
                self.connection_string,
                cursor_factory=RealDictCursor  # ใช้ RealDictCursor เพื่อให้ได้ผลลัพธ์เป็น dictionary
            )
            print("✅ เชื่อมต่อกับ Neon database สำเร็จ!")
            return True
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
            return False
    
    def disconnect(self):
        """ปิดการเชื่อมต่อ"""
        if self.connection:
            self.connection.close()
            print("🔌 ปิดการเชื่อมต่อแล้ว")
    
    def test_connection(self):
        """ทดสอบการเชื่อมต่อด้วยการ query ข้อมูลพื้นฐาน"""
        if not self.connection:
            print("❌ ยังไม่ได้เชื่อมต่อกับฐานข้อมูล")
            return False
            
        try:
            cursor = self.connection.cursor()
            
            # ทดสอบ query พื้นฐาน
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"📊 PostgreSQL Version: {version['version']}")
            
            # ตรวจสอบจำนวนตารางในฐานข้อมูล
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            tables = cursor.fetchall()
            print(f"📋 ตารางในฐานข้อมูล: {[table['table_name'] for table in tables]}")
            
            cursor.close()
            return True
            
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการทดสอบ: {e}")
            return False
    
    def get_all_books(self):
        """ดึงข้อมูลหนังสือทั้งหมด"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM books ORDER BY bookid;")
            books = cursor.fetchall()
            cursor.close()
            return books
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการดึงข้อมูลหนังสือ: {e}")
            return []
    
    def get_all_borrowers(self):
        """ดึงข้อมูลผู้ยืมทั้งหมด"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM borrowers ORDER BY return_date;")
            borrowers = cursor.fetchall()
            cursor.close()
            return borrowers
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการดึงข้อมูลผู้ยืม: {e}")
            return []
    
    def get_borrower_details(self):
        """ดึงข้อมูลผู้ยืมพร้อมรายละเอียดหนังสือ"""
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    b.title as book_title,
                    br.borrower_name,
                    br.quantity_borrowed,
                    br.return_date,
                    b.quantity as available_quantity
                FROM books b 
                JOIN borrowers br ON b.bookid = br.bookid 
                ORDER BY br.return_date;
            """
            cursor.execute(query)
            details = cursor.fetchall()
            cursor.close()
            return details
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการดึงข้อมูลรายละเอียด: {e}")
            return []
    
    def add_book(self, title, description, quantity, reviews=""):
        """เพิ่มหนังสือใหม่"""
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO books (title, description, quantity, reviews) 
                VALUES (%s, %s, %s, %s) 
                RETURNING bookid;
            """
            cursor.execute(query, (title, description, quantity, reviews))
            book_id = cursor.fetchone()['bookid']
            self.connection.commit()
            cursor.close()
            print(f"✅ เพิ่มหนังสือใหม่สำเร็จ ID: {book_id}")
            return book_id
        except Exception as e:
            self.connection.rollback()
            print(f"❌ เกิดข้อผิดพลาดในการเพิ่มหนังสือ: {e}")
            return None
    
    def add_borrower(self, borrower_name, bookid, quantity_borrowed, return_date):
        """เพิ่มผู้ยืมใหม่"""
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO borrowers (borrower_name, bookid, quantity_borrowed, return_date) 
                VALUES (%s, %s, %s, %s) 
                RETURNING id;
            """
            cursor.execute(query, (borrower_name, bookid, quantity_borrowed, return_date))
            borrower_id = cursor.fetchone()['id']
            self.connection.commit()
            cursor.close()
            print(f"✅ เพิ่มผู้ยืมใหม่สำเร็จ ID: {borrower_id}")
            return borrower_id
        except Exception as e:
            self.connection.rollback()
            print(f"❌ เกิดข้อผิดพลาดในการเพิ่มผู้ยืม: {e}")
            return None


def main():
    """ฟังก์ชันหลักสำหรับทดสอบการเชื่อมต่อและ query ข้อมูล"""
    
    print("🚀 เริ่มต้นทดสอบการเชื่อมต่อ Neon Database")
    print("=" * 50)
    
    # สร้าง instance ของ LibraryDatabase
    db = LibraryDatabase()
    
    # ทดสอบการเชื่อมต่อ
    if not db.connect():
        return
    
    # ทดสอบการเชื่อมต่อ
    if not db.test_connection():
        db.disconnect()
        return
    
    print("\n" + "=" * 50)
    print("📚 ข้อมูลหนังสือทั้งหมด:")
    books = db.get_all_books()
    for book in books:
        print(f"ID: {book['bookid']}, ชื่อ: {book['title']}, จำนวน: {book['quantity']}")
    
    print("\n" + "=" * 50)
    print("👥 ข้อมูลผู้ยืมทั้งหมด:")
    borrowers = db.get_all_borrowers()
    for borrower in borrowers:
        print(f"ชื่อ: {borrower['borrower_name']}, หนังสือ ID: {borrower['bookid']}, "
              f"จำนวน: {borrower['quantity_borrowed']}, วันคืน: {borrower['return_date']}")
    
    print("\n" + "=" * 50)
    print("🔍 รายละเอียดการยืม:")
    details = db.get_borrower_details()
    for detail in details:
        print(f"หนังสือ: {detail['book_title']}")
        print(f"ผู้ยืม: {detail['borrower_name']}")
        print(f"จำนวนที่ยืม: {detail['quantity_borrowed']}")
        print(f"วันที่คืน: {detail['return_date']}")
        print(f"จำนวนคงเหลือ: {detail['available_quantity']}")
        print("-" * 30)
    
    # ทดสอบการเพิ่มข้อมูลใหม่
    print("\n" + "=" * 50)
    print("➕ ทดสอบการเพิ่มหนังสือใหม่:")
    new_book_id = db.add_book(
        title="วิทยาศาสตร์คอมพิวเตอร์",
        description="หนังสือเรียนวิทยาศาสตร์คอมพิวเตอร์ขั้นพื้นฐาน",
        quantity=12,
        reviews="เนื้อหาทันสมัย เหมาะสำหรับผู้เริ่มต้น"
    )
    
    if new_book_id:
        print("\n➕ ทดสอบการเพิ่มผู้ยืมใหม่:")
        db.add_borrower(
            borrower_name="อรุณ ชาญชัย",
            bookid=new_book_id,
            quantity_borrowed=1,
            return_date="2025-07-25"
        )
    
    # แสดงข้อมูลหลังจากเพิ่มใหม่
    print("\n" + "=" * 50)
    print("📊 ข้อมูลหลังจากเพิ่มใหม่:")
    updated_books = db.get_all_books()
    print(f"จำนวนหนังสือทั้งหมด: {len(updated_books)}")
    
    updated_borrowers = db.get_all_borrowers()
    print(f"จำนวนผู้ยืมทั้งหมด: {len(updated_borrowers)}")
    
    # ปิดการเชื่อมต่อ
    db.disconnect()
    print("\n✨ ทดสอบเสร็จสิ้น!")


if __name__ == "__main__":
    # ติดตั้ง library ที่จำเป็น
    print("📦 ตรวจสอบ Dependencies:")
    print("ต้องติดตั้ง: pip install psycopg2-binary")
    print()
    
    main()
