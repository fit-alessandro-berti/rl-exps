import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
artifact_intake = Transition(label='Artifact Intake')
visual_inspection = Transition(label='Visual Inspection')
material_testing = Transition(label='Material Testing')
radiocarbon_dating = Transition(label='Radiocarbon Dating')
provenance_check = Transition(label='Provenance Check')
archive_research = Transition(label='Archive Research')
expert_review = Transition(label='Expert Review')
style_analysis = Transition(label='Style Analysis')
craftsmanship_eval = Transition(label='Craftsmanship Eval')
condition_check = Transition(label='Condition Check')
restoration_plan = Transition(label='Restoration Plan')
forger_risk = Transition(label='Forgery Risk')
legal_review = Transition(label='Legal Review')
report_drafting = Transition(label='Report Drafting')
catalog_entry = Transition(label='Catalog Entry')

# Define the partial order
partial_order = StrictPartialOrder(
    nodes=[
        artifact_intake,
        visual_inspection,
        material_testing,
        radiocarbon_dating,
        provenance_check,
        archive_research,
        expert_review,
        style_analysis,
        craftsmanship_eval,
        condition_check,
        restoration_plan,
        forger_risk,
        legal_review,
        report_drafting,
        catalog_entry
    ],
    order=[
        (artifact_intake, visual_inspection),
        (artifact_intake, material_testing),
        (artifact_intake, provenance_check),
        (material_testing, radiocarbon_dating),
        (provenance_check, archive_research),
        (archive_research, expert_review),
        (expert_review, style_analysis),
        (expert_review, craftsmanship_eval),
        (condition_check, restoration_plan),
        (forger_risk, legal_review),
        (legal_review, report_drafting),
        (report_drafting, catalog_entry)
    ]
)

# Define the POWL model
root = OperatorPOWL(
    operator=Operator.XOR,
    children=[
        partial_order,
        OperatorPOWL(
            operator=Operator.LOOP,
            children=[
                artifact_intake,
                OperatorPOWL(
                    operator=Operator.XOR,
                    children=[
                        OperatorPOWL(
                            operator=Operator.LOOP,
                            children=[
                                material_testing,
                                radiocarbon_dating,
                                provenance_check,
                                archive_research
                            ]
                        ),
                        OperatorPOWL(
                            operator=Operator.LOOP,
                            children=[
                                expert_review,
                                style_analysis,
                                craftsmanship_eval
                            ]
                        )
                    ]
                ),
                OperatorPOWL(
                    operator=Operator.LOOP,
                    children=[
                        condition_check,
                        restoration_plan
                    ]
                ),
                OperatorPOWL(
                    operator=Operator.LOOP,
                    children=[
                        forger_risk,
                        legal_review
                    ]
                ),
                OperatorPOWL(
                    operator=Operator.LOOP,
                    children=[
                        report_drafting,
                        catalog_entry
                    ]
                )
            ]
        )
    ]
)

print(root)