import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Workshop_Host = Transition(label='Workshop Host')
Concept_Filter = Transition(label='Concept Filter')
Prototype_Build = Transition(label='Prototype Build')
Expert_Review = Transition(label='Expert Review')
Feasibility_Check = Transition(label='Feasibility Check')
Risk_Assess = Transition(label='Risk Assess')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Performance_Review = Transition(label='Performance Review')
Scale_Plan = Transition(label='Scale Plan')
Resource_Align = Transition(label='Resource Align')
Learn_Share = Transition(label='Learn Share')
Culture_Embed = Transition(label='Culture Embed')

skip = SilentTransition()

# Cross-functional ideation workshops
xor = OperatorPOWL(operator=Operator.XOR, children=[Idea_Harvest, skip])

# Rapid prototyping and iterative feedback loops
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Prototype_Build, skip])

# Parallel feasibility assessments
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Feasibility_Check, skip])

# Continuous learning and knowledge sharing
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Learn_Share, skip])

# Loop for pilot deployments, performance review, and scale plan
loop = OperatorPOWL(operator=Operator.LOOP, children=[Pilot_Launch, Performance_Review, Scale_Plan])

root = StrictPartialOrder(nodes=[Trend_Scan, xor, xor2, xor3, xor4, loop])
root.order.add_edge(Trend_Scan, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop)
root.order.add_edge(loop, xor)