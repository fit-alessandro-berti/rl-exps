import pm4py
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
loop_inventory = OperatorPOWL(operator=Operator.LOOP, children=[inventory_check, skip])
loop_order = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_order, skip])
loop_inspect = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, skip])
loop_dispatch = OperatorPOWL(operator=Operator.LOOP, children=[dispatch_kit, skip])
loop_track = OperatorPOWL(operator=Operator.LOOP, children=[delivery_track, skip])

# Define partial order
root = StrictPartialOrder(nodes=[
    user_signup,
    preference_set,
    meal_select,
    schedule_delivery,
    supplier_match,
    loop_inventory,
    loop_order,
    loop_inspect,
    loop_dispatch,
    loop_track,
    feedback_collect,
    data_analyze,
    plan_optimize
])

# Define dependencies
root.order.add_edge(user_signup, preference_set)
root.order.add_edge(preference_set, meal_select)
root.order.add_edge(meal_select, schedule_delivery)
root.order.add_edge(schedule_delivery, supplier_match)
root.order.add_edge(supplier_match, loop_inventory)
root.order.add_edge(loop_inventory, loop_order)
root.order.add_edge(loop_order, loop_inspect)
root.order.add_edge(loop_inspect, loop_dispatch)
root.order.add_edge(loop_dispatch, loop_track)
root.order.add_edge(loop_track, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)
root.order.add_edge(data_analyze, plan_optimize)

# Print the root POWL model
print(root)