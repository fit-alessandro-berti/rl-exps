import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
user_signup       = Transition(label='User Signup')
preference_set    = Transition(label='Preference Set')
meal_select       = Transition(label='Meal Select')
schedule_delivery = Transition(label='Schedule Delivery')
supplier_match    = Transition(label='Supplier Match')
inventory_check   = Transition(label='Inventory Check')
ingredient_order  = Transition(label='Ingredient Order')
quality_inspect   = Transition(label='Quality Inspect')
meal_pack         = Transition(label='Meal Pack')
route_plan        = Transition(label='Route Plan')
dispatch_kit      = Transition(label='Dispatch Kit')
delivery_track    = Transition(label='Delivery Track')
feedback_collect  = Transition(label='Feedback Collect')
data_analyze      = Transition(label='Data Analyze')
plan_optimize     = Transition(label='Plan Optimize')

# Define the inner loop body (one iteration of the process)
inner_loop_body = StrictPartialOrder(nodes=[
    preference_set,
    meal_select,
    schedule_delivery,
    supplier_match,
    inventory_check,
    ingredient_order,
    quality_inspect,
    meal_pack,
    route_plan,
    dispatch_kit,
    delivery_track
])
# Sequence: Preference -> Meal -> Schedule -> Supplier -> Inventory -> Order -> Inspect -> Pack -> Route -> Dispatch -> Track
for a in [preference_set, meal_select, schedule_delivery, supplier_match, inventory_check, ingredient_order, quality_inspect, meal_pack, route_plan, dispatch_kit, delivery_track]:
    inner_loop_body.order.add_edge(inner_loop_body.nodes.index(a), inner_loop_body.nodes.index(a) + 1)

# Define the feedback‐data loop: collect feedback, then optionally analyze and plan optimize, repeat
feedback_collect = Transition(label='Feedback Collect')
data_analyze     = Transition(label='Data Analyze')
plan_optimize    = Transition(label='Plan Optimize')
feedback_loop    = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect, StrictPartialOrder(nodes=[data_analyze, plan_optimize])])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    user_signup,
    inner_loop_body,
    feedback_loop
])
# Sequence: Signup -> Inner Loop -> Feedback Loop
for a in [user_signup, inner_loop_body, feedback_loop]:
    root.order.add_edge(root.nodes.index(a), root.nodes.index(a) + 1)