import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection, milk_testing, curd_cutting, whey_draining, mold_inoculation, forming_cheese, salting_stage, aging_setup, climate_control])
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_tasting, packaging_prep, label_printing, distribution_plan, retail_delivery, event_coordination])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the final POWL model
print(root)