from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
signup = Transition(label='User Signup')
preferenceset = Transition(label='Preference Set')
mealselect = Transition(label='Meal Select')
scheduledelivery = Transition(label='Schedule Delivery')
suppliermatch = Transition(label='Supplier Match')
inventorycheck = Transition(label='Inventory Check')
ingredientorder = Transition(label='Ingredient Order')
qualityinspect = Transition(label='Quality Inspect')
mealpack = Transition(label='Meal Pack')
routeplan = Transition(label='Route Plan')
dispatchkit = Transition(label='Dispatch Kit')
deliverytrack = Transition(label='Delivery Track')
feedbackcollect = Transition(label='Feedback Collect')
dataanalyze = Transition(label='Data Analyze')
planoptimize = Transition(label='Plan Optimize')

# Define silent transitions
skip = SilentTransition()

# Define the process tree
loop = OperatorPOWL(operator=Operator.LOOP, children=[inventorycheck, ingredientorder, qualityinspect, mealpack, routeplan, dispatchkit, deliverytrack, feedbackcollect, dataanalyze])
xor = OperatorPOWL(operator=Operator.XOR, children=[suppliermatch, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[signup, preferenceset, mealselect, scheduledelivery, xor, loop])
root.order.add_edge(signup, preferenceset)
root.order.add_edge(preferenceset, mealselect)
root.order.add_edge(mealselect, scheduledelivery)
root.order.add_edge(scheduledelivery, xor)
root.order.add_edge(xor, loop)