# โค้ดตัวอย่างสำหรับการส่งรีวิวหนังสือไปยัง GenAI API

โค้ด Python ด้านล่างนี้เป็นตัวอย่างการส่งข้อความรีวิวหนังสือไปยัง API ของ `genai.softnix.ai` เพื่อทำการประมวลผลบางอย่าง (เช่น สรุป, วิเคราะห์ความรู้สึก) โดยใช้ไลบรารี `requests`

```python
import requests

book_reviews = '''ผมเคยพยายามสร้างนิสัยใหม่ๆ มาหลายครั้งแต่ก็ล้มเหลวตลอดจนได้มาอ่าน Atomic Habits
                หนังสือเล่มนี้เปิดมุมมองใหม่เกี่ยวกับการเปลี่ยนแปลงตัวเอง มันเน้นที่ 'ระบบ' มากกว่า 'เป้าหมาย'
                ซึ่งเป็นสิ่งที่ผมมองข้ามไปตลอด เป็นหนังสือที่ควรค่าแก่การอ่านสำหรับทุกคนที่ต้องการพัฒนาตัวเอง'''

bearer_token = "xxxx"
url = "https://genai.softnix.ai/external/api/completion-messages"
payload = {
  "inputs": {"customer_review":book_reviews},
  "citation": True,
  "response_mode": "blocking"
}
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {bearer_token}"
}
response = requests.post(url, json=payload, headers=headers, verify=False)

# หากต้องการดูผลลัพธ์ที่ได้จาก API สามารถพิมพ์ตัวแปร response ได้
# print(response.status_code)
# print(response.json())
```

## คำอธิบายโค้ด

*   `import requests`: นำเข้าไลบรารี `requests` สำหรับการส่ง HTTP requests ใน Python
*   `book_reviews`: ตัวแปรชนิดสตริง (string) ที่เก็บข้อความรีวิวหนังสือเพื่อใช้เป็นข้อมูลนำเข้า (input)
*   `bearer_token`: ตัวแปรสำหรับเก็บ Token เพื่อยืนยันตัวตนในการเข้าใช้ API **คุณต้องเปลี่ยน `"xxxx"` ให้เป็น Token ที่ถูกต้องของคุณ**
*   `url`: ที่อยู่ (Endpoint) ของ API ที่เราต้องการส่งข้อมูลไป
*   `payload`: ข้อมูลที่จะส่งไปกับ request ในรูปแบบ Dictionary ประกอบด้วย:
    *   `inputs`: ข้อมูลหลักที่ต้องการให้ AI ประมวลผล ในที่นี้คือ `book_reviews`
    *   `citation`: ตั้งค่าเป็น `True` เพื่อขอการอ้างอิงแหล่งที่มา (ถ้ามี)
    *   `response_mode`: `"blocking"` หมายถึงให้รอจนกว่า API จะประมวลผลเสร็จและส่งคำตอบกลับมา
*   `headers`: ข้อมูลส่วนหัวของ request เพื่อบอกรายละเอียดเพิ่มเติมกับเซิร์ฟเวอร์ เช่น รูปแบบของข้อมูล (`Content-Type`) และข้อมูลการยืนยันตัวตน (`Authorization`)
*   `requests.post(...)`: คำสั่งสำหรับส่งข้อมูลไปยัง `url` ที่กำหนดโดยใช้เมธอด POST พร้อมกับแนบ `payload` และ `headers` ไปด้วย `verify=False` เป็นการปิดการตรวจสอบ SSL certificate (ควรใช้ด้วยความระมัดระวัง) ผลลัพธ์ที่ได้จากเซิร์ฟเวอร์จะถูกเก็บไว้ในตัวแปร `response`