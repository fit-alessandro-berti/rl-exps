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

# Define partial order nodes
site_survey_node = StrictPartialOrder(nodes=[site_survey, structure_prep])
structure_prep_node = StrictPartialOrder(nodes=[system_install, env_control])
system_install_node = StrictPartialOrder(nodes=[nutrient_mix, crop_select])
env_control_node = StrictPartialOrder(nodes=[ai_setup, worker_train])
nutrient_mix_node = StrictPartialOrder(nodes=[pest_control, irrigation_plan])
crop_select_node = StrictPartialOrder(nodes=[data_monitor, yield_forecast])
ai_setup_node = StrictPartialOrder(nodes=[energy_audit, market_setup])
worker_train_node = StrictPartialOrder(nodes=[logistics_plan, waste_manage])

# Define dependencies between nodes
root = StrictPartialOrder(nodes=[site_survey_node, structure_prep_node, system_install_node, env_control_node, nutrient_mix_node, crop_select_node, ai_setup_node, worker_train_node])
root.order.add_edge(site_survey_node, structure_prep_node)
root.order.add_edge(structure_prep_node, system_install_node)
root.order.add_edge(system_install_node, env_control_node)
root.order.add_edge(env_control_node, nutrient_mix_node)
root.order.add_edge(nutrient_mix_node, crop_select_node)
root.order.add_edge(crop_select_node, ai_setup_node)
root.order.add_edge(ai_setup_node, worker_train_node)