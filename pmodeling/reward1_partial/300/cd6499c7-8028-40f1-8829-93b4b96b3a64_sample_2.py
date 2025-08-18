import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
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

# Define exclusive choice (XOR) for batch labeling and eco packaging
xor = OperatorPOWL(operator=Operator.XOR, children=[batch_labeling, eco_packaging])

# Define loop for inventory audit, regulatory check, and shipment planning
loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit, regulatory_check, shipment_planning])

# Define partial order with defined nodes and order
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_prep, milk_pasteurize, curd_formation, whey_drain, cheese_press, salting_process, aging_setup, temperature_control, xor, loop, vendor_liaison, waste_reduction])

# Add dependencies between nodes
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
root.order.add_edge(curd_formation, whey_drain)
root.order.add_edge(whey_drain, cheese_press)
root.order.add_edge(cheese_press, salting_process)
root.order.add_edge(salting_process, aging_setup)
root.order.add_edge(aging_setup, temperature_control)
root.order.add_edge(temperature_control, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, vendor_liaison)
root.order.add_edge(vendor_liaison, waste_reduction)

# Print the final POWL model
print(root)