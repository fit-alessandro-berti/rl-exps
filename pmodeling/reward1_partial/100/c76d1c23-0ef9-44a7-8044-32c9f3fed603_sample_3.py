from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
zoning_check = Transition(label='Zoning Check')
design_layout = Transition(label='Design Layout')
system_order = Transition(label='System Order')
structure_build = Transition(label='Structure Build')
install_hydroponics = Transition(label='Install Hydroponics')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
plant_seeding = Transition(label='Plant Seeding')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
schedule_harvest = Transition(label='Schedule Harvest')
package_produce = Transition(label='Package Produce')
local_delivery = Transition(label='Local Delivery')
analyze_data = Transition(label='Analyze Data')

# Define silent transitions
skip = SilentTransition()

# Define loop for crop selection
crop_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[select_crops, plant_seeding])

# Define exclusive choice for monitoring and pest management
monitor_and_manage_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, manage_pests])

# Define root POWL model
root = StrictPartialOrder(nodes=[site_survey, zoning_check, design_layout, system_order, structure_build, install_hydroponics, calibrate_sensors, crop_selection_loop, monitor_and_manage_choice, schedule_harvest, package_produce, local_delivery, analyze_data])
root.order.add_edge(site_survey, zoning_check)
root.order.add_edge(zoning_check, design_layout)
root.order.add_edge(design_layout, system_order)
root.order.add_edge(system_order, structure_build)
root.order.add_edge(structure_build, install_hydroponics)
root.order.add_edge(install_hydroponics, calibrate_sensors)
root.order.add_edge(calibrate_sensors, crop_selection_loop)
root.order.add_edge(crop_selection_loop, monitor_and_manage_choice)
root.order.add_edge(monitor_and_manage_choice, schedule_harvest)
root.order.add_edge(schedule_harvest, package_produce)
root.order.add_edge(package_produce, local_delivery)
root.order.add_edge(local_delivery, analyze_data)