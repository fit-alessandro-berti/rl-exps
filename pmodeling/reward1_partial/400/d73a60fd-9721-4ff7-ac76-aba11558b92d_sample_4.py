import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[system_design, permit_filing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[foundation_prep, frame_build])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, lighting_install])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[climate_control, nutrient_mix])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, pest_scouting])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[data_monitoring, waste_sorting])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, community_meet])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[yield_analysis, None])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, structural_audit, xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)