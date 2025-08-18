from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
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

# Define operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[permit_acquire, rack_design])
loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_mix, lighting_setup, sensor_install, system_test])
partial_order = StrictPartialOrder(nodes=[exclusive_choice, loop, staff_hire, training_lead, waste_manage, supply_chain, crop_cycle, data_monitor, harvest_plan, distribution])

# Define dependencies
partial_order.order.add_edge(exclusive_choice, loop)
partial_order.order.add_edge(loop, staff_hire)
partial_order.order.add_edge(staff_hire, training_lead)
partial_order.order.add_edge(training_lead, waste_manage)
partial_order.order.add_edge(waste_manage, supply_chain)
partial_order.order.add_edge(supply_chain, crop_cycle)
partial_order.order.add_edge(crop_cycle, data_monitor)
partial_order.order.add_edge(data_monitor, harvest_plan)
partial_order.order.add_edge(harvest_plan, distribution)

root = partial_order