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

# Define silent transitions for empty labels
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()
skip7 = SilentTransition()
skip8 = SilentTransition()
skip9 = SilentTransition()
skip10 = SilentTransition()
skip11 = SilentTransition()
skip12 = SilentTransition()
skip13 = SilentTransition()
skip14 = SilentTransition()
skip15 = SilentTransition()

# Define the partial order
root = StrictPartialOrder(nodes=[
    user_signup, preference_set, meal_select, schedule_delivery, supplier_match, inventory_check,
    ingredient_order, quality_inspect, meal_pack, route_plan, dispatch_kit, delivery_track,
    feedback_collect, data_analyze, plan_optimize
])

# Define the dependencies between transitions
root.order.add_edge(user_signup, preference_set)
root.order.add_edge(preference_set, meal_select)
root.order.add_edge(meal_select, schedule_delivery)
root.order.add_edge(schedule_delivery, supplier_match)
root.order.add_edge(supplier_match, inventory_check)
root.order.add_edge(inventory_check, ingredient_order)
root.order.add_edge(ingredient_order, quality_inspect)
root.order.add_edge(quality_inspect, meal_pack)
root.order.add_edge(meal_pack, route_plan)
root.order.add_edge(route_plan, dispatch_kit)
root.order.add_edge(dispatch_kit, delivery_track)
root.order.add_edge(delivery_track, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)
root.order.add_edge(data_analyze, plan_optimize)

# Add silent transitions to ensure all paths are connected
root.order.add_edge(preference_set, skip1)
root.order.add_edge(meal_select, skip2)
root.order.add_edge(schedule_delivery, skip3)
root.order.add_edge(supplier_match, skip4)
root.order.add_edge(inventory_check, skip5)
root.order.add_edge(ingredient_order, skip6)
root.order.add_edge(quality_inspect, skip7)
root.order.add_edge(meal_pack, skip8)
root.order.add_edge(route_plan, skip9)
root.order.add_edge(dispatch_kit, skip10)
root.order.add_edge(delivery_track, skip11)
root.order.add_edge(feedback_collect, skip12)
root.order.add_edge(data_analyze, skip13)
root.order.add_edge(plan_optimize, skip14)
root.order.add_edge(skip1, preference_set)
root.order.add_edge(skip2, meal_select)
root.order.add_edge(skip3, schedule_delivery)
root.order.add_edge(skip4, supplier_match)
root.order.add_edge(skip5, inventory_check)
root.order.add_edge(skip6, ingredient_order)
root.order.add_edge(skip7, quality_inspect)
root.order.add_edge(skip8, meal_pack)
root.order.add_edge(skip9, route_plan)
root.order.add_edge(skip10, dispatch_kit)
root.order.add_edge(skip11, delivery_track)
root.order.add_edge(skip12, feedback_collect)
root.order.add_edge(skip13, data_analyze)
root.order.add_edge(skip14, plan_optimize)

# Print the root of the POWL model
print(root)