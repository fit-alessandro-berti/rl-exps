import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for concurrency
skip = SilentTransition()

# Define the POWL model
loop_seed_selection = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, skip])
loop_data_monitor = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, skip])
xor_supply_chain = OperatorPOWL(operator=Operator.XOR, children=[supply_chain, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_acquire,
    rack_design,
    loop_seed_selection,
    nutrient_mix,
    lighting_setup,
    sensor_install,
    system_test,
    staff_hire,
    training_lead,
    waste_manage,
    xor_supply_chain,
    crop_cycle,
    loop_data_monitor,
    harvest_plan,
    distribution
])

# Define the partial order dependencies
root.order.add_edge(site_survey, permit_acquire)
root.order.add_edge(permit_acquire, rack_design)
root.order.add_edge(rack_design, loop_seed_selection)
root.order.add_edge(loop_seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, lighting_setup)
root.order.add_edge(lighting_setup, sensor_install)
root.order.add_edge(sensor_install, system_test)
root.order.add_edge(system_test, staff_hire)
root.order.add_edge(staff_hire, training_lead)
root.order.add_edge(training_lead, waste_manage)
root.order.add_edge(waste_manage, xor_supply_chain)
root.order.add_edge(xor_supply_chain, crop_cycle)
root.order.add_edge(crop_cycle, loop_data_monitor)
root.order.add_edge(loop_data_monitor, harvest_plan)
root.order.add_edge(harvest_plan, distribution)

print(root)