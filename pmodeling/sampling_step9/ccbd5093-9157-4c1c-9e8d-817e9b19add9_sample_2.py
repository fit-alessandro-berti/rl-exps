import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Scan_Markets = Transition(label='Scan Markets')
Host_Workshops = Transition(label='Host Workshops')
Form_Teams = Transition(label='Form Teams')
Develop_Prototypes = Transition(label='Develop Prototypes')
Simulate_Tests = Transition(label='Simulate Tests')
Collect_Feedback = Transition(label='Collect Feedback')
Review_Ethics = Transition(label='Review Ethics')
Conduct_Analysis = Transition(label='Conduct Analysis')
Identify_Partners = Transition(label='Identify Partners')
Align_Strategy = Transition(label='Align Strategy')
Launch_Pilots = Transition(label='Launch Pilots')
Monitor_Trends = Transition(label='Monitor Trends')
AI_Analytics = Transition(label='AI Analytics')
Pivot_Plans = Transition(label='Pivot Plans')
Cycle_Renewal = Transition(label='Cycle Renewal')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Scan_Markets, Host_Workshops])
xor = OperatorPOWL(operator=Operator.XOR, children=[Develop_Prototypes, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Simulate_Tests, Collect_Feedback])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Review_Ethics, Conduct_Analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Identify_Partners, Align_Strategy])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Launch_Pilots, Monitor_Trends])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[AI_Analytics, Pivot_Plans])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Cycle_Renewal, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Print the root node
print(root)