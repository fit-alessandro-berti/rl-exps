import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the artisan cheese production process
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

# Define silent activities
skip = SilentTransition()

# Define the process structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing, curd_cutting])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[whey_draining, mold_inoculation])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[forming_cheese, salting_stage])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, climate_control])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[quality_tasting, packaging_prep])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[label_printing, distribution_plan])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[retail_delivery, event_coordination])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_audit, skip])

# Define the exclusive choice for the process
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, loop9])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)
root.order.add_edge(loop4, xor)
root.order.add_edge(loop5, xor)
root.order.add_edge(loop6, xor)
root.order.add_edge(loop7, xor)
root.order.add_edge(loop8, xor)
root.order.add_edge(loop9, xor)