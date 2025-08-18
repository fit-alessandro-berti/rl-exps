from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
initiate_audit = Transition(label='Initiate Audit')
gather_documents = Transition(label='Gather Documents')
verify_suppliers = Transition(label='Verify Suppliers')
screen_transactions = Transition(label='Screen Transactions')
classify_products = Transition(label='Classify Products')
assess_risks = Transition(label='Assess Risks')
check_sanctions = Transition(label='Check Sanctions')
review_tariffs = Transition(label='Review Tariffs')
cross_verify_data = Transition(label='Cross-Verify Data')
conduct_interviews = Transition(label='Conduct Interviews')
analyze_reports = Transition(label='Analyze Reports')
identify_gaps = Transition(label='Identify Gaps')
recommend_actions = Transition(label='Recommend Actions')
implement_changes = Transition(label='Implement Changes')
monitor_compliance = Transition(label='Monitor Compliance')
finalize_report = Transition(label='Finalize Report')

# Define the control flow operators
audit_process = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[gather_documents, initiate_audit])
verification_process = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[verify_suppliers, screen_transactions, classify_products, assess_risks, check_sanctions, review_tariffs, cross_verify_data])
interview_process = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[conduct_interviews, analyze_reports])
remediation_process = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[identify_gaps, recommend_actions, implement_changes])
monitoring_process = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[monitor_compliance, finalize_report])

# Define the partial order
root = StrictPartialOrder(nodes=[audit_process, verification_process, interview_process, remediation_process, monitoring_process])
root.order.add_edge(audit_process, verification_process)
root.order.add_edge(verification_process, interview_process)
root.order.add_edge(interview_process, remediation_process)
root.order.add_edge(remediation_process, monitoring_process)

# Print the result
print(root)