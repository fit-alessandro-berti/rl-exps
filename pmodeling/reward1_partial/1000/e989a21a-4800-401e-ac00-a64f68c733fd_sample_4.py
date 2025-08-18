import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Visual_Inspect = Transition(label='Visual Inspect')
Document_Gather = Transition(label='Document Gather')
Material_Test = Transition(label='Material Test')
Pigment_Analyze = Transition(label='Pigment Analyze')
Style_Compare = Transition(label='Style Compare')
Provenance_Trace = Transition(label='Provenance Trace')
Data_Crosscheck = Transition(label='Data Crosscheck')
Infrared_Scan = Transition(label='Infrared Scan')
Xray_Fluoresce = Transition(label='Xray Fluoresce')
Expert_Consult = Transition(label='Expert Consult')
Forgery_Detect = Transition(label='Forgery Detect')
Report_Draft = Transition(label='Report Draft')
Stakeholder_Review = Transition(label='Stakeholder Review')
Final_Approval = Transition(label='Final Approval')
Archive_Store = Transition(label='Archive Store')

# Define silent transitions (empty labels)
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define the process flow
root = StrictPartialOrder(nodes=[
    Visual_Inspect,
    Document_Gather,
    Material_Test,
    Pigment_Analyze,
    Style_Compare,
    Provenance_Trace,
    Data_Crosscheck,
    Infrared_Scan,
    Xray_Fluoresce,
    Expert_Consult,
    Forgery_Detect,
    Report_Draft,
    Stakeholder_Review,
    Final_Approval,
    Archive_Store
])

# Define dependencies
root.order.add_edge(Visual_Inspect, Document_Gather)
root.order.add_edge(Document_Gather, Material_Test)
root.order.add_edge(Material_Test, Pigment_Analyze)
root.order.add_edge(Pigment_Analyze, Style_Compare)
root.order.add_edge(Style_Compare, Provenance_Trace)
root.order.add_edge(Provenance_Trace, Data_Crosscheck)
root.order.add_edge(Data_Crosscheck, Infrared_Scan)
root.order.add_edge(Infrared_Scan, Xray_Fluoresce)
root.order.add_edge(Xray_Fluoresce, Expert_Consult)
root.order.add_edge(Expert_Consult, Forgery_Detect)
root.order.add_edge(Forgery_Detect, Report_Draft)
root.order.add_edge(Report_Draft, Stakeholder_Review)
root.order.add_edge(Stakeholder_Review, Final_Approval)
root.order.add_edge(Final_Approval, Archive_Store)

print(root)