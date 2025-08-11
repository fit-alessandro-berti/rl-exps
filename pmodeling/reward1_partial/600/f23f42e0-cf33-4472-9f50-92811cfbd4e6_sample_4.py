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

# Define the loop nodes
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, quality_tasting])
tasting_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, climate_control])
packing_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, label_printing])

# Define the XOR nodes
milk_test_and_cut = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, curd_cutting])
milk_test_and_drain = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, whey_draining])
milk_test_and_inoculate = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, mold_inoculation])
milk_test_and_form = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, forming_cheese])
milk_test_and_salting = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, salting_stage])
milk_test_and_aging = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, aging_setup])
milk_test_and_control = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, climate_control])
milk_test_and_taste = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, quality_tasting])
milk_test_and_pack = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, packaging_prep])
milk_test_and_label = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, label_printing])
milk_test_and_plan = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, distribution_plan])
milk_test_and_deliver = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, retail_delivery])
milk_test_and_event = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, event_coordination])
milk_test_and_audit = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, regulatory_audit])

# Define the root node
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_test_and_cut,
    milk_test_and_drain,
    milk_test_and_inoculate,
    milk_test_and_form,
    milk_test_and_salting,
    milk_test_and_aging,
    milk_test_and_control,
    milk_test_and_taste,
    milk_test_and_pack,
    milk_test_and_label,
    milk_test_and_plan,
    milk_test_and_deliver,
    milk_test_and_event,
    milk_test_and_audit,
    aging_loop,
    tasting_loop,
    packing_loop
])

# Add edges to the root node
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_test_and_cut)
root.order.add_edge(milk_test_and_cut, milk_test_and_drain)
root.order.add_edge(milk_test_and_drain, milk_test_and_inoculate)
root.order.add_edge(milk_test_and_inoculate, milk_test_and_form)
root.order.add_edge(milk_test_and_form, milk_test_and_salting)
root.order.add_edge(milk_test_and_salting, milk_test_and_aging)
root.order.add_edge(milk_test_and_aging, milk_test_and_control)
root.order.add_edge(milk_test_and_control, milk_test_and_taste)
root.order.add_edge(milk_test_and_taste, milk_test_and_pack)
root.order.add_edge(milk_test_and_pack, milk_test_and_label)
root.order.add_edge(milk_test_and_label, milk_test_and_plan)
root.order.add_edge(milk_test_and_plan, milk_test_and_deliver)
root.order.add_edge(milk_test_and_deliver, milk_test_and_event)
root.order.add_edge(milk_test_and_event, milk_test_and_audit)
root.order.add_edge(milk_test_and_audit, aging_loop)
root.order.add_edge(aging_loop, tasting_loop)
root.order.add_edge(tasting_loop, packing_loop)

print(root)