import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
structure_build = Transition(label='Structure Build')
hydroponics_fit = Transition(label='Hydroponics Fit')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
energy_audit = Transition(label='Energy Audit')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')
supply_sync = Transition(label='Supply Sync')
data_review = Transition(label='Data Review')

skip = SilentTransition()

site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, env_analysis])
structure_build_xor = OperatorPOWL(operator=Operator.XOR, children=[structure_build, hydroponics_fit])
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, energy_audit])
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, crop_select])
pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, waste_recycle])
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, community_meet])
supply_sync_xor = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, data_review])

root = StrictPartialOrder(nodes=[site_survey_xor, structure_build_xor, nutrient_mix_xor, climate_setup_xor, pest_control_xor, growth_monitor_xor, supply_sync_xor])
root.order.add_edge(site_survey_xor, structure_build_xor)
root.order.add_edge(structure_build_xor, nutrient_mix_xor)
root.order.add_edge(nutrient_mix_xor, climate_setup_xor)
root.order.add_edge(climate_setup_xor, pest_control_xor)
root.order.add_edge(pest_control_xor, growth_monitor_xor)
root.order.add_edge(growth_monitor_xor, supply_sync_xor)