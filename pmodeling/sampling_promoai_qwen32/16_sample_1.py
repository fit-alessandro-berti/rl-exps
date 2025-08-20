import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
complete_risk_assessment = Transition(label='Complete risk assessment/mitigation')
launch_investigation = Transition(label='Launch detailed investigation')
conduct_data_analysis = Transition(label='Conduct data analysis')
conduct_interviews = Transition(label='Conduct interviews')
perform_site_visits = Transition(label='Perform site visits')
compile_audit_report = Transition(label='Compile audit report')
review_report = Transition(label='Review report by audit director')
approve_report = Transition(label='Approve report')
send_for_revision = Transition(label='Send report for revision')
update_and_resubmit_report = Transition(label='Update and resubmit report')
distribute_report = Transition(label='Distribute final report')
archive_report = Transition(label='Archive report')
close_audit_process = Transition(label='Close audit process')

# Define silent transition
skip = SilentTransition()

# Define loop for request clarifications and provide clarifications
clarification_loop = OperatorPOWL(operator=Operator.LOOP, children=[request_clarifications, provide_clarifications])

# Define choice for high risk
risk_choice = OperatorPOWL(operator=Operator.XOR, children=[skip, launch_investigation])

# Define parallel tasks for evaluating risks
evaluate_risks = StrictPartialOrder(nodes=[evaluate_financial_risks, evaluate_operational_risks, evaluate_compliance_risks])
evaluate_risks.order.add_edge(evaluate_financial_risks, complete_risk_assessment)
evaluate_risks.order.add_edge(evaluate_operational_risks, complete_risk_assessment)
evaluate_risks.order.add_edge(evaluate_compliance_risks, complete_risk_assessment)

# Define choice for report approval
report_choice = OperatorPOWL(operator=Operator.XOR, children=[approve_report, send_for_revision])

# Define loop for report revisions
report_revision_loop = OperatorPOWL(operator=Operator.LOOP, children=[update_and_resubmit_report, review_report, report_choice])

# Define root POWL model
root = StrictPartialOrder(nodes=[send_notification, prepare_financial_statements, gather_documents, check_regulatory_updates, submit_documents, review_submission, clarification_loop, evaluate_risks, risk_choice, conduct_data_analysis, conduct_interviews, perform_site_visits, compile_audit_report, report_revision_loop, distribute_report, archive_report, close_audit_process])
root.order.add_edge(send_notification, prepare_financial_statements)
root.order.add_edge(prepare_financial_statements, gather_documents)
root.order.add_edge(gather_documents, check_regulatory_updates)
root.order.add_edge(check_regulatory_updates, submit_documents)
root.order.add_edge(submit_documents, review_submission)
root.order.add_edge(review_submission, clarification_loop)
root.order.add_edge(clarification_loop, evaluate_risks)
root.order.add_edge(evaluate_risks, risk_choice)
root.order.add_edge(risk_choice, conduct_data_analysis)
root.order.add_edge(risk_choice, conduct_interviews)
root.order.add_edge(risk_choice, perform_site_visits)
root.order.add_edge(conduct_data_analysis, compile_audit_report)
root.order.add_edge(conduct_interviews, compile_audit_report)
root.order.add_edge(perform_site_visits, compile_audit_report)
root.order.add_edge(compile_audit_report, report_revision_loop)
root.order.add_edge(report_revision_loop, distribute_report)
root.order.add_edge(distribute_report, archive_report)
root.order.add_edge(archive_report, close_audit_process)