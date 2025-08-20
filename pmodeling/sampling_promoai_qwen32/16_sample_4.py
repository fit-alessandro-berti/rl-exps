import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
send_notification = Transition(label='Send notification')
prepare_financial_statements = Transition(label='Prepare financial statements')
gather_documents = Transition(label='Gather necessary documents')
check_regulatory_updates = Transition(label='Check regulatory updates')
submit_documents = Transition(label='Submit documents')
review_submission = Transition(label='Review submission')
request_clarifications = Transition(label='Request clarifications of discrepancies')
provide_clarifications = Transition(label='Receive clarifications')
evaluate_financial_risks = Transition(label='Evaluate financial risks')
evaluate_operational_risks = Transition(label='Evaluate operational risks')
evaluate_compliance_risks = Transition(label='Evaluate compliance risks')
launch_investigation = Transition(label='Launch detailed investigation')
conduct_data_analysis = Transition(label='Conduct data analysis')
conduct_interviews = Transition(label='Conduct interviews')
perform_site_visits = Transition(label='Perform site visits')
complete_risk_assessment = Transition(label='Complete risk assessment/mitigation')
compile_report = Transition(label='Compile audit report')
review_report = Transition(label='Review report by audit director')
approve_report = Transition(label='Approve report')
send_report_for_revision = Transition(label='Send report for revision')
update_and_resubmit_report = Transition(label='Update and resubmit report')
distribute_report = Transition(label='Distribute final report')
archive_report = Transition(label='Archive report')
close_audit_process = Transition(label='Close audit process')

# Define parallel activities
regional_office_tasks = StrictPartialOrder(nodes=[prepare_financial_statements, gather_documents])
central_audit_team_tasks = StrictPartialOrder(nodes=[review_submission, request_clarifications])
risk_assessment_tasks = StrictPartialOrder(nodes=[evaluate_financial_risks, evaluate_operational_risks, evaluate_compliance_risks])

# Define loop for risk assessment
risk_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment_tasks, complete_risk_assessment])

# Define choice for audit director's review
audit_director_review_choice = OperatorPOWL(operator=Operator.XOR, children=[approve_report, send_report_for_revision])

# Define main process
root = StrictPartialOrder(nodes=[send_notification, regional_office_tasks, check_regulatory_updates, submit_documents, central_audit_team_tasks, provide_clarifications, risk_assessment_loop, launch_investigation, conduct_data_analysis, conduct_interviews, perform_site_visits, compile_report, audit_director_review_choice, update_and_resubmit_report, distribute_report, archive_report, close_audit_process])

# Define order
root.order.add_edge(send_notification, regional_office_tasks)
root.order.add_edge(send_notification, check_regulatory_updates)
root.order.add_edge(regional_office_tasks, submit_documents)
root.order.add_edge(check_regulatory_updates, submit_documents)
root.order.add_edge(submit_documents, central_audit_team_tasks)
root.order.add_edge(central_audit_team_tasks, provide_clarifications)
root.order.add_edge(provide_clarifications, risk_assessment_loop)
root.order.add_edge(risk_assessment_loop, launch_investigation)
root.order.add_edge(launch_investigation, conduct_data_analysis)
root.order.add_edge(launch_investigation, conduct_interviews)
root.order.add_edge(launch_investigation, perform_site_visits)
root.order.add_edge(perform_site_visits, complete_risk_assessment)
root.order.add_edge(conduct_interviews, complete_risk_assessment)
root.order.add_edge(conduct_data_analysis, complete_risk_assessment)
root.order.add_edge(complete_risk_assessment, compile_report)
root.order.add_edge(compile_report, audit_director_review_choice)
root.order.add_edge(audit_director_review_choice, update_and_resubmit_report)
root.order.add_edge(update_and_resubmit_report, audit_director_review_choice)
root.order.add_edge(audit_director_review_choice, distribute_report)
root.order.add_edge(distribute_report, archive_report)
root.order.add_edge(archive_report, close_audit_process)