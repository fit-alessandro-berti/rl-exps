import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the POWL model
Receive_Artifact = Transition(label='Receive Artifact')
Condition_Log = Transition(label='Condition Log')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
Risk_Assess = Transition(label='Risk Assess')
ThreeD_Scan = Transition(label='3D Scan')
Legal_Review = Transition(label='Legal Review')
Insurance_Setup = Transition(label='Insurance Setup')
Certificate_Draft = Transition(label='Certificate Draft')
Certificate_Approve = Transition(label='Certificate Approve')
Climate_Pack = Transition(label='Climate Pack')
Conservation_Plan = Transition(label='Conservation Plan')
Monitoring_Schedule = Transition(label='Monitoring Schedule')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    Receive_Artifact,
    Condition_Log,
    Radiocarbon_Test,
    Spectroscopy_Scan,
    Expert_Consult,
    Provenance_Check,
    Archive_Search,
    Risk_Assess,
    ThreeD_Scan,
    Legal_Review,
    Insurance_Setup,
    Certificate_Draft,
    Certificate_Approve,
    Climate_Pack,
    Conservation_Plan,
    Monitoring_Schedule
])

# Define the dependencies (order) between transitions
root.order.add_edge(Receive_Artifact, Condition_Log)
root.order.add_edge(Condition_Log, Radiocarbon_Test)
root.order.add_edge(Radiocarbon_Test, Spectroscopy_Scan)
root.order.add_edge(Spectroscopy_Scan, Expert_Consult)
root.order.add_edge(Expert_Consult, Provenance_Check)
root.order.add_edge(Provenance_Check, Archive_Search)
root.order.add_edge(Archive_Search, Risk_Assess)
root.order.add_edge(Risk_Assess, ThreeD_Scan)
root.order.add_edge(ThreeD_Scan, Legal_Review)
root.order.add_edge(Legal_Review, Insurance_Setup)
root.order.add_edge(Insurance_Setup, Certificate_Draft)
root.order.add_edge(Certificate_Draft, Certificate_Approve)
root.order.add_edge(Certificate_Approve, Climate_Pack)
root.order.add_edge(Climate_Pack, Conservation_Plan)
root.order.add_edge(Conservation_Plan, Monitoring_Schedule)

# Now 'root' contains the POWL model for the described process