A modern web application built with **Flask** and **MySQL** that allows users to create and manage bank account records. This project demonstrates full-stack connectivity: Frontend (HTML/CSS), Backend (Python Flask), and Database (MySQL).

## 🚀 Features
- **Modern UI:** Clean, responsive design with CSS gradients and card layouts.
- **Real-time Validation:** Handles database errors (like duplicate account numbers) and displays them to the user.
- **Database Integration:** Full CRUD (Create) operation linked to a MySQL storage system.

## 🛠️ Project Architecture
The application follows a simple Client-Server architecture:
1. **Frontend:** `form.html` (Styled with CSS).
2. **Backend:** `user_reg.py` (Flask Server).
3. **Database:** `bankdb` (MySQL).



## 📋 Prerequisites
Before running this project, ensure you have:
- **Python 3.x** installed.
- **MySQL Server** installed and running.
- Necessary Python packages:
  ```bash
  pip3 install flask mysql-connector-python
