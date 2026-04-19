# blue-green-deployment
CI/CD for Containerized Applications with Blue-Green Deployment

📌 Project Overview
This project demonstrates a modern CI/CD pipeline for containerized web applications using **Docker**, **Jenkins**, and **Blue-Green Deployment** strategy.

The application used is **ElectroMart**, an e-commerce web application built with **Flask**. Two environments were created:

- 🔵 **Blue Environment** → Stable production version  
- 🟢 **Green Environment** → Updated version with enhanced UI and features  

Traffic can be switched from Blue to Green with zero downtime.

---
Live Demo

Hosted Link: `https://blue-green-deployment-fjqs.onrender.com/`

- First open → Blue Version  
- Refresh page → Green Version  

---

Technologies Used

- Python  
- Flask  
- HTML / CSS / Jinja2  
- Docker  
- Jenkins  
- NGINX  
- GitHub  
- Render  

---

Project Structure

```text
blue-green-deployment/
│── app.py
│── requirements.txt
│── static/
│── templates/
│── README.md`

- First open → Blue Version  
- Refresh page → Green Version  

---
Features
🔵 Blue Version
Stable production environment
Basic UI theme
Product listing
Cart support

🟢 Green Version
Enhanced modern UI
Search & Filters
Login / Signup
Cart & Checkout
Orders page

---

Blue-Green Deployment Workflow
-Existing users are served through Blue environment
-New version is deployed in Green environment
-Green environment is tested
-Traffic is switched from Blue → Green
-Zero downtime achieved
