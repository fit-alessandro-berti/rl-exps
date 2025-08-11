import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transition (skip)
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_check, ingredient_order])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, meal_pack])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[route_plan, dispatch_kit])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[delivery_track, feedback_collect])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, plan_optimize])

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop4])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop5])

# Define the root POWL model
root = StrictPartialOrder(nodes=[user_signup, preference_set, meal_select, schedule_delivery, supplier_match, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(user_signup, preference_set)
root.order.add_edge(preference_set, meal_select)
root.order.add_edge(meal_select, schedule_delivery)
root.order.add_edge(schedule_delivery, supplier_match)
root.order.add_edge(supplier_match, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, plan_optimize)