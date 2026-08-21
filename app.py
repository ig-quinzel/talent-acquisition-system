from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
from io import BytesIO
import os
from flask import Flask, render_template, request, redirect, url_for, send_file
app = Flask(__name__)

# Database configuration
database_url = os.environ.get("DATABASE_URL")

if database_url:
    if database_url.startswith("postgres://"):
        database_url = database_url.replace(
            "postgres://",
            "postgresql://",
            1
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url

else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///talent_acquisition.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



# Request table
class TalentRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    request_id = db.Column(db.String(20), unique=True, nullable=False)

    # Request details
    employee_name = db.Column(db.String(100), nullable=False)
    employee_id = db.Column(db.String(50))
    department = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100))
    position = db.Column(db.String(100), nullable=False)

    vacancy_reason = db.Column(db.String(50), nullable=False)
    number_of_positions = db.Column(db.Integer, default=1)

    employment_type = db.Column(db.String(50))
    location = db.Column(db.String(100))
    required_by = db.Column(db.String(20))
    priority = db.Column(db.String(30))

    experience = db.Column(db.String(100))
    qualification = db.Column(db.String(200))
    skills = db.Column(db.Text)
    salary_range = db.Column(db.String(100))
    justification = db.Column(db.Text)

    request_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Approval 1
    approval1_status = db.Column(
        db.String(30),
        default="Pending"
    )
    approval1_remarks = db.Column(db.Text)

    # Approval 2
    approval2_status = db.Column(
        db.String(30),
        default="Pending"
    )
    approval2_remarks = db.Column(db.Text)

    # HR processing
    hr_status = db.Column(
        db.String(50),
        default="Not Started"
    )

    recruiter = db.Column(db.String(100))
    candidates_received = db.Column(db.Integer, default=0)
    shortlisted = db.Column(db.Integer, default=0)
    interviewed = db.Column(db.Integer, default=0)
    selected = db.Column(db.Integer, default=0)
    joining_date = db.Column(db.String(20))

    # Final status
    final_status = db.Column(
    db.String(50),
    default="Pending Approval 1"
)

    remarks = db.Column(db.Text)

class JobOpening(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    job_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    # Link this Job Opening to the original Talent Request
    request_id = db.Column(
        db.Integer,
        db.ForeignKey("talent_request.id"),
        nullable=True
    )

    request_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    department = db.Column(
        db.String(100),
        nullable=False
    )

    position = db.Column(
        db.String(100),
        nullable=False
    )

    vacancy_reason = db.Column(
        db.String(50),
        nullable=False
    )

    number_of_positions = db.Column(
        db.Integer,
        default=1
    )

    employment_type = db.Column(
        db.String(50)
    )

    branch = db.Column(
        db.String(100)
    )

    required_by = db.Column(
        db.String(20)
    )

    priority = db.Column(
        db.String(30)
    )

    # Approval 1
    approval1_status = db.Column(
        db.String(30),
        default="Pending"
    )

    approval1_remarks = db.Column(
        db.Text
    )

    # Approval 2
    approval2_status = db.Column(
        db.String(30),
        default="Pending"
    )

    approval2_remarks = db.Column(
        db.Text
    )

    # Final Approval
    final_approval_status = db.Column(
        db.String(30),
        default="Pending"
    )

    final_approval_remarks = db.Column(
        db.Text
    )

    # Overall job status
    job_status = db.Column(
        db.String(50),
        default="Pending Approval"
    )
class JobProcessing(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    job_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    recruiter = db.Column(db.String(100))

    job_posted_date = db.Column(db.String(20))

    hr_status = db.Column(
        db.String(50),
        default="Not Started"
    )

    candidates_received = db.Column(
        db.Integer,
        default=0
    )

    shortlisted = db.Column(
        db.Integer,
        default=0
    )

    interviewed = db.Column(
        db.Integer,
        default=0
    )

    selected = db.Column(
        db.Integer,
        default=0
    )

    joining_date = db.Column(db.String(20))

    recruitment_status = db.Column(
        db.String(50),
        default="Not Started"
    )

    remarks = db.Column(db.Text)
class Candidate(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    candidate_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    # -----------------------------
    # JOB
    # -----------------------------

    job_id = db.Column(
        db.String(20),
        nullable=False
    )

    # -----------------------------
    # CANDIDATE DETAILS
    # -----------------------------

    candidate_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150)
    )

    phone = db.Column(
        db.String(20)
    )

    qualification = db.Column(
        db.String(200)
    )

    experience = db.Column(
        db.String(100)
    )

    resume = db.Column(
        db.String(255)
    )

    application_date = db.Column(
        db.String(20)
    )

    source = db.Column(
        db.String(100)
    )

    # -----------------------------
    # CANDIDATE PROCESSING
    # -----------------------------

    candidate_status = db.Column(
        db.String(50),
        default="Applied"
    )

    recruiter = db.Column(
        db.String(100)
    )

    interview_date = db.Column(
        db.String(20)
    )

    interview_result = db.Column(
        db.String(50)
    )

    selection_status = db.Column(
        db.String(50),
        default="Pending"
    )

    joining_date = db.Column(
        db.String(20)
    )

    remarks = db.Column(
        db.Text
    )
class ApprovalHistory(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    request_id = db.Column(
        db.Integer,
        db.ForeignKey("talent_request.id"),
        nullable=False
    )

    action = db.Column(
        db.String(100),
        nullable=False
    )

    performed_by = db.Column(
        db.String(100)
    )

    remarks = db.Column(
        db.Text
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
def create_job_opening(req):

    # Generate Job ID
    job_id = f"J-{1000 + req.id}"

    # Check if Job Opening already exists
    existing_job = JobOpening.query.filter_by(
        job_id=job_id
    ).first()

    if existing_job:
        return existing_job

    # Create new Job Opening
    job = JobOpening(
        job_id=job_id,

        request_date=req.request_date,

        department=req.department,
        position=req.position,

        vacancy_reason=req.vacancy_reason,
        number_of_positions=req.number_of_positions,

        employment_type=req.employment_type,
        branch=req.location,
        required_by=req.required_by,
        priority=req.priority,

        approval1_status=req.approval1_status,
        approval1_remarks=req.approval1_remarks,

        approval2_status=req.approval2_status,
        approval2_remarks=req.approval2_remarks,

        final_approval_status="Approved",

        job_status="Approved - Open"
    )

    db.session.add(job)

    return job

# Create database tables
with app.app_context():
    db.create_all()
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/request")
def request_page():
    return render_template("request.html")


@app.route("/submit-request", methods=["POST"])
def submit_request():

    # Generate request ID
    last_request = TalentRequest.query.order_by(
        TalentRequest.id.desc()
    ).first()

    if last_request:
        number = last_request.id + 1
    else:
        number = 1

    request_id = f"TA-{number:04d}"

    new_request = TalentRequest(
        request_id=request_id,

        employee_name=request.form["employee_name"],
        employee_id=request.form["employee_id"],
        department=request.form["department"],
        designation=request.form["designation"],
        position=request.form["position"],

        vacancy_reason=request.form["vacancy_reason"],
        number_of_positions=request.form["number_of_positions"],

        employment_type=request.form["employment_type"],
        location=request.form["location"],
        required_by=request.form["required_by"],
        priority=request.form["priority"],

        experience=request.form["experience"],
        qualification=request.form["qualification"],
        skills=request.form["skills"]
    )

    db.session.add(new_request)
    db.session.commit()

# --------------------------------
# CREATE JOB OPENING
# --------------------------------

    job_id = f"J-{1000 + new_request.id}"

    new_job = JobOpening(
    job_id=job_id,

    request_id=new_request.id,

    request_date=new_request.request_date,

    department=new_request.department,
    position=new_request.position,
    vacancy_reason=new_request.vacancy_reason,
    number_of_positions=new_request.number_of_positions,

    employment_type=new_request.employment_type,
    branch=new_request.location,
    required_by=new_request.required_by,
    priority=new_request.priority,

    approval1_status="Pending",
    approval1_remarks="",

    approval2_status="Pending",
    approval2_remarks="",

    final_approval_status="Pending",
    final_approval_remarks="",

    job_status="Pending Approval")

    db.session.add(new_job)
    db.session.commit()

    return redirect(url_for("view_requests"))
@app.route("/view-requests")
def view_requests():

    search = request.args.get("search", "").strip()
    department = request.args.get("department", "").strip()
    status = request.args.get("status", "").strip()

    query = TalentRequest.query

    # Search
    if search:
        query = query.filter(
            db.or_(
                TalentRequest.request_id.ilike(f"%{search}%"),
                TalentRequest.employee_name.ilike(f"%{search}%"),
                TalentRequest.position.ilike(f"%{search}%")
            )
        )

    # Department
    if department:
        query = query.filter(
            TalentRequest.department == department
        )

    requests = query.order_by(
        TalentRequest.id.desc()
    ).all()

    # --------------------------------
    # GET JOB STATUS FOR EACH REQUEST
    # --------------------------------

    job_status_data = {}

    for req in requests:

        job = JobOpening.query.filter_by(
            job_id=f"J-{1000 + req.id}"
        ).first()

        if job:
            job_status_data[req.id] = job.job_status
        else:
            job_status_data[req.id] = "Not Created"

    # --------------------------------
    # STATUS FILTER
    # --------------------------------

    if status:

        requests = [
            req for req in requests
            if job_status_data.get(req.id) == status
        ]

    # --------------------------------
    # DEPARTMENTS
    # --------------------------------

    departments = db.session.query(
        TalentRequest.department
    ).distinct().order_by(
        TalentRequest.department
    ).all()

    return render_template(
        "view_requests.html",

        requests=requests,

        job_status_data=job_status_data,

        departments=[
            d[0] for d in departments
        ],

        search=search,

        selected_department=department,

        selected_status=status
    )
@app.route("/job-openings")
def job_openings():

    openings = JobOpening.query.order_by(
        JobOpening.id.desc()
    ).all()

    return render_template(
        "job_openings.html",
        openings=openings
    )
@app.route("/job-openings/<int:job_id>/manage")
def manage_job_opening(job_id):

    job = JobOpening.query.get_or_404(job_id)

    return render_template(
        "manage_job_opening.html",
        job=job
    )
@app.route(
    "/job-openings/<int:job_id>/update",
    methods=["POST"]
)
def update_job_opening(job_id):

    job = JobOpening.query.get_or_404(job_id)

    # -----------------------------
    # APPROVAL 1
    # -----------------------------

    job.approval1_status = request.form.get(
        "approval1_status",
        "Pending"
    )

    job.approval1_remarks = request.form.get(
        "approval1_remarks",
        ""
    )

    # -----------------------------
    # APPROVAL 2
    # -----------------------------

    job.approval2_status = request.form.get(
        "approval2_status",
        "Pending"
    )

    job.approval2_remarks = request.form.get(
        "approval2_remarks",
        ""
    )

    # -----------------------------
    # FINAL APPROVAL
    # -----------------------------

    job.final_approval_status = request.form.get(
        "final_approval_status",
        "Pending"
    )

    job.final_approval_remarks = request.form.get(
        "final_approval_remarks",
        ""
    )

    # -----------------------------
    # JOB STATUS
    # -----------------------------

    job.job_status = request.form.get(
        "job_status",
        job.job_status
    )

    # -----------------------------
    # SAVE
    # -----------------------------

    db.session.commit()

    return redirect(
        url_for("job_openings")
    )
@app.route("/request/<int:request_id>")
def request_details(request_id):

    req = TalentRequest.query.get_or_404(request_id)

    # Find the JobOpening created from this request
    job = JobOpening.query.filter_by(
        request_id=req.id
    ).first()

    return render_template(
        "request_details.html",
        req=req,
        job=job
    )
@app.route("/process-requests")
def process_requests():

    search = request.args.get("search", "").strip()
    department = request.args.get("department", "").strip()
    status = request.args.get("status", "").strip()

    # Only approved jobs enter Job Processing
    query = JobOpening.query.filter(
        JobOpening.final_approval_status == "Approved"
    )

    if search:
        query = query.filter(
            db.or_(
                JobOpening.job_id.ilike(f"%{search}%"),
                JobOpening.department.ilike(f"%{search}%"),
                JobOpening.position.ilike(f"%{search}%")
            )
        )

    if department:
        query = query.filter(
            JobOpening.department == department
        )

    if status:
        query = query.filter(
            JobOpening.job_status == status
        )

    openings = query.order_by(
        JobOpening.id.desc()
    ).all()

    departments = db.session.query(
        JobOpening.department
    ).distinct().order_by(
        JobOpening.department
    ).all()

    # Get processing data for every job
    processing_data = {}

    for job in openings:

        processing = JobProcessing.query.filter_by(
            job_id=job.job_id
        ).first()

        processing_data[job.job_id] = processing

    return render_template(
        "process_requests.html",

        openings=openings,

        processing_data=processing_data,

        departments=[
            d[0] for d in departments
        ],

        search=search,

        selected_department=department,

        selected_status=status
    )
@app.route("/process-requests/<int:job_id>")
def process_job_details(job_id):

    job = JobOpening.query.get_or_404(job_id)

    processing = JobProcessing.query.filter_by(
        job_id=job.job_id
    ).first()

    return render_template(
        "process_request_details.html",
        job=job,
        processing=processing
    )
@app.route(
    "/process-requests/<int:job_id>/update",
    methods=["POST"]
)
def update_job_processing(job_id):

    job = JobOpening.query.get_or_404(job_id)

    # --------------------------------
    # FIND / CREATE PROCESSING RECORD
    # --------------------------------

    processing = JobProcessing.query.filter_by(
        job_id=job.job_id
    ).first()

    if not processing:
        processing = JobProcessing(
            job_id=job.job_id
        )
        db.session.add(processing)

    # --------------------------------
    # UPDATE PROCESSING INFORMATION
    # --------------------------------

    processing.recruiter = request.form.get(
        "recruiter", ""
    )

    processing.job_posted_date = request.form.get(
        "job_posted_date", ""
    )

    processing.hr_status = request.form.get(
        "hr_status",
        "Not Started"
    )

    processing.candidates_received = int(
        request.form.get(
            "candidates_received",
            0
        ) or 0
    )

    processing.shortlisted = int(
        request.form.get(
            "shortlisted",
            0
        ) or 0
    )

    processing.interviewed = int(
        request.form.get(
            "interviewed",
            0
        ) or 0
    )

    processing.selected = int(
        request.form.get(
            "selected",
            0
        ) or 0
    )

    processing.joining_date = request.form.get(
        "joining_date",
        ""
    )

    processing.recruitment_status = request.form.get(
        "recruitment_status",
        "Not Started"
    )

    processing.remarks = request.form.get(
        "remarks",
        ""
    )

    # --------------------------------
    # UPDATE JOB OPENING STATUS
    # --------------------------------

    if processing.recruitment_status == "Recruitment in Progress":

        job.job_status = "Recruitment in Progress"

    elif processing.recruitment_status == "Filled":

        job.job_status = "Filled"

    elif processing.recruitment_status == "On Hold":

        job.job_status = "On Hold"

    elif processing.recruitment_status == "Closed":

        job.job_status = "Closed"

    elif processing.recruitment_status == "Not Started":

        job.job_status = "Approved - Open"

    # --------------------------------
    # FIND CORRESPONDING TALENT REQUEST
    # --------------------------------

    request_record = TalentRequest.query.get(
    job.request_id
)
    if request_record:

      if job.job_status == "Approved - Open":
        request_record.final_status = "Approved"

      elif job.job_status == "Recruitment in Progress":
        request_record.final_status = "Processing"

      elif job.job_status == "Filled":
        request_record.final_status = "Closed"

      elif job.job_status == "On Hold":
        request_record.final_status = "Processing"

      elif job.job_status == "Closed":
        request_record.final_status = "Closed"

      elif job.job_status == "Rejected":
        request_record.final_status = "Rejected"

    # --------------------------------
    # SYNC JOB STATUS → REQUEST STATUS
    # --------------------------------

    if request_record:

        if job.job_status == "Approved - Open":

            request_record.final_status = "Approved"

        elif job.job_status == "Recruitment in Progress":

            request_record.final_status = "Processing"

        elif job.job_status == "Filled":

            request_record.final_status = "Closed"

        elif job.job_status == "On Hold":

            request_record.final_status = "Processing"

        elif job.job_status == "Closed":

            request_record.final_status = "Closed"

        elif job.job_status == "Rejected":

            request_record.final_status = "Rejected"

    # --------------------------------
    # ALSO SYNC HR PROCESSING DATA
    # --------------------------------

    if request_record:

        request_record.hr_status = processing.hr_status
        request_record.recruiter = processing.recruiter
        request_record.candidates_received = processing.candidates_received
        request_record.shortlisted = processing.shortlisted
        request_record.interviewed = processing.interviewed
        request_record.selected = processing.selected
        request_record.joining_date = processing.joining_date
        request_record.remarks = processing.remarks

    # --------------------------------
    # SAVE
    # --------------------------------

    db.session.commit()

    return redirect(
        url_for("process_requests")
    )
@app.route("/candidates/add")
def add_candidate():

    # Only approved jobs can receive candidates
    jobs = JobOpening.query.filter(
        JobOpening.final_approval_status == "Approved"
    ).order_by(
        JobOpening.id.desc()
    ).all()

    return render_template(
        "add_candidate.html",
        jobs=jobs
    )
@app.route("/candidates/submit", methods=["POST"])
def submit_candidate():

    # Generate Candidate ID
    last_candidate = Candidate.query.order_by(
        Candidate.id.desc()
    ).first()

    if last_candidate:
        number = last_candidate.id + 1
    else:
        number = 1

    candidate_id = f"CAN-{number:04d}"

    new_candidate = Candidate(

        candidate_id=candidate_id,

        job_id=request.form["job_id"],

        candidate_name=request.form["candidate_name"],

        email=request.form.get(
            "email",
            ""
        ),

        phone=request.form.get(
            "phone",
            ""
        ),

        qualification=request.form.get(
            "qualification",
            ""
        ),

        experience=request.form.get(
            "experience",
            ""
        ),

        resume=request.form.get(
            "resume",
            ""
        ),

        application_date=request.form.get(
            "application_date",
            ""
        ),

        source=request.form.get(
            "source",
            ""
        ),

        candidate_status="Applied",

        interview_date="",

        interview_result="",

        remarks=""
    )

    db.session.add(new_candidate)

    db.session.commit()

    return redirect(
        url_for("candidates")
    )
@app.route("/candidates")
def candidates():

    candidates = Candidate.query.order_by(
        Candidate.id.desc()
    ).all()

    return render_template(
        "candidates.html",
        candidates=candidates
    )
@app.route("/candidates/<int:candidate_id>/process")
def process_candidate(candidate_id):

    candidate = Candidate.query.get_or_404(candidate_id)

    job = JobOpening.query.filter_by(
        job_id=candidate.job_id
    ).first()

    return render_template(
        "candidate_processing.html",
        candidate=candidate,
        job=job
    )
@app.route(
    "/candidates/<int:candidate_id>/process/update",
    methods=["POST"]
)
def update_candidate_processing(candidate_id):

    candidate = Candidate.query.get_or_404(
        candidate_id
    )

    candidate.recruiter = request.form.get(
        "recruiter",
        ""
    )

    candidate.candidate_status = request.form.get(
        "candidate_status",
        "Applied"
    )

    candidate.interview_date = request.form.get(
        "interview_date",
        ""
    )

    candidate.interview_result = request.form.get(
        "interview_result",
        ""
    )

    candidate.selection_status = request.form.get(
        "selection_status",
        "Pending"
    )

    candidate.joining_date = request.form.get(
        "joining_date",
        ""
    )

    candidate.remarks = request.form.get(
        "remarks",
        ""
    )

    db.session.commit()

    return redirect(
        url_for("candidates")
    )
@app.route("/dashboard")
def dashboard():

    # -----------------------------
    # FILTER VALUES
    # -----------------------------

    department = request.args.get("department", "").strip()
    vacancy_reason = request.args.get("vacancy_reason", "").strip()
    final_status = request.args.get("final_status", "").strip()
    hr_status = request.args.get("hr_status", "").strip()
    employment_type = request.args.get("employment_type", "").strip()


    # -----------------------------
    # BASE QUERY
    # -----------------------------

    query = TalentRequest.query


    # Department
    if department:
        query = query.filter(
            TalentRequest.department == department
        )


    # Vacancy reason
    if vacancy_reason:
        query = query.filter(
            TalentRequest.vacancy_reason == vacancy_reason
        )


    # Final status
    if final_status:
        query = query.filter(
            TalentRequest.final_status == final_status
        )


    # HR status
    if hr_status:
        query = query.filter(
            TalentRequest.hr_status == hr_status
        )


    # Employment type
    if employment_type:
        query = query.filter(
            TalentRequest.employment_type == employment_type
        )


    requests_data = query.order_by(
        TalentRequest.id.asc()
    ).all()


    # -----------------------------
    # KPI VALUES
    # -----------------------------

    total_requests = len(requests_data)


    pending_approval1 = sum(
        1 for r in requests_data
        if r.approval1_status == "Pending"
    )


    pending_approval2 = sum(
        1 for r in requests_data
        if r.approval1_status == "Approved"
        and r.approval2_status == "Pending"
    )


    hr_processing = sum(
        1 for r in requests_data
        if r.hr_status != "Not Started"
        and r.final_status != "Rejected"
        and r.final_status != "Closed"
    )


    approved_requests = sum(
        1 for r in requests_data
        if r.final_status == "Approved"
    )


    rejected_requests = sum(
        1 for r in requests_data
        if r.final_status == "Rejected"
    )


    # -----------------------------
    # DEPARTMENT DATA
    # -----------------------------

    department_counts = {}

    for r in requests_data:

        dept = r.department or "Unknown"

        department_counts[dept] = (
            department_counts.get(dept, 0) + 1
        )


    department_labels = list(
        department_counts.keys()
    )

    department_values = list(
        department_counts.values()
    )


    # -----------------------------
    # VACANCY REASON
    # -----------------------------

    reason_counts = {}

    for r in requests_data:

        reason = r.vacancy_reason or "Unknown"

        reason_counts[reason] = (
            reason_counts.get(reason, 0) + 1
        )


    reason_labels = list(
        reason_counts.keys()
    )

    reason_values = list(
        reason_counts.values()
    )


    # -----------------------------
    # FINAL STATUS
    # -----------------------------

    status_counts = {}

    for r in requests_data:

        status = r.final_status or "Unknown"

        status_counts[status] = (
            status_counts.get(status, 0) + 1
        )


    status_labels = list(
        status_counts.keys()
    )

    status_values = list(
        status_counts.values()
    )


    # -----------------------------
    # HR STATUS
    # -----------------------------

    hr_counts = {}

    for r in requests_data:

        status = r.hr_status or "Unknown"

        hr_counts[status] = (
            hr_counts.get(status, 0) + 1
        )


    hr_labels = list(
        hr_counts.keys()
    )

    hr_values = list(
        hr_counts.values()
    )


    # -----------------------------
    # EMPLOYMENT TYPE
    # -----------------------------

    employment_counts = {}

    for r in requests_data:

        emp = r.employment_type or "Unknown"

        employment_counts[emp] = (
            employment_counts.get(emp, 0) + 1
        )


    employment_labels = list(
        employment_counts.keys()
    )

    employment_values = list(
        employment_counts.values()
    )


    # -----------------------------
    # POSITION DATA
    # -----------------------------

    position_counts = {}

    for r in requests_data:

        position = r.position or "Unknown"

        position_counts[position] = (
            position_counts.get(position, 0) + 1
        )


    # Sort positions by count
    position_counts = dict(
        sorted(
            position_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
    )


    position_labels = list(
        position_counts.keys()
    )

    position_values = list(
        position_counts.values()
    )


    # -----------------------------
    # MONTHLY TREND
    # -----------------------------

    monthly_counts = {}

    for r in requests_data:

        if r.request_date:

            month = r.request_date.strftime(
                "%b %Y"
            )

            monthly_counts[month] = (
                monthly_counts.get(month, 0) + 1
            )


    monthly_labels = list(
        monthly_counts.keys()
    )

    monthly_values = list(
        monthly_counts.values()
    )




    # -----------------------------
    # FILTER OPTIONS
    # -----------------------------

    departments = [
        x[0]
        for x in db.session.query(
            TalentRequest.department
        ).distinct().order_by(
            TalentRequest.department
        ).all()
        if x[0]
    ]


    vacancy_reasons = [
        x[0]
        for x in db.session.query(
            TalentRequest.vacancy_reason
        ).distinct().order_by(
            TalentRequest.vacancy_reason
        ).all()
        if x[0]
    ]


    employment_types = [
        x[0]
        for x in db.session.query(
            TalentRequest.employment_type
        ).distinct().order_by(
            TalentRequest.employment_type
        ).all()
        if x[0]
    ]


    hr_statuses = [
        x[0]
        for x in db.session.query(
            TalentRequest.hr_status
        ).distinct().order_by(
            TalentRequest.hr_status
        ).all()
        if x[0]
    ]


    final_statuses = [
        x[0]
        for x in db.session.query(
            TalentRequest.final_status
        ).distinct().order_by(
            TalentRequest.final_status
        ).all()
        if x[0]
    ]


    return render_template(
        "dashboard.html",

        total_requests=total_requests,
        pending_approval1=pending_approval1,
        pending_approval2=pending_approval2,
        hr_processing=hr_processing,
        approved_requests=approved_requests,
        rejected_requests=rejected_requests,

        department_labels=department_labels,
        department_values=department_values,

        reason_labels=reason_labels,
        reason_values=reason_values,

        status_labels=status_labels,
        status_values=status_values,

        hr_labels=hr_labels,
        hr_values=hr_values,

        employment_labels=employment_labels,
        employment_values=employment_values,

        position_labels=position_labels,
        position_values=position_values,

        monthly_labels=monthly_labels,
        monthly_values=monthly_values,

        departments=departments,
        vacancy_reasons=vacancy_reasons,
        employment_types=employment_types,
        hr_statuses=hr_statuses,
        final_statuses=final_statuses,

        selected_department=department,
        selected_vacancy_reason=vacancy_reason,
        selected_employment_type=employment_type,
        selected_hr_status=hr_status,
        selected_final_status=final_status
    )
@app.route("/export-excel")
def export_excel():

    requests = TalentRequest.query.order_by(
        TalentRequest.id.asc()
    ).all()

    data = []

    for req in requests:

        data.append({

            "Request ID": req.request_id,
            "Request Date": (
                req.request_date.strftime("%d-%m-%Y")
                if req.request_date
                else ""
            ),

            "Employee Name": req.employee_name,
            "Employee ID": req.employee_id or "",
            "Department": req.department,
            "Designation": req.designation or "",
            "Position": req.position,

            "Vacancy Reason": req.vacancy_reason,
            "Number of Positions": req.number_of_positions,

            "Employment Type": req.employment_type or "",
            "Location": req.location or "",
            "Required By": req.required_by or "",

            "Experience": req.experience or "",
            "Qualification": req.qualification or "",
            "Required Skills": req.skills or "",

            "Approval 1": req.approval1_status,
            "Approval 1 Remarks": req.approval1_remarks or "",

            "Approval 2": req.approval2_status,
            "Approval 2 Remarks": req.approval2_remarks or "",

            "HR Status": req.hr_status,
            "Recruiter": req.recruiter or "",

            "Candidates Received": req.candidates_received,
            "Shortlisted": req.shortlisted,
            "Interviewed": req.interviewed,
            "Selected": req.selected,

            "Joining Date": req.joining_date or "",

            "Final Status": req.final_status,
            "Remarks": req.remarks or ""
        })


    df = pd.DataFrame(data)


    # Create Excel file in memory

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Talent Requests"
        )


    output.seek(0)


    return send_file(
        output,
        as_attachment=True,
        download_name="Talent_Acquisition_Requests.xlsx",
        mimetype=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )
@app.route("/request/<int:request_id>/history")
def request_history(request_id):

    req = TalentRequest.query.get_or_404(request_id)

    history = ApprovalHistory.query.filter_by(
        request_id=req.id
    ).order_by(
        ApprovalHistory.timestamp.desc()
    ).all()

    return render_template(
        "request_history.html",
        req=req,
        history=history
    )

if __name__ == "__main__":
    app.run(debug=True)
