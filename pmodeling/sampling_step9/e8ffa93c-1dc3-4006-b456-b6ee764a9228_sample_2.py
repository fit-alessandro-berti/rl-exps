import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, env_analysis, structure_build])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_fit, nutrient_mix, climate_setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, crop_select, pest_control])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, harvest_plan, waste_recycle])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, supply_sync, data_review])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop4, loop5])

root = StrictPartialOrder(nodes=[xor1, xor2])
root.order.add_edge(xor1, xor2)

# Print the final result
print(root)