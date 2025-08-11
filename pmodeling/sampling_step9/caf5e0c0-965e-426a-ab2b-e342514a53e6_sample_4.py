import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define exclusive choice (XOR) for various activities
xor = OperatorPOWL(operator=Operator.XOR, children=[
    system_design,
    climate_sim,
    seed_select,
    module_setup,
    nutrient_mix,
    water_cycle,
    energy_link,
    sensor_install,
    pest_detect,
    growth_scan,
    data_sync,
    community_meet,
    reg_compliance,
    system_test,
    maintenance_plan
])

# Define loop for data sync and community meet
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_sync, community_meet])

# Define partial order
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)