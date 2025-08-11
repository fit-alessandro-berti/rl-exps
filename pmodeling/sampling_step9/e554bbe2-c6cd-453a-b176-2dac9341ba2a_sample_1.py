import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Farm_Selection = Transition(label='Farm Selection')
Milk_Testing = Transition(label='Milk Testing')
Starter_Culture = Transition(label='Starter Culture')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Microbial_Profiling = Transition(label='Microbial Profiling')
Aging_Control = Transition(label='Aging Control')
Hand_Wrapping = Transition(label='Hand Wrapping')
Quality_Audit = Transition(label='Quality Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Climate_Shipping = Transition(label='Climate Shipping')
Retail_Coordination = Transition(label='Retail Coordination')
Seasonal_Review = Transition(label='Seasonal Review')
Consumer_Survey = Transition(label='Consumer Survey')
Feedback_Analysis = Transition(label='Feedback Analysis')
Market_Adjustment = Transition(label='Market Adjustment')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[Farm_Selection, Milk_Testing, Starter_Culture, Curd_Formation, Pressing_Cheese, Aging_Control, Hand_Wrapping, Quality_Audit, Packaging_Prep, Climate_Shipping])
xor = OperatorPOWL(operator=Operator.XOR, children=[Retail_Coordination, skip])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Seasonal_Review, Consumer_Survey, Feedback_Analysis, Market_Adjustment])

root = StrictPartialOrder(nodes=[loop, xor, loop1])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, loop1)
root.order.add_edge(xor, loop1)