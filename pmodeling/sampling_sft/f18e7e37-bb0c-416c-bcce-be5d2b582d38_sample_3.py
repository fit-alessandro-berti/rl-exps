import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ts_signup   = Transition(label='User Signup')
ts_pref     = Transition(label='Preference Set')
ts_select   = Transition(label='Meal Select')
ts_sched    = Transition(label='Schedule Delivery')
ts_match    = Transition(label='Supplier Match')
ts_check    = Transition(label='Inventory Check')
ts_order    = Transition(label='Ingredient Order')
ts_inspect  = Transition(label='Quality Inspect')
ts_pack     = Transition(label='Meal Pack')
ts_route    = Transition(label='Route Plan')
ts_dispatch = Transition(label='Dispatch Kit')
ts_track    = Transition(label='Delivery Track')
ts_feedback = Transition(label='Feedback Collect')
ts_analyze  = Transition(label='Data Analyze')
ts_optimize = Transition(label='Plan Optimize')

# Build the main workflow as a strict partial order
main_workflow = StrictPartialOrder(nodes=[
    ts_signup, ts_pref, ts_select, ts_sched,
    ts_match, ts_check, ts_order, ts_inspect,
    ts_pack, ts_route, ts_dispatch, ts_track,
    ts_feedback, ts_analyze, ts_optimize
])

# Define the control-flow dependencies
main_workflow.order.add_edge(ts_signup, ts_pref)
main_workflow.order.add_edge(ts_pref, ts_select)
main_workflow.order.add_edge(ts_select, ts_sched)

# After selection, the supplier matching can proceed in parallel
main_workflow.order.add_edge(ts_sched, ts_match)
main_workflow.order.add_edge(ts_sched, ts_check)

# Both inventory and supplier match can proceed in parallel before ordering
main_workflow.order.add_edge(ts_match, ts_order)
main_workflow.order.add_edge(ts_check, ts_order)

# After ordering, both inspection and packaging can proceed in parallel
main_workflow.order.add_edge(ts_order, ts_inspect)
main_workflow.order.add_edge(ts_order, ts_pack)

# Packaging and inspection can proceed in parallel before routing
main_workflow.order.add_edge(ts_inspect, ts_route)
main_workflow.order.add_edge(ts_pack, ts_route)

# Routing and dispatching can proceed in parallel before tracking
main_workflow.order.add_edge(ts_route, ts_dispatch)
main_workflow.order.add_edge(ts_dispatch, ts_track)

# After tracking, feedback and analysis can proceed in parallel
main_workflow.order.add_edge(ts_track, ts_feedback)
main_workflow.order.add_edge(ts_track, ts_analyze)

# Feedback and analysis can proceed in parallel before optimization
main_workflow.order.add_edge(ts_feedback, ts_optimize)
main_workflow.order.add_edge(ts_analyze, ts_optimize)

# Finally, optimization can start from the feedback/analysis point
main_workflow.order.add_edge(ts_optimize, ts_signup)

# The root of the POWL model is the main workflow
root = main_workflow