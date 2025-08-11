import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the process tree operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, climate_control])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[salting_stage, packaging_prep])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[quality_tasting, label_printing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, retail_delivery])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[event_coordination, regulatory_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[
    xor1, xor2, xor3, xor4, xor5, xor6, xor7,
    milk_sourcing, culture_selection, milk_testing, curd_cutting, whey_draining, mold_inoculation, forming_cheese, salting_stage, aging_setup, climate_control, quality_tasting, packaging_prep, label_printing, distribution_plan, retail_delivery, event_coordination, regulatory_audit
])

# Define the partial order dependencies
root.order.add_edge(milk_sourcing, xor2)
root.order.add_edge(culture_selection, xor2)
root.order.add_edge(milk_testing, xor1)
root.order.add_edge(skip, xor1)
root.order.add_edge(aging_setup, xor3)
root.order.add_edge(climate_control, xor3)
root.order.add_edge(salting_stage, xor4)
root.order.add_edge(packaging_prep, xor4)
root.order.add_edge(quality_tasting, xor5)
root.order.add_edge(label_printing, xor5)
root.order.add_edge(distribution_plan, xor6)
root.order.add_edge(retail_delivery, xor6)
root.order.add_edge(event_coordination, xor7)
root.order.add_edge(regulatory_audit, xor7)

# Print the root model
print(root)