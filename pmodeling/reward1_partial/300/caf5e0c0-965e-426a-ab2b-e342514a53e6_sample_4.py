from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define a silent transition for no operation
skip = SilentTransition()

# Define a loop for the seed selection and nutrient mix
loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_select, nutrient_mix])

# Define a XOR (exclusive choice) for energy link and water cycle
xor = OperatorPOWL(operator=Operator.XOR, children=[energy_link, water_cycle])

# Define a XOR (exclusive choice) for sensor install and pest detect
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, pest_detect])

# Define a XOR (exclusive choice) for growth scan and data sync
xor3 = OperatorPOWL(operator=Operator.XOR, children=[growth_scan, data_sync])

# Define a XOR (exclusive choice) for community meet and reg compliance
xor4 = OperatorPOWL(operator=Operator.XOR, children=[community_meet, reg_compliance])

# Define a XOR (exclusive choice) for system test and maintenance plan
xor5 = OperatorPOWL(operator=Operator.XOR, children=[system_test, maintenance_plan])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    system_design,
    climate_sim,
    loop,
    xor,
    xor2,
    xor3,
    xor4,
    xor5
])

# Add edges to establish the order
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, climate_sim)
root.order.add_edge(climate_sim, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, maintenance_plan)

# Print the root POWL model
print(root)