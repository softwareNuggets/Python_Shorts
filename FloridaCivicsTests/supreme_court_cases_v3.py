## Written by Scott Johnson       2026/02/09
## For the Youtube Channel: Software Nuggets
## https://www.youtube.com/c/softwareNuggets
## Modified: Smart learning — key phrase underline, streak counter,
##           topic performance report, rich contextual hints, wrong-only practice

import tkinter as tk
from tkinter import ttk, messagebox
import random

# =========================
# QUESTIONS, ANSWERS, HINTS
# hint = one "wow" sentence that leads the student to the answer
#        WITHOUT giving the case name away.
# =========================

question_data = [

    # ── Foundations ────────────────────────────────────────────────────
    {
        "q": "Which Supreme Court case established judicial review (the power to strike down unconstitutional laws)?",
        "a": "Marbury v. Madison (1803)",
        "key": "judicial review",
        "topic": "Foundations",
        "hint": "The case arose from a political dispute over midnight appointments. Before leaving office, President John Adams appointed several Federalists to judicial positions, but incoming Secretary of State James Madison (under Jefferson) refused to deliver their commissions. William Marbury petitioned the Supreme Court to force the delivery."
    },
    {
        "q": "Which Supreme Court case held that the Supreme Court may review state court decisions involving federal law?",
        "a": "Martin v. Hunter's Lessee (1816)",
        "key": "review state court decisions involving federal law",
        "topic": "Foundations",
        "hint": "Think of a case involving a Virginia land dispute after the Revolutionary War between Martin and Hunter, where a British treaty conflicted with state law, and a state court refused to follow the Supreme Court’s ruling—leading the Court to firmly establish that it has the final word on federal law, even over state courts."
    },
    {
        "q": "Which Supreme Court case strengthened the Contracts Clause by limiting state interference with private contracts?",
        "a": "Dartmouth College v. Woodward (1819)",
        "key": "Contracts Clause",
        "topic": "Foundations",
        "hint": "New Hampshire tried to take over a small college by converting its private royal charter into a public institution — and the Supreme Court ruled that a state cannot simply rewrite a contract it doesn't like."
    },
    {
        "q": "Which Supreme Court case established broad federal power via implied powers and affirmed federal supremacy over states?",
        "a": "McCulloch v. Maryland (1819)",
        "key": "implied powers",
        "topic": "Foundations",
        "hint": "Think of a case where Maryland tried to tax a national bank, and McCulloch refused to pay—leading the Supreme Court, under John Marshall, to uphold implied powers under the Necessary and Proper Clause and declare that states cannot tax federal institutions."
    },
    {
        "q": "Which Supreme Court case limited the power of states to tax federal institutions (federal supremacy in taxation)?",
        "a": "McCulloch v. Maryland (1819)",
        "key": "states to tax federal institutions",
        "topic": "Foundations",
        "hint": "Think of the case where James McCulloch, a manager of the national bank in Baltimore, refused to pay Maryland’s tax, leading the Supreme Court to declare that states cannot tax federal institutions—'the power to tax is the power to destroy.'"
    },
    {
        "q": "Which Supreme Court case prohibited states from interfering with interstate commerce and expanded the Commerce Clause early on?",
        "a": "Gibbons v. Ogden (1824)",
        "key": "interstate commerce",
        "topic": "Foundations",
        "hint": "Two steamboat operators — Gibbons and Ogden — were fighting over who could run boats between New York and New Jersey, and the Supreme Court ruled that when commerce crosses state lines, only Congress can regulate it."
    },
    {
        "q": "Which Supreme Court case held that federal law is supreme over state law and state courts must follow it?",
        "a": "Cooper v. Aaron (1958)",
        "key": "federal law is supreme over state law",
        "topic": "Foundations",
        "hint": "Think of the case where William G. Cooper (a Little Rock school official) was on one side and John Aaron (a parent of Black students seeking desegregation) was on the other, after Governor Faubus blocked integration in Arkansas—and the Supreme Court, with all nine justices signing, declared that federal law is supreme over state law and must be followed."
    },
    {
        "q": "Which Supreme Court case established that the federal government can sue a state (state sovereignty limited by the Constitution)?",
        "a": "Chisholm v. Georgia (1793)",
        "key": "federal government can sue a state",
        "topic": "Foundations",
        "hint": "Think of the case where Alexander Chisholm (a citizen from South Carolina) sued the state of Georgia over unpaid Revolutionary War debts, and the Supreme Court said a state can be sued in federal court—a decision so controversial it led to the 11th Amendment reversing it."
    },
    {
        "q": "Which Supreme Court case established that the Bill of Rights initially applied only to the federal government (before incorporation)?",
        "a": "Barron v. Baltimore (1833)",
        "key": "Bill of Rights initially applied only to the federal government",
        "topic": "Foundations",
        "hint": "John Barron claimed Baltimore ruined his wharf and argued the Fifth Amendment required compensation, but Chief Justice Marshall ruled that the Bill of Rights limited only the federal government, not states or cities."
    },

    # ── Race & Equality ────────────────────────────────────────────────
    {
    "q": "Which Supreme Court case ruled that enslaved people were property and not citizens and that Congress could not ban slavery in the territories?",
    "a": "Dred Scott v. Sandford (1857)",
    "key": "enslaved people were property and not citizens",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Dred Scott (an enslaved man)** sued **Sandford** after living in free territory and claimed he should be free, but the Supreme Court ruled that **Black people were not citizens and were considered property**, and Congress could not ban slavery in the territories."
},
{
    "q": "Which Supreme Court case upheld the doctrine of 'separate but equal'?",
    "a": "Plessy v. Ferguson (1896)",
    "key": "separate but equal",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Homer Plessy (a mixed-race man)** sat in a whites-only train car and was arrested by **Ferguson (a judge)**, and the Supreme Court ruled that **racial segregation is allowed under 'separate but equal.'**"
},
{
    "q": "Which Supreme Court case ended racial segregation in public schools?",
    "a": "Brown v. Board of Education (1954)",
    "key": "racial segregation in public schools",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Oliver Brown (a parent of a Black student)** sued the **Board of Education** because his daughter was denied access to a white school, and the Supreme Court ruled that **segregated schools are inherently unequal.**"
},
{
    "q": "Which Supreme Court case upheld federal power to enforce civil rights against private discrimination in public accommodations?",
    "a": "Heart of Atlanta Motel, Inc. v. United States (1964)",
    "key": "civil rights against private discrimination",
    "topic": "Race & Equality",
    "hint": "Think of the case where the **Heart of Atlanta Motel (a business)** refused to serve Black customers, and the **United States government** sued, and the Supreme Court ruled that **Congress can ban private discrimination using the Commerce Clause.**"
},
{
    "q": "Which Supreme Court case held that state-imposed school segregation must be eliminated 'with all deliberate speed'?",
    "a": "Brown v. Board of Education II (1955)",
    "key": "with all deliberate speed",
    "topic": "Race & Equality",
    "hint": "Think of the follow-up case where **Brown (the same parents)** returned to court against the **Board of Education**, and the Supreme Court said schools must desegregate **'with all deliberate speed.'**"
},
{
    "q": "Which Supreme Court case upheld the internment of Japanese Americans during World War II?",
    "a": "Korematsu v. United States (1944)",
    "key": "internment of Japanese Americans",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Fred Korematsu (a Japanese American man)** refused to go to an internment camp, and the **United States government** enforced the order, and the Supreme Court ruled that **internment was allowed during wartime.**"
},
{
    "q": "Which Supreme Court case rejected 'separate but equal' in higher education as unequal in practice?",
    "a": "Sweatt v. Painter (1950)",
    "key": "separate but equal",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Heman Sweatt (a Black student)** applied to the University of Texas Law School and was denied, and **Painter (the university official)** offered a separate school, but the Supreme Court ruled that **the separate law school was not truly equal.**"
},
{
    "q": "Which Supreme Court case enforced desegregation orders over state resistance (Little Rock crisis context)?",
    "a": "Cooper v. Aaron (1958)",
    "key": "desegregation orders over state resistance",
    "topic": "Race & Equality",
    "hint": "Think of the case where **William G. Cooper (a school official)** was opposed by **John Aaron (a parent of Black students)** during the **Little Rock, Arkansas crisis**, after **Governor Faubus blocked desegregation**, and the Supreme Court — with **all nine justices signing** — ruled that **states must follow federal desegregation orders.**"
},
{
    "q": "Which Supreme Court case addressed affirmative action and held racial quotas unconstitutional but allowed race as one factor (classic landmark framing)?",
    "a": "Regents of the University of California v. Bakke (1978)",
    "key": "racial quotas unconstitutional",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Allan Bakke (a white applicant)** was denied admission to medical school by the **University of California Regents**, and the Supreme Court ruled that **racial quotas are unconstitutional, but race can be used as one factor.**"
},
{
    "q": "Which Supreme Court case limited affirmative action by requiring strict scrutiny for racial classifications by the federal government?",
    "a": "Adarand Constructors, Inc. v. Peña (1995)",
    "key": "strict scrutiny for racial classifications",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Adarand (a construction company)** lost a federal contract due to minority preferences under **Peña (a government official)**, and the Supreme Court ruled that **all federal racial classifications must pass strict scrutiny.**"
},
{
    "q": "Which Supreme Court case held that race-based districting can violate equal protection (racial gerrymandering)?",
    "a": "Shaw v. Reno (1993)",
    "key": "race-based districting",
    "topic": "Race & Equality",
    "hint": "Think of the case where **Shaw (a voter)** challenged a strangely shaped voting district created by **Reno (a government official)**, and the Supreme Court ruled that **drawing districts mainly based on race can violate equal protection.**"
},

# ── Speech & Press ─────────────────────────────────────────────────
{
    "q": "Which Supreme Court case established the 'clear and present danger' test for limits on speech?",
    "a": "Schenck v. United States (1919)",
    "key": "clear and present danger",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Charles Schenck (a man protesting the draft)** mailed flyers against World War I, and the **United States government** arrested him, and the Supreme Court ruled that **speech can be limited if it creates a 'clear and present danger.'**"
},
{
    "q": "Which Supreme Court case protected symbolic speech (like wearing an armband) for students in school if not substantially disruptive?",
    "a": "Tinker v. Des Moines Independent Community School District (1969)",
    "key": "symbolic speech",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Tinker (a student)** wore a black armband to protest the Vietnam War at a **Des Moines school**, and the Supreme Court ruled that **students have free speech rights unless it causes disruption.**"
},
{
    "q": "Which Supreme Court case held that students can be disciplined for lewd or vulgar speech at school events?",
    "a": "Bethel School District No. 403 v. Fraser (1986)",
    "key": "lewd or vulgar speech at school events",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Fraser (a student)** gave a vulgar speech at a **Bethel school event**, and the Supreme Court ruled that **schools can punish lewd or inappropriate speech.**"
},
{
    "q": "Which Supreme Court case allowed schools to regulate school-sponsored student publications (like a school newspaper)?",
    "a": "Hazelwood School District v. Kuhlmeier (1988)",
    "key": "school-sponsored student publications",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Kuhlmeier (a student)** wrote articles for a **Hazelwood school newspaper**, and the principal removed them, and the Supreme Court ruled that **schools can control school-sponsored publications.**"
},
{
    "q": "Which Supreme Court case protected flag burning as symbolic speech under the First Amendment?",
    "a": "Texas v. Johnson (1989)",
    "key": "flag burning as symbolic speech",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Johnson (a protester)** burned an American flag in **Texas**, and the Supreme Court ruled that **flag burning is protected symbolic speech.**"
},
{
    "q": "Which Supreme Court case held that the government generally cannot censor the press through prior restraint (Pentagon Papers case)?",
    "a": "New York Times Co. v. United States (1971)",
    "key": "prior restraint",
    "topic": "Speech & Press",
    "hint": "Think of the case where the **New York Times (a newspaper)** wanted to publish the Pentagon Papers, and the **United States government** tried to stop it, and the Supreme Court ruled that **the government cannot use prior restraint to censor the press.**"
},
{
    "q": "Which Supreme Court case established the 'actual malice' standard for defamation suits by public officials?",
    "a": "New York Times Co. v. Sullivan (1964)",
    "key": "actual malice",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Sullivan (a public official)** sued the **New York Times**, and the Supreme Court ruled that **public officials must prove 'actual malice' to win a defamation case.**"
},
{
    "q": "Which Supreme Court case protected the right to publish materials even if offensive, limiting obscenity prosecutions (modern obscenity test case)?",
    "a": "Miller v. California (1973)",
    "key": "obscenity",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Miller (a man mailing adult materials)** was prosecuted in **California**, and the Supreme Court created a test for **what counts as obscene speech.**"
},
{
    "q": "Which Supreme Court case held that burning a draft card was not protected speech when it interferes with government interests?",
    "a": "United States v. O'Brien (1968)",
    "key": "burning a draft card",
    "topic": "Speech & Press",
    "hint": "Think of the case where **O'Brien (a protester)** burned his draft card, and the **United States government** punished him, and the Supreme Court ruled that **speech can be limited if it interferes with important government functions.**"
},
{
    "q": "Which Supreme Court case held that corporations and unions have First Amendment protection for independent political expenditures?",
    "a": "Citizens United v. Federal Election Commission (2010)",
    "key": "independent political expenditures",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Citizens United (a political group)** wanted to spend money on political ads, and the **Federal Election Commission** tried to limit it, and the Supreme Court ruled that **corporations have free speech rights in political spending.**"
},
{
    "q": "Which Supreme Court case upheld a state's right-to-work type restrictions on union agency fees for public employees (public-sector union fees case)?",
    "a": "Janus v. AFSCME (2018)",
    "key": "union agency fees for public employees",
    "topic": "Speech & Press",
    "hint": "Think of the case where **Janus (a public worker)** refused to pay union fees to **AFSCME (a union)**, and the Supreme Court ruled that **forcing public employees to pay union fees violates free speech.**"
},

# ── Religion ───────────────────────────────────────────────────────
{
    "q": "Which Supreme Court case held that school-sponsored prayer in public schools is unconstitutional?",
    "a": "Engel v. Vitale (1962)",
    "key": "school-sponsored prayer",
    "topic": "Religion",
    "hint": "Think of the case where **Engel (a parent)** challenged a government-written prayer in schools, and **Vitale (a school official)** supported it, and the Supreme Court ruled that **school-sponsored prayer is unconstitutional.**"
},
{
    "q": "Which Supreme Court case established the Lemon test for government action concerning religion (Establishment Clause)?",
    "a": "Lemon v. Kurtzman (1971)",
    "key": "Lemon test",
    "topic": "Religion",
    "hint": "Think of the case where **Lemon (a citizen)** challenged state aid to religious schools supported by **Kurtzman (a state official)**, and the Supreme Court created the **Lemon test for church-state issues.**"
},
{
    "q": "Which Supreme Court case upheld a neutral school voucher program that included religious schools (aid-to-religion context)?",
    "a": "Zelman v. Simmons-Harris (2002)",
    "key": "school voucher program",
    "topic": "Religion",
    "hint": "Think of the case where **Zelman (a state official)** supported school vouchers and **Simmons-Harris (a parent)** used them, and the Supreme Court ruled that **voucher programs including religious schools are allowed.**"
},
{
    "q": "Which Supreme Court case held that Amish families could withdraw children from compulsory schooling beyond 8th grade for religious reasons?",
    "a": "Wisconsin v. Yoder (1972)",
    "key": "Amish families",
    "topic": "Religion",
    "hint": "Think of the case where **Yoder (an Amish parent)** refused to send children to school past 8th grade in **Wisconsin**, and the Supreme Court ruled that **religious beliefs can override compulsory education laws.**"
},

# ── Criminal Procedure ─────────────────────────────────────────────
{
    "q": "Which Supreme Court case applied the exclusionary rule to the states (illegally obtained evidence excluded from trial)?",
    "a": "Mapp v. Ohio (1961)",
    "key": "exclusionary rule",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Dollree Mapp (a woman)** had her home illegally searched in **Ohio**, and the Supreme Court ruled that **illegally obtained evidence cannot be used in state courts.**"
},
{
    "q": "Which Supreme Court case required police to inform suspects of their rights before custodial interrogation?",
    "a": "Miranda v. Arizona (1966)",
    "key": "inform suspects of their rights",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Ernesto Miranda (a suspect)** was questioned by police in **Arizona** without being told his rights, and the Supreme Court ruled that **police must inform suspects of their rights.**"
},
{
    "q": "Which Supreme Court case guaranteed the right to an attorney for indigent defendants in state felony cases?",
    "a": "Gideon v. Wainwright (1963)",
    "key": "right to an attorney for indigent defendants",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Gideon (a poor defendant)** was denied a lawyer by **Wainwright (a state official)**, and the Supreme Court ruled that **states must provide attorneys to those who cannot afford one.**"
},
{
    "q": "Which Supreme Court case required counsel for juveniles in delinquency proceedings (due process for juveniles)?",
    "a": "In re Gault (1967)",
    "key": "counsel for juveniles",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Gault (a teenager)** was punished without a lawyer, and the Supreme Court ruled that **juveniles have the right to due process, including legal counsel.**"
},
{
    "q": "Which Supreme Court case required states to provide transcripts to indigent defendants for appeals (equal justice in appeals)?",
    "a": "Griffin v. Illinois (1956)",
    "key": "transcripts to indigent defendants",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Griffin (a defendant)** could not afford a transcript in **Illinois**, and the Supreme Court ruled that **states must provide transcripts so poor defendants can appeal.**"
},
{
    "q": "Which Supreme Court case established that a suspect has a right to an attorney during police interrogation once requested?",
    "a": "Edwards v. Arizona (1981)",
    "key": "right to an attorney during police interrogation once requested",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Edwards (a suspect)** asked for a lawyer during questioning in **Arizona**, but police continued, and the Supreme Court ruled that **interrogation must stop once a lawyer is requested.**"
},
{
    "q": "Which Supreme Court case required police to obtain a warrant for most searches and seizures (strong warrant preference case)?",
    "a": "Katz v. United States (1967)",
    "key": "warrant for most searches and seizures",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Katz (a man using a phone booth)** was secretly recorded by the **United States**, and the Supreme Court ruled that **police generally need a warrant when there is an expectation of privacy.**"
},
{
    "q": "Which Supreme Court case held that students have reduced privacy rights at school and allowed reasonable searches by school officials?",
    "a": "New Jersey v. T.L.O. (1985)",
    "key": "reduced privacy rights at school",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **T.L.O. (a student)** had her purse searched in **New Jersey**, and the Supreme Court ruled that **schools only need reasonable suspicion to search students.**"
},
{
    "q": "Which Supreme Court case established the standard for police to stop-and-frisk based on reasonable suspicion?",
    "a": "Terry v. Ohio (1968)",
    "key": "stop-and-frisk",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Terry (a suspect)** was stopped and frisked by police in **Ohio**, and the Supreme Court ruled that **police can stop and frisk based on reasonable suspicion.**"
},
{
    "q": "Which Supreme Court case required that confessions be voluntary and established due process limits on coerced confessions?",
    "a": "Brown v. Mississippi (1936)",
    "key": "coerced confessions",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Brown (a defendant)** was tortured by police in **Mississippi** to confess, and the Supreme Court ruled that **coerced confessions violate due process.**"
},
{
    "q": "Which Supreme Court case extended the exclusionary rule by applying it to evidence discovered through unconstitutional searches (incorporation era framing)?",
    "a": "Weeks v. United States (1914)",
    "key": "exclusionary rule",
    "topic": "Criminal Procedure",
    "hint": "Think of the case where **Weeks (a defendant)** had his home illegally searched by the **United States**, and the Supreme Court ruled that **illegally obtained evidence cannot be used in federal court.**"
},
]

# ── Convenience lists ──────────────────────────────────────────────────
questions   = [d["q"]     for d in question_data]
answers     = [d["a"]     for d in question_data]
key_phrases = [d["key"]   for d in question_data]
topics      = [d["topic"] for d in question_data]
hints       = [d["hint"]  for d in question_data]

if len(questions) != len(answers):
    raise ValueError(f"Count mismatch: {len(questions)} questions vs {len(answers)} answers.")

# =========================
# STREAK MESSAGES
# =========================
STREAK_MESSAGES = {
    3:  "🔥 3 in a row!",
    5:  "⭐ 5-streak — great work!",
    7:  "🚀 7 correct — outstanding!",
    10: "🏆 10-STREAK! You're on fire!",
    20: "🔥🔥 You are the boss!"
}

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

        style = ttk.Style(self.dialog)
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("Title.TLabel",          font=("Segoe UI", 14, "bold"))
        style.configure("Section.TLabelframe.Label", font=("Segoe UI", 10, "bold"))
        style.configure("TLabel",                font=("Segoe UI", 10))
        style.configure("TRadiobutton",          font=("Segoe UI", 10))
        style.configure("Primary.TButton",       font=("Segoe UI", 10, "bold"), padding=(14, 8))

        container = ttk.Frame(self.dialog, padding=16)
        container.grid(row=0, column=0, sticky="nsew")
        self.dialog.columnconfigure(0, weight=1)
        self.dialog.rowconfigure(0, weight=1)

        ttk.Label(container, text="Quiz Setup", style="Title.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 10))

        opt_f = ttk.LabelFrame(container, text="Answer Options",
                                style="Section.TLabelframe", padding=12)
        opt_f.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        ttk.Label(opt_f, text="How many answer options?").grid(row=0, column=0, sticky="w")
        self.num_options_var = tk.IntVar(value=4)
        opt_row = ttk.Frame(opt_f)
        opt_row.grid(row=1, column=0, sticky="w", pady=(6, 0))
        for i, num in enumerate([2, 3, 4]):
            ttk.Radiobutton(opt_row, text=str(num),
                            variable=self.num_options_var, value=num)\
                .grid(row=0, column=i, padx=(0 if i == 0 else 18, 0))

        rand_f = ttk.LabelFrame(container, text="Question Order",
                                 style="Section.TLabelframe", padding=12)
        rand_f.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        ttk.Label(rand_f, text="Randomize questions?").grid(row=0, column=0, sticky="w")
        self.randomize_var = tk.StringVar(value="yes")
        rand_row = ttk.Frame(rand_f)
        rand_row.grid(row=1, column=0, sticky="w", pady=(6, 0))
        ttk.Radiobutton(rand_row, text="Yes", variable=self.randomize_var, value="yes")\
            .grid(row=0, column=0)
        ttk.Radiobutton(rand_row, text="No",  variable=self.randomize_var, value="no")\
            .grid(row=0, column=1, padx=(18, 0))

        mode_f = ttk.LabelFrame(container, text="Quiz Mode",
                                 style="Section.TLabelframe", padding=12)
        mode_f.grid(row=3, column=0, sticky="ew")
        self.quiz_mode_var = tk.StringVar(value="question_to_answer")
        ttk.Radiobutton(mode_f, text="1 Question → Multiple Answers",
                        variable=self.quiz_mode_var, value="question_to_answer")\
            .grid(row=0, column=0, sticky="w", pady=(0, 6))
        ttk.Radiobutton(mode_f, text="1 Answer → Multiple Questions",
                        variable=self.quiz_mode_var, value="answer_to_question")\
            .grid(row=1, column=0, sticky="w")

        btn_row = ttk.Frame(container)
        btn_row.grid(row=4, column=0, sticky="e", pady=(14, 0))
        ttk.Button(btn_row, text="Cancel", command=self.cancel)\
            .grid(row=0, column=0, padx=(0, 10))
        ttk.Button(btn_row, text="Start Quiz", style="Primary.TButton",
                   command=self.ok).grid(row=0, column=1)

        self.dialog.bind("<Return>", lambda e: self.ok())
        self.dialog.bind("<Escape>", lambda e: self.cancel())
        self.dialog.update_idletasks()
        w, h = 480, 480
        x = (self.dialog.winfo_screenwidth()  // 2) - (w // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (h // 2)
        self.dialog.geometry(f"{w}x{h}+{x}+{y}")
        self.dialog.protocol("WM_DELETE_WINDOW", self.cancel)

    def ok(self):
        self.result = {
            "num_options":         self.num_options_var.get(),
            "quiz_mode":           self.quiz_mode_var.get(),
            "randomize_questions": self.randomize_var.get() == "yes",
        }
        self.dialog.destroy()

    def cancel(self):
        self.result = None
        self.dialog.destroy()


# =========================
# TOPIC REPORT DIALOG
# =========================

class TopicReportDialog:
    def __init__(self, parent, topic_stats):
        dlg = tk.Toplevel(parent)
        dlg.title("📊 Performance by Topic")
        dlg.resizable(True, True)
        dlg.transient(parent)
        dlg.grab_set()

        tk.Label(dlg, text="Performance by Topic",
                 font=("Segoe UI", 14, "bold"), pady=8).pack()

        frame = tk.Frame(dlg)
        frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=8)

        headers    = ["Topic", "Asked", "Correct", "Wrong", "Score %"]
        col_widths = [26, 6, 8, 6, 8]
        for col, (h, w) in enumerate(zip(headers, col_widths)):
            tk.Label(frame, text=h, font=("Courier", 10, "bold"),
                     width=w, anchor="w", relief="groove", bg="#ddd")\
                .grid(row=0, column=col, padx=1, pady=1, sticky="ew")

        for row_i, (topic, s) in enumerate(
                sorted(topic_stats.items(), key=lambda x: -x[1]["asked"]), start=1):
            asked   = s["asked"]
            correct = s["correct"]
            wrong   = asked - correct
            pct     = int(100 * correct / asked) if asked else 0
            bg = "#d4edda" if pct >= 70 else ("#fff3cd" if pct >= 40 else "#f8d7da")
            for col, (val, w) in enumerate(
                    zip([topic, asked, correct, wrong, f"{pct}%"], col_widths)):
                tk.Label(frame, text=str(val), font=("Courier", 10),
                         width=w, anchor="w", bg=bg)\
                    .grid(row=row_i, column=col, padx=1, pady=1, sticky="ew")

        tk.Button(dlg, text="Close", command=dlg.destroy,
                  font=("Arial", 11), bg="steelblue", fg="white",
                  padx=16, pady=6).pack(pady=12)

        dlg.update_idletasks()
        wd = max(520, dlg.winfo_reqwidth() + 30)
        hd = dlg.winfo_reqheight() + 30
        x = (dlg.winfo_screenwidth()  // 2) - (wd // 2)
        y = (dlg.winfo_screenheight() // 2) - (hd // 2)
        dlg.geometry(f"{wd}x{hd}+{x}+{y}")
        parent.wait_window(dlg)


# =========================
# MAIN QUIZ APP
# =========================

class FCLEQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FCLE Supreme Court Quiz")
        self.root.geometry("780x700")

        setup = SetupDialog(root)
        self.root.wait_window(setup.dialog)
        if setup.result is None:
            self.root.destroy()
            return

        self.num_options         = setup.result["num_options"]
        self.quiz_mode           = setup.result["quiz_mode"]
        self.randomize_questions = setup.result["randomize_questions"]

        self.total_questions = len(questions)
        self.questions_asked = 0
        self.correct_count   = 0
        self.wrong_count     = 0

        self.wrong_question_indices = set()
        self.topic_stats            = {}
        self.current_streak         = 0
        self.best_streak            = 0

        self.practice_wrong_mode = False
        self.answered            = False
        self._current_q_idx      = 0   # original index into question_data

        self.question_pool      = self._build_pool()
        self.current_pool_index = 0

        self.build_ui()
        self.load_question()

    # ------------------------------------------------------------------
    def _build_pool(self, wrong_only=False):
        if wrong_only:
            pool = list(self.wrong_question_indices)
            random.shuffle(pool)
            return pool
        pool = list(range(len(questions)))
        if self.randomize_questions:
            random.shuffle(pool)
        return pool

    # ------------------------------------------------------------------
    def build_ui(self):
        BG = self.root.cget("bg")

        # ── Status bar ──────────────────────────────────────────────
        self.status_frame = tk.Frame(self.root, bg="#2c3e50")
        self.status_frame.pack(fill=tk.X)
        self.status_label = tk.Label(
            self.status_frame, text="", font=("Consolas", 10, "bold"),
            bg="#2c3e50", fg="white")
        self.status_label.pack(pady=5)

        # ── Streak bar ──────────────────────────────────────────────
        self.streak_frame = tk.Frame(self.root, bg="#1a252f")
        self.streak_frame.pack(fill=tk.X)
        self.streak_label = tk.Label(
            self.streak_frame, text="", font=("Arial", 10),
            bg="#1a252f", fg="#f1c40f")
        self.streak_label.pack(pady=3)

        # ── Wrong-mode banner ────────────────────────────────────────
        self.mode_banner = tk.Label(
            self.root, text="", font=("Arial", 11, "italic"),
            fg="white", bg="darkred", pady=4)

        # ── Topic label ─────────────────────────────────────────────
        self.topic_label = tk.Label(
            self.root, text="", font=("Arial", 9, "italic"), fg="#7f8c8d")
        self.topic_label.pack(pady=(8, 0))

        # ── Question (Text widget for underline support) ─────────────
        q_outer = tk.Frame(self.root, bg=BG)
        q_outer.pack(fill=tk.X, padx=20, pady=(4, 2))
        self.question_text = tk.Text(
            q_outer, height=4, wrap=tk.WORD,
            font=("Arial", 13, "bold"),
            relief=tk.FLAT, bg=BG,
            cursor="arrow", state=tk.DISABLED,
            padx=4, pady=4)
        self.question_text.pack(fill=tk.X)
        self.question_text.tag_configure(
            "normal",    font=("Arial", 13, "bold"))
        self.question_text.tag_configure(
            "underline", font=("Arial", 13, "bold"),
            underline=True, foreground="#154360")

        # ── Hint area ───────────────────────────────────────────────
        hint_outer = tk.Frame(self.root, bg="#fef9e7",
                               relief=tk.GROOVE, bd=1)
        hint_outer.pack(fill=tk.X, padx=20, pady=(4, 0))

        hint_header = tk.Frame(hint_outer, bg="#fef9e7")
        hint_header.pack(fill=tk.X, padx=8, pady=(6, 2))
        tk.Label(hint_header, text="💡 Hint",
                 font=("Arial", 10, "bold"), bg="#fef9e7",
                 fg="#7d6608").pack(side=tk.LEFT)
        self.hint_button = tk.Button(
            hint_header, text="Reveal Hint",
            command=self.show_hint,
            font=("Arial", 9), bg="#f0c419", fg="#333",
            relief=tk.RAISED, padx=8, pady=2,
            cursor="hand2")
        self.hint_button.pack(side=tk.RIGHT)

        self.hint_label = tk.Label(
            hint_outer, text="Click 'Reveal Hint' for a story clue about this case.",
            font=("Arial", 10, "italic"), fg="#784212",
            bg="#fef9e7", wraplength=720,
            justify=tk.LEFT, padx=8, pady=(0))
        self.hint_label.pack(fill=tk.X, padx=8, pady=(0, 8))

        # ── Answer buttons ──────────────────────────────────────────
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=8)
        self.buttons = []
        for i in range(self.num_options):
            btn = tk.Button(
                self.button_frame, text="", width=64,
                wraplength=530, font=("Arial", 11),
                anchor="w", justify=tk.LEFT,
                command=lambda i=i: self.check_answer(i))
            btn.pack(pady=3)
            self.buttons.append(btn)

        # ── Feedback label ──────────────────────────────────────────
        self.feedback_label = tk.Label(
            self.root, text="", font=("Arial", 12, "bold"), wraplength=720)
        self.feedback_label.pack(pady=5)

        # ── Button row 1: navigation ────────────────────────────────
        ctrl1 = tk.Frame(self.root)
        ctrl1.pack(pady=(4, 0))
        self.next_button = tk.Button(
            ctrl1, text="Next Question ▶", command=self.next_question,
            font=("Arial", 11), bg="#2980b9", fg="white", padx=12, pady=4)
        self.next_button.grid(row=0, column=0, padx=8)

        # ── Button row 2: management ────────────────────────────────
        ctrl2 = tk.Frame(self.root)
        ctrl2.pack(pady=(6, 10))
        self.restart_button = tk.Button(
            ctrl2, text="🔄 Restart Quiz", command=self.restart_quiz,
            font=("Arial", 11), bg="#e67e22", fg="white", padx=12, pady=4)
        self.restart_button.grid(row=0, column=0, padx=6)
        self.practice_wrong_button = tk.Button(
            ctrl2, text="⚠ Practice Wrong Only",
            command=self.practice_wrong_only,
            font=("Arial", 11), bg="#c0392b", fg="white", padx=12, pady=4)
        self.practice_wrong_button.grid(row=0, column=1, padx=6)
        self.report_button = tk.Button(
            ctrl2, text="📊 Topic Report",
            command=self.show_topic_report,
            font=("Arial", 11), bg="#27ae60", fg="white", padx=12, pady=4)
        self.report_button.grid(row=0, column=2, padx=6)

        self.update_status()

    # ------------------------------------------------------------------
    def update_status(self):
        if self.practice_wrong_mode:
            remaining = len(self.question_pool) - self.current_pool_index
            txt = (f"⚠ PRACTICE WRONG MODE  |  "
                   f"Wrong Q's: {len(self.wrong_question_indices)}  |  "
                   f"Remaining: {remaining}  |  "
                   f"✅ {self.correct_count}  ❌ {self.wrong_count}")
        else:
            txt = (f"Total: {self.total_questions}  |  "
                   f"Asked: {self.questions_asked}  |  "
                   f"✅ {self.correct_count}  ❌ {self.wrong_count}  |  "
                   f"Wrong logged: {len(self.wrong_question_indices)}")
        self.status_label.config(text=txt)
        self.streak_label.config(
            text=f"🔥 Streak: {self.current_streak}   |   Best: {self.best_streak}")

    # ------------------------------------------------------------------
    def load_question(self):
        if self.current_pool_index >= len(self.question_pool):
            self._handle_pool_exhausted()
            return

        self.answered = False
        self.feedback_label.config(text="")
        # Reset hint area
        self.hint_label.config(
            text="Click 'Reveal Hint' for a story clue about this case.",
            fg="#784212")
        self.hint_button.config(state=tk.NORMAL, text="Reveal Hint",
                                 bg="#f0c419")

        self._current_q_idx = self.question_pool[self.current_pool_index]
        idx = self._current_q_idx

        if self.quiz_mode == "question_to_answer":
            self._render_question("Q: " + questions[idx], key_phrases[idx])
            self.correct_answer = answers[idx]
            pool_wrong = [a for i, a in enumerate(answers) if i != idx]
            choices = [self.correct_answer] + random.sample(
                pool_wrong, min(self.num_options - 1, len(pool_wrong)))
        else:
            self._render_question("Case: " + answers[idx], None)
            self.correct_answer = questions[idx]
            pool_wrong = [questions[i] for i in range(len(questions)) if i != idx]
            choices = [self.correct_answer] + random.sample(
                pool_wrong, min(self.num_options - 1, len(pool_wrong)))

        random.shuffle(choices)
        self.current_choices = choices

        self.topic_label.config(text=f"Topic: {topics[idx]}")

        for i, btn in enumerate(self.buttons):
            btn.config(text=choices[i], bg="SystemButtonFace", state=tk.NORMAL)

    # ------------------------------------------------------------------
    def _render_question(self, full_text, key_phrase):
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete("1.0", tk.END)
        if key_phrase and key_phrase.lower() in full_text.lower():
            lo = full_text.lower()
            i  = lo.find(key_phrase.lower())
            self.question_text.insert(tk.END, full_text[:i],                 "normal")
            self.question_text.insert(tk.END, full_text[i:i+len(key_phrase)],"underline")
            self.question_text.insert(tk.END, full_text[i+len(key_phrase):], "normal")
        else:
            self.question_text.insert(tk.END, full_text, "normal")
        self.question_text.config(state=tk.DISABLED)

    # ------------------------------------------------------------------
    def show_hint(self):
        idx = self._current_q_idx
        self.hint_label.config(text=hints[idx], fg="#4a235a")
        self.hint_button.config(state=tk.DISABLED, text="Hint shown",
                                 bg="#cccccc")

    # ------------------------------------------------------------------
    def check_answer(self, index):
        if self.answered:
            return
        self.answered = True
        self.questions_asked += 1
        self.hint_button.config(state=tk.DISABLED)

        idx   = self._current_q_idx
        topic = topics[idx]
        if topic not in self.topic_stats:
            self.topic_stats[topic] = {"asked": 0, "correct": 0}
        self.topic_stats[topic]["asked"] += 1

        if self.current_choices[index] == self.correct_answer:
            self.correct_count += 1
            self.current_streak += 1
            if self.current_streak > self.best_streak:
                self.best_streak = self.current_streak
            self.topic_stats[topic]["correct"] += 1
            self.buttons[index].config(bg="light green")
            streak_msg = STREAK_MESSAGES.get(self.current_streak, "")
            self.feedback_label.config(
                text=f"✅ Correct!  {streak_msg}", fg="green")
            if self.practice_wrong_mode:
                self.wrong_question_indices.discard(idx)
        else:
            self.wrong_count += 1
            self.current_streak = 0
            self.wrong_question_indices.add(idx)
            self.buttons[index].config(bg="salmon")
            self.feedback_label.config(
                text=f"❌ Incorrect.  The answer was: {self.correct_answer}",
                fg="red")
            for i, c in enumerate(self.current_choices):
                if c == self.correct_answer:
                    self.buttons[i].config(bg="light green")

        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
        self.update_status()

    # ------------------------------------------------------------------
    def next_question(self):
        if not self.answered:
            messagebox.showwarning("Please Answer",
                                   "Select an answer before moving on.")
            return
        self.current_pool_index += 1
        self.load_question()

    # ------------------------------------------------------------------
    def _handle_pool_exhausted(self):
        if self.practice_wrong_mode:
            messagebox.showinfo(
                "Practice Complete",
                f"Finished {len(self.question_pool)} wrong question(s)!\n\n"
                f"✅ Correct this round: {self.correct_count}\n"
                f"❌ Still wrong: {self.wrong_count}\n\n"
                f"Wrong questions remaining: {len(self.wrong_question_indices)}")
            self._exit_practice_wrong_mode()
        else:
            pct = 100 * self.correct_count // self.total_questions
            messagebox.showinfo(
                "Quiz Complete",
                f"All {self.total_questions} questions done!\n\n"
                f"✅ Correct: {self.correct_count}\n"
                f"❌ Wrong:   {self.wrong_count}\n"
                f"Score: {self.correct_count}/{self.total_questions} ({pct}%)\n\n"
                f"🔥 Best streak: {self.best_streak}")
            self.restart_quiz()

    # ------------------------------------------------------------------
    def restart_quiz(self):
        self.practice_wrong_mode = False
        self._hide_mode_banner()
        self.questions_asked = 0
        self.correct_count   = 0
        self.wrong_count     = 0
        self.current_streak  = 0
        self.question_pool      = self._build_pool()
        self.current_pool_index = 0
        self.update_status()
        self.load_question()

    def practice_wrong_only(self):
        if not self.wrong_question_indices:
            messagebox.showinfo("No Wrong Answers",
                                "No incorrect answers logged yet.\n"
                                "Wrong answers are tracked automatically as you quiz.")
            return
        if not messagebox.askyesno(
                "Practice Wrong Only",
                f"{len(self.wrong_question_indices)} wrong question(s) logged.\n\n"
                "Switch to practicing only those now?\n"
                "(List shrinks as you answer them correctly.)"):
            return
        self.practice_wrong_mode = True
        self._show_mode_banner()
        self.questions_asked = 0
        self.correct_count   = 0
        self.wrong_count     = 0
        self.current_streak  = 0
        self.question_pool      = self._build_pool(wrong_only=True)
        self.current_pool_index = 0
        self.update_status()
        self.load_question()

    def show_topic_report(self):
        if not self.topic_stats:
            messagebox.showinfo("No Data Yet",
                                "Answer some questions first to see the topic report.")
            return
        TopicReportDialog(self.root, self.topic_stats)

    def _exit_practice_wrong_mode(self):
        self.practice_wrong_mode = False
        self._hide_mode_banner()
        self.restart_quiz()

    def _show_mode_banner(self):
        self.mode_banner.config(text="⚠  PRACTICE MODE: Wrong Answers Only  ⚠")
        self.mode_banner.pack(after=self.streak_frame, fill=tk.X, padx=10, pady=(0, 4))

    def _hide_mode_banner(self):
        self.mode_banner.pack_forget()


# =========================
# RUN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = FCLEQuizApp(root)
    root.mainloop()
