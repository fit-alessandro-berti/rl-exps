from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define nodes for the process
site_analysis = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit])
system_design_and_audit = OperatorPOWL(operator=Operator.XOR, children=[system_design, permit_filing])
foundation_and_frame = OperatorPOWL(operator=Operator.XOR, children=[foundation_prep, frame_build])
irrigation_and_lighting = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, lighting_install])
climate_and_nutrient = OperatorPOWL(operator=Operator.XOR, children=[climate_control, nutrient_mix])
pest_and_monitor = OperatorPOWL(operator=Operator.XOR, children=[pest_scouting, data_monitoring])
waste_and_energy = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, energy_audit])
community_and_yield = OperatorPOWL(operator=Operator.XOR, children=[community_meet, yield_analysis])

# Define the root node
root = StrictPartialOrder(nodes=[site_analysis, system_design_and_audit, foundation_and_frame, irrigation_and_lighting, climate_and_nutrient, pest_and_monitor, waste_and_energy, community_and_yield])

# Define the partial order dependencies
root.order.add_edge(site_analysis, system_design_and_audit)
root.order.add_edge(site_analysis, foundation_and_frame)
root.order.add_edge(system_design_and_audit, foundation_and_frame)
root.order.add_edge(system_design_and_audit, irrigation_and_lighting)
root.order.add_edge(foundation_and_frame, irrigation_and_lighting)
root.order.add_edge(irrigation_and_lighting, climate_and_nutrient)
root.order.add_edge(irrigation_and_lighting, pest_and_monitor)
root.order.add_edge(climate_and_nutrient, pest_and_monitor)
root.order.add_edge(climate_and_nutrient, waste_and_energy)
root.order.add_edge(pest_and_monitor, waste_and_energy)
root.order.add_edge(waste_and_energy, community_and_yield)

print(root)