import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
IdentifyDevelopmentNeeds = Transition(label='Identify development needs or career aspirations')
CreateDevelopmentPlan = Transition(label='Create personal development plan')
WorkOnSkillEnhancement = Transition(label='Work on skill enhancement')
ReceiveFeedback = Transition(label='Receive feedback and evaluation from supervisors')
ConsiderPromotion = Transition(label='Consider employee for promotion or new role')
ConductReview = Transition(label='Conducts formal performance review')
ApprovePromotion = Transition(label='Approve promotion')
AdjustCompensation = Transition(label='Adjust compensation')
SetNewResponsibilities = Transition(label='Set new responsibilities')
TransitionIntoNewRole = Transition(label='Transition into new role')

# Define loop for continuous feedback and evaluation
LoopFeedback = OperatorPOWL(operator=Operator.LOOP, children=[WorkOnSkillEnhancement, ReceiveFeedback])

# Define exclusive choice between promotion and new role
XorPromotion = OperatorPOWL(operator=Operator.XOR, children=[AdjustCompensation, SetNewResponsibilities])

# Define root node
root = StrictPartialOrder(nodes=[IdentifyDevelopmentNeeds, CreateDevelopmentPlan, LoopFeedback, ConsiderPromotion, ConductReview, ApprovePromotion, XorPromotion, TransitionIntoNewRole])

# Define dependencies
root.order.add_edge(IdentifyDevelopmentNeeds, CreateDevelopmentPlan)
root.order.add_edge(CreateDevelopmentPlan, LoopFeedback)
root.order.add_edge(LoopFeedback, ConsiderPromotion)
root.order.add_edge(ConsiderPromotion, ConductReview)
root.order.add_edge(ConductReview, ApprovePromotion)
root.order.add_edge(ApprovePromotion, XorPromotion)
root.order.add_edge(XorPromotion, TransitionIntoNewRole)

# Print the final model
print(root)