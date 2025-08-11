import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define activities
DesignConsult = Transition(label='Design Consult')
ComponentSourcing = Transition(label='Component Sourcing')
SensorCalibrate = Transition(label='Sensor Calibrate')
FirmwareIntegrate = Transition(label='Firmware Integrate')
PayloadConfigure = Transition(label='Payload Configure')
AssemblySetup = Transition(label='Assembly Setup')
WiringConnect = Transition(label='Wiring Connect')
ChassisBuild = Transition(label='Chassis Build')
SoftwareLoad = Transition(label='Software Load')
FlightTesting = Transition(label='Flight Testing')
DataAnalyze = Transition(label='Data Analyze')
RegulationCheck = Transition(label='Regulation Check')
QualityInspect = Transition(label='Quality Inspect')
PackagingPrep = Transition(label='Packaging Prep')
LogisticsPlan = Transition(label='Logistics Plan')
ClientReview = Transition(label='Client Review')
# Define silent transitions
skip = SilentTransition()
# Define loop and XOR operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[DesignConsult, ComponentSourcing])
xor = OperatorPOWL(operator=Operator.XOR, children=[SensorCalibrate, FirmwareIntegrate])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[PayloadConfigure, AssemblySetup])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[WiringConnect, ChassisBuild])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[SoftwareLoad, FlightTesting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[DataAnalyze, RegulationCheck])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[QualityInspect, PackagingPrep])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[LogisticsPlan, ClientReview])
# Define the POWL model
root = StrictPartialOrder(nodes=[loop, xor, loop2, xor2, loop3, xor3, loop4, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)