import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
user_signup      = Transition(label='User Signup')
preference_set   = Transition(label='Preference Set')
meal_select      = Transition(label='Meal Select')
schedule_delivery= Transition(label='Schedule Delivery')
supplier_match   = Transition(label='Supplier Match')
inventory_check  = Transition(label='Inventory Check')
ingredient_order = Transition(label='Ingredient Order')
quality_inspect  = Transition(label='Quality Inspect')
meal_pack        = Transition(label='Meal Pack')
route_plan       = Transition(label='Route Plan')
dispatch_kit     = Transition(label='Dispatch Kit')
delivery_track   = Transition(label='Delivery Track')
feedback_collect = Transition(label='Feedback Collect')
data_analyze     = Transition(label='Data Analyze')
plan_optimize    = Transition(label='Plan Optimize')

# Loop: daily meal processing with feedback & data analysis
daily_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    meal_select,
    schedule_delivery,
    supplier_match,
    inventory_check,
    ingredient_order,
    quality_inspect,
    meal_pack,
    route_plan,
    dispatch_kit,
    delivery_track,
    feedback_collect,
    data_analyze
])

# Root partial order
root = StrictPartialOrder(nodes=[
    user_signup,
    preference_set,
    daily_loop,
    plan_optimize
])

# Control-flow dependencies
root.order.add_edge(user_signup, preference_set)
root.order.add_edge(preference_set, daily_loop)
root.order.add_edge(daily_loop, plan_optimize)