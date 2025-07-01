# ตัวอย่าง Prompt ที่ปรับปรุงแล้วสำหรับ Gemini CLI: โครงการ AI Library

เอกสารนี้รวบรวมตัวอย่าง Prompt ที่ปรับปรุงแล้วสำหรับใช้งานกับ Gemini CLI เพื่อช่วยในการพัฒนาโครงการ "AI Library" ให้มีประสิทธิภาพมากขึ้น

---

### 1. การเริ่มต้นและทำความเข้าใจภาพรวมโครงการ

**Prompt start:**
> please understand code based in this directory and describe me


### 2. การรันโปรเจกต์ (Frontend)

**Prompt เดิม:**
> ช่วย start project port 3000 เมื่อ start เสร็จแล้ว ให้แจ้งพร้อมกับรอรับคำสั่งในการพัฒนาต่อไป

**Prompt ที่ปรับปรุงแล้ว (Improved Prompt):**

> **Task:** เริ่มการทำงานของ Frontend Development Server
>
> 1.  **Command:** รันคำสั่งที่เหมาะสมเพื่อเริ่มต้นโปรเจกต์ React (เช่น `npm run dev` หรือ `npm start`)
> 2.  **Port:** กำหนดให้เซิร์ฟเวอร์ทำงานบน port `3000`
> 3.  **Action:** หลังจากรันคำสั่งแล้ว ให้ทำสิ่งต่อไปนี้:
>     *   ตรวจสอบ output จาก terminal เพื่อยืนยันว่าเซิร์ฟเวอร์เริ่มต้นสำเร็จและทำงานบน port 3000 โดยไม่มีข้อผิดพลาด
>     *   เมื่อสำเร็จแล้ว ให้แสดงข้อความว่า "✅ Frontend server is running at http://localhost:3000"
>     *   หากเกิดข้อผิดพลาด ให้แสดง error log ทั้งหมด
>     *   ให้ process นี้ทำงานต่อไป และรอรับคำสั่งใหม่จากฉัน

---

### 3. การสร้าง Backend API สำหรับ Chatbot

**Prompt เดิม:**
> ช่วยสร้าง python backend ในการเชื่อมต่อ AI Chatbot โดยอ้างอิงตัวอย่าง python code นี้ในการเชื่อมต่อ พร้อมทั้งสร้างไฟล์ env สำหรับบันทึก API key
>
> ```python
> import requests
>
> bearer_token = "xxxxxx"
> url = "https://genai.softnix.ai/external/api/chat-messages"
> payload = {
>   "query": "หนังสือเรียนภาษาไทยเหลืออยู่กี่เล่ม",
>   "inputs": {},
>   "citation": True,
>   "response_mode": "blocking"
> }
> headers = {
>   "Content-Type": "application/json",
>   "Authorization": f"Bearer {bearer_token}"
> }
> response = requests.post(url, json=payload, headers=headers, verify=False)
> ```


### 4. Commit ขึ้น Git
>
> ช่วย commit ขึ้น git https://github.com/rujirapongsn2/ChatLibrary.git