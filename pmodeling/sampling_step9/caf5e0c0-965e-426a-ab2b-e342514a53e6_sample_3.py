import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
climate_sim = Transition(label='Climate Sim')
seed_select = Transition(label='Seed Select')
module_setup = Transition(label='Module Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
energy_link = Transition(label='Energy Link')
sensor_install = Transition(label='Sensor Install')
pest_detect = Transition(label='Pest Detect')
growth_scan = Transition(label='Growth Scan')
data_sync = Transition(label='Data Sync')
community_meet = Transition(label='Community Meet')
reg_compliance = Transition(label='Reg Compliance')
system_test = Transition(label='System Test')
maintenance_plan = Transition(label='Maintenance Plan')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[module_setup, nutrient_mix, water_cycle, energy_link])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, pest_detect, growth_scan, data_sync])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, reg_compliance, system_test, maintenance_plan])

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[climate_sim, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[seed_select, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, system_design, xor1, loop1, xor2, loop2, loop3])
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, maintenance_plan)

# Print the root POWL model
print(root)