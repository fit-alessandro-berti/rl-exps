import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
IdentifyNeed = Transition(label='Identify need for new hire')
CreateJobDesc = Transition(label='Create job description')
PostJobDesc = Transition(label='Post job description')
CollectResumes = Transition(label='Collect resumes')
ScreenResumes = Transition(label='Screen resumes')
InitialPhoneInt = Transition(label='Conduct initial phone interviews')
InviteCandidates = Transition(label='Invite candidates for interviews')
VirtualInterview = Transition(label='Conduct a virtual interview')
InPersonInterview = Transition(label='Conduct an in-person interview')
ChooseCandidate = Transition(label='Choose candidate')
ExtendOffer = Transition(label='Extend offer')
NegotiateSalary = Transition(label='Negotiate salary')
BeginOnboarding = Transition(label='Begin onboarding process')
CompletePaperwork = Transition(label='Complete paperwork')
CompleteOrientation = Transition(label='Complete orientation')
CompleteTraining = Transition(label='Complete training')

# Define silent transitions
skip = SilentTransition()

# Define loop for interview process
InterviewLoop = OperatorPOWL(operator=Operator.LOOP, children=[VirtualInterview, InPersonInterview])

# Define XOR for interview preference
InterviewXOR = OperatorPOWL(operator=Operator.XOR, children=[InterviewLoop, skip])

# Define XOR for salary negotiation
SalaryNegotiation = OperatorPOWL(operator=Operator.XOR, children=[NegotiateSalary, skip])

# Define strict partial order for onboarding process
OnboardingProcess = StrictPartialOrder(nodes=[CompletePaperwork, CompleteOrientation, CompleteTraining])

# Define the root strict partial order
root = StrictPartialOrder(nodes=[IdentifyNeed, CreateJobDesc, PostJobDesc, CollectResumes, ScreenResumes, InitialPhoneInt, InviteCandidates, InterviewXOR, ChooseCandidate, ExtendOffer, SalaryNegotiation, BeginOnboarding, OnboardingProcess])

# Define the order of transitions
root.order.add_edge(IdentifyNeed, CreateJobDesc)
root.order.add_edge(CreateJobDesc, PostJobDesc)
root.order.add_edge(PostJobDesc, CollectResumes)
root.order.add_edge(CollectResumes, ScreenResumes)
root.order.add_edge(ScreenResumes, InitialPhoneInt)
root.order.add_edge(InitialPhoneInt, InviteCandidates)
root.order.add_edge(InviteCandidates, InterviewXOR)
root.order.add_edge(InterviewXOR, ChooseCandidate)
root.order.add_edge(ChooseCandidate, ExtendOffer)
root.order.add_edge(ExtendOffer, SalaryNegotiation)
root.order.add_edge(SalaryNegotiation, BeginOnboarding)
root.order.add_edge(BeginOnboarding, OnboardingProcess)
root.order.add_edge(OnboardingProcess, CompletePaperwork)
root.order.add_edge(CompletePaperwork, CompleteOrientation)
root.order.add_edge(CompleteOrientation, CompleteTraining)