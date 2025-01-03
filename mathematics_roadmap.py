import streamlit as st
from mathematics_roadmap import create_math_roadmap, draw_math_roadmap

st.set_page_config(layout="wide", page_title="Mathematics Learning Roadmap")

st.title("Mathematics Learning Roadmap")

# Create and display the graph
G = create_math_roadmap()
fig = draw_math_roadmap(G)

# Display the plot in Streamlit
st.pyplot(fig)

# Add book recommendations section
st.header("Book Recommendations by Subject")

# Get all subjects sorted by name
subjects_sorted = sorted(G.nodes(data=True), key=lambda x: x[1]['name'])

# Create tabs for different categories
categories = ["All", "Essential", "Recommended", "Optional"]
tabs = st.tabs(categories)

for tab, category in zip(tabs, categories):
    with tab:
        for node_id, data in subjects_sorted:
            if category == "All" or data['category'] == category.lower():
                if data['books']:  # Only show subjects with books
                    st.subheader(data['name'])
                    for book in data['books']:
                        st.markdown(f"- {book}")
                    st.markdown("---")

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List

# [Previous class definitions for Book and Subject]
# [Previous COLORS and BORDERS definitions]
# [Previous subjects and connections definitions]

def create_math_roadmap():
    G = nx.DiGraph()
    
    # Add nodes
    for subject_id, subject in subjects.items():
        G.add_node(subject_id,
                  name=subject.name,
                  category=subject.category,
                  books=[f"{b.title} by {b.author}" for b in subject.books])
    
    # Add edges
    for start, end in connections:
        G.add_edge(start, end)
        
    return G

def draw_math_roadmap(G):
    # Create a new figure
    fig, ax = plt.subplots(figsize=(24, 18))
    
    # Use kamada_kawai_layout for better node placement
    pos = nx.kamada_kawai_layout(G)
    
    # Draw nodes by category
    for category in ["essential", "recommended", "optional"]:
        nodelist = [n for n,attr in G.nodes(data=True) if attr["category"] == category]
        nx.draw_networkx_nodes(G, pos,
                             nodelist=nodelist,
                             node_color=COLORS[category],
                             edgecolors=BORDERS[category],
                             node_size=3000,
                             ax=ax)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, 
                          edge_color='gray',
                          arrows=True,
                          arrowsize=20,
                          width=1.5,
                          ax=ax)
    
    # Add labels
    labels = {n: G.nodes[n]["name"] for n in G.nodes()}
    nx.draw_networkx_labels(G, pos,
                          labels,
                          font_size=8,
                          ax=ax)
    
    plt.title("Mathematics Learning Roadmap", fontsize=16, pad=20)
    plt.axis('off')
    plt.tight_layout()
    
    return fig

if __name__ == "__main__":
    # This will only run if the file is run directly (not imported)
    G = create_math_roadmap()
    plt = draw_math_roadmap(G)
    plt.show()

# Python
__pycache__/
*.py[cod]
*$py.class
.env
.venv
env/
venv/
ENV/

# Streamlit
.streamlit/secrets.toml

# IDEs
.idea/
.vscode/
*.swp
*.swo
from typing import Dict, List
import networkx as nx
import matplotlib.pyplot as plt

class Book:
    def __init__(self, title: str, author: str, category: str):
        self.title = title
        self.author = author 
        self.category = category

class Subject:
    def __init__(self, name: str, category: str, books: List[Book]):
        self.name = name
        self.category = category
        self.books = books

COLORS = {
    "essential": "#dae8fc",
    "recommended": "#e1d5e7",
    "optional": "#fff2cc"
}

BORDERS = {
    "essential": "#6c8ebf", 
    "recommended": "#9673a6",
    "optional": "#d6b656"
}
subjects = {
    "Start1": Subject("Start Philosophy", "recommended", []),
    "Start2": Subject("Start Mathematics", "essential", []),
    
    "IntroPhilosophy": Subject("Introduction to Philosophy", "recommended", [
        Book("Think: A Compelling Introduction to Philosophy", "Simon Blackburn", "recommended"),
        Book("Philosophy: A Text with Readings", "Manuel Velasquez", "recommended"),
        Book("Thinking It Through: An Introduction to Contemporary Philosophy", "Kwame Appiah", "recommended")
    ]),
    
    "IntroLogic": Subject("Introduction to Logic", "recommended", [
        Book("The Power of Logic", "Frances Howard-Snyder, Daniel Howard-Snyder, Ryan Wasserman", "recommended"),
        Book("A Concise Introduction to Logic", "Patrick J. Hurley", "recommended")
    ]),
    
    "ProblemSolving": Subject("Problem Solving", "recommended", [
        Book("How to Solve It", "G. Polya", "recommended"),
        Book("Solving Mathematical Problems", "Terence Tao", "recommended"),
        Book("Mathematical Discovery", "George Polya", "recommended"),
        Book("How to Solve Mathematical Problems", "Wayne Wickelgren", "recommended")
    ]),

    "PhilosophyLanguage": Subject("Philosophy of Language", "recommended", [
        Book("Philosophy of Language", "Alexander Miller", "recommended"),
        Book("Philosophy of Language", "William G. Lycan", "recommended"),
        Book("An Introduction to Philosophy of Language", "Michael Morris", "recommended"),
        Book("Philosophy of Language: An Introduction", "Chris Daly", "recommended")
    ]),

    "PhilosophyMath": Subject("Philosophy of Mathematics and Logic", "recommended", [
        Book("Introduction to Logic and Methodology", "Alfred Tarski", "recommended"),
        Book("Introduction to Mathematical Philosophy", "Bertrand Russell", "recommended"),
        Book("Mathematical Thought", "Evert W. Beth", "recommended"),
        Book("On the Philosophy of Logic", "Jennifer Fisher", "recommended"),
        Book("Philosophy of Logics", "Susan Haack", "recommended"),
        Book("Philosophy of Mathematics", "James Robert Brown", "recommended"),
        Book("The Foundations of Arithmetic", "Gottlob Frege", "recommended"),
        Book("The Concept of Logical Consequence", "John Etchemendy", "recommended"),
        Book("The Concept of Logical Consequence: An Introduction", "Matthew W. McKeon", "recommended")
    ])
}
subjects.update({
    "Precalculus": Subject("Precalculus", "essential", [
        Book("Precalculus: Mathematics for Calculus", "Stewart, Redlin, Watson", "essential"),
        Book("Precalculus", "Michael Sullivan", "essential")
    ]),
    
    "Calculus": Subject("Calculus", "essential", [
        Book("Calculus: Early Transcendentals", "James Stewart", "essential"),
        Book("Thomas' Calculus", "George B. Thomas Jr.", "essential"),
        Book("Infinite Powers", "Steven H. Strogatz", "recommended")
    ]),

    "Physics": Subject("Introduction to Physics", "optional", [
        Book("Physics for Scientists and Engineers with Modern Physics", "Raymond A. Serway, John W. Jewett Jr.", "optional"),
        Book("An Introduction to Physical Science", "James T. Shipman, Jerry D. Wilson, Charles A. Higgens Jr.", "optional"),
        Book("Physics for Scientists and Engineers: A Strategic Approach", "Randall D. Knight", "optional")
    ]),

    "LinearAlgebra": Subject("Introduction to Linear Algebra", "essential", [
        Book("Elementary Linear Algebra", "Howard Anton, Chris Rorres", "essential"),
        Book("Introduction to Linear Algebra", "Gilbert Strang", "essential"),
        Book("Linear Algebra and Its Applications", "Lay, Lay, McDonald", "essential")
    ]),

    "AdvancedLinearAlgebra": Subject("Advanced Linear Algebra", "essential", [
        Book("Linear Algebra Done Right", "Sheldon Axler", "essential"),
        Book("Linear Algebra", "Serge Lang", "essential"),
        Book("Finite-Dimensional Vector Spaces", "Paul R. Halmos", "essential"),
        Book("Linear Algebra Done Wrong", "Sergei Treil", "essential"),
        Book("Linear Algebra", "Georgi E. Shilov & Richard A. Silverman", "essential")
    ]),

    "ProofsDiscrete": Subject("Naive Set Theory, Mathematical Reasoning, and Discrete Mathematics", "essential", [
        Book("How to Prove It", "Daniel J. Velleman", "essential"),
        Book("Book of Proof", "Richard Hammak", "essential"),
        Book("Introduction to Mathematical Proofs", "Charles E. Roberts", "essential"),
        Book("Proofs and Fundamentals", "Ethan D. Bloch", "essential"),
        Book("Discrete Mathematics with Applications", "Susanna S. Epp", "essential"),
        Book("Discrete Mathematics and Its Applications", "Kenneth H. Rosen", "essential"),
        Book("Mathematics: A Discrete Introduction", "Edward R. Scheinerman", "essential")
    ])
})
subjects.update({
    "MathLogic": Subject("Introduction to Mathematical Logic and Model Theory", "essential", [
        Book("Mathematical Logic", "Ian Chiswell, Wilfrid Hodges", "essential"),
        Book("Propositional and Predicate Calculus", "Derek Goldrei", "essential"),
        Book("A Mathematical Introduction to Logic", "Herbert Enderton", "essential"),
        Book("A Friendly Introduction to Mathematical Logic", "Christopher C. Leary", "essential"),
        Book("A First Course in Logic", "Shawn Hedman", "essential"),
        Book("Introduction to Mathematical Logic", "Elliott Mendelson", "essential")
    ]),

    "SetTheory": Subject("Introduction to Axiomatic Set Theory", "essential", [
        Book("Classic Set Theory", "Derek Goldrei", "essential"),
        Book("Elements of Set Theory", "Herbert Enderton", "essential"),
        Book("Introduction to Set Theory", "Karel Hrbacek, Thomas Jech", "essential"),
        Book("Foundations of Set Theory", "A.A. Fraenkel, Y. Bar-Hillel, A. Levy", "essential"),
        Book("A First Course in Mathematical Logic and Set Theory", "Michael L. O'Leary", "essential")
    ]),

    "CategoryTheory": Subject("Category Theory", "essential", [
        Book("Category Theory", "Steve Awodey", "essential"),
        Book("Basic Category Theory", "Tom Leinster", "essential"),
        Book("Abstract and Concrete Categories: The Joy of Cats", "Jiri Adamek", "essential"),
        Book("Category Theory: A Gentle Introduction", "Peter Smith", "essential"),
        Book("Category Theory in Context", "Emily Riehl", "essential")
    ]),

    "UniversalAlgebra": Subject("Universal Algebra", "essential", [
        Book("Universal Algebra", "P.M. Cohn", "essential"),
        Book("A Course in Universal Algebra", "Stanley Burris, H.P. Sankappanavar", "essential"),
        Book("Universal Algebra", "G. Gratzer", "essential"),
        Book("Universal Algebra", "Clifford Bergman", "essential"),
        Book("Post-Modern Algebra", "Jonathan D. H. Smith, Anna B. Romanowska", "essential")
    ])
})
subjects.update({
    "EuclideanGeometry": Subject("Euclidean and Non-Euclidean Geometry", "essential", [
        Book("Foundations of Euclidean and Non-Euclidean Geometry", "Ellery B. Golos", "essential"),
        Book("Foundations of Geometry", "Gerard A. Venema", "essential"),
        Book("Euclidean and Non-Euclidean Geometry", "Marvin Jay Greenberg", "essential"),
        Book("Modern Geometries", "John R. Smart", "essential"),
        Book("The Four Pillars of Geometry", "John Stillwell", "essential"),
        Book("A Modern View of Geometry", "Leonard M. Blumenthal", "essential"),
        Book("Classical Geometry", "I. E. L., J. E. L., A. C. F. L., G. W. T.", "essential"),
        Book("Euclidean Geometry", "M. Solomonovich", "essential"),
        Book("Geometry", "D. A. Brannan, M. F. Esplen, J. J. Gray", "essential"),
        Book("Introduction To Non-Euclidean Geometry", "Harold E. Wolfe", "essential"),
        Book("Modern Geometry with Applications", "George A. Jennings", "essential"),
        Book("Projective Geometry", "H. S. M. Coxeter", "essential"),
        Book("Transformation Geometry", "George E. Martin", "essential"),
        Book("The Foundations of Geometry and the Non-Euclidean Plane", "George E. Martin", "essential")
    ]),

    "DifferentialGeometry": Subject("Introduction to Differential Geometry", "essential", [
        Book("A Differential Approach to Geometry", "Francis Borceux", "essential"),
        Book("Differential Geometry of Curves and Surfaces", "Kristopher Tapp", "essential"),
        Book("Differential Geometry of Curves and Surfaces", "Manfredo P. Do Carmo", "essential"),
        Book("Elementary Differential Geometry", "Barrett O'Neill", "essential"),
        Book("Elementary Differential Geometry", "Andrew Pressley", "essential")
    ]),

    "AdvancedDifferentialGeometry": Subject("Advanced Differential Geometry", "essential", [
        Book("Manifolds, Tensors and Forms", "Paul Renteln", "essential"),
        Book("An Introduction to Differentiable Manifolds and Riemannian Geometry", "William M. Boothby", "essential"),
        Book("Introduction to Smooth Manifolds", "John M. Lee", "essential"),
        Book("A Comprehensive Introduction to Differential Geometry", "Michael Spivak", "essential"),
        Book("First Steps in Differential Geometry", "Andrew Mclnerney", "essential")
    ])
})
subjects.update({
    "AlgebraicGeometry": Subject("Algebraic Geometry", "essential", [
        Book("Basic Algebraic Geometry", "Igor R. Shafarevich", "essential"),
        Book("A Royal Road to Algebraic Geometry", "Audune Holme", "essential"),
        Book("Algebraic Geometry: A First Course", "Joe Harris", "essential"),
        Book("Elementary Algebraic Geometry", "Keith Kendig", "essential"),
        Book("Introduction to Algebraic Geometry", "Justin R. Smith", "essential")
    ]),

    "AlgebraicTopology": Subject("Algebraic Topology", "essential", [
        Book("Algebraic Topology: An Introduction", "William Massey", "essential"),
        Book("Algebraic Topology", "Allen Hatcher", "essential"),
        Book("Elements of Algebraic Topology", "James Munkres", "essential"),
        Book("A First Course in Algebraic Topology", "C. Kosniowski", "essential")
    ]),

    "TopologyMotivation": Subject("Algebraic Topology Motivation", "essential", [
        Book("Invitation to Combinatorial Topology", "Maurice Frechet and Ky Fan", "essential"),
        Book("Basic Concepts of Algebraic Topology", "Fred H. Croom", "essential"),
        Book("Basic Topology", "M.A. Armstrong", "essential"),
        Book("Topology", "John G. Hocking, Gail S. Young", "essential"),
        Book("Topology", "Klaus Janich", "essential")
    ]),

    "AlgebraicGeometryMotivation": Subject("Algebraic Geometry Motivation", "essential", [
        Book("Introduction to Algebraic Geometry", "Brendan Hassett", "essential"),
        Book("Ideals Varieties and Algorithms", "David A. Cox, John Little, Donal O'Shea", "essential")
    ])
})
subjects.update({
    "RealAnalysis": Subject("Introduction to Real Analysis", "essential", [
        Book("Introduction to Real Analysis", "Robert G. Bartle, Donald R. Sherbert", "essential"),
        Book("How to Think About Analysis", "Lara Alcock", "essential"),
        Book("Introduction to Real Analysis", "William F. Trench", "essential"),
        Book("From Calculus to Analysis", "Steen Pedersen", "essential"),
        Book("Writing Proofs in Analysis", "Jonathan M. Kane", "essential")
    ]),

    "ComplexAnalysis": Subject("Introduction to Complex Analysis", "essential", [
        Book("Complex Analysis", "John M. Howie", "essential"),
        Book("Complex Analysis with Applications", "Dennis G. Zill", "essential"),
        Book("Complex Variables and Applications", "James Ward Brown, Ruel Churchill", "essential"),
        Book("Complex Variables", "Mark J. Ablowitz", "essential"),
        Book("Visual Complex Analysis", "Tristan Needham", "essential")
    ]),

    "GeneralTopology": Subject("Introduction to General Topology", "essential", [
        Book("Topology", "James Munkres", "essential"),
        Book("General Topology", "Stephen Willard", "essential"),
        Book("Topology Without Tears", "Sidney A. Morris", "essential"),
        Book("Topological Spaces", "Gerard Buskes, Arnoud van Rooij", "essential"),
        Book("Introduction to Metric and Topological Spaces", "Wilson A. Sutherland", "essential"),
        Book("First Concepts of Topology", "W. G. Chinn & N. E. Steenrod", "essential")
    ]),

    "FunctionalAnalysis": Subject("Introduction to Functional Analysis", "essential", [
        Book("Introductory Functional Analysis with Applications", "Erwin Kreyszig", "essential"),
        Book("Principles of Functional Analysis", "Martin Schechter", "essential")
    ])
})
subjects.update({
    "DifferentialEquations": Subject("Introduction to Differential Equations", "essential", [
        Book("Elementary Differential Equations and Boundary Value Problems", "William E. Boyce, Richard C. DiPrima", "essential"),
        Book("Differential Equations", "Dennis Zill, Warren Wright", "essential"),
        Book("Fundamentals of Differential Equations", "David Snider, Edward B. Saff, R. Kent Nagle", "essential")
    ]),

    "ProbabilityTheory": Subject("Probability Theory", "essential", [
        Book("A First Course in Probability Theory", "Sheldon Ross", "essential"),
        Book("Introduction to Probability", "Dimitri Berstekas, John N. Tsitsiklis", "essential"),
        Book("A Natural Introduction to Probability", "R. Meester", "essential"),
        Book("Introduction to Probability", "Joseph K. Blitzstein, Jessica Hwang", "essential")
    ]),

    "Statistics": Subject("Mathematical Statistics", "essential", [
        Book("Introduction to Mathematical Statistics", "Robert V. Hogg, Joseph W. McKean, Allen T. Craig", "essential"),
        Book("Mathematical Statistics with Applications", "Dennis D. Wackerly, William Mendenhall, Richard L. Scheaffer", "essential"),
        Book("Modern Mathematical Statistics with Applications", "Jay L. Devore, Kenneth N. Berk", "essential")
    ]),

    "AdvancedProbability": Subject("Advanced Probability Theory", "essential", [
        Book("An Introduction to Probability and Statistics", "V. K. Rohatgi, A. K. Md. E. Saleh", "essential"),
        Book("A First Look at Rigorous Probability Theory", "Jeffrey S. Rosenthal", "essential"),
        Book("A User's Guide to Measure Theoretic Probability", "David Pollard", "essential"),
        Book("Probability", "A. N. Shiryayev", "essential"),
        Book("Probability and Measure", "Patrick Billingsley", "essential"),
        Book("An Introduction to Probability Theory and Its Applications", "William Feller", "essential")
    ])
})
subjects.update({
    "NumericalAnalysis": Subject("Introduction to Numerical Analysis", "essential", [
        Book("Numerical Analysis", "Timothy Sauer", "essential"),
        Book("Numerical Analysis", "Richard Burden, Jr. Douglas Faires", "essential"),
        Book("Numerical Methods That Usually Work", "Forman S. Acton", "essential"),
        Book("An Introduction to Numerical Methods and Analysis", "James F. Epperson", "essential")
    ]),

    "OptimizationTheory": Subject("Introduction to Optimization Theory", "essential", [
        Book("A First Course in Optimization Theory", "Rangarajan K. Sundaram", "essential"),
        Book("Introduction to Linear Optimization", "Dimitris Bertsimas, John N. Tsitsiklis", "essential"),
        Book("Applied Optimization", "Ross Baldick", "essential"),
        Book("An Introduction to Optimization", "Edwin K.P. Chong, Stanislaw H. Zak", "essential"),
        Book("Practical Optimization", "Philip E. Gill, Walter Murray, Margaret H. Wright", "essential")
    ]),

    "ConvexOptimization": Subject("Convex Optimization", "essential", [
        Book("Convex Optimization Theory", "Dimitri P. Bertsekas", "essential"),
        Book("Convex Optimization", "Stephen Boyd, Lieven Vandenberghe", "essential"),
        Book("Convex Analysis and Nonlinear Optimization", "Jonathan M. Borwein, Adrian S. Lewis", "essential"),
        Book("Foundations of Optimization", "Osman Güler", "essential")
    ]),

    "ProgrammingPython": Subject("Introduction to Programming with Python", "optional", [
        Book("Head First Python", "Paul Barry", "optional"),
        Book("Think Python: How to think like a computer scientist", "Allen B. Downey", "optional"),
        Book("A Beginners Guide to Python 3 Programming", "John Hunt", "optional")
    ])
})
subjects.update({
    "AdvancedStatistics": Subject("Advanced Mathematical Statistics", "essential", [
        Book("Statistical Inference", "George Casella, Roger L. Berger", "essential"),
        Book("Mathematical Statistics: Basic Ideas and Selected Topics", "Kjell A. Doksum, Peter J. Bickel", "essential"),
        Book("Robust Statistics", "Frank R. H., Elvezio M. R., Peter J. R., Werner A. S.", "essential"),
        Book("Theory of Statistics", "Mark J. Schervish", "essential"),
        Book("All of Statistics", "Larry Wasserman", "essential"),
        Book("All of Nonparametric Statistics", "Larry Wasserman", "essential")
    ]),

    "TimeSeriesAnalysis": Subject("Time Series Analysis", "essential", [
        Book("Introduction to Time Series Analysis and Forecasting", "Douglas C. Montgomery, Cheryl L. Jennings, Murat Kulahci", "essential"),
        Book("Introduction to Time Series and Forecasting", "Peter J. Brockwell, Richard A. Davis", "essential"),
        Book("Applied Time Series Analysis", "Terence C. Mills", "essential")
    ]),

    "StochasticCalculus": Subject("Stochastic Calculus", "essential", [
        Book("Applied Stochastic Differential Equations", "Simo Särkkä, Arno Solin", "essential"),
        Book("A First Course in Stochastic Calculus", "Louis-Pierre Arguin", "essential"),
        Book("Introduction To Stochastic Calculus With Applications", "Fima C. Klebaner", "essential"),
        Book("Stochastic Calculus", "Mircea Grigoriu", "essential"),
        Book("Stochastic Calculus: An Introduction Through Theory and Exercises", "Paolo Baldi", "essential")
    ]),

    "LatticeTheory": Subject("Introduction to Lattice Theory", "essential", [
        Book("Introduction to Lattices and Order", "B.A. Davey", "essential"),
        Book("Lattices and Ordered Sets", "Steven Roman", "essential")
    ]),

    "NumberTheory": Subject("Introduction to Number Theory", "essential", [
        Book("Elementary Number Theory", "David Burton", "essential"),
        Book("Elementary Number Theory with Applications", "Thomas Koshy", "essential"),
        Book("Elementary Number Theory", "Kenneth H. Rosen", "essential")
    ]),

    "AlgebraicNumbers": Subject("Algebraic Number Theory", "essential", [
        Book("An Introduction to the Theory of Numbers", "Ivan Niven, Herbert S. Zuckerman, Hugh L. Montgomery", "essential"),
        Book("Number Fields", "Daniel A. Marcus", "essential")
    ])
})
connections = [
    # Core Philosophy Path
    ("Start1", "IntroPhilosophy"),
    ("IntroPhilosophy", "IntroLogic"),
    ("IntroLogic", "PhilosophyLanguage"),
    ("PhilosophyLanguage", "PhilosophyMath"),
    ("PhilosophyMath", "MathLogic"),

    # Core Mathematics Path
    ("Start2", "Precalculus"),
    ("Precalculus", "Calculus"),
    ("Calculus", "LinearAlgebra"),
    ("LinearAlgebra", "ProofsDiscrete"),
    ("Calculus", "Physics"),

    # Pure Mathematics Branches
    ("ProofsDiscrete", "RealAnalysis"),
    ("ProofsDiscrete", "NumberTheory"),
    ("ProofsDiscrete", "AbstractAlgebra"),
    ("RealAnalysis", "ComplexAnalysis"),
    ("RealAnalysis", "GeneralTopology"),
    ("RealAnalysis", "FunctionalAnalysis"),
    ("ComplexAnalysis", "AdvancedAnalysis"),

    # Geometry Track
    ("ProofsDiscrete", "EuclideanGeometry"),
    ("EuclideanGeometry", "DifferentialGeometry"),
    ("AbstractAlgebra", "AlgebraicGeometry"),
    ("GeneralTopology", "DifferentialGeometry"),
    ("TopologyMotivation", "AlgebraicTopology"),
    ("AlgebraicGeometryMotivation", "AlgebraicGeometry"),

    # Algebra Track
    ("LinearAlgebra", "AdvancedLinearAlgebra"),
    ("AdvancedLinearAlgebra", "AlgebraicNumbers"),
    ("NumberTheory", "AlgebraicNumbers"),

    # Logic and Foundations Track
    ("MathLogic", "SetTheory"),
    ("SetTheory", "CategoryTheory"),
    ("SetTheory", "UniversalAlgebra"),
    ("UniversalAlgebra", "CategoryTheory"),
    ("AbstractAlgebra", "UniversalAlgebra"),
    ("AbstractAlgebra", "LatticeTheory"),
    ("LatticeTheory", "CategoryTheory"),

    # Applied Mathematics Track
    ("Calculus", "DifferentialEquations"),
    ("Calculus", "ProbabilityTheory"),
    ("ProbabilityTheory", "Statistics"),
    ("Statistics", "AdvancedStatistics"),
    ("ProbabilityTheory", "StochasticCalculus"),
    ("Statistics", "TimeSeriesAnalysis"),
    ("LinearAlgebra", "NumericalAnalysis"),
    ("LinearAlgebra", "OptimizationTheory"),
    ("OptimizationTheory", "ConvexOptimization"),

    # Programming and Applications
    ("ProofsDiscrete", "ProgrammingPython"),

    # Cross Connections
    ("ComplexAnalysis", "AlgebraicGeometry"),
    ("DifferentialGeometry", "AlgebraicGeometry"),
    ("NumberTheory", "AlgebraicGeometry"),
    ("GeneralTopology", "AlgebraicGeometry"),
    ("FunctionalAnalysis", "AdvancedAnalysis"),
    
    # Bidirectional Relationships
    ("CategoryTheory", "AlgebraicGeometry"),
    ("TopologyMotivation", "GeneralTopology"),
    ("AlgebraicTopology", "AlgebraicGeometry")
]
def create_math_roadmap():
    G = nx.DiGraph()
    
    # Add nodes
    for subject_id, subject in subjects.items():
        G.add_node(subject_id,
                  name=subject.name,
                  category=subject.category,
                  books=[f"{b.title} by {b.author}" for b in subject.books])
    
    # Add edges
    for start, end in connections:
        G.add_edge(start, end)
        
    return G

def draw_math_roadmap(G):
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    plt.figure(figsize=(24,18))
    
    # Draw nodes by category
    for category in ["essential", "recommended", "optional"]:
        nodelist = [n for n,attr in G.nodes(data=True) if attr["category"] == category]
        nx.draw_networkx_nodes(G, pos,
                             nodelist=nodelist,
                             node_color=COLORS[category],
                             edgecolors=BORDERS[category],
                             node_size=3000)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, 
                          arrowsize=20, width=1.5)
    
    # Add labels
    labels = {n: G.nodes[n]["name"] for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)
    
    plt.title("Complete Mathematics Learning Roadmap", fontsize=16, pad=20)
    plt.axis('off')
    plt.tight_layout()
    
    return plt

# Create and visualize
G = create_math_roadmap()
plt = draw_math_roadmap(G)
plt.show()
