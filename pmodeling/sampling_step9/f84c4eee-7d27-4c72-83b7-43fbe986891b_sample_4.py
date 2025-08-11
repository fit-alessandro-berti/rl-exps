import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
sourcing = Transition(label='Component Sourcing')
assembly = Transition(label='Frame Assembly')
sensor_mount = Transition(label='Sensor Mounting')
wiring = Transition(label='Wiring Harness')
circuit_test = Transition(label='Circuit Testing')
firmware_load = Transition(label='Firmware Loading')
initial_calib = Transition(label='Initial Calibration')
software_int = Transition(label='Software Integration')
flight_test = Transition(label='Flight Testing')
data_log = Transition(label='Data Logging')
perf_tune = Transition(label='Performance Tuning')
pack_prep = Transition(label='Packaging Prep')
custom_label = Transition(label='Custom Labeling')
doc_print = Transition(label='Documentation Print')
quality_rev = Transition(label='Quality Review')
client_train = Transition(label='Client Training')
remote_mon = Transition(label='Remote Monitoring')
firmware_update = Transition(label='Firmware Update')

# Define the silent transitions
skip = SilentTransition()

# Define the loop
loop_initial_calib = OperatorPOWL(operator=Operator.LOOP, children=[initial_calib, circuit_test, firmware_load, software_int, flight_test, data_log, perf_tune, quality_rev])
loop_remote_mon = OperatorPOWL(operator=Operator.LOOP, children=[remote_mon, firmware_update])

# Define the xor
xor = OperatorPOWL(operator=Operator.XOR, children=[client_train, loop_initial_calib, loop_remote_mon])

# Define the root
root = StrictPartialOrder(nodes=[sourcing, assembly, sensor_mount, wiring, circuit_test, firmware_load, initial_calib, software_int, flight_test, data_log, perf_tune, pack_prep, custom_label, doc_print, quality_rev, client_train, remote_mon, firmware_update])
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, sensor_mount)
root.order.add_edge(sensor_mount, wiring)
root.order.add_edge(wiring, circuit_test)
root.order.add_edge(circuit_test, firmware_load)
root.order.add_edge(firmware_load, software_int)
root.order.add_edge(software_int, flight_test)
root.order.add_edge(flight_test, data_log)
root.order.add_edge(data_log, perf_tune)
root.order.add_edge(perf_tune, quality_rev)
root.order.add_edge(quality_rev, client_train)
root.order.add_edge(client_train, loop_initial_calib)
root.order.add_edge(loop_initial_calib, loop_remote_mon)
root.order.add_edge(loop_remote_mon, remote_mon)
root.order.add_edge(remote_mon, firmware_update)
root.order.add_edge(firmware_update, loop_remote_mon)
root.order.add_edge(loop_remote_mon, xor)
root.order.add_edge(xor, firmware_update)
root.order.add_edge(firmware_update, root)

print(root)