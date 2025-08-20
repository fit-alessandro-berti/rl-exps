import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Identify = Transition(label='Identify development needs or career aspirations')
CreatePlan = Transition(label='Create personal development plan')
WorkOnSkills = Transition(label='Work on skill enhancement')
ReceiveFeedback = Transition(label='Receive feedback and evaluation from supervisors')
ConsiderPromotion = Transition(label='Consider employee for promotion or new role')
ConductReview = Transition(label='Conducts formal performance review')
Approve = Transition(label='Approve promotion')
AdjustCompensation = Transition(label='Adjust compensation')
SetResponsibilities = Transition(label='Set new responsibilities')
TransitionIntoNewRole = Transition(label='Transition into new role')

# Define transitions
ConsiderPromotionToConductReview = OperatorPOWL(operator=Operator.XOR, children=[ConsiderPromotion, ConductReview])
ApproveToAdjustCompensation = OperatorPOWL(operator=Operator.XOR, children=[Approve, AdjustCompensation])
SetResponsibilitiesToTransitionIntoNewRole = OperatorPOWL(operator=Operator.XOR, children=[SetResponsibilities, TransitionIntoNewRole])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[Identify, CreatePlan, WorkOnSkills, ReceiveFeedback, ConsiderPromotionToConductReview, ApproveToAdjustCompensation, SetResponsibilitiesToTransitionIntoNewRole])
root.order.add_edge(Identify, CreatePlan)
root.order.add_edge(CreatePlan, WorkOnSkills)
root.order.add_edge(WorkOnSkills, ReceiveFeedback)
root.order.add_edge(ReceiveFeedback, ConsiderPromotionToConductReview)
root.order.add_edge(ConsiderPromotionToConductReview, ApproveToAdjustCompensation)
root.order.add_edge(ApproveToAdjustCompensation, SetResponsibilitiesToTransitionIntoNewRole)