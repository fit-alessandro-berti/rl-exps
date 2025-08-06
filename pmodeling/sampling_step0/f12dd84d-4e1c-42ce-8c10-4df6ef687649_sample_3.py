import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Curd_Processing = Transition(label='Curd Processing')
Salt_Application = Transition(label='Salt Application')
Mold_Inoculation = Transition(label='Mold Inoculation')
Press_Molding = Transition(label='Press Molding')
Brine_Soaking = Transition(label='Brine Soaking')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Microbial_Check = Transition(label='Microbial Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Trace_Logging = Transition(label='Trace Logging')
Distribution_Plan = Transition(label='Distribution Plan')
Customer_Review = Transition(label='Customer Review')
Inventory_Audit = Transition(label='Inventory Audit')
Sustainability_Audit = Transition(label='Sustainability Audit')

skip = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Quality_Testing, Curd_Processing, Salt_Application, Mold_Inoculation, Press_Molding, Brine_Soaking, Aging_Setup, Humidity_Control, Microbial_Check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Design, Label_Printing, Trace_Logging, Distribution_Plan, Customer_Review, Inventory_Audit, Sustainability_Audit])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)