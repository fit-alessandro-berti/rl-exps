import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
signup = Transition(label='User Signup')
preferences = Transition(label='Preference Set')
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

# Define the partial order
root = StrictPartialOrder(nodes=[signup, preferences, meal_select, schedule_delivery, supplier_match, inventory_check, ingredient_order, quality_inspect, meal_pack, route_plan, dispatch_kit, delivery_track, feedback_collect, data_analyze, plan_optimize])
root.order.add_edge(signup, preferences)
root.order.add_edge(preferences, meal_select)
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