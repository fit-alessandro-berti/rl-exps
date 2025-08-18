import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.process_tree.obj import ProcessTree

# Define activities
user_signup = Transition(label='User Signup')
set_preference = Transition(label='Preference Set')
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

# Define sub-processes
inventory_and_quality = StrictPartialOrder(nodes=[inventory_check, quality_inspect])
ingredient_and_packing = StrictPartialOrder(nodes=[ingredient_order, meal_pack])
delivery_and_tracking = StrictPartialOrder(nodes=[dispatch_kit, delivery_track])
feedback_and_analysis = StrictPartialOrder(nodes=[feedback_collect, data_analyze])

# Define main process
user_signup_subprocess = StrictPartialOrder(nodes=[user_signup, set_preference, meal_select, schedule_delivery, supplier_match])
inventory_and_quality_subprocess = StrictPartialOrder(nodes=[inventory_check, quality_inspect])
ingredient_and_packing_subprocess = StrictPartialOrder(nodes=[ingredient_order, meal_pack])
delivery_and_tracking_subprocess = StrictPartialOrder(nodes=[dispatch_kit, delivery_track])
feedback_and_analysis_subprocess = StrictPartialOrder(nodes=[feedback_collect, data_analyze])
plan_optimize_subprocess = StrictPartialOrder(nodes=[plan_optimize])

# Define main process structure
root = StrictPartialOrder(nodes=[
    user_signup_subprocess,
    inventory_and_quality_subprocess,
    ingredient_and_packing_subprocess,
    delivery_and_tracking_subprocess,
    feedback_and_analysis_subprocess,
    plan_optimize_subprocess
])

# Define dependencies
root.order.add_edge(user_signup_subprocess, inventory_and_quality_subprocess)
root.order.add_edge(user_signup_subprocess, ingredient_and_packing_subprocess)
root.order.add_edge(user_signup_subprocess, delivery_and_tracking_subprocess)
root.order.add_edge(user_signup_subprocess, feedback_and_analysis_subprocess)
root.order.add_edge(user_signup_subprocess, plan_optimize_subprocess)

root.order.add_edge(inventory_and_quality_subprocess, ingredient_and_packing_subprocess)
root.order.add_edge(ingredient_and_packing_subprocess, delivery_and_tracking_subprocess)
root.order.add_edge(delivery_and_tracking_subprocess, feedback_and_analysis_subprocess)
root.order.add_edge(feedback_and_analysis_subprocess, plan_optimize_subprocess)

print(root)