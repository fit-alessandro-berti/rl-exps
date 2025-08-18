import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
provenance_research = Transition(label='Provenance Research')
scientific_testing = Transition(label='Scientific Testing')
radiocarbon_dating = Transition(label='Radiocarbon Dating')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
legal_clearance = Transition(label='Legal Clearance')
heritage_compliance = Transition(label='Heritage Compliance')
digital_archiving = Transition(label='Digital Archiving')
expert_review = Transition(label='Expert Review')
committee_vote = Transition(label='Committee Vote')
acquisition_approval = Transition(label='Acquisition Approval')
conservation_plan = Transition(label='Conservation Plan')
storage_setup = Transition(label='Storage Setup')
stakeholder_update = Transition(label='Stakeholder Update')

# Define silent transitions
skip = SilentTransition()

# Define sub-workflows
provenance_workflow = StrictPartialOrder(nodes=[provenance_research, skip])
legal_workflow = StrictPartialOrder(nodes=[legal_clearance, skip])
heritage_workflow = StrictPartialOrder(nodes=[heritage_compliance, skip])
digital_workflow = StrictPartialOrder(nodes=[digital_archiving, skip])
expert_workflow = StrictPartialOrder(nodes=[expert_review, committee_vote])

# Define the main workflow
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    provenance_workflow,
    scientific_testing,
    radiocarbon_dating,
    spectroscopy_scan,
    legal_workflow,
    heritage_workflow,
    digital_workflow,
    expert_workflow,
    acquisition_approval,
    conservation_plan,
    storage_setup,
    stakeholder_update
])

# Define dependencies between nodes
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, provenance_workflow)
root.order.add_edge(provenance_workflow, scientific_testing)
root.order.add_edge(scientific_testing, radiocarbon_dating)
root.order.add_edge(scientific_testing, spectroscopy_scan)
root.order.add_edge(spectroscopy_scan, legal_workflow)
root.order.add_edge(legal_workflow, heritage_workflow)
root.order.add_edge(heritage_workflow, digital_workflow)
root.order.add_edge(digital_workflow, expert_workflow)
root.order.add_edge(expert_workflow, acquisition_approval)
root.order.add_edge(acquisition_approval, conservation_plan)
root.order.add_edge(conservation_plan, storage_setup)
root.order.add_edge(storage_setup, stakeholder_update)