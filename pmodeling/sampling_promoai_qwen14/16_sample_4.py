import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
send_notification = Transition(label='Send notification')
prepare_financial_statements = Transition(label='Prepare financial statements')
gather_documents = Transition(label='Gather necessary documents')
check_regulatory_updates = Transition(label='Check regulatory updates')
submit_documents = Transition(label='Submit documents')
review_submission = Transition(label='Review submission')
request_clarifications = Transition(label='Request clarifications of discrepancies')
provide_clarifications = Transition(label='Receive clarifications')
complete_risk_assessment = Transition(label='Complete risk assessment/mitigation')
evaluate_financial_risks = Transition(label='Evaluate financial risks')
evaluate_operational_risks = Transition(label='Evaluate operational risks')
evaluate_compliance_risks = Transition(label='Evaluate compliance risks')
launch_investigation = Transition(label='Launch detailed investigation')
conduct_data_analysis = Transition(label='Conduct data analysis')
conduct_interviews = Transition(label='Conduct interviews')
perform_site_visits = Transition(label='Perform site visits')
compile_audit_report = Transition(label='Compile audit report')
review_report = Transition(label='Review report by audit director')
approve_report = Transition(label='Approve report')
send_report_for_revision = Transition(label='Send report for revision')
update_and_resubmit_report = Transition(label='Update and resubmit report')
distribute_final_report = Transition(label='Distribute final report')
archive_report = Transition(label='Archive report')
close_audit_process = Transition(label='Close audit process')

# Define loops and choices
loop_clarifications = OperatorPOWL(operator=Operator.LOOP, children=[request_clarifications, provide_clarifications])
loop_revision = OperatorPOWL(operator=Operator.LOOP, children=[send_report_for_revision, update_and_resubmit_report])
loop_investigation = OperatorPOWL(operator=Operator.LOOP, children=[conduct_data_analysis, conduct_interviews, perform_site_visits])
loop_risk_evaluation = OperatorPOWL(operator=Operator.LOOP, children=[evaluate_financial_risks, evaluate_operational_risks, evaluate_compliance_risks])

choice_risk_evaluation = OperatorPOWL(operator=Operator.XOR, children=[loop_risk_evaluation, complete_risk_assessment])

# Define partial orders
preparation_order = StrictPartialOrder(nodes=[send_notification, prepare_financial_statements, gather_documents, check_regulatory_updates])
submission_order = StrictPartialOrder(nodes=[submit_documents, review_submission])
clarifications_order = StrictPartialOrder(nodes=[loop_clarifications, complete_risk_assessment])
risk_evaluation_order = StrictPartialOrder(nodes=[choice_risk_evaluation, launch_investigation])
report_order = StrictPartialOrder(nodes=[compile_audit_report, review_report])
approval_order = StrictPartialOrder(nodes=[approve_report, send_report_for_revision])
revision_order = StrictPartialOrder(nodes=[loop_revision, distribute_final_report])
closing_order = StrictPartialOrder(nodes=[archive_report, close_audit_process])

# Connect partial orders
root = StrictPartialOrder(nodes=[preparation_order, submission_order, clarifications_order, risk_evaluation_order, report_order, approval_order, revision_order, closing_order])
root.order.add_edge(preparation_order, submission_order)
root.order.add_edge(submission_order, clarifications_order)
root.order.add_edge(clarifications_order, risk_evaluation_order)
root.order.add_edge(risk_evaluation_order, report_order)
root.order.add_edge(report_order, approval_order)
root.order.add_edge(approval_order, revision_order)
root.order.add_edge(revision_order, closing_order)