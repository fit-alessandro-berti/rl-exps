import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define loops and choices
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    initiate_audit, gather_documents, verify_suppliers, screen_transactions, classify_products,
    assess_risks, check_sanctions, review_tariffs, cross_verify_data, conduct_interviews,
    analyze_reports, identify_gaps, recommend_actions, implement_changes, monitor_compliance
])
sanctions_loop = OperatorPOWL(operator=Operator.LOOP, children=[check_sanctions])
tariffs_loop = OperatorPOWL(operator=Operator.LOOP, children=[review_tariffs])
finalize_loop = OperatorPOWL(operator=Operator.LOOP, children=[finalize_report])

# Define exclusive choices
data_choice = OperatorPOWL(operator=Operator.XOR, children=[cross_verify_data, analyze_reports])
risk_choice = OperatorPOWL(operator=Operator.XOR, children=[assess_risks, identify_gaps])
remediation_choice = OperatorPOWL(operator=Operator.XOR, children=[recommend_actions, implement_changes])
monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_compliance, finalize_loop])

# Define the root node
root = StrictPartialOrder(nodes=[
    audit_loop, data_choice, risk_choice, remediation_choice, monitor_choice, finalize_loop
])
root.order.add_edge(audit_loop, data_choice)
root.order.add_edge(data_choice, risk_choice)
root.order.add_edge(risk_choice, remediation_choice)
root.order.add_edge(remediation_choice, monitor_choice)
root.order.add_edge(monitor_choice, finalize_loop)

# Print the root node
print(root)