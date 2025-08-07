import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
design = Transition(label='Design Consult')
comp_sourcing = Transition(label='Component Sourcing')
sensor_cal = Transition(label='Sensor Calibrate')
firmware_int = Transition(label='Firmware Integrate')
payload_conf = Transition(label='Payload Configure')
assembly_setup = Transition(label='Assembly Setup')
wiring_conn = Transition(label='Wiring Connect')
chassis_build = Transition(label='Chassis Build')
software_load = Transition(label='Software Load')
flight_test = Transition(label='Flight Testing')
data_analyze = Transition(label='Data Analyze')
reg_check = Transition(label='Regulation Check')
quality_inspect = Transition(label='Quality Inspect')
pack_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_review = Transition(label='Client Review')

# Loop for iterative flight testing and data analysis
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flight_test, data_analyze]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    design,
    comp_sourcing,
    sensor_cal,
    firmware_int,
    payload_conf,
    assembly_setup,
    wiring_conn,
    chassis_build,
    software_load,
    flight_loop,
    reg_check,
    quality_inspect,
    pack_prep,
    logistics_plan,
    client_review
])

# Define the control-flow edges
root.order.add_edge(design, comp_sourcing)
root.order.add_edge(comp_sourcing, sensor_cal)
root.order.add_edge(comp_sourcing, firmware_int)
root.order.add_edge(sensor_cal, payload_conf)
root.order.add_edge(firmware_int, payload_conf)
root.order.add_edge(payload_conf, assembly_setup)
root.order.add_edge(assembly_setup, wiring_conn)
root.order.add_edge(wiring_conn, chassis_build)
root.order.add_edge(chassis_build, software_load)
root.order.add_edge(software_load, flight_loop)
root.order.add_edge(flight_loop, reg_check)
root.order.add_edge(flight_loop, quality_inspect)
root.order.add_edge(reg_check, pack_prep)
root.order.add_edge(reg_check, logistics_plan)
root.order.add_edge(quality_inspect, pack_prep)
root.order.add_edge(quality_inspect, logistics_plan)
root.order.add_edge(pack_prep, client_review)
root.order.add_edge(logistics_plan, client_review)

# Print the root model for verification
print(root)