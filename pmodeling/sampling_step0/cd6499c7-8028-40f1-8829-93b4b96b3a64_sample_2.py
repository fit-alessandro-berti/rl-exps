import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions
skip = SilentTransition()

# Define loops and XORs
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, temperature_control, batch_labeling])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging, inventory_audit, order_coordination])
regulatory_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check, shipment_planning, vendor_liaison])
waste_reduction_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_reduction])

# Define partial order
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_prep, milk_pasturize, curd_formation, whey_drain, cheese_press, salting_process, aging_loop, packaging_loop, regulatory_loop, waste_reduction_loop])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_formation)
root.order.add_edge(curd_formation, whey_drain)
root.order.add_edge(whey_drain, cheese_press)
root.order.add_edge(cheese_press, salting_process)
root.order.add_edge(salting_process, aging_loop)
root.order.add_edge(aging_loop, packaging_loop)
root.order.add_edge(packaging_loop, regulatory_loop)
root.order.add_edge(regulatory_loop, waste_reduction_loop)