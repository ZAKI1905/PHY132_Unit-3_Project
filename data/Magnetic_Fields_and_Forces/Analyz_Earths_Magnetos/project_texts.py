project_steps_texts = [
    {
        "title": "Overview",
        "content": """**Analyzing Earth’s Magnetosphere and the Physics of Solar Wind Interactions**

**Project Objectives:**
- Understand the structure of Earth's magnetosphere and its interaction with the solar wind.
- Analyze the motion of charged particles in magnetic fields using algebra-based physics.
- Interpret physical quantities such as pressure, magnetic field strength, and particle velocity.
- Create diagrams and perform numerical calculations that demonstrate conceptual and mathematical understanding.
- Practice scientific reasoning by evaluating real or simulated data (e.g., from NASA or other space missions).
"""
    },
    {
        "title": "Part 1: Conceptual Overview (20%)",
        "content": """**Task 1:**
- Define the term *magnetosphere* and describe how Earth's magnetic field is generated (e.g., the role of the geodynamo in Earth's core).
- Draw a well-labeled diagram showing:
  - Earth's magnetic field lines
  - The *magnetopause*
  - The *bow shock*
  - The *Van Allen radiation belts*

**Guiding Questions:**
- What is the physical origin of Earth's magnetic field?
- Why is the magnetosphere shaped like a tear-drop rather than a sphere?
"""
    },
    {
        "title": "Part 2: Solar Wind and Magnetic Pressure (20%)",
        "content": """**Task 2:**
- Define the *solar wind*. Describe its composition (primarily protons and electrons) and typical speed (400–600 km/s).
- Explain how the solar wind interacts with Earth's magnetic field to create the magnetopause. Include a labeled diagram showing pressure balance.

**Quantitative Analysis:**
- Calculate the *magnetic pressure* using the formula:
  \[
  P_{\\text{mag}} = \\frac{B^2}{2\\mu_0}
  \]
  where:
  - \( B \\approx 25~\\text{nT} = 25 \\times 10^{-9}~\\text{T} \) (typical near the magnetopause)
  - \( \\mu_0 = 4\\pi \\times 10^{-7}~\\text{T} \\cdot \\text{m/A} \) (permeability of free space)

- Calculate the *dynamic pressure* of the solar wind using:
  \[
  P_{\\text{dyn}} = \\rho v^2
  \]
  where:
  - \( \\rho \\approx 5 \\times 10^{-21}~\\text{kg/m}^3 \) (solar wind mass density)
  - \( v \\approx 500~\\text{km/s} = 5 \\times 10^5~\\text{m/s} \)

**Guiding Questions:**
- How do the pressures \( P_{\\text{mag}} \) and \( P_{\\text{dyn}} \) determine the standoff distance of the magnetopause?
- What happens if solar wind pressure increases?
"""
    },
    {
        "title": "Part 3: Charged Particle Motion (30%)",
        "content": """**Task 3:**
- Consider a proton with speed \( v = 5 \\times 10^6~\\text{m/s} \) entering Earth's magnetic field (\( B = 3 \\times 10^{-5}~\\text{T} \)).
- Calculate its circular path radius using:
  \[
  r = \\frac{mv}{qB}
  \]
  where:
  - \( m = 1.67 \\times 10^{-27}~\\text{kg} \) (mass of a proton)
  - \( q = 1.6 \\times 10^{-19}~\\text{C} \)

- Then calculate its orbital (gyration) frequency:
  \[
  f = \\frac{v}{2\\pi r}
  \]

**Guiding Questions:**
- Why do charged particles become trapped in Earth’s magnetic field?
- Why does the proton follow a circular (or helical) path instead of changing speed?
"""
    },
    {
        "title": "Part 4: Real-World Analysis and Interpretation (20%)",
        "content": """**Task 4:**
- Repeat the same analysis for an electron with:
  - \( v \\approx 2 \\times 10^7~\\text{m/s} \)
  - \( m = 9.11 \\times 10^{-31}~\\text{kg} \)
  - \( B = 3 \\times 10^{-5}~\\text{T} \)

- Calculate the orbit radius and compare it to the proton case.

**Guiding Questions:**
- Why is the electron’s orbit much smaller?
- How does mass affect the degree of magnetic trapping?
- Would electrons spiral more tightly or loosely than protons, and why?
"""
    },
    {
        "title": "Part 5: Synthesis & Reflection (10%)",
        "content": """**Task 5:**
- Summarize your key findings. Highlight connections between your calculations and the physical concepts discussed.
- Reflect on broader questions such as:
  - How does Earth’s magnetosphere protect life from cosmic and solar radiation?
  - What would happen if Earth’s magnetic field were significantly weaker or reversed?
"""
    }
]