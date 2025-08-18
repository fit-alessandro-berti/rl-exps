root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Audit'),
        Transition(label='Layout Design'),
        Transition(label='System Install'),
        Transition(label='Climate Setup'),
        Transition(label='Water Testing'),
        Transition(label='Nutrient Mix'),
        Transition(label='Seed Selection'),
        Transition(label='Planting Prep'),
        Transition(label='Growth Monitor'),
        Transition(label='Pest Inspect'),
        Transition(label='Harvest Plan'),
        Transition(label='Packaging Prep'),
        Transition(label='Distribution'),
        Transition(label='Sustainability')
    ],
    order=[
        ('Site Survey', 'Structural Audit'),
        ('Structural Audit', 'Layout Design'),
        ('Layout Design', 'System Install'),
        ('System Install', 'Climate Setup'),
        ('Climate Setup', 'Water Testing'),
        ('Water Testing', 'Nutrient Mix'),
        ('Nutrient Mix', 'Seed Selection'),
        ('Seed Selection', 'Planting Prep'),
        ('Planting Prep', 'Growth Monitor'),
        ('Growth Monitor', 'Pest Inspect'),
        ('Pest Inspect', 'Harvest Plan'),
        ('Harvest Plan', 'Packaging Prep'),
        ('Packaging Prep', 'Distribution'),
        ('Distribution', 'Sustainability')
    ]
)