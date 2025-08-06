from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loop nodes and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_acquire, rack_design, seed_selection, nutrient_mix, lighting_setup, sensor_install, system_test])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[staff_hire, training_lead, waste_manage, supply_chain])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[crop_cycle, data_monitor, harvest_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[distribution])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)

# Print the root of the POWL model
print(root)