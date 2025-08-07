import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
initiate = Transition(label='Initiate Audit')
gather = Transition(label='Gather Documents')
verify_suppliers = Transition(label='Verify Suppliers')
screen_transactions = Transition(label='Screen Transactions')
check_sanctions = Transition(label='Check Sanctions')
review_tariffs = Transition(label='Review Tariffs')
classify_products = Transition(label='Classify Products')
cross_verify = Transition(label='Cross-Verify Data')
conduct_interviews = Transition(label='Conduct Interviews')
analyze_reports = Transition(label='Analyze Reports')
identify_gaps = Transition(label='Identify Gaps')
recommend_actions = Transition(label='Recommend Actions')
implement_changes = Transition(label='Implement Changes')
monitor_compliance = Transition(label='Monitor Compliance')
finalize_report = Transition(label='Finalize Report')

# Build the partial order
root = StrictPartialOrder(nodes=[
    initiate,
    gather,
    verify_suppliers,
    screen_transactions,
    check_sanctions,
    review_tariffs,
    classify_products,
    cross_verify,
    conduct_interviews,
    analyze_reports,
    identify_gaps,
    recommend_actions,
    implement_changes,
    monitor_compliance,
    finalize_report
])

# Define the control-flow dependencies
# Initiate -> Gather Documents
root.order.add_edge(initiate, gather)

# Gather -> Verify Suppliers, Screen Transactions, Check Sanctions, Review Tariffs
for t in [verify_suppliers, screen_transactions, check_sanctions, review_tariffs]:
    root.order.add_edge(gather, t)

# After all verifications, Cross-Verify Data
for t in [verify_suppliers, screen_transactions, check_sanctions, review_tariffs]:
    root.order.add_edge(t, cross_verify)

# Cross-Verify -> Classify Products, Conduct Interviews
for t in [classify_products, conduct_interviews]:
    root.order.add_edge(cross_verify, t)

# After classification and interviews, Analyze Reports
for t in [classify_products, conduct_interviews]:
    root.order.add_edge(t, analyze_reports)

# Analyze Reports -> Identify Gaps, Recommend Actions
for t in [identify_gaps, recommend_actions]:
    root.order.add_edge(analyze_reports, t)

# Identify Gaps -> Implement Changes, Monitor Compliance
for t in [implement_changes, monitor_compliance]:
    root.order.add_edge(identify_gaps, t)

# Implement Changes -> Monitor Compliance
root.order.add_edge(implement_changes, monitor_compliance)

# Monitor Compliance -> Finalize Report
root.order.add_edge(monitor_compliance, finalize_report)