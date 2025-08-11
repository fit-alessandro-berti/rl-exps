import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
skip = SilentTransition()

# Define the process tree
permit_acquire_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_acquire])
rack_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[rack_design])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
lighting_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[lighting_setup])
sensor_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install])
system_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_test])
staff_hire_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_hire])
training_lead_loop = OperatorPOWL(operator=Operator.LOOP, children=[training_lead])
waste_manage_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage])
supply_chain_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_chain])
crop_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_cycle])
data_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor])
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan])
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution])

# Define the partial order
root = StrictPartialOrder(nodes=[
    permit_acquire_loop,
    rack_design_loop,
    nutrient_mix_loop,
    lighting_setup_loop,
    sensor_install_loop,
    system_test_loop,
    staff_hire_loop,
    training_lead_loop,
    waste_manage_loop,
    supply_chain_loop,
    crop_cycle_loop,
    data_monitor_loop,
    harvest_plan_loop,
    distribution_loop
])
root.order.add_edge(permit_acquire_loop, rack_design_loop)
root.order.add_edge(rack_design_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, lighting_setup_loop)
root.order.add_edge(lighting_setup_loop, sensor_install_loop)
root.order.add_edge(sensor_install_loop, system_test_loop)
root.order.add_edge(system_test_loop, staff_hire_loop)
root.order.add_edge(staff_hire_loop, training_lead_loop)
root.order.add_edge(training_lead_loop, waste_manage_loop)
root.order.add_edge(waste_manage_loop, supply_chain_loop)
root.order.add_edge(supply_chain_loop, crop_cycle_loop)
root.order.add_edge(crop_cycle_loop, data_monitor_loop)
root.order.add_edge(data_monitor_loop, harvest_plan_loop)
root.order.add_edge(harvest_plan_loop, distribution_loop)

# Print the POWL model
print(root)