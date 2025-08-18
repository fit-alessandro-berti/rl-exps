import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Inquiry_Intake = Transition(label='Inquiry Intake')
Consultation_Call = Transition(label='Consultation Call')
Concept_Draft = Transition(label='Concept Draft')
Feedback_Loop = Transition(label='Feedback Loop')
Contract_Setup = Transition(label='Contract Setup')
Artist_Match = Transition(label='Artist Match')
Material_Sourcing = Transition(label='Material Sourcing')
Ethics_Review = Transition(label='Ethics Review')
Progress_Check = Transition(label='Progress Check')
Milestone_Approve = Transition(label='Milestone Approve')
Quality_Audit = Transition(label='Quality Audit')
Copyright_Transfer = Transition(label='Copyright Transfer')
Packaging_Plan = Transition(label='Packaging Plan')
Shipping_Arrange = Transition(label='Shipping Arrange')
Post_Delivery = Transition(label='Post Delivery')
Client_Survey = Transition(label='Client Survey')

# Define the structure of the process using Partial Order
root = StrictPartialOrder(nodes=[
    Inquiry_Intake,
    Consultation_Call,
    Concept_Draft,
    Feedback_Loop,
    Contract_Setup,
    Artist_Match,
    Material_Sourcing,
    Ethics_Review,
    Progress_Check,
    Milestone_Approve,
    Quality_Audit,
    Copyright_Transfer,
    Packaging_Plan,
    Shipping_Arrange,
    Post_Delivery,
    Client_Survey
])

# Define the dependencies between activities (using an empty set for now as we're not defining any specific dependencies)
root.order = set()

print(root)