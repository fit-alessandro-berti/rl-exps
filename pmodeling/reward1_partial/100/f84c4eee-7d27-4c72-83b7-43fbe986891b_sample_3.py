import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Sensor_Mounting = Transition(label='Sensor Mounting')
Wiring_Harness = Transition(label='Wiring Harness')
Circuit_Testing = Transition(label='Circuit Testing')
Firmware_Loading = Transition(label='Firmware Loading')
Initial_Calibration = Transition(label='Initial Calibration')
Software_Integration = Transition(label='Software Integration')
Flight_Testing = Transition(label='Flight Testing')
Data_Logging = Transition(label='Data Logging')
Performance_Tuning = Transition(label='Performance Tuning')
Packaging_Prep = Transition(label='Packaging Prep')
Custom_Labeling = Transition(label='Custom Labeling')
Documentation_Print = Transition(label='Documentation Print')
Quality_Review = Transition(label='Quality Review')
Client_Training = Transition(label='Client Training')
Remote_Monitoring = Transition(label='Remote Monitoring')
Firmware_Update = Transition(label='Firmware Update')

# Define silent transitions
skip = SilentTransition()

# Define the process flow
assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[Component_Sourcing, Frame_Assembly, Sensor_Mounting, Wiring_Harness, Circuit_Testing, Firmware_Loading, Initial_Calibration])
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[Flight_Testing, Data_Logging, Performance_Tuning])
calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[Software_Integration])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Prep, Custom_Labeling, Documentation_Print])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Review])
training_loop = OperatorPOWL(operator=Operator.LOOP, children=[Client_Training])
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[Remote_Monitoring, Firmware_Update])

# Connect the loops
root = StrictPartialOrder(nodes=[assembly_loop, test_loop, calibration_loop, packaging_loop, quality_loop, training_loop, monitoring_loop])
root.order.add_edge(assembly_loop, test_loop)
root.order.add_edge(test_loop, calibration_loop)
root.order.add_edge(calibration_loop, packaging_loop)
root.order.add_edge(packaging_loop, quality_loop)
root.order.add_edge(quality_loop, training_loop)
root.order.add_edge(training_loop, monitoring_loop)

print(root)