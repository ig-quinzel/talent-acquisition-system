# Talent Acquisition Management System

A web-based Talent Acquisition Management System built using Flask and SQLite to streamline the recruitment workflow from manpower request submission to candidate selection and joining.

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
📊 System Modules
1. Talent Requests

HR or employees can submit manpower requests with details such as:

Employee information
Department
Position
Vacancy reason
Number of positions
Employment type
Location
Required experience
Qualification
Skills
Priority
2. Job Openings

Approved recruitment requests are managed as job openings.

Job statuses include:

Pending Approval
Approved - Open
Recruitment in Progress
On Hold
Filled
Closed
3. Recruitment Processing

Recruiters can update:

Recruiter
Job posted date
HR status
Candidates received
Shortlisted candidates
Interviewed candidates
Selected candidates
Joining date
Recruitment status
Remarks
4. Candidate Management

Candidates can be added against specific job openings and processed through different recruitment stages.

Candidate information includes:

Candidate ID
Name
Email
Phone
Qualification
Experience
Resume
Application date
Source
Candidate status
Interview date
Interview result
Selection status
Joining date
5. Dashboard

The dashboard provides an overview of recruitment activity through:

Total requests
Pending approvals
HR processing
Approved requests
Rejected requests
Department-wise requests
Vacancy reason analysis
Recruitment status analysis
Employment type analysis
Position-wise requests
Monthly request trends
6. Excel Export

Talent acquisition request data can be exported to Excel for reporting and further analysis.

🛠️ Technology Stack
Backend: Python, Flask
Database: SQLite
ORM: SQLAlchemy
Frontend: HTML, CSS, Jinja2
Data Processing: Pandas
Excel Export: OpenPyXL
Development Environment: Visual Studio Code
📁 Project Structure
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
⚙️ Installation

Clone the repository:

git clone <repository-url>

Navigate to the project directory:

cd Talent-Acquisition-System

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The application will be available at:

http://127.0.0.1:5000
🎯 Purpose

The system is designed to digitize and simplify the traditional talent acquisition workflow by connecting recruitment requests, approval processes, job openings, recruitment processing, and candidate management in a single platform.

👩‍💻 Author

Nandana K.

Data Science | Flask | Python | SQL | Power BI



### One more thing


For your GitHub repo, I'd use:


**Name:** `talent-acquisition-management-system`


**Description:**


> Flask-based Talent Acquisition Management System for recruitment requests, approvals, job openings, candidate processing, and recruitment tracking.


**Topics:**


`flask` `python` `sqlalchemy` `sqlite` `talent-acquisition` `recruitment` `hr-management` `candidate-management` `jinja2` `pandas`
