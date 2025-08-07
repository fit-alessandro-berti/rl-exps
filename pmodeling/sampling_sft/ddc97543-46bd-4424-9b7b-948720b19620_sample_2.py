import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structure_prep   = Transition(label='Structure Prep')
system_install   = Transition(label='System Install')
env_control      = Transition(label='Env Control')
nutrient_mix     = Transition(label='Nutrient Mix')
crop_select      = Transition(label='Crop Select')
ai_setup         = Transition(label='AI Setup')
worker_train     = Transition(label='Worker Train')
pest_control     = Transition(label='Pest Control')
irrigation_plan  = Transition(label='Irrigation Plan')
data_monitor     = Transition(label='Data Monitor')
yield_forecast   = Transition(label='Yield Forecast')
energy_audit     = Transition(label='Energy Audit')
market_setup     = Transition(label='Market Setup')
logistics_plan   = Transition(label='Logistics Plan')
waste_manage     = Transition(label='Waste Manage')

# Define the loop for continuous monitoring and optimization
# A = AI Setup -> Data Monitor -> Yield Forecast -> Energy Audit
A = StrictPartialOrder(nodes=[ai_setup, data_monitor, yield_forecast, energy_audit])
A.order.add_edge(ai_setup, data_monitor)
A.order.add_edge(data_monitor, yield_forecast)
A.order.add_edge(yield_forecast, energy_audit)

# B = Site Survey -> Structure Prep -> System Install -> Env Control -> Nutrient Mix -> Crop Select -> Pest Control -> Irrigation Plan
B = StrictPartialOrder(nodes=[
    site_survey, structure_prep, system_install,
    env_control, nutrient_mix, crop_select,
    pest_control, irrigation_plan
])
B.order.add_edge(site_survey, structure_prep)
B.order.add_edge(structure_prep, system_install)
B.order.add_edge(system_install, env_control)
B.order.add_edge(env_control, nutrient_mix)
B.order.add_edge(nutrient_mix, crop_select)
B.order.add_edge(crop_select, pest_control)
B.order.add_edge(pest_control, irrigation_plan)

# LOOP: execute B, then optionally A and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[B, A])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    loop, market_setup, logistics_plan, waste_manage
])
root.order.add_edge(loop, market_setup)
root.order.add_edge(loop, logistics_plan)
root.order.add_edge(loop, waste_manage)