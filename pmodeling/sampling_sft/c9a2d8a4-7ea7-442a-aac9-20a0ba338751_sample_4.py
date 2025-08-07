import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initiate = Transition(label='Initiate Audit')
gather_docs = Transition(label='Gather Documents')
verify_suppliers = Transition(label='Verify Suppliers')
screen_trans = Transition(label='Screen Transactions')
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

# Loop for continuous monitoring and compliance review
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_compliance, finalize_report]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    initiate,
    gather_docs,
    verify_suppliers,
    screen_trans,
    classify_products,
    check_sanctions,
    review_tariffs,
    cross_verify,
    conduct_interviews,
    analyze_reports,
    identify_gaps,
    recommend_actions,
    implement_changes,
    monitor_loop
])

# Define the control-flow dependencies
root.order.add_edge(initiate, gather_docs)
root.order.add_edge(gather_docs, verify_suppliers)
root.order.add_edge(gather_docs, screen_trans)
root.order.add_edge(verify_suppliers, classify_products)
root.order.add_edge(screen_trans, classify_products)
root.order.add_edge(classify_products, check_sanctions)
root.order.add_edge(classify_products, review_tariffs)
root.order.add_edge(check_sanctions, cross_verify)
root.order.add_edge(review_tariffs, cross_verify)
root.order.add_edge(cross_verify, conduct_interviews)
root.order.add_edge(conduct_interviews, analyze_reports)
root.order.add_edge(analyze_reports, identify_gaps)
root.order.add_edge(identify_gaps, recommend_actions)
root.order.add_edge(recommend_actions, implement_changes)
root.order.add_edge(implement_changes, monitor_loop)

# Finalize the report after all other steps
root.order.add_edge(monitor_loop, finalize_report)