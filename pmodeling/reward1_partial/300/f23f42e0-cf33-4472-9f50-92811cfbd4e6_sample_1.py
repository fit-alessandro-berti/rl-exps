import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, curd_cutting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, mold_inoculation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forming_cheese, salting_stage])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, climate_control])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[quality_tasting, packaging_prep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[label_printing, distribution_plan])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, event_coordination])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)