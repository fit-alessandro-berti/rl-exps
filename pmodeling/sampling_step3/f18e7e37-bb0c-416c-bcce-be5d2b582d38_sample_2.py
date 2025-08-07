import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
signup = Transition(label='User Signup')
set_preferences = Transition(label='Preference Set')
meal_selection = Transition(label='Meal Select')
schedule_delivery = Transition(label='Schedule Delivery')
supplier_match = Transition(label='Supplier Match')
inventory_check = Transition(label='Inventory Check')
ingredient_order = Transition(label='Ingredient Order')
quality_inspect = Transition(label='Quality Inspect')
meal_packaging = Transition(label='Meal Pack')
route_planning = Transition(label='Route Plan')
dispatch_kit = Transition(label='Dispatch Kit')
delivery_tracking = Transition(label='Delivery Track')
feedback_collection = Transition(label='Feedback Collect')
data_analysis = Transition(label='Data Analyze')
plan_optimization = Transition(label='Plan Optimize')

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[signup, set_preferences, meal_selection, schedule_delivery, supplier_match, inventory_check, ingredient_order, quality_inspect, meal_packaging, route_planning, dispatch_kit, delivery_tracking, feedback_collection, data_analysis, plan_optimization])

# Define the dependencies between activities
root.order.add_edge(signup, set_preferences)
root.order.add_edge(set_preferences, meal_selection)
root.order.add_edge(meal_selection, schedule_delivery)
root.order.add_edge(schedule_delivery, supplier_match)
root.order.add_edge(supplier_match, inventory_check)
root.order.add_edge(inventory_check, ingredient_order)
root.order.add_edge(ingredient_order, quality_inspect)
root.order.add_edge(quality_inspect, meal_packaging)
root.order.add_edge(meal_packaging, route_planning)
root.order.add_edge(route_planning, dispatch_kit)
root.order.add_edge(dispatch_kit, delivery_tracking)
root.order.add_edge(delivery_tracking, feedback_collection)
root.order.add_edge(feedback_collection, data_analysis)
root.order.add_edge(data_analysis, plan_optimization)

# Save the root node
print(root)