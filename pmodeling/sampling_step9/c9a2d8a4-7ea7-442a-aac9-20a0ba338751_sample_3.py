import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[screen_transactions, cross_verify_data])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[classify_products, cross_verify_data])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[assess_risks, check_sanctions])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[review_tariffs, check_sanctions])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[conduct_interviews, analyze_reports])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[identify_gaps, analyze_reports])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[recommend_actions, analyze_reports])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[implement_changes, analyze_reports])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[monitor_compliance, analyze_reports])

# Define the partial order
root = StrictPartialOrder(nodes=[initiate_audit, gather_documents, verify_suppliers, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, finalize_report])
root.order.add_edge(initiate_audit, gather_documents)
root.order.add_edge(gather_documents, verify_suppliers)
root.order.add_edge(verify_suppliers, xor1)
root.order.add_edge(verify_suppliers, xor2)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor5, xor7)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, finalize_report)

# Print the root of the POWL model
print(root)