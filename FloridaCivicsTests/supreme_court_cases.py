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
    # Foundations / Judicial power / Structure
    "Which Supreme Court case established judicial review (the power to strike down unconstitutional laws)?",
    "Which Supreme Court case held that the Supreme Court may review state court decisions involving federal law?",
    "Which Supreme Court case strengthened the Contracts Clause by limiting state interference with private contracts?",
    "Which Supreme Court case established broad federal power via implied powers and affirmed federal supremacy over states?",
    "Which Supreme Court case limited the power of states to tax federal institutions (federal supremacy in taxation)?",
    "Which Supreme Court case prohibited states from interfering with interstate commerce and expanded the Commerce Clause early on?",
    "Which Supreme Court case held that federal law is supreme over state law and state courts must follow it?",
    "Which Supreme Court case established that the federal government can sue a state (state sovereignty limited by the Constitution)?",
    "Which Supreme Court case established that the Bill of Rights initially applied only to the federal government (before incorporation)?",

    # Slavery / Reconstruction / Race
    "Which Supreme Court case ruled that enslaved people were property and not citizens and that Congress could not ban slavery in the territories?",
    "Which Supreme Court case upheld the doctrine of 'separate but equal'?",
    "Which Supreme Court case ended racial segregation in public schools?",
    "Which Supreme Court case upheld federal power to enforce civil rights against private discrimination in public accommodations?",
    "Which Supreme Court case held that state-imposed school segregation must be eliminated 'with all deliberate speed'?",
    "Which Supreme Court case upheld the internment of Japanese Americans during World War II?",
    "Which Supreme Court case rejected 'separate but equal' in higher education as unequal in practice?",
    "Which Supreme Court case enforced desegregation orders over state resistance (Little Rock crisis context)?",
    "Which Supreme Court case addressed affirmative action and held racial quotas unconstitutional but allowed race as one factor (classic landmark framing)?",
    "Which Supreme Court case limited affirmative action by requiring strict scrutiny for racial classifications by the federal government?",
    "Which Supreme Court case held that race-based districting can violate equal protection (racial gerrymandering)?",

    # Speech / Press / Assembly
    "Which Supreme Court case established the 'clear and present danger' test for limits on speech?",
    "Which Supreme Court case protected symbolic speech (like wearing an armband) for students in school if not substantially disruptive?",
    "Which Supreme Court case held that students can be disciplined for lewd or vulgar speech at school events?",
    "Which Supreme Court case allowed schools to regulate school-sponsored student publications (like a school newspaper)?",
    "Which Supreme Court case protected flag burning as symbolic speech under the First Amendment?",
    "Which Supreme Court case held that the government generally cannot censor the press through prior restraint (Pentagon Papers case)?",
    "Which Supreme Court case established the 'actual malice' standard for defamation suits by public officials?",
    "Which Supreme Court case protected the right to publish materials even if offensive, limiting obscenity prosecutions (modern obscenity test case)?",
    "Which Supreme Court case held that burning a draft card was not protected speech when it interferes with government interests?",
    "Which Supreme Court case held that corporations and unions have First Amendment protection for independent political expenditures?",
    "Which Supreme Court case upheld a state's right-to-work type restrictions on union agency fees for public employees (public-sector union fees case)?",

    # Religion
    "Which Supreme Court case held that school-sponsored prayer in public schools is unconstitutional?",
    "Which Supreme Court case established the Lemon test for government action concerning religion (Establishment Clause)?",
    "Which Supreme Court case upheld a neutral school voucher program that included religious schools (aid-to-religion context)?",
    "Which Supreme Court case held that Amish families could withdraw children from compulsory schooling beyond 8th grade for religious reasons?",

    # Criminal procedure / Rights of the accused
    "Which Supreme Court case applied the exclusionary rule to the states (illegally obtained evidence excluded from trial)?",
    "Which Supreme Court case required police to inform suspects of their rights before custodial interrogation?",
    "Which Supreme Court case guaranteed the right to an attorney for indigent defendants in state felony cases?",
    "Which Supreme Court case required counsel for juveniles in delinquency proceedings (due process for juveniles)?",
    "Which Supreme Court case required states to provide transcripts to indigent defendants for appeals (equal justice in appeals)?",
    "Which Supreme Court case established that a suspect has a right to an attorney during police interrogation once requested?",
    "Which Supreme Court case required police to obtain a warrant for most searches and seizures (strong warrant preference case)?",
    "Which Supreme Court case held that students have reduced privacy rights at school and allowed reasonable searches by school officials?",
    "Which Supreme Court case established the standard for police to stop-and-frisk based on reasonable suspicion?",
    "Which Supreme Court case required that confessions be voluntary and established due process limits on coerced confessions?",
    "Which Supreme Court case extended the exclusionary rule by applying it to evidence discovered through unconstitutional searches (incorporation era framing)?",

    # Privacy / Substantive due process
    "Which Supreme Court case established a constitutional right to privacy in marital contraception?",
    "Which Supreme Court case extended privacy rights to contraception for unmarried people?",
    "Which Supreme Court case extended the right to privacy to abortion decisions (historic landmark framing)?",
    "Which Supreme Court case reaffirmed core abortion protections while allowing some state regulation (undue burden standard case)?",
    "Which Supreme Court case struck down bans on interracial marriage?",
    "Which Supreme Court case invalidated sodomy laws and protected intimate adult relationships (privacy/liberty case)?",
    "Which Supreme Court case held that same-sex couples have a constitutional right to marry?",
    "Which Supreme Court case upheld mandatory vaccination laws as a valid use of state police power (public health power case)?",

    # Federalism / Commerce / Economic regulation
    "Which Supreme Court case upheld broad federal power to regulate local activities affecting interstate commerce (Wickard principle)?",
    "Which Supreme Court case allowed Congress to regulate discrimination by hotels and places affecting interstate commerce?",
    "Which Supreme Court case allowed Congress to regulate discrimination by restaurants under the Commerce Clause?",
    "Which Supreme Court case limited Congress’s Commerce Clause power by striking down the Gun-Free School Zones Act?",
    "Which Supreme Court case limited Congress’s Commerce Clause power regarding violence against women legislation?",
    "Which Supreme Court case upheld New Deal-era minimum wage laws and shifted away from strict freedom-of-contract doctrine?",
    "Which Supreme Court case upheld economic regulation and marked the decline of Lochner-era scrutiny (rational basis era marker)?",
    "Which Supreme Court case struck down early federal income tax as unconstitutional prior to the 16th Amendment (historic tax case)?",

    # Elections / Representation / Political process
    "Which Supreme Court case held that redistricting/apportionment disputes are justiciable (courts can hear them)?",
    "Which Supreme Court case established 'one person, one vote' for state legislative districts?",
    "Which Supreme Court case allowed limits on some campaign contributions as constitutional (campaign finance landmark)?",
    "Which Supreme Court case resolved the 2000 presidential election recount dispute in Florida?",
    "Which Supreme Court case held that partisan gerrymandering claims present political questions not suitable for federal courts?",
    "Which Supreme Court case strengthened the Voting Rights Act by requiring certain jurisdictions to obtain federal approval before changing voting laws (classic VRA case)?",

    # Separation of powers / Executive power
    "Which Supreme Court case held that the president can remove executive officials and strengthened executive control (early separation of powers case)?",
    "Which Supreme Court case limited executive privilege and required President Nixon to turn over the Watergate tapes?",
    "Which Supreme Court case held that military tribunals for civilians are unconstitutional when civilian courts are open?",
    "Which Supreme Court case held that the president has some immunity for official acts (executive power landmark framing)?",

    # Second Amendment
    "Which Supreme Court case held that the Second Amendment protects an individual right to possess a firearm for self-defense in the home?",
    "Which Supreme Court case incorporated the Second Amendment against the states through the Fourteenth Amendment?",

    # Due process / Equality / Modern civil liberties (often tested)
    "Which Supreme Court case required states to provide equal protection in public education for undocumented children (school access case)?",
    "Which Supreme Court case upheld school desegregation busing as a remedy (busing case)?",
    "Which Supreme Court case limited school busing across district lines absent proof of inter-district violation (desegregation limits case)?",
    "Which Supreme Court case held that police generally need a warrant to search digital information on a cell phone seized during arrest?",
]

answers = [
    # Foundations / Judicial power / Structure
    "Marbury v. Madison (1803)",
    "Martin v. Hunter's Lessee (1816)",
    "Dartmouth College v. Woodward (1819)",
    "McCulloch v. Maryland (1819)",
    "McCulloch v. Maryland (1819)",
    "Gibbons v. Ogden (1824)",
    "Cooper v. Aaron (1958)",
    "Chisholm v. Georgia (1793)",
    "Barron v. Baltimore (1833)",

    # Slavery / Reconstruction / Race
    "Dred Scott v. Sandford (1857)",
    "Plessy v. Ferguson (1896)",
    "Brown v. Board of Education (1954)",
    "Heart of Atlanta Motel, Inc. v. United States (1964)",
    "Brown v. Board of Education II (1955)",
    "Korematsu v. United States (1944)",
    "Sweatt v. Painter (1950)",
    "Cooper v. Aaron (1958)",
    "Regents of the University of California v. Bakke (1978)",
    "Adarand Constructors, Inc. v. Peña (1995)",
    "Shaw v. Reno (1993)",

    # Speech / Press / Assembly
    "Schenck v. United States (1919)",
    "Tinker v. Des Moines Independent Community School District (1969)",
    "Bethel School District No. 403 v. Fraser (1986)",
    "Hazelwood School District v. Kuhlmeier (1988)",
    "Texas v. Johnson (1989)",
    "New York Times Co. v. United States (1971)",
    "New York Times Co. v. Sullivan (1964)",
    "Miller v. California (1973)",
    "United States v. O'Brien (1968)",
    "Citizens United v. Federal Election Commission (2010)",
    "Janus v. AFSCME (2018)",

    # Religion
    "Engel v. Vitale (1962)",
    "Lemon v. Kurtzman (1971)",
    "Zelman v. Simmons-Harris (2002)",
    "Wisconsin v. Yoder (1972)",

    # Criminal procedure / Rights of the accused
    "Mapp v. Ohio (1961)",
    "Miranda v. Arizona (1966)",
    "Gideon v. Wainwright (1963)",
    "In re Gault (1967)",
    "Griffin v. Illinois (1956)",
    "Edwards v. Arizona (1981)",
    "Katz v. United States (1967)",
    "New Jersey v. T.L.O. (1985)",
    "Terry v. Ohio (1968)",
    "Brown v. Mississippi (1936)",
    "Weeks v. United States (1914)",

    # Privacy / Substantive due process
    "Griswold v. Connecticut (1965)",
    "Eisenstadt v. Baird (1972)",
    "Roe v. Wade (1973)",
    "Planned Parenthood v. Casey (1992)",
    "Loving v. Virginia (1967)",
    "Lawrence v. Texas (2003)",
    "Obergefell v. Hodges (2015)",
    "Jacobson v. Massachusetts (1905)",

    # Federalism / Commerce / Economic regulation
    "Wickard v. Filburn (1942)",
    "Heart of Atlanta Motel, Inc. v. United States (1964)",
    "Katzenbach v. McClung (1964)",
    "United States v. Lopez (1995)",
    "United States v. Morrison (2000)",
    "West Coast Hotel Co. v. Parrish (1937)",
    "United States v. Carolene Products Co. (1938)",
    "Pollock v. Farmers' Loan & Trust Co. (1895)",

    # Elections / Representation / Political process
    "Baker v. Carr (1962)",
    "Reynolds v. Sims (1964)",
    "Buckley v. Valeo (1976)",
    "Bush v. Gore (2000)",
    "Rucho v. Common Cause (2019)",
    "South Carolina v. Katzenbach (1966)",

    # Separation of powers / Executive power
    "Myers v. United States (1926)",
    "United States v. Nixon (1974)",
    "Ex parte Milligan (1866)",
    "Nixon v. Fitzgerald (1982)",

    # Second Amendment
    "District of Columbia v. Heller (2008)",
    "McDonald v. Chicago (2010)",

    # Due process / Equality / Modern civil liberties
    "Plyler v. Doe (1982)",
    "Swann v. Charlotte-Mecklenburg Board of Education (1971)",
    "Milliken v. Bradley (1974)",
    "Riley v. California (2014)",
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
        self.dialog.title("Quiz Setup")
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
        self.root.title("FCLE Supreme Court Quiz")
        self.root.geometry("700x500")

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
