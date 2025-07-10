# webhook-repo


✅ README.md for Your GitHub Webhook Assignment

# 🔔 GitHub Webhook Listener with Flask + MongoDB

This project listens to GitHub events like push and pull request merge, stores them in MongoDB, and shows them on a live UI.

---

## 📌 What I Built

- A Flask server to receive GitHub webhooks
- A MongoDB database to store events
- A frontend page to display events in real-time
- Used ngrok to expose my localhost to GitHub
- GitHub Actions send webhook data to my Flask app

---

## 🛠 Technologies Used

- Python (Flask)
- MongoDB (local)
- GitHub Actions
- ngrok (for local public URL)
- HTML (for UI)

---

## 📦 Python Packages Used

Install these first:

```bash
pip install flask pymongo dnspython python-dateutil


---

🗂 Folder Structure

webhook-project/
│
├── app.py                  # Flask server
├── templates/
│   └── events.html         # HTML to display GitHub events
├── .github/
│   └── workflows/
│       └── webhook.yml     # GitHub Action to send webhook


---

🚀 Step-by-Step Setup

1. Clone Repo & Set Up Flask

git clone <your-repo-url>
cd webhook-project
pip install -r requirements.txt  # or install manually

Create a file app.py and add your Flask code.

2. Start MongoDB Locally

Make sure MongoDB is installed on your system.

Run:

mongod

(MongoDB will now run on localhost:27017)

3. Start Flask App

In terminal:

python app.py

Should show:

Running on http://127.0.0.1:5000/

4. Start ngrok

In another terminal:

ngrok http 5000

Copy the HTTPS URL shown (e.g., https://abc1234.ngrok.io)

5. Update webhook.yml

In .github/workflows/webhook.yml, replace <your-ngrok-url> with your current ngrok HTTPS URL.

Push this file to GitHub.


---

🧪 How to Test Webhooks

✅ For Push Events:

1. Make a change in the repo


2. Run:



git add .
git commit -m "Test push"
git push

You’ll see event data in your Flask terminal.


---

✅ For Merge Events:

1. Create a new branch:



git checkout -b feature/merge-test
echo "Test" >> merge.md
git add .
git commit -m "Merge test"
git push origin feature/merge-test

2. Go to GitHub → Create Pull Request → Merge It



Now the webhook will trigger with action: "merge" and show in the UI.


---

⚠ Common Errors & Fixes

❌ Error	💡 Fix

500 Internal Server Error	Caused by timestamp format — fixed using dateutil.parser
bash: git: command not found	Git was not installed — installed from git-scm.com
Flask shows data = None	You missed -H "Content-Type: application/json" in curl
PR merged but nothing happens	Forgot to update ngrok URL in webhook.yml
MongoDB not showing DB	Fixed by running mongod first, then checking MongoDB Compass
Timestamp format error	Solved using: timestamp = parser.parse(data["timestamp"])



---

✅ Final Output

Your web UI shows a live list of recent GitHub events (pushes and merges)

MongoDB stores each event with full details

You now have a working full-stack project 🔥



---

🧠 What I Learned

How to work with Flask and MongoDB

How GitHub Actions work

How webhooks send data

How to debug real-time backend errors

How to expose localhost using ngrok



---

✅ Next Steps (Optional)

Deploy Flask app on Render

Use MongoDB Atlas (free cloud database)

Add login system or admin panel

Improve UI using Bootstrap



---

🙌 Made with 💻 by [Ketan Ikhankar]

