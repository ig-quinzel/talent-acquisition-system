# Talent Acquisition Management System

A web-based **Talent Acquisition Management System** built using **Flask and SQLite** to streamline the recruitment workflow from manpower request submission to candidate selection and joining.

---

## 🚀 Features

- Talent acquisition request submission
- Multi-level approval workflow
- Job opening management
- Job status tracking
- Recruitment processing
- Candidate management
- Candidate interview and selection tracking
- Recruiter assignment
- Joining date tracking
- Recruitment status updates
- Request and job status synchronization
- Dashboard with recruitment insights
- Search and filtering
- Excel export of talent acquisition requests
- Approval history tracking

---

## 🔄 Recruitment Workflow

```text
Talent Request
      ↓
Approval 1
      ↓
Approval 2
      ↓
Final Approval
      ↓
Job Opening
      ↓
Recruitment Processing
      ↓
Candidate Applications
      ↓
Shortlisting
      ↓
Interview
      ↓
Selection
      ↓
Joining
```

---

# 📊 System Modules

## 1. Talent Requests

HR or employees can submit manpower requests with details such as:

- Employee information
- Department
- Position
- Vacancy reason
- Number of positions
- Employment type
- Location
- Required experience
- Qualification
- Skills
- Priority
- Required by date

---

## 2. Job Openings

Approved recruitment requests are managed as job openings.

### Job Statuses

- `Pending Approval`
- `Approved - Open`
- `Recruitment in Progress`
- `On Hold`
- `Filled`
- `Closed`

The job opening is linked to its original talent acquisition request, allowing the request status to remain synchronized with the current job status.

---

## 3. Recruitment Processing

Recruiters can update the recruitment progress of each job opening.

### Recruitment Information

- Recruiter
- Job posted date
- HR status
- Candidates received
- Shortlisted candidates
- Interviewed candidates
- Selected candidates
- Joining date
- Recruitment status
- Remarks

---

## 4. Candidate Management

Candidates can be added against specific job openings and processed through different recruitment stages.

### Candidate Information

- Candidate ID
- Candidate name
- Email
- Phone
- Qualification
- Experience
- Resume
- Application date
- Source
- Candidate status
- Recruiter
- Interview date
- Interview result
- Selection status
- Joining date
- Remarks

### Candidate Workflow

```text
Applied
   ↓
Shortlisted
   ↓
Interviewed
   ↓
Selected
   ↓
Joining
```

---

## 5. Dashboard

The dashboard provides an overview of recruitment activity and request trends.

### Key Performance Indicators

- Total requests
- Pending Approval 1
- Pending Approval 2
- HR Processing
- Approved Requests
- Rejected Requests

### Dashboard Analysis

- Department-wise requests
- Vacancy reason analysis
- Recruitment status analysis
- Employment type analysis
- Position-wise requests
- Monthly request trends
- HR status analysis

---

## 6. Search & Filtering

The system provides filtering and search functionality for easier request management.

Users can search and filter based on:

- Request ID
- Employee name
- Position
- Department
- Job status
- Recruitment status

---

## 7. Excel Export

Talent acquisition request data can be exported to **Excel** for reporting and further analysis.

The exported data includes:

- Request ID
- Request Date
- Employee Name
- Employee ID
- Department
- Designation
- Position
- Vacancy Reason
- Number of Positions
- Employment Type
- Location
- Required By
- Experience
- Qualification
- Required Skills
- Approval Status
- HR Status
- Recruiter
- Candidates Received
- Shortlisted
- Interviewed
- Selected
- Joining Date
- Final Status
- Remarks

---

## 8. Approval History

The system maintains approval history for recruitment requests.

The history records:

- Approval action
- Person who performed the action
- Remarks
- Timestamp

This provides better traceability of recruitment requests throughout the approval process.

---

# 🔄 Status Synchronization

The system synchronizes the status between **Job Openings** and **Talent Requests**.

For example:

| Job Opening Status | Request Status |
|---|---|
| Approved - Open | Approved |
| Recruitment in Progress | Processing |
| On Hold | Processing |
| Filled | Closed |
| Closed | Closed |
| Rejected | Rejected |

This ensures that the request status reflects the current recruitment stage of its corresponding job opening.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Backend programming |
| **Flask** | Web application framework |
| **SQLite** | Database |
| **SQLAlchemy** | Database ORM |
| **HTML** | Frontend structure |
| **CSS** | Frontend styling |
| **Jinja2** | Template rendering |
| **Pandas** | Data processing |
| **OpenPyXL** | Excel export |
| **Visual Studio Code** | Development environment |

---

# 📁 Project Structure

```text
Talent-Acquisition-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── request.html
│   ├── view_requests.html
│   ├── request_details.html
│   ├── request_history.html
│   ├── job_openings.html
│   ├── manage_job_opening.html
│   ├── process_requests.html
│   ├── process_request_details.html
│   ├── candidates.html
│   ├── add_candidate.html
│   ├── candidate_processing.html
│   └── dashboard.html
│
└── static/
    └── css/
        └── style.css
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
```

---

## 2. Navigate to the Project Directory

```bash
cd talent-acquisition-management-system
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
```

---

## 5. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 💾 Database

The application uses **SQLite** as its database.

The database file is:

```text
talent_acquisition.db
```

The database stores information related to:

- Talent requests
- Job openings
- Recruitment processing
- Candidates
- Approval history

The database tables are automatically created when the application starts.

---

# 🎯 Purpose

The system is designed to **digitize and simplify the traditional talent acquisition workflow** by connecting recruitment requests, approval processes, job openings, recruitment processing, candidate management, selection, and joining in a single platform.

Instead of maintaining recruitment information across multiple spreadsheets and separate processes, the system provides a centralized platform for HR teams to manage and track recruitment activities.

---

# 📈 Recruitment Tracking

The system enables HR and recruiters to track the complete recruitment lifecycle:

```text
Manpower Requirement
        ↓
Talent Request
        ↓
Approval Workflow
        ↓
Job Opening
        ↓
Job Posting
        ↓
Candidate Applications
        ↓
Shortlisting
        ↓
Interview
        ↓
Selection
        ↓
Joining
```

This provides visibility into the current stage of each recruitment request and job opening.

---

# 🔮 Future Enhancements

Potential future improvements include:

- User authentication
- Role-based access control
- HR/Admin/Recruiter roles
- Email notifications for approvals
- Resume file upload and storage
- Advanced candidate search
- Automated candidate screening
- Interview scheduling
- Recruitment turnaround-time analytics
- Automated recruitment reports
- Cloud database integration
- Production deployment
- Candidate communication and notifications

---

# 👩‍💻 Author

## Nandana K.

**Data Science | Python | Flask | SQL | Power BI**

---

# 🏷️ GitHub Topics

Recommended repository topics:

```text
flask
python
sqlalchemy
sqlite
talent-acquisition
recruitment
hr-management
candidate-management
jinja2
pandas
```

---

# 📄 License

This project is developed for educational and internship purposes.
