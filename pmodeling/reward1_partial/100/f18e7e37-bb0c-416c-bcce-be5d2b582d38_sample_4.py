from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
user_signup = Transition(label='User Signup')
preference_set = Transition(label='Preference Set')
meal_select = Transition(label='Meal Select')
schedule_delivery = Transition(label='Schedule Delivery')
supplier_match = Transition(label='Supplier Match')
inventory_check = Transition(label='Inventory Check')
ingredient_order = Transition(label='Ingredient Order')
quality_inspect = Transition(label='Quality Inspect')
meal_pack = Transition(label='Meal Pack')
route_plan = Transition(label='Route Plan')
dispatch_kit = Transition(label='Dispatch Kit')
delivery_track = Transition(label='Delivery Track')
feedback_collect = Transition(label='Feedback Collect')
data_analyze = Transition(label='Data Analyze')
plan_optimize = Transition(label='Plan Optimize')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop_supplier_match = OperatorPOWL(operator=Operator.LOOP, children=[supplier_match, inventory_check, ingredient_order])
loop_quality_inspect = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect])
loop_meal_pack = OperatorPOWL(operator=Operator.LOOP, children=[meal_pack])
loop_route_plan = OperatorPOWL(operator=Operator.LOOP, children=[route_plan, dispatch_kit])
loop_delivery_track = OperatorPOWL(operator=Operator.LOOP, children=[delivery_track])
xor_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, data_analyze])
xor_plan_optimize = OperatorPOWL(operator=Operator.XOR, children=[plan_optimize])

# Construct the POWL model
root = StrictPartialOrder(nodes=[user_signup, preference_set, meal_select, schedule_delivery, loop_supplier_match, loop_quality_inspect, loop_meal_pack, loop_route_plan, loop_delivery_track, xor_feedback_collect, xor_plan_optimize])
root.order.add_edge(user_signup, preference_set)
root.order.add_edge(preference_set, meal_select)
root.order.add_edge(meal_select, schedule_delivery)
root.order.add_edge(schedule_delivery, loop_supplier_match)
root.order.add_edge(loop_supplier_match, loop_quality_inspect)
root.order.add_edge(loop_quality_inspect, loop_meal_pack)
root.order.add_edge(loop_meal_pack, loop_route_plan)
root.order.add_edge(loop_route_plan, loop_delivery_track)
root.order.add_edge(loop_delivery_track, xor_feedback_collect)
root.order.add_edge(xor_feedback_collect, xor_plan_optimize)

print(root)