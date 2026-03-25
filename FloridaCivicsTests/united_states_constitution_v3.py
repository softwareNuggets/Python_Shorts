## Written by Scott Johnson       2026/02/09
## For the Youtube Channel: Software Nuggets
## https://www.youtube.com/c/softwareNuggets
## Version 3  — Smart engine from supreme_court_cases_v3.py merged into
##              united_states_constitution_v3.py
##              Features: key-phrase underline, streak counter, topic report,
##                        rich contextual hints, wrong-only practice mode

import tkinter as tk
from tkinter import ttk, messagebox
import random

# =========================
# QUESTION DATA
# q   = the question text
# a   = the correct answer
# key = important phrase inside q to underline
# topic = category (used in Topic Report)
# hint  = one "wow" sentence — a story clue that leads the student
#         to the answer WITHOUT giving it away
# =========================

question_data = [
    {
        "q": "Which document created the first national government of the United States before the Constitution?",
        "a": "Articles of Confederation",
        "key": "first national government",
        "topic": "Articles of Confederation",
        "hint": "Key words: first national government, before the Constitution. After the American Revolution, around 1781, the United States used the Articles of Confederation as its first national plan of government. It was created because the states feared a strong central government like Britain had."
    },
    {
        "q": "What major weakness of the Articles of Confederation convinced many leaders that a new constitution was needed?",
        "a": "The national government was too weak to tax, regulate trade, or enforce laws effectively",
        "key": "weakness of Articles",
        "topic": "Articles of Confederation",
        "hint": "Key words: weakness of the Articles. In the 1780s, Congress under the Articles of Confederation could not collect taxes, regulate trade between states, or force states to obey national laws. That weakness is why leaders like James Madison and George Washington wanted a stronger Constitution."
    },
    {
        "q": "What event in 1786-1787 showed the weakness of the Articles of Confederation and alarmed many American leaders?",
        "a": "Shays' Rebellion",
        "key": "rebellion showed weakness",
        "topic": "Shays' Rebellion",
        "hint": "Key words: 1786-1787, weakness of the Articles. Shays' Rebellion was an uprising of farmers in Massachusetts led by Daniel Shays. It frightened national leaders because the government seemed too weak to keep order, which helped push support for writing the Constitution."
    },
    {
        "q": "What meeting was called in 1787 to revise the Articles of Confederation but ended up creating a new Constitution?",
        "a": "The Constitutional Convention",
        "key": "1787 meeting",
        "topic": "Constitutional Convention",
        "hint": "Key words: 1787 meeting, revise the Articles. In Philadelphia in 1787, delegates met at the Constitutional Convention. They were supposed to fix the Articles of Confederation, but instead they created an entirely new Constitution."
    },
    {
        "q": "Who is often called the 'Father of the Constitution'?",
        "a": "James Madison",
        "key": "Father of Constitution",
        "topic": "James Madison",
        "hint": "Key words: Father of the Constitution. James Madison earned this title because at the 1787 Constitutional Convention he came prepared with ideas, helped shape the Virginia Plan, and later defended the Constitution in the Federalist Papers."
    },
    {
        "q": "What was the purpose of the Preamble to the Constitution?",
        "a": "To state the goals and purposes of the new government",
        "key": "purpose of Preamble",
        "topic": "Preamble",
        "hint": "Key words: purpose of the Preamble. The Preamble is the opening part of the Constitution, written in 1787, that begins with 'We the People.' Its job is to explain why the Constitution was written and what goals the new government was supposed to achieve."
    },
    {
        "q": "What are the first three words of the Constitution?",
        "a": "We the People",
        "key": "first three words",
        "topic": "Popular Sovereignty",
        "hint": "Key words: first three words. The Constitution begins with 'We the People' because the framers wanted to show that government gets its power from the people, not from a king or a state government."
    },
    {
        "q": "What principle means that government gets its power from the people?",
        "a": "Popular sovereignty",
        "key": "power from people",
        "topic": "Popular Sovereignty",
        "hint": "Key words: power from the people. Popular sovereignty is the principle that the people are the source of government authority. This idea is shown in the Constitution's opening words, 'We the People,' written in 1787."
    },
    {
        "q": "What principle means that everyone, including government officials, must obey the law?",
        "a": "Rule of law",
        "key": "everyone obeys law",
        "topic": "Rule of Law",
        "hint": "Key words: everyone must obey the law. Rule of law means no one is above the law, not even the president or judges. The framers believed this was necessary so America would not become another monarchy or dictatorship."
    },
    {
        "q": "What principle divides government power among legislative, executive, and judicial branches?",
        "a": "Separation of powers",
        "key": "divide power branches",
        "topic": "Separation of Powers",
        "hint": "Key words: divide power among branches. Separation of powers means the Constitution split power into three branches in 1787 so that lawmaking, law enforcement, and judging would not all be controlled by one person or group."
    },
    {
        "q": "What system allows each branch of government to limit the power of the others?",
        "a": "Checks and balances",
        "key": "branches limit each other",
        "topic": "Checks and Balances",
        "hint": "Key words: branches limit each other. Checks and balances is the system the framers created so each branch could stop abuse by the others. For example, the president can veto bills, the Senate confirms judges, and courts can declare laws unconstitutional."
    },
    {
        "q": "What principle means that powers not given to the national government are reserved to the states or the people?",
        "a": "Federalism",
        "key": "shared power national and state",
        "topic": "Federalism",
        "hint": "Key words: powers reserved to states or people. Federalism is the system where power is shared between the national government and the states. The framers used it because they wanted a stronger national government than under the Articles, but not a completely centralized one."
    },
    {
        "q": "Which branch of government makes laws?",
        "a": "The legislative branch",
        "key": "makes laws",
        "topic": "Legislative Branch",
        "hint": "Key words: makes laws. The legislative branch, created in Article I of the Constitution, is Congress. Its main job is to write and pass laws."
    },
    {
        "q": "Which branch of government carries out or enforces laws?",
        "a": "The executive branch",
        "key": "enforces laws",
        "topic": "Executive Branch",
        "hint": "Key words: carries out or enforces laws. The executive branch, created in Article II, is headed by the president. Its job is to enforce the laws Congress passes."
    },
    {
        "q": "Which branch of government interprets laws?",
        "a": "The judicial branch",
        "key": "interprets laws",
        "topic": "Judicial Branch",
        "hint": "Key words: interprets laws. The judicial branch, created in Article III, includes the Supreme Court and other federal courts. Its job is to explain what laws mean and decide whether they fit the Constitution."
    },
    {
        "q": "How many branches of government does the Constitution establish?",
        "a": "Three",
        "key": "number of branches",
        "topic": "Structure of Government",
        "hint": "Key words: how many branches. The Constitution divides the national government into three branches: legislative, executive, and judicial. The framers did this in 1787 to prevent too much power from gathering in one place."
    },
    {
        "q": "What is the name of the two-house legislature created by the Constitution?",
        "a": "Congress",
        "key": "two-house legislature",
        "topic": "Congress",
        "hint": "Key words: two-house legislature. The Constitution created Congress as the national legislature. It has two houses, the House of Representatives and the Senate, because of compromises made at the Constitutional Convention."
    },
    {
        "q": "What are the two houses of Congress?",
        "a": "The House of Representatives and the Senate",
        "key": "two houses",
        "topic": "Bicameral Legislature",
        "hint": "Key words: two houses of Congress. Congress is divided into the House of Representatives and the Senate. This two-house, or bicameral, structure came from the Great Compromise in 1787."
    },
    {
        "q": "Which plan at the Constitutional Convention favored representation based on population?",
        "a": "The Virginia Plan",
        "key": "population plan",
        "topic": "Virginia Plan",
        "hint": "Key words: representation based on population. The Virginia Plan, supported mainly by large states in 1787, wanted representation in Congress based on state population, which would give bigger states more power."
    },
    {
        "q": "Which plan at the Constitutional Convention favored equal representation for each state?",
        "a": "The New Jersey Plan",
        "key": "equal state plan",
        "topic": "New Jersey Plan",
        "hint": "Key words: equal representation for each state. The New Jersey Plan, supported by smaller states in 1787, wanted each state to have the same number of votes so big states would not dominate the government."
    },
    {
        "q": "What compromise created a Congress with one house based on population and one house with equal representation for states?",
        "a": "The Great Compromise",
        "key": "population and equal representation",
        "topic": "Great Compromise",
        "hint": "Key words: one house by population, one house equal by state. The Great Compromise, also called the Connecticut Compromise, solved the big-state vs small-state argument in 1787 by creating the House based on population and the Senate with equal representation."
    },
    {
        "q": "In which house of Congress does each state have equal representation?",
        "a": "The Senate",
        "key": "equal representation house",
        "topic": "Senate",
        "hint": "Key words: equal representation. In the Senate, every state gets the same representation, two senators each, because the Great Compromise protected small states at the Constitutional Convention."
    },
    {
        "q": "How many U.S. senators does each state have?",
        "a": "Two",
        "key": "senators per state",
        "topic": "Senate Representation",
        "hint": "Key words: senators per state. Every state has two senators, no matter its population. This rule was written into the Constitution in 1787 as part of the Great Compromise."
    },
    {
        "q": "In which house of Congress is representation based on population?",
        "a": "The House of Representatives",
        "key": "population-based house",
        "topic": "House of Representatives",
        "hint": "Key words: representation based on population. The House of Representatives is the chamber where states get seats based on population, which means larger states get more representatives."
    },
    {
        "q": "How long is a term for a member of the House of Representatives?",
        "a": "Two years",
        "key": "House term",
        "topic": "House of Representatives",
        "hint": "Key words: House term. Members of the House serve two-year terms because the framers wanted them to stay close to the people and face elections often."
    },
    {
        "q": "How long is a term for a U.S. senator?",
        "a": "Six years",
        "key": "Senate term",
        "topic": "Senate",
        "hint": "Key words: Senate term. U.S. senators serve six-year terms. The framers gave them longer terms than House members so the Senate would be calmer and less driven by sudden public emotion."
    },
    {
        "q": "How long is a presidential term under the Constitution?",
        "a": "Four years",
        "key": "presidential term",
        "topic": "Presidency",
        "hint": "Key words: presidential term. The Constitution gives the president a four-year term. The framers wanted enough time to lead the country, but not so much time that the office would look like a king."
    },
    {
        "q": "What is the minimum age to serve in the House of Representatives?",
        "a": "25",
        "key": "minimum age House",
        "topic": "Qualifications for House",
        "hint": "Key words: minimum age for the House. To serve in the House of Representatives, the Constitution says a person must be at least 25 years old. The House has the lowest age requirement because it was designed to be closest to the people."
    },
    {
        "q": "What is the minimum age to serve in the Senate?",
        "a": "30",
        "key": "minimum age Senate",
        "topic": "Qualifications for Senate",
        "hint": "Key words: minimum age for the Senate. To be a senator, a person must be at least 30 years old. The framers wanted senators to be older and more experienced than House members."
    },
    {
        "q": "What is the minimum age to be president of the United States?",
        "a": "35",
        "key": "minimum age president",
        "topic": "Qualifications for President",
        "hint": "Key words: minimum age for president. The Constitution requires a president to be at least 35 years old, because the framers thought the nation's chief executive should have maturity and experience."
    },
    {
        "q": "What constitutional requirement says the president must be born a U.S. citizen or be a citizen at the time the Constitution was adopted?",
        "a": "Natural-born citizen requirement",
        "key": "president citizenship requirement",
        "topic": "Qualifications for President",
        "hint": "Key words: president must be born a U.S. citizen. Article II includes the natural-born citizen requirement because the framers worried about foreign influence over the presidency."
    },
    {
        "q": "Who presides over the Senate when the Senate is in session, although not as a regular voting member?",
        "a": "The vice president",
        "key": "presides over Senate",
        "topic": "Vice President",
        "hint": "Key words: presides over the Senate. The vice president has this constitutional role even though the office belongs to the executive branch. The vice president normally does not vote, but can cast a tie-breaking vote."
    },
    {
        "q": "Which chamber of Congress has the power to impeach federal officials?",
        "a": "The House of Representatives",
        "key": "power to impeach",
        "topic": "Impeachment",
        "hint": "Key words: power to impeach. The House of Representatives brings impeachment charges, which is like making a formal accusation. This is the first step in the impeachment process."
    },
    {
        "q": "Which chamber of Congress conducts impeachment trials and can remove officials from office?",
        "a": "The Senate",
        "key": "impeachment trial",
        "topic": "Impeachment",
        "hint": "Key words: conducts impeachment trials. After the House impeaches, the Senate holds the trial and decides whether to remove the official. The Senate acts like the court in an impeachment case."
    },
    {
        "q": "Who presides over a presidential impeachment trial in the Senate?",
        "a": "The Chief Justice of the United States",
        "key": "presides presidential impeachment",
        "topic": "Impeachment",
        "hint": "Key words: who presides over a presidential impeachment trial. In that special case, the Chief Justice presides instead of the vice president, because the vice president has a conflict of interest and might become president."
    },
    {
        "q": "What vote is required in the Senate to convict and remove an impeached official?",
        "a": "A two-thirds vote",
        "key": "Senate conviction vote",
        "topic": "Impeachment",
        "hint": "Key words: vote required to convict in the Senate. It takes a two-thirds vote to remove an impeached official. The framers made this difficult so officials could not be removed for ordinary political disagreements."
    },
    {
        "q": "What power allows the president to reject a bill passed by Congress?",
        "a": "The veto power",
        "key": "reject bill",
        "topic": "Presidential Powers",
        "hint": "Key words: president rejects a bill. The veto power lets the president refuse to sign a bill passed by Congress. This is one of the main checks the executive branch has on the legislative branch."
    },
    {
        "q": "What vote is needed in both houses of Congress to override a presidential veto?",
        "a": "A two-thirds vote in each house",
        "key": "override veto",
        "topic": "Checks and Balances",
        "hint": "Key words: override a veto. Congress can still pass a bill over the president's objection, but only with a two-thirds vote in both the House and Senate. This keeps the veto strong, but not absolute."
    },
    {
        "q": "Which article of the Constitution establishes the legislative branch?",
        "a": "Article I",
        "key": "article legislative branch",
        "topic": "Articles of the Constitution",
        "hint": "Key words: article that establishes the legislative branch. Article I is about Congress, the branch that makes laws. The framers put it first because they expected the legislature to be the central branch of government."
    },
    {
        "q": "Which article of the Constitution establishes the executive branch?",
        "a": "Article II",
        "key": "article executive branch",
        "topic": "Articles of the Constitution",
        "hint": "Key words: article that establishes the executive branch. Article II creates the presidency and explains the powers and duties of the president."
    },
    {
        "q": "Which article of the Constitution establishes the judicial branch?",
        "a": "Article III",
        "key": "article judicial branch",
        "topic": "Articles of the Constitution",
        "hint": "Key words: article that establishes the judicial branch. Article III creates the Supreme Court and the federal judiciary, giving courts the job of deciding cases under the Constitution and laws."
    },
    {
        "q": "Which article explains how the Constitution can be amended?",
        "a": "Article V",
        "key": "article amendments",
        "topic": "Amendment Process",
        "hint": "Key words: article about amendments. Article V explains how the Constitution can be formally changed. The framers included this because they knew the country would change over time."
    },
    {
        "q": "Which article declares the Constitution, federal laws, and treaties to be the supreme law of the land?",
        "a": "Article VI",
        "key": "supreme law article",
        "topic": "Supremacy Clause",
        "hint": "Key words: supreme law of the land. Article VI contains the Supremacy Clause, which says the Constitution and valid federal laws are higher than conflicting state laws."
    },
    {
        "q": "What is the Supremacy Clause?",
        "a": "The constitutional rule that federal law is supreme over conflicting state law",
        "key": "federal over state law",
        "topic": "Supremacy Clause",
        "hint": "Key words: federal law over state law. The Supremacy Clause, found in Article VI, means that when a valid federal law conflicts with a state law, the federal law wins."
    },
    {
        "q": "What is an amendment?",
        "a": "A formal change or addition to the Constitution",
        "key": "define amendment",
        "topic": "Amendments",
        "hint": "Key words: formal change to the Constitution. An amendment is an official change or addition to the Constitution. Amendments exist because the framers knew the government would need a legal way to adapt."
    },
    {
        "q": "How many amendments does the Constitution currently have?",
        "a": "27",
        "key": "number of amendments",
        "topic": "Amendments",
        "hint": "Key words: how many amendments. The Constitution has 27 amendments in total. The first 10 are the Bill of Rights, and later amendments dealt with slavery, voting, presidential terms, and other major issues."
    },
    {
        "q": "What are the first ten amendments to the Constitution called?",
        "a": "The Bill of Rights",
        "key": "first ten amendments",
        "topic": "Bill of Rights",
        "hint": "Key words: first ten amendments. The Bill of Rights was added in 1791 to protect individual freedoms and to answer Anti-Federalist fears that the new national government would become too powerful."
    },
    {
        "q": "Why was the Bill of Rights added to the Constitution?",
        "a": "To protect individual liberties and win support for ratification",
        "key": "why Bill of Rights added",
        "topic": "Ratification Debate",
        "hint": "Key words: why the Bill of Rights was added. During the ratification fight in 1787-1788, Anti-Federalists argued the Constitution did not protect individual rights strongly enough. The Bill of Rights was promised to protect liberty and help win approval."
    },
    {
        "q": "What does the First Amendment protect?",
        "a": "Freedoms of religion, speech, press, assembly, and petition",
        "key": "First Amendment freedoms",
        "topic": "First Amendment",
        "hint": "Key words: what does the First Amendment protect. The First Amendment protects religion, speech, press, assembly, and petition. These were considered essential freedoms in a republic where citizens must be able to think, speak, worship, and protest freely."
    },
    {
        "q": "Which amendment protects freedom of speech?",
        "a": "The First Amendment",
        "key": "freedom of speech amendment",
        "topic": "First Amendment",
        "hint": "Key words: freedom of speech. Freedom of speech is one of the five core protections listed in the First Amendment, added in 1791 as part of the Bill of Rights."
    },
    {
        "q": "Which amendment protects the right to keep and bear arms?",
        "a": "The Second Amendment",
        "key": "keep and bear arms",
        "topic": "Second Amendment",
        "hint": "Key words: keep and bear arms. The Second Amendment, part of the Bill of Rights in 1791, protects the right to keep and bear arms. It grew out of early American fears of standing armies and the importance of militias."
    },
    {
        "q": "Which amendment protects people from unreasonable searches and seizures?",
        "a": "The Fourth Amendment",
        "key": "unreasonable searches",
        "topic": "Fourth Amendment",
        "hint": "Key words: unreasonable searches and seizures. The Fourth Amendment protects privacy by requiring the government to have legal justification, usually probable cause and a warrant, before searching people or property."
    },
    {
        "q": "Which amendment protects the rights of accused persons, including due process and protection against self-incrimination?",
        "a": "The Fifth Amendment",
        "key": "due process self-incrimination",
        "topic": "Fifth Amendment",
        "hint": "Key words: due process, self-incrimination. The Fifth Amendment protects accused people by requiring due process and allowing a person not to be forced to testify against himself, which is why people say 'I plead the Fifth.'"
    },
    {
        "q": "Which amendment guarantees the right to a speedy and public trial?",
        "a": "The Sixth Amendment",
        "key": "speedy public trial",
        "topic": "Sixth Amendment",
        "hint": "Key words: speedy and public trial. The Sixth Amendment protects people accused of crimes by guaranteeing a fair process, including a quick public trial, a lawyer, and an impartial jury."
    },
    {
        "q": "Which amendment protects against cruel and unusual punishment?",
        "a": "The Eighth Amendment",
        "key": "cruel unusual punishment",
        "topic": "Eighth Amendment",
        "hint": "Key words: cruel and unusual punishment. The Eighth Amendment limits how harsh the government can be when punishing someone. It was included in the Bill of Rights to prevent abuse by the justice system."
    },
    {
        "q": "Which amendment says that powers not delegated to the United States are reserved to the states or the people?",
        "a": "The Tenth Amendment",
        "key": "reserved powers amendment",
        "topic": "Tenth Amendment",
        "hint": "Key words: powers reserved to the states or the people. The Tenth Amendment, added in 1791, reinforces federalism by saying the national government only has the powers given to it, and the rest stay with states or the people."
    },
    {
        "q": "What is due process of law?",
        "a": "The government must follow fair legal procedures before taking away life, liberty, or property",
        "key": "define due process",
        "topic": "Due Process",
        "hint": "Key words: fair legal procedures. Due process means the government cannot just punish, jail, or take property from someone without following proper legal steps. This idea appears in the Fifth and Fourteenth Amendments."
    },
    {
        "q": "What is judicial review?",
        "a": "The power of courts to declare laws or government actions unconstitutional",
        "key": "power to declare unconstitutional",
        "topic": "Judicial Review",
        "hint": "Key words: courts declare laws unconstitutional. Judicial review is the power of courts, especially the Supreme Court, to strike down laws or government acts that violate the Constitution."
    },
    {
        "q": "Which Supreme Court case established judicial review?",
        "a": "Marbury v. Madison",
        "key": "case established judicial review",
        "topic": "Marbury v. Madison",
        "hint": "Key words: case that established judicial review. In 1803, Marbury v. Madison, led by Chief Justice John Marshall, established that the Supreme Court can declare laws unconstitutional."
    },
    {
        "q": "Who has the power to nominate federal judges?",
        "a": "The president",
        "key": "nominate judges",
        "topic": "Appointments",
        "hint": "Key words: nominate federal judges. Under Article II, the president chooses nominees for federal judgeships, including the Supreme Court. This gives the executive branch an important role in shaping the courts."
    },
    {
        "q": "Who has the power to confirm federal judges nominated by the president?",
        "a": "The Senate",
        "key": "confirm judges",
        "topic": "Appointments",
        "hint": "Key words: confirm federal judges. The Senate must approve judicial nominees through its advice and consent power. This is a check on the president's appointment power."
    },
    {
        "q": "Why do federal judges serve during 'good behavior' instead of for fixed terms?",
        "a": "To help preserve judicial independence",
        "key": "why judges serve during good behavior",
        "topic": "Judicial Independence",
        "hint": "Key words: why judges serve during good behavior. Federal judges were given life tenure in practice so they could make decisions based on law and the Constitution, not fear losing office because of politics."
    },
    {
        "q": "What is the highest court in the United States?",
        "a": "The Supreme Court",
        "key": "highest court",
        "topic": "Supreme Court",
        "hint": "Key words: highest court in the United States. The Supreme Court is the top federal court, created by Article III. It has the final say in major constitutional and federal legal disputes."
    },
    {
        "q": "What are expressed or enumerated powers?",
        "a": "Powers specifically listed in the Constitution",
        "key": "specifically listed powers",
        "topic": "Enumerated Powers",
        "hint": "Key words: specifically listed powers. Enumerated powers are powers directly written into the Constitution, especially in Article I, Section 8, where Congress is given named powers like taxing and regulating commerce."
    },
    {
        "q": "What is an implied power?",
        "a": "A power not stated directly but reasonably inferred from the Constitution",
        "key": "implied power",
        "topic": "Implied Powers",
        "hint": "Key words: not stated directly, but inferred. An implied power is a power the government can use even if the exact words are not written, as long as it is reasonably connected to an enumerated power."
    },
    {
        "q": "Which clause gives Congress authority to make laws needed to carry out its enumerated powers?",
        "a": "The Necessary and Proper Clause",
        "key": "carry out enumerated powers",
        "topic": "Necessary and Proper Clause",
        "hint": "Key words: make laws needed to carry out enumerated powers. The Necessary and Proper Clause in Article I, Section 8 gives Congress flexibility to pass laws needed to use its listed powers."
    },
    {
        "q": "What is another name for the Necessary and Proper Clause?",
        "a": "The Elastic Clause",
        "key": "other name necessary proper",
        "topic": "Elastic Clause",
        "hint": "Key words: another name for Necessary and Proper Clause. It is called the Elastic Clause because it lets congressional power stretch to meet practical needs."
    },
    {
        "q": "Which Supreme Court case upheld the idea of implied powers and supported the constitutionality of a national bank?",
        "a": "McCulloch v. Maryland",
        "key": "implied powers national bank",
        "topic": "McCulloch v. Maryland",
        "hint": "Key words: implied powers, national bank. In McCulloch v. Maryland in 1819, Chief Justice John Marshall said Congress had implied powers under the Necessary and Proper Clause, and that states could not tax the national bank."
    },
    {
        "q": "What does the Constitution forbid states from doing if it conflicts with valid federal law?",
        "a": "Making or enforcing laws that contradict federal law",
        "key": "state law conflict",
        "topic": "Federal Supremacy",
        "hint": "Key words: states cannot conflict with federal law. Because of the Supremacy Clause in Article VI, states cannot make or enforce laws that go against valid federal law."
    },
    {
        "q": "What does the Full Faith and Credit Clause require states to do?",
        "a": "Recognize the public acts, records, and judicial decisions of other states",
        "key": "recognize acts records judgments",
        "topic": "Article IV",
        "hint": "Key words: recognize records and court decisions from other states. The Full Faith and Credit Clause in Article IV helps hold the union together by requiring states to respect one another's official acts and judgments."
    },
    {
        "q": "What does the Extradition Clause require?",
        "a": "A person charged with a crime who flees to another state must be returned to the state where the crime was committed",
        "key": "return fugitive to state",
        "topic": "Article IV",
        "hint": "Key words: return a fugitive to the state where the crime happened. The Extradition Clause in Article IV prevents people from escaping criminal charges just by crossing a state border."
    },
    {
        "q": "What is ratification?",
        "a": "Formal approval of the Constitution",
        "key": "formal approval constitution",
        "topic": "Ratification",
        "hint": "Key words: formal approval. Ratification means officially approving the Constitution. After it was written in 1787, special state conventions had to vote on whether to accept it."
    },
    {
        "q": "How many states were required to ratify the Constitution for it to take effect?",
        "a": "Nine",
        "key": "states required ratification",
        "topic": "Ratification",
        "hint": "Key words: how many states were needed. The Constitution required ratification by 9 of the 13 states to take effect, which made adoption easier than requiring all 13."
    },
    {
        "q": "What were supporters of the Constitution called during the ratification debate?",
        "a": "Federalists",
        "key": "supporters of Constitution",
        "topic": "Federalists",
        "hint": "Key words: supporters of the Constitution. Federalists, including Alexander Hamilton, James Madison, and John Jay, argued in 1787-1788 that America needed a stronger national government than the Articles provided."
    },
    {
        "q": "What were opponents of the Constitution called during the ratification debate?",
        "a": "Anti-Federalists",
        "key": "opponents of Constitution",
        "topic": "Anti-Federalists",
        "hint": "Key words: opponents of the Constitution. Anti-Federalists feared the new national government would be too strong and demanded better protections for individual rights, which helped lead to the Bill of Rights."
    },
    {
        "q": "What collection of essays argued in favor of ratifying the Constitution?",
        "a": "The Federalist Papers",
        "key": "essays for ratification",
        "topic": "Federalist Papers",
        "hint": "Key words: essays that argued for ratification. The Federalist Papers were a series of essays written in 1787-1788 to persuade states, especially New York, to approve the Constitution."
    },
    {
        "q": "Who wrote most of the Federalist Papers?",
        "a": "Alexander Hamilton, James Madison, and John Jay",
        "key": "authors Federalist Papers",
        "topic": "Federalist Papers",
        "hint": "Key words: who wrote the Federalist Papers. The main authors were Alexander Hamilton, James Madison, and John Jay, writing under the name Publius to defend the Constitution."
    },
    {
        "q": "What did Federalist No. 10 warn about?",
        "a": "The danger of factions",
        "key": "Federalist 10 factions",
        "topic": "Federalist No. 10",
        "hint": "Key words: Federalist No. 10. In this essay, James Madison warned about factions, meaning groups driven by self-interest that might harm the rights of others or the common good."
    },
    {
        "q": "According to Madison, what is a faction?",
        "a": "A group of citizens united by a common interest that may act against the rights of others or the public good",
        "key": "define faction",
        "topic": "Federalist No. 10",
        "hint": "Key words: what is a faction. In Federalist No. 10, Madison defined a faction as a group of people united by a common interest or passion that could threaten others' rights or the public good."
    },
    {
        "q": "What did Federalist No. 51 explain?",
        "a": "How separation of powers and checks and balances protect liberty",
        "key": "Federalist 51",
        "topic": "Federalist No. 51",
        "hint": "Key words: Federalist No. 51. In this essay, Madison explained why government power must be divided and each branch must check the others, so liberty would be protected."
    },
    {
        "q": "What phrase from Federalist No. 51 summarizes the need for limited government?",
        "a": "If men were angels, no government would be necessary",
        "key": "if men were angels",
        "topic": "Federalist No. 51",
        "hint": "Key words: famous phrase from Federalist No. 51. James Madison wrote, 'If men were angels, no government would be necessary,' meaning government is needed because people are imperfect, but government itself also must be limited."
    },
    {
        "q": "What does republicanism mean in the context of the Constitution?",
        "a": "A system in which people elect representatives to govern on their behalf",
        "key": "define republicanism",
        "topic": "Republican Government",
        "hint": "Key words: people elect representatives. Republicanism means citizens rule indirectly by choosing representatives. The framers preferred this to direct democracy because they believed representatives could make more stable decisions."
    },
    {
        "q": "What is the Guarantee Clause of Article IV?",
        "a": "The promise that every state will have a republican form of government",
        "key": "guarantee clause",
        "topic": "Article IV",
        "hint": "Key words: Article IV, republican form of government. The Guarantee Clause says the United States must make sure every state has a republican government, meaning no state can become a monarchy or dictatorship."
    },
    {
        "q": "What is habeas corpus?",
        "a": "The right to be brought before a court so the legality of detention can be reviewed",
        "key": "define habeas corpus",
        "topic": "Habeas Corpus",
        "hint": "Key words: legality of detention reviewed by a court. Habeas corpus protects people from being locked up without legal reason. It forces the government to justify why someone is being held."
    },
    {
        "q": "What is a bill of attainder?",
        "a": "A law that punishes a person without a trial",
        "key": "define bill of attainder",
        "topic": "Limits on Government",
        "hint": "Key words: punishes a person without a trial. A bill of attainder is forbidden by the Constitution because lawmakers are not supposed to decide guilt and punishment without the courts."
    },
    {
        "q": "What is an ex post facto law?",
        "a": "A law that makes an act a crime after it was committed",
        "key": "define ex post facto",
        "topic": "Limits on Government",
        "hint": "Key words: makes something a crime after the fact. An ex post facto law is unconstitutional because people must know what the law is before they can be punished for breaking it."
    },
    {
        "q": "What constitutional provision prevents the government from establishing an official religion?",
        "a": "The Establishment Clause of the First Amendment",
        "key": "no official religion",
        "topic": "First Amendment",
        "hint": "Key words: government cannot establish an official religion. The Establishment Clause in the First Amendment was included because many early Americans wanted to avoid government-controlled religion like they had seen in Europe."
    },
    {
        "q": "What constitutional provision protects the right to practice religion freely?",
        "a": "The Free Exercise Clause of the First Amendment",
        "key": "practice religion freely",
        "topic": "First Amendment",
        "hint": "Key words: practice religion freely. The Free Exercise Clause protects a person's right to follow his or her religion without unnecessary government interference."
    },
    {
        "q": "What amendment abolished slavery in the United States?",
        "a": "The Thirteenth Amendment",
        "key": "abolished slavery",
        "topic": "Reconstruction Amendments",
        "hint": "Key words: abolished slavery. The Thirteenth Amendment, adopted after the Civil War in 1865, ended slavery in the United States."
    },
    {
        "q": "What amendment guarantees equal protection of the laws and defines national citizenship?",
        "a": "The Fourteenth Amendment",
        "key": "equal protection citizenship",
        "topic": "Fourteenth Amendment",
        "hint": "Key words: equal protection, citizenship. The Fourteenth Amendment, adopted in 1868 after the Civil War, says people born or naturalized in the U.S. are citizens and guarantees equal protection of the laws."
    },
    {
        "q": "What amendment says the right to vote cannot be denied because of race?",
        "a": "The Fifteenth Amendment",
        "key": "vote race amendment",
        "topic": "Fifteenth Amendment",
        "hint": "Key words: voting cannot be denied because of race. The Fifteenth Amendment, adopted in 1870 during Reconstruction, was meant to protect voting rights for Black men after the Civil War."
    },
    {
        "q": "What amendment provided for the direct election of U.S. senators?",
        "a": "The Seventeenth Amendment",
        "key": "direct election senators",
        "topic": "Seventeenth Amendment",
        "hint": "Key words: direct election of senators. The Seventeenth Amendment, adopted in 1913, changed the original system so U.S. senators would be elected directly by the people instead of chosen by state legislatures."
    },
    {
        "q": "What amendment gave women the right to vote?",
        "a": "The Nineteenth Amendment",
        "key": "women vote amendment",
        "topic": "Nineteenth Amendment",
        "hint": "Key words: women gained the right to vote. The Nineteenth Amendment, ratified in 1920, was the result of a long women's suffrage movement led by activists such as Susan B. Anthony and Elizabeth Cady Stanton."
    },
    {
        "q": "What amendment limited presidents to two elected terms?",
        "a": "The Twenty-Second Amendment",
        "key": "two-term limit president",
        "topic": "Twenty-Second Amendment",
        "hint": "Key words: presidents limited to two terms. The Twenty-Second Amendment was adopted in 1951 after Franklin D. Roosevelt had been elected four times, and it made the two-term limit official."
    },
    {
        "q": "What amendment lowered the voting age to 18?",
        "a": "The Twenty-Sixth Amendment",
        "key": "voting age 18",
        "topic": "Twenty-Sixth Amendment",
        "hint": "Key words: voting age lowered to 18. The Twenty-Sixth Amendment was ratified in 1971 during the Vietnam War era, when many argued that if 18-year-olds were old enough to fight, they were old enough to vote."
    },
    {
        "q": "What amendment ended poll taxes in federal elections?",
        "a": "The Twenty-Fourth Amendment",
        "key": "ended poll tax",
        "topic": "Twenty-Fourth Amendment",
        "hint": "Key words: ended poll taxes. The Twenty-Fourth Amendment, ratified in 1964, banned poll taxes in federal elections because they were used to keep poor people, especially Black citizens in the South, from voting."
    },
    {
        "q": "What does the Constitution require before a person can be convicted of treason?",
        "a": "Testimony of two witnesses to the same overt act or a confession in open court",
        "key": "treason proof requirement",
        "topic": "Treason",
        "hint": "Key words: what proof is required for treason. The Constitution makes treason hard to prove because the framers knew governments in history had abused treason charges. It requires two witnesses to the same overt act or a confession in open court."
    },
    {
        "q": "What is treason according to the Constitution?",
        "a": "Levying war against the United States or giving aid and comfort to its enemies",
        "key": "define treason",
        "topic": "Treason",
        "hint": "Key words: define treason. The Constitution defines treason narrowly as levying war against the United States or giving aid and comfort to its enemies, so the government could not easily label political opponents as traitors."
    }
]

# ── Convenience lists ──────────────────────────────────────────────────
questions   = [d["q"]     for d in question_data]
answers     = [d["a"]     for d in question_data]
key_phrases = [d["key"]   for d in question_data]
topics      = [d["topic"] for d in question_data]
hints       = [d["hint"]  for d in question_data]

if len(questions) != len(answers):
    raise ValueError(f"Count mismatch: {len(questions)} q vs {len(answers)} a.")

# =========================
# STREAK MESSAGES
# =========================
STREAK_MESSAGES = {
    3:  "🔥 3 in a row!",
    5:  "⭐ 5-streak — great work!",
    7:  "🚀 7 correct — outstanding!",
    10: "🏆 10-STREAK! You're on fire!",
}

# =========================
# SETUP DIALOG
# =========================

class SetupDialog:
    def __init__(self, parent):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Quiz Setup – United States Constitution")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()

        style = ttk.Style(self.dialog)
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("Title.TLabel",              font=("Segoe UI", 14, "bold"))
        style.configure("Section.TLabelframe.Label", font=("Segoe UI", 10, "bold"))
        style.configure("TLabel",                    font=("Segoe UI", 10))
        style.configure("TRadiobutton",              font=("Segoe UI", 10))
        style.configure("Primary.TButton",           font=("Segoe UI", 10, "bold"), padding=(14, 8))

        container = ttk.Frame(self.dialog, padding=16)
        container.grid(row=0, column=0, sticky="nsew")
        self.dialog.columnconfigure(0, weight=1)
        self.dialog.rowconfigure(0, weight=1)

        ttk.Label(container, text="Quiz Setup", style="Title.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 10))

        # Answer options
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

        # Question order
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

        # Quiz mode
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
        w, h = 500, 480
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
        col_widths = [30, 6, 8, 6, 8]
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
        wd = max(560, dlg.winfo_reqwidth() + 30)
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
        self.root.title('FCLE – United States Constitution')
        self.root.geometry("800x720")

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

        self.wrong_question_indices = set()   # persists across restarts
        self.topic_stats            = {}       # topic -> {asked, correct}
        self.current_streak         = 0
        self.best_streak            = 0

        self.practice_wrong_mode = False
        self.answered            = False
        self._current_q_idx      = 0

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

        # ── Wrong-mode banner (packed/unpacked dynamically) ──────────
        self.mode_banner = tk.Label(
            self.root, text="", font=("Arial", 11, "italic"),
            fg="white", bg="darkred", pady=4)

        # ── Topic label ─────────────────────────────────────────────
        self.topic_label = tk.Label(
            self.root, text="", font=("Arial", 9, "italic"), fg="#7f8c8d")
        self.topic_label.pack(pady=(8, 0))

        # ── Question Text widget (supports underline tag) ────────────
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

        # ── Hint panel ──────────────────────────────────────────────
        hint_outer = tk.Frame(self.root, bg="#fef9e7", relief=tk.GROOVE, bd=1)
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
            relief=tk.RAISED, padx=8, pady=2, cursor="hand2")
        self.hint_button.pack(side=tk.RIGHT)

        self.hint_label = tk.Label(
            hint_outer,
            text="Click 'Reveal Hint' for a story clue about this concept.",
            font=("Arial", 10, "italic"), fg="#784212",
            bg="#fef9e7", wraplength=740, justify=tk.LEFT,
            padx=8, pady=0)
        self.hint_label.pack(fill=tk.X, padx=8, pady=(0, 8))

        # ── Answer buttons ──────────────────────────────────────────
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=6)
        self.buttons = []
        for i in range(self.num_options):
            btn = tk.Button(
                self.button_frame, text="", width=68,
                wraplength=580, font=("Arial", 11),
                anchor="w", justify=tk.LEFT,
                command=lambda i=i: self.check_answer(i))
            btn.pack(pady=3)
            self.buttons.append(btn)

        # ── Feedback label ──────────────────────────────────────────
        self.feedback_label = tk.Label(
            self.root, text="", font=("Arial", 12, "bold"), wraplength=740)
        self.feedback_label.pack(pady=5)

        # ── Button row 1 — navigation ────────────────────────────────
        ctrl1 = tk.Frame(self.root)
        ctrl1.pack(pady=(4, 0))
        self.next_button = tk.Button(
            ctrl1, text="Next Question ▶", command=self.next_question,
            font=("Arial", 11), bg="#2980b9", fg="white", padx=12, pady=4)
        self.next_button.grid(row=0, column=0, padx=8)

        # ── Button row 2 — management ────────────────────────────────
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
        self.hint_label.config(
            text="Click 'Reveal Hint' for a story clue about this concept.",
            fg="#784212")
        self.hint_button.config(state=tk.NORMAL, text="Reveal Hint", bg="#f0c419")

        self._current_q_idx = self.question_pool[self.current_pool_index]
        idx = self._current_q_idx

        if self.quiz_mode == "question_to_answer":
            self._render_question("Q: " + questions[idx], key_phrases[idx])
            self.correct_answer = answers[idx]
            pool_wrong = [a for i, a in enumerate(answers) if i != idx]
            choices = [self.correct_answer] + random.sample(
                pool_wrong, min(self.num_options - 1, len(pool_wrong)))
        else:
            self._render_question("Answer: " + answers[idx], None)
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
        """Write question into Text widget, underlining the key phrase."""
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete("1.0", tk.END)
        if key_phrase and key_phrase.lower() in full_text.lower():
            lo = full_text.lower()
            i  = lo.find(key_phrase.lower())
            self.question_text.insert(tk.END, full_text[:i],                   "normal")
            self.question_text.insert(tk.END, full_text[i:i+len(key_phrase)],  "underline")
            self.question_text.insert(tk.END, full_text[i+len(key_phrase):],   "normal")
        else:
            self.question_text.insert(tk.END, full_text, "normal")
        self.question_text.config(state=tk.DISABLED)

    # ------------------------------------------------------------------
    def show_hint(self):
        idx = self._current_q_idx
        self.hint_label.config(text=hints[idx], fg="#4a235a")
        self.hint_button.config(state=tk.DISABLED, text="Hint shown", bg="#cccccc")

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
                f"Finished practicing {len(self.question_pool)} wrong question(s)!\n\n"
                f"✅ Correct this round: {self.correct_count}\n"
                f"❌ Still wrong: {self.wrong_count}\n\n"
                f"Wrong questions remaining: {len(self.wrong_question_indices)}\n"
                "(Questions you got right have been removed from your wrong list.)")
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
            messagebox.showinfo(
                "No Wrong Answers",
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
