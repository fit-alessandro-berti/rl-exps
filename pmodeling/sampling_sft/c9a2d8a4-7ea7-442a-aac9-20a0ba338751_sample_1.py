import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
initiate = Transition(label='Initiate Audit')
gather = Transition(label='Gather Documents')
verify = Transition(label='Verify Suppliers')
screen = Transition(label='Screen Transactions')
classify = Transition(label='Classify Products')
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

# Build the loop body: Conduct Interviews -> Analyze Reports -> Identify Gaps -> Recommend Actions -> Implement Changes
body = StrictPartialOrder(nodes=[conduct_interviews, analyze_reports, identify_gaps, recommend_actions, implement_changes])
body.order.add_edge(conduct_interviews, analyze_reports)
body.order.add_edge(analyze_reports, identify_gaps)
body.order.add_edge(identify_gaps, recommend_actions)
body.order.add_edge(recommend_actions, implement_changes)

# Loop: repeat the above body until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, finalize_report])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    initiate, gather, verify, screen, classify, check_sanctions, review_tariffs, cross_verify,
    loop, finalize_report
])

# Sequence: Initiate Audit -> Gather Documents -> Verify Suppliers -> Screen Transactions -> Classify Products
root.order.add_edge(initiate, gather)
root.order.add_edge(gather, verify)
root.order.add_edge(verify, screen)
root.order.add_edge(screen, classify)

# Parallel: Check Sanctions, Review Tariffs, Cross-Verify Data
root.order.add_edge(classify, check_sanctions)
root.order.add_edge(classify, review_tariffs)
root.order.add_edge(classify, cross_verify)

# After the loop, finalize the report
root.order.add_edge(loop, finalize_report)

# Finalize: Finalize Report (no further dependencies)