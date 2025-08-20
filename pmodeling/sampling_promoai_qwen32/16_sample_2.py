import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
send_notification = Transition(label='Send notification')
prepare_statements = Transition(label='Prepare financial statements')
gather_documents = Transition(label='Gather necessary documents')
check_regulatory = Transition(label='Check regulatory updates')
submit_documents = Transition(label='Submit documents')
review_submission = Transition(label='Review submission')
request_clarifications = Transition(label='Request clarifications of discrepancies')
receive_clarifications = Transition(label='Receive clarifications')
evaluate_financial = Transition(label='Evaluate financial risks')
evaluate_operational = Transition(label='Evaluate operational risks')
evaluate_compliance = Transition(label='Evaluate compliance risks')
launch_investigation = Transition(label='Launch detailed investigation')
conduct_data_analysis = Transition(label='Conduct data analysis')
conduct_interviews = Transition(label='Conduct interviews')
perform_site_visits = Transition(label='Perform site visits')
compile_report = Transition(label='Compile audit report')
review_report = Transition(label='Review report by audit director')
send_for_revision = Transition(label='Send report for revision')
update_report = Transition(label='Update and resubmit report')
approve_report = Transition(label='Approve report')
archive_report = Transition(label='Archive report')
distribute_report = Transition(label='Distribute final report')
close_process = Transition(label='Close audit process')

# Define concurrent tasks for risk assessment
risk_assessment = StrictPartialOrder(nodes=[evaluate_financial, evaluate_operational, evaluate_compliance])
risk_assessment.order.add_edge(evaluate_financial, evaluate_operational)
risk_assessment.order.add_edge(evaluate_financial, evaluate_compliance)
risk_assessment.order.add_edge(evaluate_operational, evaluate_compliance)

# Define investigation tasks
investigation = StrictPartialOrder(nodes=[conduct_data_analysis, conduct_interviews, perform_site_visits])
investigation.order.add_edge(conduct_data_analysis, conduct_interviews)
investigation.order.add_edge(conduct_data_analysis, perform_site_visits)
investigation.order.add_edge(conduct_interviews, perform_site_visits)

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    send_notification,
    prepare_statements,
    gather_documents,
    check_regulatory,
    submit_documents,
    review_submission,
    request_clarifications,
    receive_clarifications,
    risk_assessment,
    launch_investigation,
    investigation,
    compile_report,
    review_report,
    send_for_revision,
    update_report,
    approve_report,
    archive_report,
    distribute_report,
    close_process
])

# Define the order of the tasks
root.order.add_edge(send_notification, prepare_statements)
root.order.add_edge(send_notification, gather_documents)
root.order.add_edge(prepare_statements, gather_documents)
root.order.add_edge(gather_documents, submit_documents)
root.order.add_edge(check_regulatory, submit_documents)
root.order.add_edge(submit_documents, review_submission)
root.order.add_edge(review_submission, request_clarifications)
root.order.add_edge(request_clarifications, receive_clarifications)
root.order.add_edge(receive_clarifications, risk_assessment)
root.order.add_edge(risk_assessment, launch_investigation)
root.order.add_edge(launch_investigation, investigation)
root.order.add_edge(investigation, compile_report)
root.order.add_edge(compile_report, review_report)
root.order.add_edge(review_report, send_for_revision)
root.order.add_edge(review_report, approve_report)
root.order.add_edge(send_for_revision, update_report)
root.order.add_edge(update_report, review_report)
root.order.add_edge(approve_report, archive_report)
root.order.add_edge(archive_report, distribute_report)
root.order.add_edge(distribute_report, close_process)

# Return the root POWL model
root