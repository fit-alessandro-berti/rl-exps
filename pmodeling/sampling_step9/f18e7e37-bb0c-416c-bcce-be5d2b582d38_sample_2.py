import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

UserSignup = Transition(label='User Signup')
PreferenceSet = Transition(label='Preference Set')
MealSelect = Transition(label='Meal Select')
ScheduleDelivery = Transition(label='Schedule Delivery')
SupplierMatch = Transition(label='Supplier Match')
InventoryCheck = Transition(label='Inventory Check')
IngredientOrder = Transition(label='Ingredient Order')
QualityInspect = Transition(label='Quality Inspect')
MealPack = Transition(label='Meal Pack')
RoutePlan = Transition(label='Route Plan')
DispatchKit = Transition(label='Dispatch Kit')
DeliveryTrack = Transition(label='Delivery Track')
FeedbackCollect = Transition(label='Feedback Collect')
DataAnalyze = Transition(label='Data Analyze')
PlanOptimize = Transition(label='Plan Optimize')

skip = SilentTransition()

# Loop for inventory check and quality inspection
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[InventoryCheck, QualityInspect])

# Choice for meal selection based on dietary preferences
choice1 = OperatorPOWL(operator=Operator.XOR, children=[MealSelect, skip])

# Loop for supplier matching and ingredient ordering
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[SupplierMatch, IngredientOrder])

# Loop for route planning and kit dispatch
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[RoutePlan, DispatchKit])

# Loop for delivery tracking and feedback collection
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[DeliveryTrack, FeedbackCollect])

# Loop for data analysis and plan optimization
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalyze, PlanOptimize])

root = StrictPartialOrder(nodes=[UserSignup, PreferenceSet, loop1, choice1, loop2, loop3, loop4, loop5])
root.order.add_edge(UserSignup, PreferenceSet)
root.order.add_edge(PreferenceSet, loop1)
root.order.add_edge(loop1, choice1)
root.order.add_edge(choice1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, UserSignup)