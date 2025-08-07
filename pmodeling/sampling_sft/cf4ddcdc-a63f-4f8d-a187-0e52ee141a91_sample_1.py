import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
return_req      = Transition(label='Return Request')
auth_check      = Transition(label='Authorization Check')
pickup_sched    = Transition(label='Pickup Schedule')
transport_disp  = Transition(label='Transport Dispatch')
receiving_goods = Transition(label='Receiving Goods')
quality_inspect = Transition(label='Quality Inspect')
sort_items      = Transition(label='Sort Items')
refurb_prep     = Transition(label='Refurbish Prep')
recycle_proc    = Transition(label='Recycle Process')
inv_update      = Transition(label='Inventory Update')
cust_notify     = Transition(label='Customer Notify')
disposal_arr    = Transition(label='Disposal Arrange')
compliance_aud  = Transition(label='Compliance Audit')
cost_analysis   = Transition(label='Cost Analysis')
report_gen      = Transition(label='Report Generate')

# Define the refurbishment branch: Sort Items -> Refurbish Prep -> Recycle Process
refurb_branch = StrictPartialOrder(nodes=[sort_items, refurb_prep, recycle_proc])
refurb_branch.order.add_edge(sort_items, refurb_prep)
refurb_branch.order.add_edge(refurb_prep, recycle_proc)

# Define the disposal branch: Sort Items -> Disposal Arrange
disposal_branch = StrictPartialOrder(nodes=[sort_items, disposal_arr])
disposal_branch.order.add_edge(sort_items, disposal_arr)

# Define the choice between refurbishment and disposal
xor_branch = OperatorPOWL(operator=Operator.XOR, children=[refurb_branch, disposal_branch])

# Define the compliance audit and cost analysis branch: Compliance Audit -> Cost Analysis
compliance_branch = StrictPartialOrder(nodes=[compliance_aud, cost_analysis])
compliance_branch.order.add_edge(compliance_aud, cost_analysis)

# Define the final report branch: Cost Analysis -> Report Generate
report_branch = StrictPartialOrder(nodes=[cost_analysis, report_gen])
report_branch.order.add_edge(cost_analysis, report_gen)

# Define the overall process as a partial order
root = StrictPartialOrder(nodes=[
    return_req, auth_check, pickup_sched, transport_disp, receiving_goods,
    quality_inspect, xor_branch, cust_notify,
    compliance_branch, report_branch
])

# Sequential dependencies
root.order.add_edge(return_req, auth_check)
root.order.add_edge(auth_check, pickup_sched)
root.order.add_edge(pickup_sched, transport_disp)
root.order.add_edge(transport_disp, receiving_goods)
root.order.add_edge(receiving_goods, quality_inspect)
root.order.add_edge(quality_inspect, xor_branch)
root.order.add_edge(xor_branch, cust_notify)

# Parallel compliance and cost analysis branches
root.order.add_edge(xor_branch, compliance_branch)
root.order.add_edge(xor_branch, report_branch)

# Final dependencies
root.order.add_edge(compliance_branch, report_branch)
root.order.add_edge(report_branch, report_gen)