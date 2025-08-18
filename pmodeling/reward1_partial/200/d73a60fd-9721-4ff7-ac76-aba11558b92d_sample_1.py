import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
system_design = Transition(label='System Design')
permit_filing = Transition(label='Permit Filing')
foundation_prep = Transition(label='Foundation Prep')
frame_build = Transition(label='Frame Build')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
climate_control = Transition(label='Climate Control')
nutrient_mix = Transition(label='Nutrient Mix')
crop_planting = Transition(label='Crop Planting')
pest_scouting = Transition(label='Pest Scouting')
data_monitoring = Transition(label='Data Monitoring')
waste_sorting = Transition(label='Waste Sorting')
energy_audit = Transition(label='Energy Audit')
community_meet = Transition(label='Community Meet')
yield_analysis = Transition(label='Yield Analysis')

skip = SilentTransition()

site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit])
system_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_design, permit_filing, foundation_prep, frame_build, irrigation_setup, lighting_install, climate_control])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, crop_planting])
pest_scouting_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scouting, data_monitoring, waste_sorting, energy_audit, community_meet, yield_analysis])

root = StrictPartialOrder(nodes=[site_audit_loop, system_design_loop, nutrient_mix_loop, pest_scouting_loop])
root.order.add_edge(site_audit_loop, system_design_loop)
root.order.add_edge(system_design_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, pest_scouting_loop)