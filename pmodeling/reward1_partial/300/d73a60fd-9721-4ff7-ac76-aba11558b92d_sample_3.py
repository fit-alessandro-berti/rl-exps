from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL operators
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit])
system_design_choice = OperatorPOWL(operator=Operator.XOR, children=[system_design, permit_filing])
foundation_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[foundation_prep, frame_build])
irrigation_lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup, lighting_install])
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, nutrient_mix])
pest_scouting_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scouting, data_monitoring])
waste_sorting_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sorting, energy_audit])
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, yield_analysis])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_audit_loop, system_design_choice, foundation_prep_loop, irrigation_lighting_loop, climate_control_loop, pest_scouting_loop, waste_sorting_loop, community_meet_loop])
root.order.add_edge(site_audit_loop, system_design_choice)
root.order.add_edge(system_design_choice, foundation_prep_loop)
root.order.add_edge(foundation_prep_loop, irrigation_lighting_loop)
root.order.add_edge(irrigation_lighting_loop, climate_control_loop)
root.order.add_edge(climate_control_loop, pest_scouting_loop)
root.order.add_edge(pest_scouting_loop, waste_sorting_loop)
root.order.add_edge(waste_sorting_loop, community_meet_loop)

# Print the root POWL model
print(root)