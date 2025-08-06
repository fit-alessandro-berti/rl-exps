import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_sim, seed_select])
water_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle])
energy_link_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_link])
sensor_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install])
pest_detect_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect])
growth_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_scan])

# Define the XORs
xor = OperatorPOWL(operator=Operator.XOR, children=[data_sync, community_meet])

# Define the root
root = StrictPartialOrder(nodes=[site_survey, system_design, climate_loop, module_setup, nutrient_mix, water_cycle_loop, energy_link_loop, sensor_install_loop, pest_detect_loop, growth_scan_loop, xor, reg_compliance, system_test, maintenance_plan])
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, climate_loop)
root.order.add_edge(climate_loop, module_setup)
root.order.add_edge(module_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, water_cycle_loop)
root.order.add_edge(water_cycle_loop, energy_link_loop)
root.order.add_edge(energy_link_loop, sensor_install_loop)
root.order.add_edge(sensor_install_loop, pest_detect_loop)
root.order.add_edge(pest_detect_loop, growth_scan_loop)
root.order.add_edge(growth_scan_loop, xor)
root.order.add_edge(xor, reg_compliance)
root.order.add_edge(reg_compliance, system_test)
root.order.add_edge(system_test, maintenance_plan)

print(root)