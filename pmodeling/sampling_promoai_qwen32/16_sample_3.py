import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
send_notification = Transition(label='Send notification')
prepare_financial_statements = Transition(label='Prepare financial statements')
gather_necessary_documents = Transition(label='Gather necessary documents')
check_regulatory_updates = Transition(label='Check regulatory updates')
submit_documents = Transition(label='Submit documents')
review_submission = Transition(label='Review submission')
request_clarifications = Transition(label='Request clarifications of discrepancies')
receive_clarifications = Transition(label='Receive clarifications')
conduct_risk_assessment = Transition(label='Evaluate financial risks')
conduct_risk_assessment2 = Transition(label='Evaluate operational risks')
conduct_risk_assessment3 = Transition(label='Evaluate compliance risks')
launch_investigation = Transition(label='Launch detailed investigation')
conduct_data_analysis = Transition(label='Conduct data analysis')
conduct_interviews = Transition(label='Conduct interviews')
perform_site_visits = Transition(label='Perform site visits')
compile_audit_report = Transition(label='Compile audit report')
review_report = Transition(label='Review report by audit director')
approve_report = Transition(label='Approve report')
send_report_for_revision = Transition(label='Send report for revision')
update_resubmit_report = Transition(label='Update and resubmit report')
distribute_final_report = Transition(label='Distribute final report')
archive_report = Transition(label='Archive report')
close_audit_process = Transition(label='Close audit process')

# Define the loop and choice nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[request_clarifications, receive_clarifications])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[send_report_for_revision, update_resubmit_report])
choice1 = OperatorPOWL(operator=Operator.XOR, children=[approve_report, send_report_for_revision])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[conduct_risk_assessment, conduct_risk_assessment2, conduct_risk_assessment3])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[conduct_data_analysis, conduct_interviews, perform_site_visits])

# Define the partial order
root = StrictPartialOrder(nodes=[
    send_notification, prepare_financial_statements, gather_necessary_documents, check_regulatory_updates, submit_documents,
    review_submission, loop1, loop2, choice1, choice2, choice3, launch_investigation, compile_audit_report,
    review_report, approve_report, send_report_for_revision, update_resubmit_report, distribute_final_report,
    archive_report, close_audit_process
])

# Define the edges
root.order.add_edge(send_notification, prepare_financial_statements)
root.order.add_edge(send_notification, check_regulatory_updates)
root.order.add_edge(prepare_financial_statements, gather_necessary_documents)
root.order.add_edge(gather_necessary_documents, submit_documents)
root.order.add_edge(check_regulatory_updates, submit_documents)
root.order.add_edge(submit_documents, review_submission)
root.order.add_edge(review_submission, loop1)
root.order.add_edge(loop1, choice1)
root.order.add_edge(choice1, compile_audit_report)
root.order.add_edge(compile_audit_report, review_report)
root.order.add_edge(review_report, choice1)
root.order.add_edge(choice1, send_report_for_revision)
root.order.add_edge(send_report_for_revision, update_resubmit_report)
root.order.add_edge(update_resubmit_report, review_report)
root.order.add_edge(choice1, approve_report)
root.order.add_edge(approve_report, distribute_final_report)
root.order.add_edge(distribute_final_report, archive_report)
root.order.add_edge(archive_report, close_audit_process)
root.order.add_edge(choice1, launch_investigation)
root.order.add_edge(launch_investigation, choice3)
root.order.add_edge(choice3, compile_audit_report)
root.order.add_edge(choice2, compile_audit_report)
root.order.add_edge(compile_audit_report, review_report)
root.order.add_edge(review_report, choice1)
root.order.add_edge(choice1, send_report_for_revision)
root.order.add_edge(send_report_for_revision, update_resubmit_report)
root.order.add_edge(update_resubmit_report, review_report)
root.order.add_edge(choice1, approve_report)
root.order.add_edge(approve_report, distribute_final_report)
root.order.add_edge(distribute_final_report, archive_report)
root.order.add_edge(archive_report, close_audit_process)