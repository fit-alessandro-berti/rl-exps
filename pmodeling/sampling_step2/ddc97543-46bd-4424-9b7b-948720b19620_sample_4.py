import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
env_control = Transition(label='Env Control')
nutrient_mix = Transition(label='Nutrient Mix')
crop_select = Transition(label='Crop Select')
ai_setup = Transition(label='AI Setup')
worker_train = Transition(label='Worker Train')
pest_control = Transition(label='Pest Control')
irrigation_plan = Transition(label='Irrigation Plan')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_audit = Transition(label='Energy Audit')
market_setup = Transition(label='Market Setup')
logistics_plan = Transition(label='Logistics Plan')
waste_manage = Transition(label='Waste Manage')

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, structure_prep, system_install, env_control, nutrient_mix, crop_select, ai_setup, worker_train, pest_control, irrigation_plan, data_monitor, yield_forecast, energy_audit, market_setup, logistics_plan, waste_manage])

# Define dependencies
root.order.add_edge(site_survey, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, env_control)
root.order.add_edge(env_control, nutrient_mix)
root.order.add_edge(nutrient_mix, crop_select)
root.order.add_edge(crop_select, ai_setup)
root.order.add_edge(ai_setup, worker_train)
root.order.add_edge(worker_train, pest_control)
root.order.add_edge(pest_control, irrigation_plan)
root.order.add_edge(irrigation_plan, data_monitor)
root.order.add_edge(data_monitor, yield_forecast)
root.order.add_edge(yield_forecast, energy_audit)
root.order.add_edge(energy_audit, market_setup)
root.order.add_edge(market_setup, logistics_plan)
root.order.add_edge(logistics_plan, waste_manage)

# Save the final result in the variable 'root'