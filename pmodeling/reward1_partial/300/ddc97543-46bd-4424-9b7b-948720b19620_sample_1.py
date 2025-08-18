import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow
site_survey_node = StrictPartialOrder(nodes=[site_survey])
structure_prep_node = StrictPartialOrder(nodes=[structure_prep])
system_install_node = StrictPartialOrder(nodes=[system_install])
env_control_node = StrictPartialOrder(nodes=[env_control])
nutrient_mix_node = StrictPartialOrder(nodes=[nutrient_mix])
crop_select_node = StrictPartialOrder(nodes=[crop_select])
ai_setup_node = StrictPartialOrder(nodes=[ai_setup])
worker_train_node = StrictPartialOrder(nodes=[worker_train])
pest_control_node = StrictPartialOrder(nodes=[pest_control])
irrigation_plan_node = StrictPartialOrder(nodes=[irrigation_plan])
data_monitor_node = StrictPartialOrder(nodes=[data_monitor])
yield_forecast_node = StrictPartialOrder(nodes=[yield_forecast])
energy_audit_node = StrictPartialOrder(nodes=[energy_audit])
market_setup_node = StrictPartialOrder(nodes=[market_setup])
logistics_plan_node = StrictPartialOrder(nodes=[logistics_plan])
waste_manage_node = StrictPartialOrder(nodes=[waste_manage])

# Define the dependencies between activities
root = StrictPartialOrder(nodes=[site_survey_node, structure_prep_node, system_install_node, env_control_node, nutrient_mix_node, crop_select_node, ai_setup_node, worker_train_node, pest_control_node, irrigation_plan_node, data_monitor_node, yield_forecast_node, energy_audit_node, market_setup_node, logistics_plan_node, waste_manage_node])

root.order.add_edge(site_survey_node, structure_prep_node)
root.order.add_edge(structure_prep_node, system_install_node)
root.order.add_edge(system_install_node, env_control_node)
root.order.add_edge(env_control_node, nutrient_mix_node)
root.order.add_edge(nutrient_mix_node, crop_select_node)
root.order.add_edge(crop_select_node, ai_setup_node)
root.order.add_edge(ai_setup_node, worker_train_node)
root.order.add_edge(worker_train_node, pest_control_node)
root.order.add_edge(pest_control_node, irrigation_plan_node)
root.order.add_edge(irrigation_plan_node, data_monitor_node)
root.order.add_edge(data_monitor_node, yield_forecast_node)
root.order.add_edge(yield_forecast_node, energy_audit_node)
root.order.add_edge(energy_audit_node, market_setup_node)
root.order.add_edge(market_setup_node, logistics_plan_node)
root.order.add_edge(logistics_plan_node, waste_manage_node)

# Print the final POWL model
print(root)