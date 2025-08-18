import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
Initial_Assess = Transition(label='Initial Assess')
Disassemble_Parts = Transition(label='Disassemble Parts')
Ultrasonic_Clean = Transition(label='Ultrasonic Clean')
Inspect_Components = Transition(label='Inspect Components')
Fabricate_Gears = Transition(label='Fabricate Gears')
Dial_Restoration = Transition(label='Dial Restoration')
Repaint_Markers = Transition(label='Repaint Markers')
Reassemble_Movement = Transition(label='Reassemble Movement')
Lubricate_Bearings = Transition(label='Lubricate Bearings')
Calibrate_Timing = Transition(label='Calibrate Timing')
Polish_Case = Transition(label='Polish Case')
Re_case_Watch = Transition(label='Re-case Watch')
Quality_Testing = Transition(label='Quality Testing')
Document_Process = Transition(label='Document Process')
Package_Product = Transition(label='Package Product')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Initial_Assess, 
    Disassemble_Parts, 
    Ultrasonic_Clean, 
    Inspect_Components, 
    Fabricate_Gears, 
    Dial_Restoration, 
    Repaint_Markers, 
    Reassemble_Movement, 
    Lubricate_Bearings, 
    Calibrate_Timing, 
    Polish_Case, 
    Re_case_Watch, 
    Quality_Testing, 
    Document_Process, 
    Package_Product
])

# Define the dependencies
root.order.add_edge(Initial_Assess, Disassemble_Parts)
root.order.add_edge(Disassemble_Parts, Ultrasonic_Clean)
root.order.add_edge(Ultrasonic_Clean, Inspect_Components)
root.order.add_edge(Inspect_Components, Fabricate_Gears)
root.order.add_edge(Fabricate_Gears, Dial_Restoration)
root.order.add_edge(Dial_Restoration, Repaint_Markers)
root.order.add_edge(Repaint_Markers, Reassemble_Movement)
root.order.add_edge(Reassemble_Movement, Lubricate_Bearings)
root.order.add_edge(Lubricate_Bearings, Calibrate_Timing)
root.order.add_edge(Calibrate_Timing, Polish_Case)
root.order.add_edge(Polish_Case, Re_case_Watch)
root.order.add_edge(Re_case_Watch, Quality_Testing)
root.order.add_edge(Quality_Testing, Document_Process)
root.order.add_edge(Document_Process, Package_Product)

print(root)