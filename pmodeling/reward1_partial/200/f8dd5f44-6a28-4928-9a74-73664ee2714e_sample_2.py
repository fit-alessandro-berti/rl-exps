import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
sensor_deployment = Transition(label='Sensor Deployment')
growth_monitoring = Transition(label='Growth Monitoring')
pest_detection = Transition(label='Pest Detection')
automated_harvest = Transition(label='Automated Harvest')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
biodegradable_pack = Transition(label='Biodegradable Pack')
inventory_sync = Transition(label='Inventory Sync')
demand_forecast = Transition(label='Demand Forecast')
micro_fulfillment = Transition(label='Micro Fulfillment')
local_dispatch = Transition(label='Local Dispatch')
consumer_feedback = Transition(label='Consumer Feedback')
crop_adjustment = Transition(label='Crop Adjustment')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    seed_selection,
    nutrient_mix,
    environment_setup,
    sensor_deployment,
    growth_monitoring,
    pest_detection,
    automated_harvest,
    quality_check,
    packaging_prep,
    biodegradable_pack,
    inventory_sync,
    demand_forecast
])
xor = OperatorPOWL(operator=Operator.XOR, children=[
    micro_fulfillment,
    local_dispatch,
    consumer_feedback,
    crop_adjustment
])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)