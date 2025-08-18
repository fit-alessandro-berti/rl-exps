import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
user_signup = Transition(label='User Signup')
set_preferences = Transition(label='Preference Set')
select_meal = Transition(label='Meal Select')
schedule_delivery = Transition(label='Schedule Delivery')
supplier_match = Transition(label='Supplier Match')
inventory_check = Transition(label='Inventory Check')
order_ingredient = Transition(label='Ingredient Order')
quality_inspect = Transition(label='Quality Inspect')
pack_meal = Transition(label='Meal Pack')
route_plan = Transition(label='Route Plan')
dispatch_kit = Transition(label='Dispatch Kit')
track_delivery = Transition(label='Delivery Track')
collect_feedback = Transition(label='Feedback Collect')
analyze_data = Transition(label='Data Analyze')
optimize_plan = Transition(label='Plan Optimize')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define the process structure
root = StrictPartialOrder(nodes=[
    user_signup,
    set_preferences,
    select_meal,
    schedule_delivery,
    supplier_match,
    inventory_check,
    order_ingredient,
    quality_inspect,
    pack_meal,
    route_plan,
    dispatch_kit,
    track_delivery,
    collect_feedback,
    analyze_data,
    optimize_plan
])

# Define the dependencies
root.order.add_edge(user_signup, set_preferences)
root.order.add_edge(set_preferences, select_meal)
root.order.add_edge(select_meal, schedule_delivery)
root.order.add_edge(schedule_delivery, supplier_match)
root.order.add_edge(supplier_match, inventory_check)
root.order.add_edge(inventory_check, order_ingredient)
root.order.add_edge(order_ingredient, quality_inspect)
root.order.add_edge(quality_inspect, pack_meal)
root.order.add_edge(pack_meal, route_plan)
root.order.add_edge(route_plan, dispatch_kit)
root.order.add_edge(dispatch_kit, track_delivery)
root.order.add_edge(track_delivery, collect_feedback)
root.order.add_edge(collect_feedback, analyze_data)
root.order.add_edge(analyze_data, optimize_plan)

# Print the root of the POWL model
print(root)