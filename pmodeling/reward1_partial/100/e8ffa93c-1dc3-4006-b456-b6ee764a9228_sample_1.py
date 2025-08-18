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

# Define loops and choices
site_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, env_analysis])
build_loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_build, hydroponics_fit, nutrient_mix, climate_setup])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan])
recycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle])
meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet])
sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync])
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review])

# Define XORs
site_xor = OperatorPOWL(operator=Operator.XOR, children=[site_loop, skip])
build_xor = OperatorPOWL(operator=Operator.XOR, children=[build_loop, skip])
energy_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_loop, skip])
pest_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_loop, skip])
monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[monitor_loop, skip])
harvest_xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_loop, skip])
recycle_xor = OperatorPOWL(operator=Operator.XOR, children=[recycle_loop, skip])
meet_xor = OperatorPOWL(operator=Operator.XOR, children=[meet_loop, skip])
sync_xor = OperatorPOWL(operator=Operator.XOR, children=[sync_loop, skip])
data_xor = OperatorPOWL(operator=Operator.XOR, children=[data_loop, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_xor, build_xor, energy_xor, pest_xor, monitor_xor, harvest_xor, recycle_xor, meet_xor, sync_xor, data_xor])
root.order.add_edge(site_xor, build_xor)
root.order.add_edge(build_xor, energy_xor)
root.order.add_edge(energy_xor, pest_xor)
root.order.add_edge(pest_xor, monitor_xor)
root.order.add_edge(monitor_xor, harvest_xor)
root.order.add_edge(harvest_xor, recycle_xor)
root.order.add_edge(recycle_xor, meet_xor)
root.order.add_edge(meet_xor, sync_xor)
root.order.add_edge(sync_xor, data_xor)

print(root)