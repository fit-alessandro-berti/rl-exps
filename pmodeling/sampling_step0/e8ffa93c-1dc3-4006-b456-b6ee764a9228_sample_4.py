from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[env_analysis, structure_build])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_fit, nutrient_mix, climate_setup, energy_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, pest_control, growth_monitor, harvest_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, community_meet, supply_sync])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_review])

# Construct the root model
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop)