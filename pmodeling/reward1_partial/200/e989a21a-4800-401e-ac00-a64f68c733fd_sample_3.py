import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the process model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        # Define the dependencies between nodes
        (Visual_Inspect, Document_Gather),
        (Document_Gather, Material_Test),
        (Material_Test, Pigment_Analyze),
        (Pigment_Analyze, Style_Compare),
        (Style_Compare, Provenance_Trace),
        (Provenance_Trace, Data_Crosscheck),
        (Data_Crosscheck, Infrared_Scan),
        (Infrared_Scan, Xray_Fluoresce),
        (Xray_Fluoresce, Expert_Consult),
        (Expert_Consult, Forgery_Detect),
        (Forgery_Detect, Report_Draft),
        (Report_Draft, Stakeholder_Review),
        (Stakeholder_Review, Final_Approval),
        (Final_Approval, Archive_Store)
    ]
)

# Print the root model
print(root)