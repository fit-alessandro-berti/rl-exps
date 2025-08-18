from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        site_survey,
        zoning_check,
        design_layout,
        system_order,
        structure_build,
        install_hydroponics,
        calibrate_sensors,
        select_crops,
        plant_seeding,
        monitor_growth,
        manage_pests,
        schedule_harvest,
        package_produce,
        local_delivery,
        analyze_data
    ],
    order={
        site_survey: [zoning_check],
        zoning_check: [design_layout],
        design_layout: [system_order],
        system_order: [structure_build],
        structure_build: [install_hydroponics],
        install_hydroponics: [calibrate_sensors],
        calibrate_sensors: [select_crops],
        select_crops: [plant_seeding],
        plant_seeding: [monitor_growth],
        monitor_growth: [manage_pests],
        manage_pests: [schedule_harvest],
        schedule_harvest: [package_produce],
        package_produce: [local_delivery],
        local_delivery: [analyze_data]
    }
)

# Add additional edges for concurrency or loops if needed
# For example, if there are concurrent activities:
# root.order.add_edge(zoning_check, design_layout)
# root.order.add_edge(system_order, structure_build)
# root.order.add_edge(install_hydroponics, calibrate_sensors)
# root.order.add_edge(select_crops, plant_seeding)
# root.order.add_edge(monitor_growth, manage_pests)
# root.order.add_edge(schedule_harvest, package_produce)
# root.order.add_edge(local_delivery, analyze_data)

# Define loops if needed
# For example, if there is a loop in monitoring growth:
# loop_monitor_growth = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, manage_pests])
# root.nodes.append(loop_monitor_growth)
# root.order.add_edge(monitor_growth, loop_monitor_growth)
# root.order.add_edge(loop_monitor_growth, manage_pests)
# root.order.add_edge(manage_pests, loop_monitor_growth)

# Define exclusive choices if needed
# For example, if there is a choice between local delivery and online sales:
# xor_local_delivery_online_sales = OperatorPOWL(operator=Operator.XOR, children=[local_delivery, analyze_data])
# root.nodes.append(xor_local_delivery_online_sales)
# root.order.add_edge(local_delivery, xor_local_delivery_online_sales)
# root.order.add_edge(analyze_data, xor_local_delivery_online_sales)
# root.order.add_edge(xor_local_delivery_online_sales, analyze_data)

# Print the final root node to verify the POWL model
print(root)