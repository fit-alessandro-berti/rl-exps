import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Block = Transition(label='Pressing Block')
Brining_Bath = Transition(label='Brining Bath')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Demand_Forecast = Transition(label='Demand Forecast')
Retail_Outreach = Transition(label='Retail Outreach')
Customer_Feedback = Transition(label='Customer Feedback')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Quality_Testing])
xor = OperatorPOWL(operator=Operator.XOR, children=[Starter_Culture, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)