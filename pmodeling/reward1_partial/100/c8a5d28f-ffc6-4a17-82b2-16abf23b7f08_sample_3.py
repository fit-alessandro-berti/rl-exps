import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
Pasteurize = Transition(label='Milk Pasteurize')
CultureAddition = Transition(label='Culture Addition')
CurdCutting = Transition(label='Curd Cutting')
WheyDrain = Transition(label='Whey Drain')
CheeseMolding = Transition(label='Cheese Molding')
Aging = Transition(label='Controlled Aging')
SensoryCheck = Transition(label='Sensory Check')
HealthCertify = Transition(label='Health Certify')
CustomLabeling = Transition(label='Custom Labeling')
ColdPackaging = Transition(label='Cold Packaging')
LogisticsSetup = Transition(label='Logistics Setup')
ExportDocs = Transition(label='Export Docs')
CustomsClearance = Transition(label='Customs Clearance')
ShipmentTrack = Transition(label='Shipment Track')
ClientFeedback = Transition(label='Client Feedback')

skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[QualityTesting, Pasteurize, CultureAddition, CurdCutting, WheyDrain, CheeseMolding, Aging, SensoryCheck])
xor = OperatorPOWL(operator=Operator.XOR, children=[HealthCertify, CustomLabeling, ColdPackaging, LogisticsSetup, ExportDocs, CustomsClearance, ShipmentTrack, ClientFeedback])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Add dependencies
root.order.add_edge(QualityTesting, Pasteurize)
root.order.add_edge(Pasteurize, CultureAddition)
root.order.add_edge(CultureAddition, CurdCutting)
root.order.add_edge(CurdCutting, WheyDrain)
root.order.add_edge(WheyDrain, CheeseMolding)
root.order.add_edge(CheeseMolding, Aging)
root.order.add_edge(Aging, SensoryCheck)
root.order.add_edge(HealthCertify, CustomLabeling)
root.order.add_edge(CustomLabeling, ColdPackaging)
root.order.add_edge(ColdPackaging, LogisticsSetup)
root.order.add_edge(LogisticsSetup, ExportDocs)
root.order.add_edge(ExportDocs, CustomsClearance)
root.order.add_edge(CustomsClearance, ShipmentTrack)
root.order.add_edge(ShipmentTrack, ClientFeedback)