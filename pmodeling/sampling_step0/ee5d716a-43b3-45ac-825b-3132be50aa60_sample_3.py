import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
verify_artwork = Transition(label='Verify Artwork')
analyze_provenance = Transition(label='Analyze Provenance')
set_reserve = Transition(label='Set Reserve')
activate_auction = Transition(label='Activate Auction')
monitor_bids = Transition(label='Monitor Bids')
adjust_pricing = Transition(label='Adjust Pricing')
enable_fractional = Transition(label='Enable Fractional')
validate_bidders = Transition(label='Validate Bidders')
resolve_disputes = Transition(label='Resolve Disputes')
distribute_royalties = Transition(label='Distribute Royalties')
promote_auction = Transition(label='Promote Auction')
process_payments = Transition(label='Process Payments')
confirm_ownership = Transition(label='Confirm Ownership')
arrange_shipping = Transition(label='Arrange Shipping')
track_delivery = Transition(label='Track Delivery')
report_analytics = Transition(label='Report Analytics')

# Define loops and choices
loop_verify_analyze = OperatorPOWL(operator=Operator.LOOP, children=[analyze_provenance, verify_artwork])
loop_set_reserve = OperatorPOWL(operator=Operator.LOOP, children=[set_reserve, activate_auction])
loop_monitor_adjust = OperatorPOWL(operator=Operator.LOOP, children=[monitor_bids, adjust_pricing])
loop_enable_validate = OperatorPOWL(operator=Operator.LOOP, children=[enable_fractional, validate_bidders])
loop_resolve_distribute = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes, distribute_royalties])
loop_promote_process = OperatorPOWL(operator=Operator.LOOP, children=[promote_auction, process_payments])
loop_confirm_arrange = OperatorPOWL(operator=Operator.LOOP, children=[confirm_ownership, arrange_shipping])
loop_track_report = OperatorPOWL(operator=Operator.LOOP, children=[track_delivery, report_analytics])

# Define root POWL
root = StrictPartialOrder(nodes=[
    loop_verify_analyze,
    loop_set_reserve,
    loop_monitor_adjust,
    loop_enable_validate,
    loop_resolve_distribute,
    loop_promote_process,
    loop_confirm_arrange,
    loop_track_report
])
root.order.add_edge(loop_verify_analyze, loop_set_reserve)
root.order.add_edge(loop_set_reserve, loop_monitor_adjust)
root.order.add_edge(loop_monitor_adjust, loop_enable_validate)
root.order.add_edge(loop_enable_validate, loop_resolve_distribute)
root.order.add_edge(loop_resolve_distribute, loop_promote_process)
root.order.add_edge(loop_promote_process, loop_confirm_arrange)
root.order.add_edge(loop_confirm_arrange, loop_track_report)