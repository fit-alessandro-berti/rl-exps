import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Expert_Review = Transition(label='Expert Review')
Legal_Audit = Transition(label='Legal Audit')
Condition_Report = Transition(label='Condition Report')
Carbon_Dating = Transition(label='Carbon Dating')
Ownership_Verify = Transition(label='Ownership Verify')
Historical_Match = Transition(label='Historical Match')
Customs_Clearance = Transition(label='Customs Clearance')
Risk_Assessment = Transition(label='Risk Assessment')
Ethics_Approval = Transition(label='Ethics Approval')
Restoration_Plan = Transition(label='Restoration Plan')
Final_Approval = Transition(label='Final Approval')
Catalog_Entry = Transition(label='Catalog Entry')
Exhibit_Preparation = Transition(label='Exhibit Prep')

# Define silent transitions
skip = SilentTransition()

# Define the workflow model
# Start with provenance check, then proceed to material scan, expert review, and legal audit
# After these, proceed to condition report, carbon dating, ownership verify, historical match, customs clearance, risk assessment, and ethics approval
# Then, proceed to restoration plan, final approval, and catalog entry
# Finally, proceed to exhibit preparation
root = StrictPartialOrder(nodes=[
    Provenance_Check,
    Material_Scan,
    Expert_Review,
    Legal_Audit,
    Condition_Report,
    Carbon_Dating,
    Ownership_Verify,
    Historical_Match,
    Customs_Clearance,
    Risk_Assessment,
    Ethics_Approval,
    Restoration_Plan,
    Final_Approval,
    Catalog_Entry,
    Exhibit_Preparation
])

# Define dependencies between activities
root.order.add_edge(Provenance_Check, Material_Scan)
root.order.add_edge(Material_Scan, Expert_Review)
root.order.add_edge(Expert_Review, Legal_Audit)
root.order.add_edge(Legal_Audit, Condition_Report)
root.order.add_edge(Condition_Report, Carbon_Dating)
root.order.add_edge(Carbon_Dating, Ownership_Verify)
root.order.add_edge(Ownership_Verify, Historical_Match)
root.order.add_edge(Historical_Match, Customs_Clearance)
root.order.add_edge(Customs_Clearance, Risk_Assessment)
root.order.add_edge(Risk_Assessment, Ethics_Approval)
root.order.add_edge(Ethics_Approval, Restoration_Plan)
root.order.add_edge(Restoration_Plan, Final_Approval)
root.order.add_edge(Final_Approval, Catalog_Entry)
root.order.add_edge(Catalog_Entry, Exhibit_Preparation)

print(root)