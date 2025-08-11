import pm4py
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
skip = SilentTransition()

# Define loops and exclusive choices
loop = OperatorPOWL(operator=Operator.LOOP, children=[foundation_prep, frame_build, irrigation_setup, lighting_install, climate_control, nutrient_mix, crop_planting, pest_scouting])
xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analysis, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root to see the POWL model
print(root)