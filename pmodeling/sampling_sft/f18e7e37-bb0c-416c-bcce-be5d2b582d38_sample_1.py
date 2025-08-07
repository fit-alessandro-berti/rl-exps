import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
user_signup   = Transition(label='User Signup')
preference_set = Transition(label='Preference Set')
meal_select   = Transition(label='Meal Select')
schedule_delivery = Transition(label='Schedule Delivery')
supplier_match = Transition(label='Supplier Match')
inventory_check = Transition(label='Inventory Check')
ingredient_order = Transition(label='Ingredient Order')
quality_inspect = Transition(label='Quality Inspect')
meal_pack      = Transition(label='Meal Pack')
route_plan     = Transition(label='Route Plan')
dispatch_kit   = Transition(label='Dispatch Kit')
delivery_track = Transition(label='Delivery Track')
feedback_collect = Transition(label='Feedback Collect')
data_analyze   = Transition(label='Data Analyze')
plan_optimize  = Transition(label='Plan Optimize')

# Build the loop body: Quality Inspect -> Meal Pack -> Route Plan -> Dispatch Kit -> Delivery Track
body = StrictPartialOrder(nodes=[quality_inspect, meal_pack, route_plan, dispatch_kit, delivery_track])
body.order.add_edge(quality_inspect, meal_pack)
body.order.add_edge(meal_pack, route_plan)
body.order.add_edge(route_plan, dispatch_kit)
body.order.add_edge(dispatch_kit, delivery_track)

# Loop: Schedule Delivery -> body (then optionally repeat)
loop = OperatorPOWL(operator=Operator.LOOP, children=[schedule_delivery, body])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    user_signup, preference_set, meal_select, loop,
    feedback_collect, data_analyze, plan_optimize
])

# Define the control-flow dependencies
root.order.add_edge(user_signup, preference_set)
root.order.add_edge(preference_set, meal_select)
root.order.add_edge(meal_select, loop)
root.order.add_edge(loop, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)
root.order.add_edge(data_analyze, plan_optimize)

# Print the root model for verification
print(root)