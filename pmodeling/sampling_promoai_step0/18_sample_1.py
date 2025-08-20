root = StrictPartialOrder()

# Submission
submit = Transition('Submit application online')
root.nodes.add(submit)

# Application Review
review = Transition('Review application and documents')
root.nodes.add(review)
root.order.add_edge(submit, review)

# Notify missing documents
missing = Transition('Notify applicant of missing documents')
root.nodes.add(missing)
root.order.add_edge(review, missing)

# Provide missing documents
provide = Transition('Provide missing documents')
root.nodes.add(provide)
root.order.add_edge(missing, provide)

# Admission Committee
admit = Transition('Evaluate application by admissions committee')
root.nodes.add(admit)
root.order.add_edge(provide, admit)

# Finance Department
fee = Transition('Process fees or waivers')
root.nodes.add(fee)
root.order.add_edge(review, fee)

# Acceptance Letter
accept = Transition('Send acceptance letter')
root.nodes.add(accept)
root.order.add_edge(admit, accept)

# Orientation
orient = Transition('Send orientation materials')
root.nodes.add(orient)
root.order.add_edge(admit, orient)

# Rejection Letter
reject = Transition('Send rejection letter')
root.nodes.add(reject)
root.order.add_edge(admit, reject)

# Loop for Enrollment
enroll = Transition('Confirm enrollment')
root.nodes.add(enroll)
root.order.add_edge(accept, enroll)
root.order.add_edge(reject, enroll)

# IT Department
it = Transition('Set up IT accounts')
root.nodes.add(it)
root.order.add_edge(enroll, it)

# International Student Office
intl = Transition('Assist with visa processing')
root.nodes.add(intl)
root.order.add_edge(enroll, intl)

# Academic Advisor
advisor = Transition('Meet with academic advisor')
root.nodes.add(advisor)
root.order.add_edge(enroll, advisor)

# Select Courses
select = Transition('Select courses')
root.nodes.add(select)
root.order.add_edge(advisor, select)

# Resolve Schedule Conflicts
resolve = Transition('Resolve schedule conflicts')
root.nodes.add(resolve)
root.order.add_edge(select, resolve)

# Begin Attending Classes
begin = Transition('Begin attending classes')
root.nodes.add(begin)
root.order.add_edge(resolve, begin)

# Add/Drop Courses
add_drop = Transition('Add/drop courses')
root.nodes.add(add_drop)
root.order.add_edge(begin, add_drop)

# Graduate
graduate = Transition('Graduate')
root.nodes.add(graduate)
root.order.add_edge(begin, graduate)

# Loop for Semesters
semester = Transition('Semester')
root.nodes.add(semester)
root.order.add_edge(enroll, semester)

# Loop for Grades
grade = Transition('Post grades')
root.nodes.add(grade)
root.order.add_edge(begin, grade)

# Loop for Grades
review_grades = Transition('Review grades online')
root.nodes.add(review_grades)
root.order.add_edge(grade, review_grades)

# Loop for Appeals
appeal = Transition('Submit appeal form')
root.nodes.add(appeal)
root.order.add_edge(grade, appeal)

# Loop for Appeals
appeal_committee = Transition('Meet with appeals committee')
root.nodes.add(appeal_committee)
root.order.add_edge(appeal, appeal_committee)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root.order.add_edge(appeal_committee, decision)

# Loop for Appeals
decision = Transition('Await decision')
root.nodes.add(decision)
root