from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    user_signup, preference_set, meal_select, schedule_delivery,
    supplier_match, inventory_check, ingredient_order, quality_inspect,
    meal_pack, route_plan, dispatch_kit, delivery_track, feedback_collect,
    data_analyze, plan_optimize
])

# Define dependencies between activities if necessary (not explicitly shown in the problem statement)
# For example, if User Signup must occur before Preference Set, add the following line:
# root.order.add_edge(user_signup, preference_set)

# The 'root' variable now contains the POWL model for the process