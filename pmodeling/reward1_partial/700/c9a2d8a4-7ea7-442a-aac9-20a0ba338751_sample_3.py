import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[check_sanctions, review_tariffs])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[cross_verify_data, conduct_interviews])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[identify_gaps, recommend_actions])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[implement_changes, monitor_compliance])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[finalize_report])

# Define the partial order
root = StrictPartialOrder(nodes=[initiate_audit, gather_documents, verify_suppliers, screen_transactions, classify_products, assess_risks, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(initiate_audit, gather_documents)
root.order.add_edge(gather_documents, verify_suppliers)
root.order.add_edge(verify_suppliers, screen_transactions)
root.order.add_edge(screen_transactions, classify_products)
root.order.add_edge(classify_products, assess_risks)
root.order.add_edge(assess_risks, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, finalize_report)