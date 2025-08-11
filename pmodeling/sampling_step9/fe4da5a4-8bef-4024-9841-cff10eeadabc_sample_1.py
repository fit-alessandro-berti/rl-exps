import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

PermitSecuring = Transition(label='Permit Securing')
StructureCheck = Transition(label='Structure Check')
SoilTesting = Transition(label='Soil Testing')
WaterAnalysis = Transition(label='Water Analysis')
MaterialSourcing = Transition(label='Material Sourcing')
PlanterSetup = Transition(label='Planter Setup')
SensorInstall = Transition(label='Sensor Install')
IrrigationSetup = Transition(label='Irrigation Setup')
VendorLiaison = Transition(label='Vendor Liaison')
StaffTraining = Transition(label='Staff Training')
PestControl = Transition(label='Pest Control')
ProduceMarketing = Transition(label='Produce Marketing')
CropRotation = Transition(label='Crop Rotation')
HealthAudit = Transition(label='Health Audit')
WasteComposting = Transition(label='Waste Composting')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[PermitSecuring, StructureCheck, SoilTesting, WaterAnalysis, MaterialSourcing, PlanterSetup, SensorInstall, IrrigationSetup, VendorLiaison, StaffTraining, PestControl, ProduceMarketing, CropRotation, HealthAudit, WasteComposting])

xor = OperatorPOWL(operator=Operator.XOR, children=[HealthAudit, WasteComposting])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)