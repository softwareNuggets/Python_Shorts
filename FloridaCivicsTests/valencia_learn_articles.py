## Written by Scott Johnson       2026/02/09
## For the Youtube Channel: Software Nuggets
## https://www.youtube.com/c/softwareNuggets

import tkinter as tk
from tkinter import ttk, messagebox
import random

# =========================
# QUESTIONS & ANSWERS
# =========================

questions = [

    # Articles of Confederation
    "Which document created the first national government of the United States before the Constitution?",
    "Which document established a weak national government with no executive or judicial branch?",
    "Under which document did Congress lack the power to tax?",
    "Under which document did Congress lack the power to regulate interstate commerce?",
    "What major weakness of the Articles of Confederation involved changing the document?",
    "Which event exposed the weaknesses of the Articles of Confederation and led to the Constitutional Convention?",
    "Under the Articles of Confederation, how many votes did each state have in Congress?",
    "Why was the Articles of Confederation government considered weak?",

    # Article I – Legislative Branch
    "Which Article of the Constitution establishes the legislative branch?",
    "What branch of government is created in Article I?",
    "What are the two chambers of Congress created in Article I?",
    "Which chamber of Congress is based on population?",
    "Which chamber of Congress provides equal representation to each state?",
    "What is the term length for members of the House of Representatives?",
    "What is the term length for U.S. Senators?",
    "Which chamber has the power to impeach?",
    "Which chamber has the power to conduct impeachment trials?",
    "What is the minimum age requirement to serve in the House of Representatives?",
    "What is the minimum age requirement to serve in the Senate?",
    "Which clause in Article I allows Congress to make laws necessary and proper to carry out its powers?",
    "What is another name for the Necessary and Proper Clause?",
    "Which clause gives Congress the power to regulate trade between states?",
    "Which clause gives Congress the power to collect taxes?",
    "Which clause allows Congress to declare war?",
    "What are expressed (enumerated) powers?",
    "What are implied powers?",
    "What are concurrent powers?",
    "Which Article describes the process for how a bill becomes a law?",

    # Article II – Executive Branch
    "Which Article of the Constitution establishes the executive branch?",
    "What branch of government is created in Article II?",
    "What is the term length of the President?",
    "What are the qualifications to be President?",
    "Who serves as Commander in Chief according to Article II?",
    "What power allows the President to reject legislation?",
    "What is a presidential veto?",
    "What is the role of the President in making treaties?",
    "What role does the Senate play in approving presidential appointments?",
    "What is the President’s duty under the Take Care Clause?",

    # Article III – Judicial Branch
    "Which Article of the Constitution establishes the judicial branch?",
    "What branch of government is created in Article III?",
    "What is the highest court created by Article III?",
    "What is the term length for federal judges?",
    "What types of cases does the federal judiciary hear?",
    "Which Article outlines the crime of treason?",

    # Article IV – States’ Relations
    "Which Article explains the relationship between states?",
    "Which clause requires states to honor public acts, records, and court decisions of other states?",
    "Which clause ensures citizens of each state are treated equally in other states?",
    "Which clause requires states to return fugitives to the state where the crime was committed?",
    "Which Article describes the process for admitting new states?",
    "Which Article guarantees a republican form of government to each state?",

    # Article V – Amendments
    "Which Article explains the amendment process?",
    "How many methods are there to propose an amendment?",
    "How many methods are there to ratify an amendment?",
    "What fraction of Congress is required to propose an amendment?",
    "What fraction of states is required to ratify an amendment?",
    "Which Article makes the Constitution flexible?",

    # Article VI – Supremacy
    "Which Article contains the Supremacy Clause?",
    "What does the Supremacy Clause establish?",
    "Which Article requires government officials to take an oath to support the Constitution?",
    "Which Article states there is no religious test for public office?",

    # Article VII – Ratification
    "Which Article explains how the Constitution was ratified?",
    "How many states were required to ratify the Constitution?",
    "What type of conventions were used to ratify the Constitution?",

    # Checks and Balances (Article Connections)
    "Which branch can veto laws passed by Congress?",
    "Which branch can override a presidential veto?",
    "Which branch confirms presidential appointments?",
    "Which branch can declare laws unconstitutional?",
    "Which branch has the power to impeach the President?",
    "Which branch conducts impeachment trials?",
    "Which branch appoints federal judges?",

    # Federalism & Structure
    "Which system of government divides power between national and state governments?",
    "What are reserved powers?",
    "Which amendment reinforces reserved powers?",
    "What are delegated powers?",
    "What is the main purpose of separation of powers?",
    "What is the main purpose of checks and balances?",
    
    # Articles of Confederation – scenario style
    "A national economic crisis hits, but Congress can only ask states for money and many refuse. Which weakness of the Articles of Confederation is shown?",
    "Two states begin charging taxes on each other’s goods at the border, hurting trade. Under the Articles of Confederation, what power did Congress lack that would fix this?",
    "Congress wants to build a national army quickly, but states ignore requests for soldiers. Under the Articles of Confederation, why can Congress not force compliance?",
    "A small uprising of farmers threatens state courts and the national government cannot respond effectively. Which event best illustrates this problem and helped lead to the Constitution?",
    "Thirteen states must all agree to fix a major problem in the national government, but one state refuses. What Articles of Confederation rule is causing the failure?",

    # Article I (Legislative) – scenario style
    "Congress passes a law raising income taxes. Which Article gives Congress the power to levy taxes?",
    "Congress creates a new agency to enforce consumer-safety rules even though the agency is not named in the Constitution. Which clause best supports Congress creating the agency?",
    "Congress passes a law regulating activity that occurs only within one state, arguing it affects national markets. Which constitutional power is Congress using?",
    "A bill passes the House but fails in the Senate. What constitutional principle explains why passage requires approval by both chambers?",
    "The House investigates a cabinet secretary for corruption and votes to impeach. What is the Senate’s next constitutional role?",
    "A member of Congress proposes a law, but the Constitution does not list that exact power. Supporters argue the law is needed to carry out listed powers. What type of power is being claimed?",
    "Congress passes a law and the President signs it. Later, Congress tries to punish a specific person without a trial using a law. What constitutional restriction is being violated?",
    "Congress passes a law that applies only to one individual, declaring them guilty of a crime without court proceedings. What is this called?",
    "Congress passes a law requiring people to be punished for actions that were legal when committed. What constitutional restriction is violated?",
    "A representative is elected from a large state and a senator is elected from the same state. Which constitutional idea explains why their constituencies are represented differently?",

    # Article II (Executive) – scenario style
    "Congress passes a bill, but the President returns it unsigned with objections. What formal power is the President using?",
    "The President signs a treaty with another country. What must happen next for the treaty to take effect under the Constitution?",
    "The President nominates a Supreme Court justice. Which body must confirm the nominee?",
    "During a military conflict, the President orders troops into action. Which constitutional role supports the President’s authority in this situation?",
    "A President directs executive agencies to enforce environmental laws. Which constitutional duty is being carried out?",
    "A President issues an executive order that critics claim goes beyond the Constitution and laws passed by Congress. Which branch has the power to review and possibly invalidate the action?",
    "A President wants to remove a top executive official who opposes the President’s policy. Which constitutional principle supports the President’s control over the executive branch?",
    "The President is accused of using official power for personal gain. Which constitutional process can remove the President from office?",
    "A President refuses to follow a law passed by Congress that is constitutional. Which constitutional duty is being violated?",
    "A President pardons someone convicted of a federal crime. Which type of presidential power is being used?",

    # Article III (Judicial) – scenario style
    "A federal court rules that a state law violates the U.S. Constitution. Which principle allows courts to strike down unconstitutional laws?",
    "A person argues that their First Amendment rights were violated by a state law. Why can the case be heard in federal court?",
    "Congress passes a law, and soon after, the Supreme Court declares it unconstitutional. What power is the Court using?",
    "A federal judge makes unpopular rulings, but cannot easily be removed from office. What constitutional feature explains this independence?",
    "Two states dispute the location of their border. Which court is most likely to have original jurisdiction?",
    "A citizen is charged with treason for helping an enemy during war. Which Article defines treason and sets rules for convicting someone of it?",
    "A defendant argues their confession was forced by police threats. Which general constitutional principle protects against coerced confessions (due process)?",
    "A state passes a law that conflicts with a federal court ruling interpreting the Constitution. Which branch’s interpretation prevails, and why?",

    # Article IV (States & relations) – scenario style
    "A couple legally marries in State A and moves to State B. State B must recognize the marriage license from State A. Which clause requires this?",
    "A person commits a felony in State X, then flees to State Y. State X requests the person be returned to face trial. Which clause applies?",
    "A state denies citizens from other states access to its courts for the same protections its own citizens receive. Which clause is being violated?",
    "State A’s court issues a custody order. The parent moves to State B, and State B must enforce the order. Which clause requires this?",
    "Congress votes to admit a new state into the United States. Which Article describes the process for admitting new states?",
    "A state tries to replace its elected legislature with a monarchy-style ruler. Which constitutional guarantee would be violated?",
    "A hurricane devastates one state, and the national government provides aid and protection. Which Article’s ideas support cooperation among states and the federal government?",

    # Article V (Amendment process) – scenario style
    "A proposed amendment passes both the House and Senate by a two-thirds vote. What must happen next for it to become part of the Constitution?",
    "A proposed amendment is supported by many states, and two-thirds of state legislatures demand a convention. What is this step called?",
    "Thirty-eight states approve an amendment. Why is this number significant?",
    "Congress proposes an amendment, but only a simple majority of states approve it. What happens to the amendment?",
    "A citizen argues the Constitution should be easy to change like a regular law. Which Article shows the Constitution was designed to be harder to change, and how?",

    # Article VI (Supremacy, oaths, no religious test) – scenario style
    "A state law allows something that federal law prohibits. A court must decide which law controls. Which clause resolves this conflict?",
    "A state judge refuses to enforce a federal law because they personally disagree with it. Which constitutional requirement is being ignored?",
    "A state requires all elected officials to pass a test proving they follow a specific religion. Which constitutional rule is violated?",
    "A state constitution conflicts with the U.S. Constitution. Which legal authority is highest and must be followed?",
    "A state passes a law that contradicts a treaty ratified by the United States. Under the Constitution, what is the correct outcome?",

    # Article VII (Ratification) – scenario style
    "After the Constitution was written, it did not require all 13 states to approve it before taking effect. What did it require instead?",
    "A state holds a special meeting where citizens vote on whether to approve the Constitution. What is this type of meeting called?",
    "Supporters argued the Constitution should take effect once 9 states approved it. Which Article describes this rule?",

    # Checks & Balances / Separation of powers – scenario style
    "Congress passes a bill, the President vetoes it, and Congress votes again and the bill becomes law anyway. What happened?",
    "The President appoints an ambassador, but the Senate refuses to approve the appointment. What principle is being demonstrated?",
    "The Supreme Court rules that a law violates the Constitution, even though the law was popular. What principle is shown?",
    "Congress threatens to remove Supreme Court justices because it dislikes a decision. What constitutional idea protects judicial independence?",
    "A President tries to make laws without Congress by issuing executive orders that function like statutes. Which constitutional principle limits this?",
    "The House impeaches a President, but the Senate fails to reach the required vote to convict. What is the result?",
    "Congress creates a law enforcing its own interpretation of the Constitution, but the Supreme Court issues a different interpretation in a case. Which interpretation controls in that case?",

    # Federalism – scenario style
    "The federal government sets a nationwide minimum age to vote in federal elections. States must follow it. Which power relationship is this?",
    "A state sets speed limits and requires driver’s licenses. The federal government generally allows states to do this. What kind of power is this?",
    "Both the state and federal government can tax income. What kind of power is this?",
    "The national government declares war, but states also maintain National Guard units. Which constitutional system is being shown?",
]

answers = [

    # Articles of Confederation
    "Articles of Confederation",
    "Articles of Confederation",
    "Articles of Confederation",
    "Articles of Confederation",
    "Required unanimous consent of all states to amend",
    "Shays’ Rebellion",
    "One vote per state",
    "It lacked power to tax, regulate trade, and enforce laws",

    # Article I
    "Article I",
    "Legislative branch",
    "House of Representatives and Senate",
    "House of Representatives",
    "Senate",
    "2 years",
    "6 years",
    "House of Representatives",
    "Senate",
    "25 years old",
    "30 years old",
    "Necessary and Proper Clause",
    "Elastic Clause",
    "Commerce Clause",
    "Taxing and Spending Clause",
    "War Powers Clause",
    "Powers specifically listed in the Constitution",
    "Powers not specifically listed but implied by the Necessary and Proper Clause",
    "Powers shared by national and state governments",
    "Article I",

    # Article II
    "Article II",
    "Executive branch",
    "4 years",
    "35 years old, natural-born citizen, 14 years residency",
    "President",
    "Veto power",
    "The President’s rejection of a bill",
    "Negotiates treaties (approved by Senate)",
    "Senate confirms appointments by majority vote",
    "To ensure laws are faithfully executed",

    # Article III
    "Article III",
    "Judicial branch",
    "Supreme Court",
    "Life term (during good behavior)",
    "Cases involving federal law, Constitution, treaties, disputes between states",
    "Article III",

    # Article IV
    "Article IV",
    "Full Faith and Credit Clause",
    "Privileges and Immunities Clause",
    "Extradition Clause",
    "Article IV",
    "Article IV",

    # Article V
    "Article V",
    "Two",
    "Two",
    "Two-thirds of both houses of Congress",
    "Three-fourths of the states",
    "Article V",

    # Article VI
    "Article VI",
    "Federal law is the supreme law of the land",
    "Article VI",
    "Article VI",

    # Article VII
    "Article VII",
    "Nine states",
    "State ratifying conventions",

    # Checks and Balances
    "Executive branch",
    "Legislative branch",
    "Legislative branch (Senate)",
    "Judicial branch",
    "Legislative branch (House)",
    "Legislative branch (Senate)",
    "Executive branch",

    # Federalism
    "Federalism",
    "Powers kept by the states",
    "Tenth Amendment",
    "Powers given to the national government",
    "To prevent concentration of power",
    "To ensure no branch becomes too powerful",
    
    # Articles of Confederation – scenario style
    "Congress could not tax (it could only request money from states)",
    "The power to regulate interstate commerce",
    "There was no strong national executive/enforcement power (states could ignore Congress)",
    "Shays’ Rebellion",
    "Unanimous consent was required to amend the Articles",

    # Article I – scenario style
    "Article I (Taxing and Spending power)",
    "Necessary and Proper Clause (Elastic Clause)",
    "Commerce Clause",
    "Bicameralism (two-house legislature)",
    "Hold an impeachment trial and vote to convict or acquit",
    "Implied power",
    "It violates constitutional limits on Congress (due process protections)",
    "Bill of attainder",
    "Ex post facto law",
    "Great Compromise (House by population, Senate equal)",

    # Article II – scenario style
    "Veto",
    "Senate must approve by a two-thirds vote",
    "U.S. Senate",
    "Commander in Chief",
    "Take Care Clause (faithfully execute the laws)",
    "Judicial branch (courts can review constitutionality)",
    "Executive control / unitary executive principle (presidential removal power concept)",
    "Impeachment (House impeaches, Senate convicts)",
    "Take Care Clause duty is violated (failure to enforce the law)",
    "Pardon power (executive clemency)",

    # Article III – scenario style
    "Judicial review",
    "It involves a constitutional issue/federal question (federal law)",
    "Judicial review",
    "Life tenure during good behavior",
    "The U.S. Supreme Court",
    "Article III",
    "Due process (Fifth/Fourteenth Amendment principles)",
    "Judicial branch interpretation prevails (courts interpret the Constitution)",

    # Article IV – scenario style
    "Full Faith and Credit Clause",
    "Extradition Clause",
    "Privileges and Immunities Clause",
    "Full Faith and Credit Clause",
    "Article IV",
    "Guarantee Clause (republican form of government)",
    "Article IV (states’ relations/cooperation concepts)",

    # Article V – scenario style
    "Ratification by three-fourths of the states",
    "A national convention to propose amendments (constitutional convention method)",
    "It equals three-fourths of the states (required for ratification)",
    "It fails (does not become part of the Constitution)",
    "Article V; it requires supermajorities to propose and ratify amendments",

    # Article VI – scenario style
    "Supremacy Clause",
    "Oath of office requirement to support the Constitution",
    "No religious test clause",
    "The U.S. Constitution is supreme",
    "Federal treaty prevails over conflicting state law (Supremacy Clause)",

    # Article VII – scenario style
    "Ratification by 9 states",
    "State ratifying convention",
    "Article VII",

    # Checks & Balances / Separation of powers – scenario style
    "Congress overrode the veto with a two-thirds vote in both houses",
    "Checks and balances (Senate advice and consent)",
    "Judicial review / checks and balances",
    "Life tenure and separation of powers protect independence",
    "Separation of powers (lawmaking is mainly legislative)",
    "The President is acquitted and stays in office",
    "The Supreme Court’s interpretation controls in the case (judicial review)",

    # Federalism – scenario style
    "Federal supremacy / delegated national authority in elections (federal law prevails)",
    "Reserved power (state police power)",
    "Concurrent power",
    "Federalism",
]


# Ensure questions and answers align
if len(questions) != len(answers):
    raise ValueError(f"Questions ({len(questions)}) and Answers ({len(answers)}) must have same length.")

# =========================
# SETUP DIALOG
# =========================

class SetupDialog:
    def __init__(self, parent):
        self.result = None

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Quiz Setup - Articles (Origins and Purposes of Law and Government)")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()

        # Styling (ttk)
        style = ttk.Style(self.dialog)
        try:
            style.theme_use("clam")
        except:
            pass

        style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))
        style.configure("Section.TLabelframe.Label", font=("Segoe UI", 10, "bold"))
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TRadiobutton", font=("Segoe UI", 10))
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=(14, 8))

        container = ttk.Frame(self.dialog, padding=16)
        container.grid(row=0, column=0, sticky="nsew")
        self.dialog.columnconfigure(0, weight=1)
        self.dialog.rowconfigure(0, weight=1)

        ttk.Label(container, text="Quiz Setup", style="Title.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )

        # Answer options
        options_frame = ttk.LabelFrame(container, text="Answer Options", style="Section.TLabelframe", padding=12)
        options_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        options_frame.columnconfigure(0, weight=1)

        ttk.Label(options_frame, text="How many answer options?").grid(row=0, column=0, sticky="w")

        self.num_options_var = tk.IntVar(value=4)
        opt_row = ttk.Frame(options_frame)
        opt_row.grid(row=1, column=0, sticky="w", pady=(6, 0))

        for i, num in enumerate([2, 3, 4]):
            ttk.Radiobutton(opt_row, text=str(num), variable=self.num_options_var, value=num)\
                .grid(row=0, column=i, padx=(0 if i == 0 else 18, 0))

        # Randomize questions
        rand_frame = ttk.LabelFrame(container, text="Question Order", style="Section.TLabelframe", padding=12)
        rand_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        rand_frame.columnconfigure(0, weight=1)

        ttk.Label(rand_frame, text="Do you want me to randomize the questions?").grid(row=0, column=0, sticky="w")

        self.randomize_var = tk.StringVar(value="yes")
        rand_row = ttk.Frame(rand_frame)
        rand_row.grid(row=1, column=0, sticky="w", pady=(6, 0))

        ttk.Radiobutton(rand_row, text="Yes", variable=self.randomize_var, value="yes").grid(row=0, column=0)
        ttk.Radiobutton(rand_row, text="No",  variable=self.randomize_var, value="no").grid(row=0, column=1, padx=(18, 0))

        # Quiz mode
        mode_frame = ttk.LabelFrame(container, text="Quiz Mode", style="Section.TLabelframe", padding=12)
        mode_frame.grid(row=3, column=0, sticky="ew")
        mode_frame.columnconfigure(0, weight=1)

        self.quiz_mode_var = tk.StringVar(value="question_to_answer")

        ttk.Radiobutton(
            mode_frame,
            text="1 Question → Multiple Answers",
            variable=self.quiz_mode_var,
            value="question_to_answer",
        ).grid(row=0, column=0, sticky="w", pady=(0, 6))

        ttk.Radiobutton(
            mode_frame,
            text="1 Answer → Multiple Questions",
            variable=self.quiz_mode_var,
            value="answer_to_question",
        ).grid(row=1, column=0, sticky="w")

        # Buttons
        button_row = ttk.Frame(container)
        button_row.grid(row=4, column=0, sticky="e", pady=(14, 0))

        ttk.Button(button_row, text="Cancel", command=self.cancel).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(button_row, text="Start Quiz", style="Primary.TButton", command=self.ok).grid(row=0, column=1)

        # Enter = OK, Esc = Cancel
        self.dialog.bind("<Return>", lambda e: self.ok())
        self.dialog.bind("<Escape>", lambda e: self.cancel())

        # Size + center
        self.dialog.update_idletasks()
        w, h = 480, 480
        x = (self.dialog.winfo_screenwidth() // 2) - (w // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (h // 2)
        self.dialog.geometry(f"{w}x{h}+{x}+{y}")

        self.dialog.protocol("WM_DELETE_WINDOW", self.cancel)

    def ok(self):
        self.result = {
            "num_options": self.num_options_var.get(),
            "quiz_mode": self.quiz_mode_var.get(),
            "randomize_questions": (self.randomize_var.get() == "yes"),
        }
        self.dialog.destroy()

    def cancel(self):
        self.result = None
        self.dialog.destroy()

# =========================
# MAIN QUIZ APP
# =========================

class FCLEQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FCLE Origins and Purposes of Law and Government, \"Articles\"")
        self.root.geometry("750x650")

        # Get setup configuration
        setup = SetupDialog(root)
        self.root.wait_window(setup.dialog)

        if setup.result is None:
            self.root.destroy()
            return

        self.num_options = setup.result["num_options"]
        self.quiz_mode = setup.result["quiz_mode"]
        self.randomize_questions = setup.result["randomize_questions"]

        # Initialize statistics
        self.total_questions = len(questions)
        self.questions_asked = 0
        self.correct_count = 0
        self.wrong_count = 0

        # Create question pool (indices)
        self.question_pool = list(range(len(questions)))
        if self.randomize_questions:
            random.shuffle(self.question_pool)
        self.current_pool_index = 0

        # Track if current question is answered
        self.answered = False

        # Build UI
        self.build_ui()
        self.load_question()

    def build_ui(self):
        # Status bar at top
        self.status_frame = tk.Frame(self.root, bg="lightgray", height=50)
        self.status_frame.pack(fill=tk.X, padx=10, pady=5)

        self.status_label = tk.Label(
            self.status_frame,
            text="",
            font=("Arial", 12, "bold"),
            bg="lightgray"
        )
        self.status_label.pack(pady=10)
        self.update_status()

        # Question/Answer display area
        self.prompt_label = tk.Label(
            self.root,
            text="",
            wraplength=650,
            font=("Arial", 14, "bold"),
            justify=tk.LEFT
        )
        self.prompt_label.pack(pady=20)

        # Answer buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.buttons = []
        for i in range(self.num_options):
            btn = tk.Button(
                self.button_frame,
                text="",
                width=60,
                wraplength=500,
                font=("Arial", 11),
                command=lambda i=i: self.check_answer(i)
            )
            btn.pack(pady=5)
            self.buttons.append(btn)

        # Feedback label
        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            wraplength=650
        )
        self.feedback_label.pack(pady=10)

        # Control buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        self.next_button = tk.Button(
            control_frame,
            text="Next Question",
            command=self.next_question,
            font=("Arial", 11),
            bg="blue",
            fg="white"
        )
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.restart_button = tk.Button(
            control_frame,
            text="Restart Quiz",
            command=self.restart_quiz,
            font=("Arial", 11),
            bg="orange",
            fg="white"
        )
        self.restart_button.pack(side=tk.LEFT, padx=5)

    def update_status(self):
        status_text = (
            f"Total Questions: {self.total_questions}  |  "
            f"Asked: {self.questions_asked}  |  "
            f"Correct: {self.correct_count}  |  "
            f"Wrong: {self.wrong_count}"
        )
        self.status_label.config(text=status_text)

    def load_question(self):
        # Check if all questions have been asked
        if self.current_pool_index >= len(self.question_pool):
            messagebox.showinfo(
                "Quiz Complete",
                f"You've completed all {self.total_questions} questions!\n\n"
                f"Correct: {self.correct_count}\n"
                f"Wrong: {self.wrong_count}\n"
                f"Score: {self.correct_count}/{self.total_questions} "
                f"({100 * self.correct_count // self.total_questions}%)"
            )
            self.restart_quiz()
            return

        self.answered = False
        self.feedback_label.config(text="")

        # Get current question index
        question_idx = self.question_pool[self.current_pool_index]

        if self.quiz_mode == "question_to_answer":
            # Mode: Show question, choose from answers
            self.prompt_label.config(text=f"Question: {questions[question_idx]}")
            self.correct_answer = answers[question_idx]

            # Build answer choices
            choices = [self.correct_answer]
            all_answers = list(set(answers))
            wrong_answers = [a for a in all_answers if a != self.correct_answer]

            if len(wrong_answers) < self.num_options - 1:
                messagebox.showerror("Error", "Not enough unique answers for this configuration")
                return

            choices += random.sample(wrong_answers, self.num_options - 1)
            random.shuffle(choices)
            self.current_choices = choices

        else:
            # Mode: Show answer, choose from questions
            self.prompt_label.config(text=f"Case: {answers[question_idx]}")
            self.correct_answer = questions[question_idx]

            choices = [self.correct_answer]
            wrong_questions = [questions[i] for i in range(len(questions)) if i != question_idx]

            if len(wrong_questions) < self.num_options - 1:
                messagebox.showerror("Error", "Not enough unique questions for this configuration")
                return

            choices += random.sample(wrong_questions, self.num_options - 1)
            random.shuffle(choices)
            self.current_choices = choices

        # Update button texts and reset colors
        for i, btn in enumerate(self.buttons):
            btn.config(text=self.current_choices[i], bg="SystemButtonFace", state=tk.NORMAL)

    def check_answer(self, index):
        if self.answered:
            return

        self.answered = True
        self.questions_asked += 1

        if self.current_choices[index] == self.correct_answer:
            self.correct_count += 1
            self.feedback_label.config(text="✅ Correct!", fg="green")
            self.buttons[index].config(bg="light green")
        else:
            self.wrong_count += 1
            self.feedback_label.config(
                text=f"❌ Incorrect. Correct answer:\n{self.correct_answer}",
                fg="red"
            )
            self.buttons[index].config(bg="salmon")

            for i, choice in enumerate(self.current_choices):
                if choice == self.correct_answer:
                    self.buttons[i].config(bg="light green")

        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

        self.update_status()

    def next_question(self):
        if not self.answered:
            messagebox.showwarning("Please Answer", "Please select an answer before moving to the next question.")
            return

        self.current_pool_index += 1
        self.load_question()

    def restart_quiz(self):
        self.questions_asked = 0
        self.correct_count = 0
        self.wrong_count = 0

        self.question_pool = list(range(len(questions)))
        if self.randomize_questions:
            random.shuffle(self.question_pool)
        self.current_pool_index = 0

        self.update_status()
        self.load_question()

# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    root = tk.Tk()
    app = FCLEQuizApp(root)
    root.mainloop()
