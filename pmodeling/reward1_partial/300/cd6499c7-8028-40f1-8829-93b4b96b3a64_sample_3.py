import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
milk_pasturize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_drain = Transition(label='Whey Drain')
cheese_press = Transition(label='Cheese Press')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
temperature_control = Transition(label='Temperature Control')
batch_labeling = Transition(label='Batch Labeling')
eco_packaging = Transition(label='Eco Packaging')
inventory_audit = Transition(label='Inventory Audit')
order_coordination = Transition(label='Order Coordination')
regulatory_check = Transition(label='Regulatory Check')
shipment_planning = Transition(label='Shipment Planning')
vendor_liaison = Transition(label='Vendor Liaison')
waste_reduction = Transition(label='Waste Reduction')

# Define loops and choices
quality_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_prep])
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasturize, curd_formation, whey_drain, cheese_press, salting_process])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, temperature_control])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_labeling, eco_packaging])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit])
coordination_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_coordination])
regulatory_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check])
shipment_loop = OperatorPOWL(operator=Operator.LOOP, children=[shipment_planning])
vendor_loop = OperatorPOWL(operator=Operator.LOOP, children=[vendor_liaison])
waste_reduction_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_reduction])

# Define exclusive choices
fermentation_choice = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, packaging_loop])
aging_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, regulatory_loop])
shipment_choice = OperatorPOWL(operator=Operator.XOR, children=[shipment_loop, vendor_loop])
waste_reduction_choice = OperatorPOWL(operator=Operator.XOR, children=[audit_loop, coordination_loop])
regulatory_choice = OperatorPOWL(operator=Operator.XOR, children=[regulatory_loop, vendor_loop])
audit_choice = OperatorPOWL(operator=Operator.XOR, children=[audit_loop, coordination_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_control_loop,
    fermentation_choice,
    aging_choice,
    shipment_choice,
    waste_reduction_choice,
    regulatory_choice,
    audit_choice
])

# Add dependencies
root.order.add_edge(milk_sourcing, quality_control_loop)
root.order.add_edge(quality_control_loop, fermentation_choice)
root.order.add_edge(fermentation_choice, aging_choice)
root.order.add_edge(aging_choice, shipment_choice)
root.order.add_edge(shipment_choice, waste_reduction_choice)
root.order.add_edge(waste_reduction_choice, regulatory_choice)
root.order.add_edge(regulatory_choice, audit_choice)

# Print the root POWL model
print(root)