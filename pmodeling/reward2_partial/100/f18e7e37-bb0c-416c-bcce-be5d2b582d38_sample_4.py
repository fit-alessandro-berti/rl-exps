from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
user_signup = Transition(label='User Signup')
set_preferences = Transition(label='Preference Set')
select_meal = Transition(label='Meal Select')
set_delivery = Transition(label='Schedule Delivery')
match_supplier = Transition(label='Supplier Match')
check_inventory = Transition(label='Inventory Check')
order_ingredients = Transition(label='Ingredient Order')
inspect_quality = Transition(label='Quality Inspect')
pack_meal = Transition(label='Meal Pack')
plan_route = Transition(label='Route Plan')
dispatch_kit = Transition(label='Dispatch Kit')
track_delivery = Transition(label='Delivery Track')
collect_feedback = Transition(label='Feedback Collect')
analyze_data = Transition(label='Data Analyze')
optimize_plan = Transition(label='Plan Optimize')

# Create the partial order
root = StrictPartialOrder(nodes=[
    user_signup, set_preferences, select_meal, set_delivery, match_supplier,
    check_inventory, order_ingredients, inspect_quality, pack_meal, plan_route,
    dispatch_kit, track_delivery, collect_feedback, analyze_data, optimize_plan
])

# Define the dependencies between nodes
root.order.add_edge(user_signup, set_preferences)
root.order.add_edge(set_preferences, select_meal)
root.order.add_edge(select_meal, set_delivery)
root.order.add_edge(set_delivery, match_supplier)
root.order.add_edge(match_supplier, check_inventory)
root.order.add_edge(check_inventory, order_ingredients)
root.order.add_edge(order_ingredients, inspect_quality)
root.order.add_edge(inspect_quality, pack_meal)
root.order.add_edge(pack_meal, plan_route)
root.order.add_edge(plan_route, dispatch_kit)
root.order.add_edge(dispatch_kit, track_delivery)
root.order.add_edge(track_delivery, collect_feedback)
root.order.add_edge(collect_feedback, analyze_data)
root.order.add_edge(analyze_data, optimize_plan)

# Print the final POWL model
print(root)