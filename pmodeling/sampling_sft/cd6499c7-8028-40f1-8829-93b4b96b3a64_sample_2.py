import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing      = Transition(label='Milk Sourcing')
quality_testing    = Transition(label='Quality Testing')
starter_prep       = Transition(label='Starter Prep')
milk_pasteurize    = Transition(label='Milk Pasteurize')
curd_formation     = Transition(label='Curd Formation')
whey_drain         = Transition(label='Whey Drain')
cheese_press       = Transition(label='Cheese Press')
salting_process    = Transition(label='Salting Process')
aging_setup        = Transition(label='Aging Setup')
temp_control       = Transition(label='Temperature Control')
batch_labeling     = Transition(label='Batch Labeling')
eco_packaging      = Transition(label='Eco Packaging')
inventory_audit    = Transition(label='Inventory Audit')
order_coordination = Transition(label='Order Coordination')
regulatory_check   = Transition(label='Regulatory Check')
shipment_planning  = Transition(label='Shipment Planning')
vendor_liaison     = Transition(label='Vendor Liaison')
waste_reduction    = Transition(label='Waste Reduction')

# Build the aging loop: do aging_setup, then optionally repeat with temp_control
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_setup, temp_control]
)

# Build the main production pipeline as a partial order
production_pipeline = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        starter_prep,
        milk_pasteurize,
        curd_formation,
        whey_drain,
        cheese_press,
        salting_process,
        aging_loop,
        batch_labeling,
        eco_packaging
    ]
)
# Define the ordering constraints
production_pipeline.order.add_edge(milk_sourcing, quality_testing)
production_pipeline.order.add_edge(quality_testing, starter_prep)
production_pipeline.order.add_edge(starter_prep, milk_pasteurize)
production_pipeline.order.add_edge(milk_pasteurize, curd_formation)
production_pipeline.order.add_edge(curd_formation, whey_drain)
production_pipeline.order.add_edge(whey_drain, cheese_press)
production_pipeline.order.add_edge(cheese_press, salting_process)
production_pipeline.order.add_edge(salting_process, aging_loop)
production_pipeline.order.add_edge(aging_loop, batch_labeling)
production_pipeline.order.add_edge(batch_labeling, eco_packaging)

# Build the distribution chain as a partial order
distribution_chain = StrictPartialOrder(
    nodes=[
        inventory_audit,
        regulatory_check,
        shipment_planning,
        order_coordination,
        vendor_liaison,
        waste_reduction
    ]
)
# Define the ordering constraints
distribution_chain.order.add_edge(inventory_audit, regulatory_check)
distribution_chain.order.add_edge(regulatory_check, shipment_planning)
distribution_chain.order.add_edge(shipment_planning, order_coordination)
distribution_chain.order.add_edge(order_coordination, vendor_liaison)
distribution_chain.order.add_edge(vendor_liaison, waste_reduction)

# Assemble the root partial order combining production and distribution
root = StrictPartialOrder(
    nodes=[
        production_pipeline,
        distribution_chain
    ]
)
root.order.add_edge(production_pipeline, distribution_chain)

# Print the root partial order for verification
print(root)