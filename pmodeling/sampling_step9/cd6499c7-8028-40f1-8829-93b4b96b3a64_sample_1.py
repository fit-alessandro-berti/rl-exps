import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
xor = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)