# 🔐 XXE Attack & Defense (Python)

## 📌 Overview

This project demonstrates the **XML External Entity (XXE) vulnerability** and how it can be prevented. It includes a vulnerable XML parser that allows data leakage and a secure version that blocks the attack.

---

## 📁 Files

* `vulnerable_app.py` → XXE attack works
* `secure_app.py` → XXE attack blocked

---

## ⚙️ Setup

```bash
pip install flask lxml
```

---

## ▶️ Run

```bash
python vulnerable_app.py
# OR
python secure_app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 💣 Test Payload (Windows)

```xml
<?xml version="1.0"?>
<!DOCTYPE data [
<!ENTITY xxe SYSTEM "file:///C:/Windows/System32/drivers/etc/hosts">
]>
<data>&xxe;</data>
```

---

## 🎯 Result

* Vulnerable app → shows file content 😈
* Secure app → blocks attack 🛡️

---

## 👤 Author

Umar Draz
