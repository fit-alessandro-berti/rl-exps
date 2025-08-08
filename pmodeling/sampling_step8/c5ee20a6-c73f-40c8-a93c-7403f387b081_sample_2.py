import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Initial_Assess = Transition(label='Initial Assess')
Condition_Scan = Transition(label='Condition Scan')
Material_Test = Transition(label='Material Test')
Historical_Check = Transition(label='Historical Check')
Provenance_Verify = Transition(label='Provenance Verify')
Parts_Sourcing = Transition(label='Parts Sourcing')
Gentle_Clean = Transition(label='Gentle Clean')
Stabilize_Item = Transition(label='Stabilize Item')
Structural_Repair = Transition(label='Structural Repair')
Surface_Finish = Transition(label='Surface Finish')
Expert_Consult = Transition(label='Expert Consult')
Archival_Review = Transition(label='Archival Review')
Ethics_Audit = Transition(label='Ethics Audit')
Quality_Inspect = Transition(label='Quality Inspect')
Photo_Document = Transition(label='Photo Document')
Packaging_Prep = Transition(label='Packaging Prep')
Report_Generate = Transition(label='Report Generate')
Certify_Provenance = Transition(label='Certify Provenance')

# Define a silent transition for skipping parts sourcing and gentle clean
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Initial_Assess,
        Condition_Scan,
        Material_Test,
        Historical_Check,
        Provenance_Verify,
        Parts_Sourcing,
        skip,
        Gentle_Clean,
        Stabilize_Item,
        Structural_Repair,
        Surface_Finish,
        Expert_Consult,
        Archival_Review,
        Ethics_Audit,
        Quality_Inspect,
        Photo_Document,
        Packaging_Prep,
        Report_Generate,
        Certify_Provenance
    ]
)

# Define the partial order relationships
root.order.add_edge(Initial_Assess, Condition_Scan)
root.order.add_edge(Condition_Scan, Material_Test)
root.order.add_edge(Material_Test, Historical_Check)
root.order.add_edge(Historical_Check, Provenance_Verify)
root.order.add_edge(Provenance_Verify, Parts_Sourcing)
root.order.add_edge(Parts_Sourcing, skip)
root.order.add_edge(skip, Gentle_Clean)
root.order.add_edge(Gentle_Clean, Stabilize_Item)
root.order.add_edge(Stabilize_Item, Structural_Repair)
root.order.add_edge(Structural_Repair, Surface_Finish)
root.order.add_edge(Surface_Finish, Expert_Consult)
root.order.add_edge(Expert_Consult, Archival_Review)
root.order.add_edge(Archival_Review, Ethics_Audit)
root.order.add_edge(Ethics_Audit, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Photo_Document)
root.order.add_edge(Photo_Document, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Report_Generate)
root.order.add_edge(Report_Generate, Certify_Provenance)