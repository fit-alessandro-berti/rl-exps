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

# Define the process steps
loop = OperatorPOWL(operator=Operator.LOOP, children=[InventoryCheck, IngredientOrder, QualityInspect, MealPack])
xor = OperatorPOWL(operator=Operator.XOR, children=[DispatchKit, DeliveryTrack])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the POWL model
print(root)