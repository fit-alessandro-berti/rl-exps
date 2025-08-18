import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Discover_Item = Transition(label='Discover Item')
Document_Find = Transition(label='Document Find')
Initial_Survey = Transition(label='Initial Survey')
Image_Capture = Transition(label='Image Capture')
Material_Testing = Transition(label='Material Testing')
Style_Compare = Transition(label='Style Compare')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Check = Transition(label='Provenance Check')
Ownership_Verify = Transition(label='Ownership Verify')
Legal_Review = Transition(label='Legal Review')
Risk_Assess = Transition(label='Risk Assess')
Conservation_Plan = Transition(label='Conservation Plan')
Certification = Transition(label='Certification')
Secure_Transfer = Transition(label='Secure Transfer')
Dispute_Resolve = Transition(label='Dispute Resolve')
Final_Archive = Transition(label='Final Archive')

# Define transitions for the POWL model
skip = SilentTransition()

# Define the process flow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Initial_Survey, Document_Find])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Image_Capture, Material_Testing])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Style_Compare, Expert_Consult])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Provenance_Check, Ownership_Verify])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Legal_Review, Risk_Assess])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Conservation_Plan, Certification])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Secure_Transfer, Dispute_Resolve])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Final_Archive, skip])

# Create the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])

# Add dependencies between loops
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)

print(root)