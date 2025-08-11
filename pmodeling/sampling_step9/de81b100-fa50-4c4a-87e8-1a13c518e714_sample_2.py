import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the silent transition
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_acquire])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[rack_design, seed_selection])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, lighting_setup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, system_test])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[staff_hire, training_lead])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage, supply_chain])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[crop_cycle, data_monitor])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, distribution])

# Define the XOR node
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)
root.order.add_edge(loop4, xor)
root.order.add_edge(loop5, xor)
root.order.add_edge(loop6, xor)
root.order.add_edge(loop7, xor)
root.order.add_edge(loop8, xor)

print(root)