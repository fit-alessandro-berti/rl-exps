import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Send_notification = Transition(label='Send notification')
Prepare_financial_statements = Transition(label='Prepare financial statements')
Gather_necessary_documents = Transition(label='Gather necessary documents')
Check_regulatory_updates = Transition(label='Check regulatory updates')
Submit_documents = Transition(label='Submit documents')
Review_submission = Transition(label='Review submission')
Request_clarifications = Transition(label='Request clarifications of discrepancies')
Receive_clarifications = Transition(label='Receive clarifications')
Complete_risk_assessment = Transition(label='Complete risk assessment/mitigation')
Evaluate_financial_risks = Transition(label='Evaluate financial risks')
Evaluate_operational_risks = Transition(label='Evaluate operational risks')
Evaluate_compliance_risks = Transition(label='Evaluate compliance risks')
Launch_detailed_investigation = Transition(label='Launch detailed investigation')
Conduct_data_analysis = Transition(label='Conduct data analysis')
Conduct_interviews = Transition(label='Conduct interviews')
Perform_site_visits = Transition(label='Perform site visits')
Compile_audit_report = Transition(label='Compile audit report')
Review_report_by_audit_director = Transition(label='Review report by audit director')
Send_report_for_revision = Transition(label='Send report for revision')
Update_and_resubmit_report = Transition(label='Update and resubmit report')
Approve_report = Transition(label='Approve report')
Distribute_final_report = Transition(label='Distribute final report')
Archive_report = Transition(label='Archive report')
Close_audit_process = Transition(label='Close audit process')

# Define the choice nodes
Check_regulatory_updates_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Check_regulatory_updates, SilentTransition()])
Complete_risk_assessment_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Complete_risk_assessment, SilentTransition()])
Evaluate_financial_risks_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Evaluate_financial_risks, SilentTransition()])
Evaluate_operational_risks_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Evaluate_operational_risks, SilentTransition()])
Evaluate_compliance_risks_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Evaluate_compliance_risks, SilentTransition()])
Conduct_data_analysis_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Conduct_data_analysis, SilentTransition()])
Conduct_interviews_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Conduct_interviews, SilentTransition()])
Perform_site_visits_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Perform_site_visits, SilentTransition()])
Send_report_for_revision_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Send_report_for_revision, SilentTransition()])
Update_and_resubmit_report_or_skip = OperatorPOWL(operator=Operator.XOR, children=[Update_and_resubmit_report, SilentTransition()])

# Define the loop nodes
Request_clarifications_loop = OperatorPOWL(operator=Operator.LOOP, children=[Request_clarifications, Receive_clarifications])
Complete_risk_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[Complete_risk_assessment_or_skip, Evaluate_financial_risks_or_skip, Evaluate_operational_risks_or_skip, Evaluate_compliance_risks_or_skip])
Conduct_investigation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Launch_detailed_investigation, Conduct_data_analysis_or_skip, Conduct_interviews_or_skip, Perform_site_visits_or_skip])
Review_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[Review_report_by_audit_director, Send_report_for_revision_or_skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    Send_notification,
    Prepare_financial_statements,
    Gather_necessary_documents,
    Check_regulatory_updates_or_skip,
    Submit_documents,
    Review_submission,
    Request_clarifications_loop,
    Complete_risk_assessment_loop,
    Conduct_investigation_loop,
    Compile_audit_report,
    Review_report_loop,
    Approve_report,
    Distribute_final_report,
    Archive_report,
    Close_audit_process
])

# Define the order
root.order.add_edge(Send_notification, Prepare_financial_statements)
root.order.add_edge(Prepare_financial_statements, Gather_necessary_documents)
root.order.add_edge(Gather_necessary_documents, Check_regulatory_updates_or_skip)
root.order.add_edge(Check_regulatory_updates_or_skip, Submit_documents)
root.order.add_edge(Submit_documents, Review_submission)
root.order.add_edge(Review_submission, Request_clarifications_loop)
root.order.add_edge(Request_clarifications_loop, Complete_risk_assessment_loop)
root.order.add_edge(Complete_risk_assessment_loop, Conduct_investigation_loop)
root.order.add_edge(Conduct_investigation_loop, Compile_audit_report)
root.order.add_edge(Compile_audit_report, Review_report_loop)
root.order.add_edge(Review_report_loop, Approve_report)
root.order.add_edge(Approve_report, Distribute_final_report)
root.order.add_edge(Distribute_final_report, Archive_report)
root.order.add_edge(Archive_report, Close_audit_process)