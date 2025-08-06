import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
signup = Transition(label='User Signup')
set_prefs = Transition(label='Preference Set')
select_meal = Transition(label='Meal Select')
schedule_delivery = Transition(label='Schedule Delivery')
match_suppliers = Transition(label='Supplier Match')
check_inventory = Transition(label='Inventory Check')
order_ingredients = Transition(label='Ingredient Order')
inspect_quality = Transition(label='Quality Inspect')
pack_meal = Transition(label='Meal Pack')
route_plan = Transition(label='Route Plan')
dispatch_kit = Transition(label='Dispatch Kit')
track_delivery = Transition(label='Delivery Track')
collect_feedback = Transition(label='Feedback Collect')
analyze_data = Transition(label='Data Analyze')
optimize_plan = Transition(label='Plan Optimize')

# Define the partial order structure
root = StrictPartialOrder(nodes=[signup, set_prefs, select_meal, schedule_delivery, match_suppliers, check_inventory, order_ingredients, inspect_quality, pack_meal, route_plan, dispatch_kit, track_delivery, collect_feedback, analyze_data, optimize_plan])

# Define the dependencies between transitions
root.order.add_edge(signup, set_prefs)
root.order.add_edge(set_prefs, select_meal)
root.order.add_edge(select_meal, schedule_delivery)
root.order.add_edge(schedule_delivery, match_suppliers)
root.order.add_edge(match_suppliers, check_inventory)
root.order.add_edge(check_inventory, order_ingredients)
root.order.add_edge(order_ingredients, inspect_quality)
root.order.add_edge(inspect_quality, pack_meal)
root.order.add_edge(pack_meal, route_plan)
root.order.add_edge(route_plan, dispatch_kit)
root.order.add_edge(dispatch_kit, track_delivery)
root.order.add_edge(track_delivery, collect_feedback)
root.order.add_edge(collect_feedback, analyze_data)
root.order.add_edge(analyze_data, optimize_plan)

print(root)