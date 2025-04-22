project_steps_texts = [
    {
        "title": "Overview",
        "content": """**Become a Circuit Detective: Identify and Fix a Faulty Circuit**

**Project Objectives:**
- Apply Kirchhoff’s Junction and Loop Rules to analyze a multiloop circuit.
- Identify inconsistencies between measured and calculated values.
- Propose corrections to make the circuit physically and mathematically consistent.
- Practice clear diagramming and algebraic reasoning in circuit analysis.
"""
    },
    {
        "title": "Part 1: Analyzing the Given Circuit (25%)",
        "content": """**Task 1:**
- Study the provided circuit diagram, which includes:
  - A battery (\( V = 12~\\text{V} \))
  - Three resistors: \( R_1 = 3~\\Omega \), \( R_2 = 4~\\Omega \), \( R_3 = 6~\\Omega \)
  - Marked current values in each branch (e.g., “Current through \( R_2 \) = 1.5 A”)

**Diagram Note:** You will be given this circuit in class or through your course site.

**Guiding Questions:**
- Are the junction and loop equations consistent with the given numbers?
- Is total energy conserved around each loop?
"""
    },
    {
        "title": "Part 2: Applying Kirchhoff’s Rules (25%)",
        "content": """**Task 2:**
- Write out Kirchhoff’s **Loop Rule** for both loops in the circuit.
  - Loop A: includes \( R_1 \) and \( R_2 \)
  - Loop B: includes \( R_1 \) and \( R_3 \)

- Write Kirchhoff’s **Junction Rule** for the node where current splits.

**Equations:**
\[
\\sum V = 0 \\quad (\\text{around each loop})
\\]
\[
I_{\\text{in}} = I_{\\text{out}} \\quad (\\text{at each junction})
\]

**Guiding Questions:**
- Do the current values satisfy conservation at the junction?
- Does the battery voltage balance the sum of voltage drops?
"""
    },
    {
        "title": "Part 3: Identifying the Faults (25%)",
        "content": """**Task 3:**
- Compare your calculated current and voltage values with those provided.
- Determine which resistor values or current labels are inconsistent.

**Analysis Task:**
- Show your corrected calculations and highlight mismatches.
- Suggest which value (or values) are likely incorrect and explain why.

**Guiding Questions:**
- Could the battery be underperforming?
- Are the resistors mislabeled or is the diagram incomplete?
"""
    },
    {
        "title": "Part 4: Propose a Corrected Circuit (15%)",
        "content": """**Task 4:**
- Redraw the circuit with corrected values that satisfy all laws.
- Recalculate all currents and voltages to verify that your version works.

**Optional Extension:**
- Add a fourth resistor to create a second loop, and analyze how it affects the original current paths.

**Guiding Questions:**
- How does your corrected circuit restore conservation laws?
- Could there be more than one “fix”? Justify your choices.
"""
    },
    {
        "title": "Part 5: Synthesis & Reflection (10%)",
        "content": """**Task 5:**
- Summarize what you discovered and fixed in the original circuit.
- Reflect: How does careful analysis reveal hidden flaws in electrical designs?

**Bonus Consideration:**
- Why is real-world circuit analysis often more complicated than textbook examples?
"""
    }
]