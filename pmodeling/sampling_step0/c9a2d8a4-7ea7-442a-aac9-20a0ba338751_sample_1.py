import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transition (no label)
skip = SilentTransition()

# Define the exclusive choice (XOR) of cross-verify data and conduct interviews
xor = OperatorPOWL(operator=Operator.XOR, children=[cross_verify_data, conduct_interviews])

# Define the loop of assess risks, check sanctions, review tariffs, and cross-verify data
loop = OperatorPOWL(operator=Operator.LOOP, children=[assess_risks, check_sanctions, review_tariffs, cross_verify_data])

# Define the root POWL model
root = StrictPartialOrder(nodes=[initiate_audit, gather_documents, verify_suppliers, screen_transactions, classify_products, loop, xor, analyze_reports, identify_gaps, recommend_actions, implement_changes, monitor_compliance, finalize_report])

# Add edges to the root POWL model
root.order.add_edge(initiate_audit, gather_documents)
root.order.add_edge(gather_documents, verify_suppliers)
root.order.add_edge(verify_suppliers, screen_transactions)
root.order.add_edge(screen_transactions, classify_products)
root.order.add_edge(classify_products, loop)
root.order.add_edge(loop, analyze_reports)
root.order.add_edge(analyze_reports, identify_gaps)
root.order.add_edge(identify_gaps, recommend_actions)
root.order.add_edge(recommend_actions, implement_changes)
root.order.add_edge(implement_changes, monitor_compliance)
root.order.add_edge(monitor_compliance, finalize_report)
root.order.add_edge(finalize_report, xor)

# Return the root POWL model
return root