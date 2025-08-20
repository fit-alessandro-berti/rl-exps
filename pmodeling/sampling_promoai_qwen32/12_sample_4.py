import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
IdentifyDevelopmentNeeds = Transition(label='Identify development needs or career aspirations')
CreatePersonalDevPlan = Transition(label='Create personal development plan')
WorkOnSkillEnhancement = Transition(label='Work on skill enhancement')
ReceiveFeedback = Transition(label='Receive feedback and evaluation from supervisors')
ConsiderPromotion = Transition(label='Consider employee for promotion or new role')
ConductFormalReview = Transition(label='Conducts formal performance review')
ApprovePromotion = Transition(label='Approve promotion')
AdjustCompensation = Transition(label='Adjust compensation')
SetNewResponsibilities = Transition(label='Set new responsibilities')
TransitionIntoNewRole = Transition(label='Transition into new role')

# Define the structure of the POWL model
root = StrictPartialOrder(nodes=[IdentifyDevelopmentNeeds, CreatePersonalDevPlan, WorkOnSkillEnhancement, ReceiveFeedback, ConsiderPromotion, ConductFormalReview, ApprovePromotion, AdjustCompensation, SetNewResponsibilities, TransitionIntoNewRole])

# Define the order of the activities
root.order.add_edge(IdentifyDevelopmentNeeds, CreatePersonalDevPlan)
root.order.add_edge(CreatePersonalDevPlan, WorkOnSkillEnhancement)
root.order.add_edge(WorkOnSkillEnhancement, ReceiveFeedback)
root.order.add_edge(ReceiveFeedback, ConsiderPromotion)
root.order.add_edge(ConsiderPromotion, ConductFormalReview)
root.order.add_edge(ConductFormalReview, ApprovePromotion)
root.order.add_edge(ApprovePromotion, AdjustCompensation)
root.order.add_edge(AdjustCompensation, SetNewResponsibilities)
root.order.add_edge(SetNewResponsibilities, TransitionIntoNewRole)

# Return the final result in the variable 'root'
root