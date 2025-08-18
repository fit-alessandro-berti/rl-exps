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
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_review, skip])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, env_analysis, structure_build, hydroponics_fit, nutrient_mix, climate_setup, energy_audit, crop_select])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4])
root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)