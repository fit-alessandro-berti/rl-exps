import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SubmitApplication = Transition(label='Submit application online')
ReviewDocuments = Transition(label='Review application and documents')
NotifyMissing = Transition(label='Notify applicant of missing documents')
EvaluateApplication = Transition(label='Evaluate application by admissions committee')
ProcessFees = Transition(label='Process fees or waivers')
SendAcceptance = Transition(label='Send acceptance letter')
SendRejection = Transition(label='Send rejection letter')
ConfirmEnrollment = Transition(label='Confirm enrollment')
CancelApplication = Transition(label='Cancel application')
SendOrientation = Transition(label='Send orientation materials')
SetupIT = Transition(label='Set up IT accounts')
AssistVisa = Transition(label='Assist with visa processing')
ObtainID = Transition(label='Obtain student ID card')
MeetAdvisor = Transition(label='Meet with academic advisor')
SelectCourses = Transition(label='Select courses')
ResolveConflicts = Transition(label='Resolve schedule conflicts')
BeginAttending = Transition(label='Begin attending classes')
AddDrop = Transition(label='Add/drop courses')
PostGrades = Transition(label='Post grades')
ReviewGrades = Transition(label='Review grades online')
SubmitAppeal = Transition(label='Submit appeal form')
MeetAppeals = Transition(label='Meet with appeals committee')
AwaitDecision = Transition(label='Await decision')
Graduate = Transition(label='Graduate')
Withdraw = Transition(label='Withdraw')

# Define choices and loops
Choice1 = OperatorPOWL(operator=Operator.XOR, children=[SendAcceptance, SendRejection])
Choice2 = OperatorPOWL(operator=Operator.XOR, children=[ConfirmEnrollment, CancelApplication])
Choice3 = OperatorPOWL(operator=Operator.XOR, children=[SubmitAppeal, SilentTransition()])
Loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Choice3, MeetAppeals, AwaitDecision])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    SubmitApplication, ReviewDocuments, NotifyMissing, EvaluateApplication, ProcessFees, Choice1,
    Choice2, SendOrientation, SetupIT, AssistVisa, ObtainID, MeetAdvisor, SelectCourses, ResolveConflicts,
    BeginAttending, AddDrop, PostGrades, ReviewGrades, Loop1, Graduate, Withdraw
])

# Define the partial order
root.order.add_edge(SubmitApplication, ReviewDocuments)
root.order.add_edge(ReviewDocuments, EvaluateApplication)
root.order.add_edge(ReviewDocuments, NotifyMissing)
root.order.add_edge(NotifyMissing, ReviewDocuments)
root.order.add_edge(EvaluateApplication, Choice1)
root.order.add_edge(ProcessFees, Choice1)
root.order.add_edge(Choice1, Choice2)
root.order.add_edge(Choice2, SendOrientation)
root.order.add_edge(Choice2, SetupIT)
root.order.add_edge(SendOrientation, AssistVisa)
root.order.add_edge(AssistVisa, ObtainID)
root.order.add_edge(ObtainID, MeetAdvisor)
root.order.add_edge(MeetAdvisor, SelectCourses)
root.order.add_edge(SelectCourses, ResolveConflicts)
root.order.add_edge(ResolveConflicts, BeginAttending)
root.order.add_edge(BeginAttending, AddDrop)
root.order.add_edge(AddDrop, PostGrades)
root.order.add_edge(PostGrades, ReviewGrades)
root.order.add_edge(ReviewGrades, Loop1)
root.order.add_edge(Loop1, Graduate)
root.order.add_edge(Loop1, Withdraw)