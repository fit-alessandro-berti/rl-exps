import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
permit_acquire = Transition(label='Permit Acquire')
rack_design = Transition(label='Rack Design')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
lighting_setup = Transition(label='Lighting Setup')
sensor_install = Transition(label='Sensor Install')
system_test = Transition(label='System Test')
staff_hire = Transition(label='Staff Hire')
training_lead = Transition(label='Training Lead')
waste_manage = Transition(label='Waste Manage')
supply_chain = Transition(label='Supply Chain')
crop_cycle = Transition(label='Crop Cycle')
data_monitor = Transition(label='Data Monitor')
harvest_plan = Transition(label='Harvest Plan')
distribution = Transition(label='Distribution')

# Define the loop and exclusive choice
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_cycle, system_test, data_monitor, distribution])
xor = OperatorPOWL(operator=Operator.XOR, children=[staff_hire, training_lead])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, permit_acquire, rack_design, seed_selection, nutrient_mix, lighting_setup, sensor_install, loop, xor])
root.order.add_edge(site_survey, permit_acquire)
root.order.add_edge(permit_acquire, rack_design)
root.order.add_edge(rack_design, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, lighting_setup)
root.order.add_edge(lighting_setup, sensor_install)
root.order.add_edge(sensor_install, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, staff_hire)
root.order.add_edge(xor, training_lead)

# Print the root
print(root)