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

# Workflow steps
step1 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
step2 = OperatorPOWL(operator=Operator.XOR, children=[environment_setup, sensor_deployment])
step3 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_detection])
step4 = OperatorPOWL(operator=Operator.XOR, children=[automated_harvest, quality_check])
step5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, biodegradable_pack])
step6 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, demand_forecast])
step7 = OperatorPOWL(operator=Operator.XOR, children=[micro_fulfillment, local_dispatch])
step8 = OperatorPOWL(operator=Operator.XOR, children=[consumer_feedback, crop_adjustment])

# Partial Order
root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5, step6, step7, step8])
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)
root.order.add_edge(step6, step7)
root.order.add_edge(step7, step8)

print(root)