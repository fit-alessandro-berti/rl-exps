import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loops
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing, starter_prep, milk_pasteurize, curd_formation, whey_drain, cheese_press, salting_process, aging_setup, temperature_control, batch_labeling, eco_packaging, inventory_audit, order_coordination, regulatory_check, shipment_planning, vendor_liaison, waste_reduction])

# Define exclusive choice
sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[sourcing_loop])

# Define root
root = StrictPartialOrder(nodes=[sourcing_choice])