import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
sourcing = Transition(label='Component Sourcing')
assembly = Transition(label='Frame Assembly')
motor = Transition(label='Motor Installation')
sensor = Transition(label='Sensor Mounting')
wiring = Transition(label='Wiring Setup')
firmware = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration = Transition(label='Calibration Phase')
testing = Transition(label='Stress Testing')
simulation = Transition(label='Flight Simulation')
adjustment = Transition(label='Pattern Adjustment')
inspect = Transition(label='Quality Inspect')
compliance = Transition(label='Compliance Check')
packaging = Transition(label='Packaging Final')
delivery = Transition(label='Delivery Setup')

# Define the workflow
sourcing_to_assembly = OperatorPOWL(operator=Operator.XOR, children=[sourcing, assembly])
assembly_to_motor = OperatorPOWL(operator=Operator.XOR, children=[assembly, motor])
motor_to_sensor = OperatorPOWL(operator=Operator.XOR, children=[motor, sensor])
sensor_to_wiring = OperatorPOWL(operator=Operator.XOR, children=[sensor, wiring])
wiring_to_firmware = OperatorPOWL(operator=Operator.XOR, children=[wiring, firmware])
firmware_to_ai = OperatorPOWL(operator=Operator.XOR, children=[firmware, ai_module])
ai_to_calibration = OperatorPOWL(operator=Operator.XOR, children=[ai_module, calibration])
calibration_to_testing = OperatorPOWL(operator=Operator.XOR, children=[calibration, testing])
testing_to_simulation = OperatorPOWL(operator=Operator.XOR, children=[testing, simulation])
simulation_to_adjustment = OperatorPOWL(operator=Operator.XOR, children=[simulation, adjustment])
adjustment_to_inspect = OperatorPOWL(operator=Operator.XOR, children=[adjustment, inspect])
inspect_to_compliance = OperatorPOWL(operator=Operator.XOR, children=[inspect, compliance])
compliance_to_packaging = OperatorPOWL(operator=Operator.XOR, children=[compliance, packaging])
packaging_to_delivery = OperatorPOWL(operator=Operator.XOR, children=[packaging, delivery])

# Create the root node
root = StrictPartialOrder(nodes=[
    sourcing_to_assembly, assembly_to_motor, motor_to_sensor, sensor_to_wiring,
    wiring_to_firmware, firmware_to_ai, ai_to_calibration, calibration_to_testing,
    testing_to_simulation, simulation_to_adjustment, adjustment_to_inspect,
    inspect_to_compliance, compliance_to_packaging, packaging_to_delivery
])

# Add dependencies
root.order.add_edge(sourcing_to_assembly, assembly_to_motor)
root.order.add_edge(assembly_to_motor, motor_to_sensor)
root.order.add_edge(motor_to_sensor, sensor_to_wiring)
root.order.add_edge(sensor_to_wiring, wiring_to_firmware)
root.order.add_edge(wiring_to_firmware, firmware_to_ai)
root.order.add_edge(firmware_to_ai, ai_to_calibration)
root.order.add_edge(ai_to_calibration, calibration_to_testing)
root.order.add_edge(calibration_to_testing, testing_to_simulation)
root.order.add_edge(testing_to_simulation, simulation_to_adjustment)
root.order.add_edge(simulation_to_adjustment, adjustment_to_inspect)
root.order.add_edge(adjustment_to_inspect, inspect_to_compliance)
root.order.add_edge(inspect_to_compliance, compliance_to_packaging)
root.order.add_edge(compliance_to_packaging, packaging_to_delivery)

print(root)