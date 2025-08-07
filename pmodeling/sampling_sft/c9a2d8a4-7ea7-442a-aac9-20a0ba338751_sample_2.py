import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
initiate = Transition(label='Initiate Audit')
gather_docs = Transition(label='Gather Documents')
verify_suppliers = Transition(label='Verify Suppliers')
screen_transactions = Transition(label='Screen Transactions')
classify_products = Transition(label='Classify Products')
check_sanctions = Transition(label='Check Sanctions')
review_tariffs = Transition(label='Review Tariffs')
cross_verify = Transition(label='Cross-Verify Data')
conduct_interviews = Transition(label='Conduct Interviews')
analyze_reports = Transition(label='Analyze Reports')
identify_gaps = Transition(label='Identify Gaps')
recommend_actions = Transition(label='Recommend Actions')
implement_changes = Transition(label='Implement Changes')
monitor_compliance = Transition(label='Monitor Compliance')
finalize_report = Transition(label='Finalize Report')

# Define the loop body: cross-verify, analyze, identify gaps, recommend actions, implement changes
loop_body = StrictPartialOrder(nodes=[cross_verify, analyze_reports, identify_gaps, recommend_actions, implement_changes])

# Loop: do cross-verify, then either exit or do the body and repeat
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[cross_verify, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    initiate,
    gather_docs,
    verify_suppliers,
    screen_transactions,
    classify_products,
    check_sanctions,
    review_tariffs,
    audit_loop,
    conduct_interviews,
    finalize_report
])

# Define the control-flow dependencies
root.order.add_edge(initiate, gather_docs)
root.order.add_edge(gather_docs, verify_suppliers)
root.order.add_edge(gather_docs, screen_transactions)
root.order.add_edge(verify_suppliers, classify_products)
root.order.add_edge(screen_transactions, classify_products)
root.order.add_edge(classify_products, check_sanctions)
root.order.add_edge(classify_products, review_tariffs)
root.order.add_edge(check_sanctions, audit_loop)
root.order.add_edge(review_tariffs, audit_loop)
root.order.add_edge(audit_loop, conduct_interviews)
root.order.add_edge(conduct_interviews, finalize_report)