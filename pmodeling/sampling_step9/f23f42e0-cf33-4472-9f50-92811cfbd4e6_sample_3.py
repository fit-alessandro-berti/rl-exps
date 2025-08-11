import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculation = Transition(label='Mold Inoculation')
forming_cheese = Transition(label='Forming Cheese')
salting_stage = Transition(label='Salting Stage')
aging_setup = Transition(label='Aging Setup')
climate_control = Transition(label='Climate Control')
quality_tasting = Transition(label='Quality Tasting')
packaging_prep = Transition(label='Packaging Prep')
label_printing = Transition(label='Label Printing')
distribution_plan = Transition(label='Distribution Plan')
retail_delivery = Transition(label='Retail Delivery')
event_coordination = Transition(label='Event Coordination')
regulatory_audit = Transition(label='Regulatory Audit')

# Define silent transitions
skip = SilentTransition()

# Define operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection])
xor = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculation, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[forming_cheese, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[salting_stage, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[climate_control, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[quality_tasting, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[label_printing, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, skip])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[event_coordination, skip])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_audit, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12, xor13, xor14, xor15])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, xor14)
root.order.add_edge(xor14, xor15)

# Print the root
print(root)