import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
InitialAssess = Transition(label='Initial Assess')
DisassembleParts = Transition(label='Disassemble Parts')
UltrasonicClean = Transition(label='Ultrasonic Clean')
InspectComponents = Transition(label='Inspect Components')
FabricateGears = Transition(label='Fabricate Gears')
DialRestoration = Transition(label='Dial Restoration')
RepaintMarkers = Transition(label='Repaint Markers')
ReassembleMovement = Transition(label='Reassemble Movement')
LubricateBearings = Transition(label='Lubricate Bearings')
CalibrateTiming = Transition(label='Calibrate Timing')
PolishCase = Transition(label='Polish Case')
ReCaseWatch = Transition(label='Re-case Watch')
QualityTesting = Transition(label='Quality Testing')
DocumentProcess = Transition(label='Document Process')
PackageProduct = Transition(label='Package Product')

# Define the loop for gear fabrication
fabrication_loop = OperatorPOWL(operator=Operator.LOOP, children=[InspectComponents, FabricateGears])

# Define the exclusive choice for dial restoration
dial_restoration_choice = OperatorPOWL(operator=Operator.XOR, children=[DialRestoration, RepaintMarkers])

# Define the partial order
root = StrictPartialOrder(nodes=[InitialAssess, DisassembleParts, UltrasonicClean, InspectComponents, fabrication_loop, dial_restoration_choice, ReassembleMovement, LubricateBearings, CalibrateTiming, PolishCase, ReCaseWatch, QualityTesting, DocumentProcess, PackageProduct])

# Define the dependencies between nodes
root.order.add_edge(InitialAssess, DisassembleParts)
root.order.add_edge(DisassembleParts, UltrasonicClean)
root.order.add_edge(UltrasonicClean, InspectComponents)
root.order.add_edge(InspectComponents, fabrication_loop)
root.order.add_edge(fabrication_loop, dial_restoration_choice)
root.order.add_edge(dial_restoration_choice, ReassembleMovement)
root.order.add_edge(ReassembleMovement, LubricateBearings)
root.order.add_edge(LubricateBearings, CalibrateTiming)
root.order.add_edge(CalibrateTiming, PolishCase)
root.order.add_edge(PolishCase, ReCaseWatch)
root.order.add_edge(ReCaseWatch, QualityTesting)
root.order.add_edge(QualityTesting, DocumentProcess)
root.order.add_edge(DocumentProcess, PackageProduct)

print(root)