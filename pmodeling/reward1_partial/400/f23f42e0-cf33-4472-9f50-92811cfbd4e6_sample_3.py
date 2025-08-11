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

# Define the control-flow operators
xor_quality_tasting = OperatorPOWL(operator=Operator.XOR, children=[quality_tasting, packaging_prep])
xor_distribution_plan = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, retail_delivery])
xor_event_coordination = OperatorPOWL(operator=Operator.XOR, children=[event_coordination, regulatory_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_testing,
    curd_cutting,
    whey_draining,
    mold_inoculation,
    forming_cheese,
    salting_stage,
    aging_setup,
    climate_control,
    xor_quality_tasting,
    xor_distribution_plan,
    xor_event_coordination
])

# Add edges for the partial order
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(milk_sourcing, milk_testing)
root.order.add_edge(culture_selection, curd_cutting)
root.order.add_edge(culture_selection, whey_draining)
root.order.add_edge(milk_testing, mold_inoculation)
root.order.add_edge(curd_cutting, forming_cheese)
root.order.add_edge(whey_draining, salting_stage)
root.order.add_edge(forming_cheese, aging_setup)
root.order.add_edge(salting_stage, climate_control)
root.order.add_edge(climate_control, xor_quality_tasting)
root.order.add_edge(climate_control, xor_distribution_plan)
root.order.add_edge(climate_control, xor_event_coordination)

print(root)