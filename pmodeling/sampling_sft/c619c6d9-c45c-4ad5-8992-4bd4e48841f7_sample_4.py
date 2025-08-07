import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
design = Transition(label='Design Consult')
sourcing = Transition(label='Component Sourcing')
calibrate = Transition(label='Sensor Calibrate')
firmware = Transition(label='Firmware Integrate')
payload = Transition(label='Payload Configure')
assembly = Transition(label='Assembly Setup')
wiring = Transition(label='Wiring Connect')
chassis = Transition(label='Chassis Build')
software = Transition(label='Software Load')
flight = Transition(label='Flight Testing')
analyze = Transition(label='Data Analyze')
reg_check = Transition(label='Regulation Check')
quality = Transition(label='Quality Inspect')
packaging = Transition(label='Packaging Prep')
logistics = Transition(label='Logistics Plan')
client_review = Transition(label='Client Review')

# Loop for iterative flight testing: Flight Testing -> Data Analyze -> Regulation Check
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight, analyze])
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_loop, reg_check])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    design, sourcing, calibrate, firmware, payload,
    assembly, wiring, chassis, software,
    test_loop, quality, packaging, logistics, client_review
])

# Define the control-flow dependencies
root.order.add_edge(design, sourcing)
root.order.add_edge(sourcing, calibrate)
root.order.add_edge(calibrate, firmware)
root.order.add_edge(firmware, payload)
root.order.add_edge(payload, assembly)
root.order.add_edge(assembly, wiring)
root.order.add_edge(wiring, chassis)
root.order.add_edge(chassis, software)
root.order.add_edge(software, test_loop)
root.order.add_edge(test_loop, quality)
root.order.add_edge(quality, packaging)
root.order.add_edge(packaging, logistics)
root.order.add_edge(logistics, client_review)