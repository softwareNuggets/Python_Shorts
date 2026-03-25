## Written by Scott Johnson       2026/02/09
## For the Youtube Channel: Software Nuggets
## https://www.youtube.com/c/softwareNuggets
## Version 2b — Smart engine from supreme_court_cases_v3.py merged into
##              valencia_learn_articles_2.py
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

    # ── Articles of Confederation ──────────────────────────────────────
    {
        "q": "Which document created the first national government of the United States before the Constitution?",
        "a": "Articles of Confederation",
        "key": "first national government",
        "topic": "Articles of Confederation",
        "hint": "After independence, the former colonies were terrified of a strong central government — so they created one so weak it could barely function, with no president, no national courts, and a Congress that could only beg states for money."
    },
    {
        "q": "Which document established a weak national government with no executive or judicial branch?",
        "a": "Articles of Confederation",
        "key": "no executive or judicial branch",
        "topic": "Articles of Confederation",
        "hint": "The framers of this document had just fought a war against a king, so they deliberately left out a president and national courts — decisions they would later deeply regret when the country nearly fell apart."
    },
    {
        "q": "Under which document did Congress lack the power to tax?",
        "a": "Articles of Confederation",
        "key": "lack the power to tax",
        "topic": "Articles of Confederation",
        "hint": "The national government could not pay its Revolutionary War debts or soldiers' wages because it could only send states a letter asking for money — and states routinely ignored it."
    },
    {
        "q": "Under which document did Congress lack the power to regulate interstate commerce?",
        "a": "Articles of Confederation",
        "key": "lack the power to regulate interstate commerce",
        "topic": "Articles of Confederation",
        "hint": "States began acting like separate countries — Virginia taxed New Jersey's goods and New York taxed Connecticut's — creating an economic disaster that could only be fixed by scrapping the entire document."
    },
    {
        "q": "What major weakness of the Articles of Confederation involved changing the document?",
        "a": "Required unanimous consent of all states to amend",
        "key": "unanimous consent of all states to amend",
        "topic": "Articles of Confederation",
        "hint": "Even one state out of thirteen — no matter how small or self-interested — could permanently block any improvement to the national government, making meaningful reform essentially impossible."
    },
    {
        "q": "Which event exposed the weaknesses of the Articles of Confederation and led to the Constitutional Convention?",
        "a": "Shays' Rebellion",
        "key": "weaknesses of the Articles of Confederation",
        "topic": "Articles of Confederation",
        "hint": "A Massachusetts farmer and Revolutionary War veteran named Daniel — angry over debt and taxes — led hundreds of armed men to shut down state courts in 1786, and the national government could do absolutely nothing to stop it."
    },
    {
        "q": "Under the Articles of Confederation, how many votes did each state have in Congress?",
        "a": "One vote per state",
        "key": "votes did each state have",
        "topic": "Articles of Confederation",
        "hint": "Tiny Delaware with 60,000 people had exactly the same voice as Virginia with nearly 750,000 — a one-state, one-vote rule that larger states resented and that made passing almost anything nearly impossible."
    },
    {
        "q": "Why was the Articles of Confederation government considered weak?",
        "a": "It lacked power to tax, regulate trade, and enforce laws",
        "key": "lacked power to tax, regulate trade, and enforce laws",
        "topic": "Articles of Confederation",
        "hint": "Congress could pass resolutions all day long, but without the power to tax, control trade, or force anyone to comply, those resolutions were little more than polite suggestions that states were free to ignore."
    },

    # ── Article I — Legislative Branch ────────────────────────────────
    {
        "q": "Which Article of the Constitution establishes the legislative branch?",
        "a": "Article I",
        "key": "establishes the legislative branch",
        "topic": "Article I – Legislative",
        "hint": "The framers listed it first and made it the longest article because they believed Congress — the branch closest to the people — would be the most powerful and therefore needed the most careful definition."
    },
    {
        "q": "What branch of government is created in Article I?",
        "a": "Legislative branch",
        "key": "branch of government is created in Article I",
        "topic": "Article I – Legislative",
        "hint": "Article I opens with the words 'All legislative Powers herein granted shall be vested in a Congress' — establishing the branch whose sole job is to write the laws of the nation."
    },
    {
        "q": "What are the two chambers of Congress created in Article I?",
        "a": "House of Representatives and Senate",
        "key": "two chambers of Congress",
        "topic": "Article I – Legislative",
        "hint": "The framers created a two-house solution as a compromise between large states (who wanted representation by population) and small states (who wanted equal votes) — a deal that almost broke the Convention."
    },
    {
        "q": "Which chamber of Congress is based on population?",
        "a": "House of Representatives",
        "key": "based on population",
        "topic": "Article I – Legislative",
        "hint": "California sends 52 members to this chamber while Wyoming sends only 1 — because the size of each state's delegation is recalculated after every 10-year census to reflect where Americans actually live."
    },
    {
        "q": "Which chamber of Congress provides equal representation to each state?",
        "a": "Senate",
        "key": "equal representation to each state",
        "topic": "Article I – Legislative",
        "hint": "Whether a state has 300,000 people or 40 million, it always sends exactly two members here — a rule that gives smaller states dramatically more per-person power and was the only way to get small states to sign the Constitution."
    },
    {
        "q": "What is the term length for members of the House of Representatives?",
        "a": "2 years",
        "key": "term length for members of the House",
        "topic": "Article I – Legislative",
        "hint": "The framers made this the shortest term of any federal officeholder, believing the House should be the chamber most tightly connected to — and most quickly answerable to — the voters."
    },
    {
        "q": "What is the term length for U.S. Senators?",
        "a": "6 years",
        "key": "term length for U.S. Senators",
        "topic": "Article I – Legislative",
        "hint": "The framers gave senators three times longer terms than House members, envisioning the Senate as a more deliberate, stable 'cooling saucer' that would calm the passionate, rapidly changing impulses of the lower chamber."
    },
    {
        "q": "Which chamber has the power to impeach?",
        "a": "House of Representatives",
        "key": "power to impeach",
        "topic": "Article I – Legislative",
        "hint": "This chamber acts like a grand jury — it investigates and votes on formal charges against the President or other officers, with a simple majority needed to send the case to the other chamber for trial."
    },
    {
        "q": "Which chamber has the power to conduct impeachment trials?",
        "a": "Senate",
        "key": "conduct impeachment trials",
        "topic": "Article I – Legislative",
        "hint": "When the President is on trial here, the Chief Justice of the United States presides — and a two-thirds supermajority is required for conviction and removal, a threshold that has never been reached in U.S. history."
    },
    {
        "q": "What is the minimum age requirement to serve in the House of Representatives?",
        "a": "25 years old",
        "key": "minimum age requirement to serve in the House",
        "topic": "Article I – Legislative",
        "hint": "At this age, a person is considered old enough to represent constituents in the lower chamber — five years younger than the requirement for the Senate, reflecting the House's role as the chamber closest to everyday citizens."
    },
    {
        "q": "What is the minimum age requirement to serve in the Senate?",
        "a": "30 years old",
        "key": "minimum age requirement to serve in the Senate",
        "topic": "Article I – Legislative",
        "hint": "The framers set a higher age bar for the Senate because they envisioned it as the more experienced, deliberative chamber — a place for seasoned statesmen, not young firebrands."
    },
    {
        "q": "Which clause in Article I allows Congress to make laws necessary and proper to carry out its powers?",
        "a": "Necessary and Proper Clause",
        "key": "necessary and proper to carry out its powers",
        "topic": "Article I – Legislative",
        "hint": "These two words — 'necessary and proper' — have stretched Congressional power enormously over 200 years, allowing Congress to create a national bank, build interstate highways, and regulate things never imagined by the framers."
    },
    {
        "q": "What is another name for the Necessary and Proper Clause?",
        "a": "Elastic Clause",
        "key": "another name for the Necessary and Proper Clause",
        "topic": "Article I – Legislative",
        "hint": "It earned this nickname because, like a rubber band, it can be stretched to cover almost any action Congress wants to take — as long as the action relates to one of Congress's listed powers."
    },
    {
        "q": "Which clause gives Congress the power to regulate trade between states?",
        "a": "Commerce Clause",
        "key": "regulate trade between states",
        "topic": "Article I – Legislative",
        "hint": "This three-word clause — 'regulate Commerce among' the states — became one of the most powerful sentences in the Constitution, used to justify everything from civil rights laws to environmental regulations to the Affordable Care Act."
    },
    {
        "q": "Which clause gives Congress the power to collect taxes?",
        "a": "Taxing and Spending Clause",
        "key": "collect taxes",
        "topic": "Article I – Legislative",
        "hint": "The Founders deliberately gave this power to Congress — not the President — because they believed that the branch directly representing the people should control the nation's purse strings."
    },
    {
        "q": "Which clause allows Congress to declare war?",
        "a": "War Powers Clause",
        "key": "declare war",
        "topic": "Article I – Legislative",
        "hint": "The Constitution gives this solemn power exclusively to Congress, not the President — yet the United States has fought in Korea, Vietnam, and dozens of other conflicts without Congress ever formally using these words."
    },
    {
        "q": "What are expressed (enumerated) powers?",
        "a": "Powers specifically listed in the Constitution",
        "key": "expressed (enumerated) powers",
        "topic": "Article I – Legislative",
        "hint": "Article I, Section 8 spells out 18 specific things Congress is allowed to do — from coining money to establishing post offices — and for the first century of the republic, these listed powers were considered the firm outer boundary of federal authority."
    },
    {
        "q": "What are implied powers?",
        "a": "Powers not specifically listed but implied by the Necessary and Proper Clause",
        "key": "implied powers",
        "topic": "Article I – Legislative",
        "hint": "Chief Justice John Marshall established in 1819 that Congress doesn't need an explicit permission slip for every action — if a power logically flows from the Constitution's listed powers, Congress can use it."
    },
    {
        "q": "What are concurrent powers?",
        "a": "Powers shared by national and state governments",
        "key": "concurrent powers",
        "topic": "Article I – Legislative",
        "hint": "When you pay both a federal income tax and a state income tax on the same paycheck, you are experiencing this type of power — authority that the Constitution allows both levels of government to exercise simultaneously."
    },
    {
        "q": "Which Article describes the process for how a bill becomes a law?",
        "a": "Article I",
        "key": "how a bill becomes a law",
        "topic": "Article I – Legislative",
        "hint": "The process is spelled out in Section 7 of this article — a bill must pass both chambers, then go to the President who can sign it, veto it, or let it become law without signature after 10 days."
    },

    # ── Article II — Executive Branch ─────────────────────────────────
    {
        "q": "Which Article of the Constitution establishes the executive branch?",
        "a": "Article II",
        "key": "establishes the executive branch",
        "topic": "Article II – Executive",
        "hint": "The framers were so worried about creating another king that they debated this article fiercely — they knew the executive needed enough power to govern effectively but not so much power that democracy would be threatened."
    },
    {
        "q": "What branch of government is created in Article II?",
        "a": "Executive branch",
        "key": "branch of government is created in Article II",
        "topic": "Article II – Executive",
        "hint": "This branch is headed by a single person — a deliberate choice by the framers who believed one accountable leader was better than a committee, because one person can be praised or blamed for decisions."
    },
    {
        "q": "What is the term length of the President?",
        "a": "4 years",
        "key": "term length of the President",
        "topic": "Article II – Executive",
        "hint": "The framers chose this length as a balance — long enough for the President to develop and execute policies, but short enough that voters could remove someone who abused the office."
    },
    {
        "q": "What are the qualifications to be President?",
        "a": "35 years old, natural-born citizen, 14 years residency",
        "key": "qualifications to be President",
        "topic": "Article II – Executive",
        "hint": "The three requirements in Article II are age (older than for Congress), birthplace (a rule added out of fear of foreign influence), and residency (to ensure the person understands American life) — together forming the most restrictive eligibility rules for any federal office."
    },
    {
        "q": "Who serves as Commander in Chief according to Article II?",
        "a": "President",
        "key": "Commander in Chief",
        "topic": "Article II – Executive",
        "hint": "The framers gave military command to an elected civilian — not a general — because they feared giving a military officer political power, having just fought a war against a government where the two were dangerously combined."
    },
    {
        "q": "What power allows the President to reject legislation?",
        "a": "Veto power",
        "key": "reject legislation",
        "topic": "Article II – Executive",
        "hint": "This Latin word meaning 'I forbid' gives the President a powerful check on Congress — though Congress can fight back by mustering a two-thirds supermajority in both chambers to override it."
    },
    {
        "q": "What is a presidential veto?",
        "a": "The President's rejection of a bill",
        "key": "presidential veto",
        "topic": "Article II – Executive",
        "hint": "When a President sends a bill back to Congress unsigned with written objections, it doesn't die — it returns to Congress with a higher bar to clear, requiring that two-thirds of both chambers agree to make it law anyway."
    },
    {
        "q": "What is the role of the President in making treaties?",
        "a": "Negotiates treaties (approved by Senate)",
        "key": "role of the President in making treaties",
        "topic": "Article II – Executive",
        "hint": "The President can shake hands with a foreign leader and sign a deal, but that deal is worthless under the Constitution until two-thirds of the Senate agrees — a check designed to prevent one person from entangling the nation in foreign commitments."
    },
    {
        "q": "What role does the Senate play in approving presidential appointments?",
        "a": "Senate confirms appointments by majority vote",
        "key": "approving presidential appointments",
        "topic": "Article II – Executive",
        "hint": "Every Supreme Court justice, Cabinet secretary, and federal ambassador must first survive this chamber's scrutiny — a confirmation process the framers designed to prevent the President from filling the government with unqualified loyalists."
    },
    {
        "q": "What is the President's duty under the Take Care Clause?",
        "a": "To ensure laws are faithfully executed",
        "key": "Take Care Clause",
        "topic": "Article II – Executive",
        "hint": "This clause has been used to argue that a President who refuses to enforce a law Congress passed is violating a direct constitutional duty — the executive branch exists to carry out laws, not to pick and choose which ones to follow."
    },

    # ── Article III — Judicial Branch ─────────────────────────────────
    {
        "q": "Which Article of the Constitution establishes the judicial branch?",
        "a": "Article III",
        "key": "establishes the judicial branch",
        "topic": "Article III – Judicial",
        "hint": "It is the shortest of the three articles establishing the branches — the framers left Congress to fill in nearly all the details of court structure, which is why the number of Supreme Court justices appears nowhere in the Constitution itself."
    },
    {
        "q": "What branch of government is created in Article III?",
        "a": "Judicial branch",
        "key": "branch of government is created in Article III",
        "topic": "Article III – Judicial",
        "hint": "This branch had the least power at the founding — Alexander Hamilton called it the 'least dangerous branch' because it could neither fight wars like the executive nor tax and spend like the legislature."
    },
    {
        "q": "What is the highest court created by Article III?",
        "a": "Supreme Court",
        "key": "highest court",
        "topic": "Article III – Judicial",
        "hint": "Article III requires only one federal court by name — all lower federal courts were created later by Congress using its Article I power — making this the only court with a direct constitutional guarantee of existence."
    },
    {
        "q": "What is the term length for federal judges?",
        "a": "Life term (during good behavior)",
        "key": "term length for federal judges",
        "topic": "Article III – Judicial",
        "hint": "Federal judges can only be removed by impeachment — not by an election or by a President who dislikes their rulings — a lifetime guarantee designed to ensure judges decide cases based on law, not on what is politically popular."
    },
    {
        "q": "What types of cases does the federal judiciary hear?",
        "a": "Cases involving federal law, Constitution, treaties, disputes between states",
        "key": "types of cases does the federal judiciary hear",
        "topic": "Article III – Judicial",
        "hint": "Federal courts are not for every lawsuit — they are specifically for cases where the Constitution, federal law, or treaties are at stake, or where the parties are from different states, or where a state itself is a party."
    },
    {
        "q": "Which Article outlines the crime of treason?",
        "a": "Article III",
        "key": "crime of treason",
        "topic": "Article III – Judicial",
        "hint": "The framers were so afraid of politically motivated treason prosecutions — having seen them used by monarchs to silence opponents — that they wrote the definition directly into the Constitution and required two witnesses or a confession in open court."
    },

    # ── Article IV — States' Relations ────────────────────────────────
    {
        "q": "Which Article explains the relationship between states?",
        "a": "Article IV",
        "key": "relationship between states",
        "topic": "Article IV – States",
        "hint": "This article is what turns a collection of 50 separate governments into a genuine union — without it, a criminal could simply drive across a state line to escape justice, or a marriage legal in one state could be meaningless in another."
    },
    {
        "q": "Which clause requires states to honor public acts, records, and court decisions of other states?",
        "a": "Full Faith and Credit Clause",
        "key": "honor public acts, records, and court decisions",
        "topic": "Article IV – States",
        "hint": "Because of this clause, your driver's license is valid in all 50 states, a divorce granted in Florida is recognized in California, and a debt judgment from a New York court can be collected in Texas."
    },
    {
        "q": "Which clause ensures citizens of each state are treated equally in other states?",
        "a": "Privileges and Immunities Clause",
        "key": "citizens of each state are treated equally in other states",
        "topic": "Article IV – States",
        "hint": "This clause prevents states from treating out-of-state visitors like second-class residents — a state cannot bar a citizen from another state from buying property, practicing a profession, or accessing its courts."
    },
    {
        "q": "Which clause requires states to return fugitives to the state where the crime was committed?",
        "a": "Extradition Clause",
        "key": "return fugitives to the state where the crime was committed",
        "topic": "Article IV – States",
        "hint": "Before this clause, criminals could simply run across a state border and be safe — this provision makes sure that state borders cannot be used as a legal shield against justice."
    },
    {
        "q": "Which Article describes the process for admitting new states?",
        "a": "Article IV",
        "key": "process for admitting new states",
        "topic": "Article IV – States",
        "hint": "Under this article, Congress has admitted 37 states beyond the original 13 — including Hawaii and Alaska in 1959 — and the rules make clear that new states enter on equal footing with existing ones, not as junior partners."
    },
    {
        "q": "Which Article guarantees a republican form of government to each state?",
        "a": "Article IV",
        "key": "guarantees a republican form of government",
        "topic": "Article IV – States",
        "hint": "This guarantee means no state can lawfully replace its elected legislature with a king, a dictator, or a military junta — the federal government is constitutionally obligated to step in to protect representative governance in every state."
    },

    # ── Article V — Amendments ────────────────────────────────────────
    {
        "q": "Which Article explains the amendment process?",
        "a": "Article V",
        "key": "amendment process",
        "topic": "Article V – Amendments",
        "hint": "The framers deliberately made this process difficult — remembering the fatal flaw of the Articles of Confederation, which required unanimous consent — while still leaving a path for change so the Constitution wouldn't become a straitjacket."
    },
    {
        "q": "How many methods are there to propose an amendment?",
        "a": "Two",
        "key": "methods are there to propose an amendment",
        "topic": "Article V – Amendments",
        "hint": "Method one — used for all 27 amendments so far — requires two-thirds of both houses of Congress; method two — never yet used — allows two-thirds of state legislatures to call a national convention to propose amendments."
    },
    {
        "q": "How many methods are there to ratify an amendment?",
        "a": "Two",
        "key": "methods are there to ratify an amendment",
        "topic": "Article V – Amendments",
        "hint": "Once an amendment is proposed, Congress chooses how it will be ratified — either by three-fourths of state legislatures (the usual method) or by special state conventions (used only once, for the 21st Amendment repealing Prohibition)."
    },
    {
        "q": "What fraction of Congress is required to propose an amendment?",
        "a": "Two-thirds of both houses of Congress",
        "key": "fraction of Congress is required to propose an amendment",
        "topic": "Article V – Amendments",
        "hint": "A simple majority is not enough — any proposed change to the Constitution must clear a much higher bar in both the House and Senate, ensuring that only ideas with very broad support even get to be considered."
    },
    {
        "q": "What fraction of states is required to ratify an amendment?",
        "a": "Three-fourths of the states",
        "key": "fraction of states is required to ratify",
        "topic": "Article V – Amendments",
        "hint": "38 out of 50 states must agree — meaning just 13 states representing a small fraction of the American population can permanently block a constitutional change that the vast majority of Americans want."
    },
    {
        "q": "Which Article makes the Constitution flexible?",
        "a": "Article V",
        "key": "makes the Constitution flexible",
        "topic": "Article V – Amendments",
        "hint": "Without this article, the Constitution would be frozen in 1787 — slavery could never have been abolished by amendment, women could never have been guaranteed the vote, and the voting age could never have been lowered to 18."
    },

    # ── Article VI — Supremacy ────────────────────────────────────────
    {
        "q": "Which Article contains the Supremacy Clause?",
        "a": "Article VI",
        "key": "Supremacy Clause",
        "topic": "Article VI – Supremacy",
        "hint": "This clause is the linchpin of the entire federal system — without it, every state could decide for itself whether to follow federal law, turning the United States into 50 separate countries with 50 different legal systems."
    },
    {
        "q": "What does the Supremacy Clause establish?",
        "a": "Federal law is the supreme law of the land",
        "key": "Supremacy Clause establish",
        "topic": "Article VI – Supremacy",
        "hint": "The clause explicitly calls the Constitution, federal laws, and treaties 'the supreme Law of the Land' — meaning state judges are bound to follow them even if their own state's constitution or laws say something different."
    },
    {
        "q": "Which Article requires government officials to take an oath to support the Constitution?",
        "a": "Article VI",
        "key": "oath to support the Constitution",
        "topic": "Article VI – Supremacy",
        "hint": "Every senator, representative, state legislator, and executive and judicial officer — federal and state alike — must swear or affirm to support the Constitution before taking office, making personal loyalty to the document a universal requirement."
    },
    {
        "q": "Which Article states there is no religious test for public office?",
        "a": "Article VI",
        "key": "no religious test for public office",
        "topic": "Article VI – Supremacy",
        "hint": "At the time of the founding, several states required officeholders to be Protestant Christians — this clause made clear that the federal government would never impose such a requirement, a radical idea for its era."
    },

    # ── Article VII — Ratification ────────────────────────────────────
    {
        "q": "Which Article explains how the Constitution was ratified?",
        "a": "Article VII",
        "key": "how the Constitution was ratified",
        "topic": "Article VII – Ratification",
        "hint": "This is the shortest article — just one sentence — but it contained a bold gamble: the framers declared the Constitution would take effect as soon as 9 of the 13 states agreed, even if the other 4 never did."
    },
    {
        "q": "How many states were required to ratify the Constitution?",
        "a": "Nine states",
        "key": "states were required to ratify",
        "topic": "Article VII – Ratification",
        "hint": "This number — nine out of thirteen — was a deliberate departure from the Articles of Confederation's requirement of unanimous consent, and it meant the framers were willing to leave holdout states outside the new union if necessary."
    },
    {
        "q": "What type of conventions were used to ratify the Constitution?",
        "a": "State ratifying conventions",
        "key": "type of conventions were used to ratify",
        "topic": "Article VII – Ratification",
        "hint": "The framers bypassed state legislatures entirely — knowing some would never agree — and called for special elected conventions in each state, so the people themselves (not established politicians) would decide the Constitution's fate."
    },

    # ── Checks and Balances ───────────────────────────────────────────
    {
        "q": "Which branch can veto laws passed by Congress?",
        "a": "Executive branch",
        "key": "veto laws passed by Congress",
        "topic": "Checks & Balances",
        "hint": "This power gives one person the ability to single-handedly block the work of 535 elected legislators — making it one of the most powerful individual acts in American government, yet one that Congress can still overcome with enough votes."
    },
    {
        "q": "Which branch can override a presidential veto?",
        "a": "Legislative branch",
        "key": "override a presidential veto",
        "topic": "Checks & Balances",
        "hint": "A two-thirds vote in both the House and Senate can make a bill law over a President's objection — but this threshold is so high that fewer than 5% of all vetoes in American history have been overridden."
    },
    {
        "q": "Which branch confirms presidential appointments?",
        "a": "Legislative branch (Senate)",
        "key": "confirms presidential appointments",
        "topic": "Checks & Balances",
        "hint": "The framers specifically gave this power to the Senate — not the whole Congress — because they wanted a smaller, more deliberate body scrutinizing who would fill the courts and the Cabinet, not an easily inflamed majority."
    },
    {
        "q": "Which branch can declare laws unconstitutional?",
        "a": "Judicial branch",
        "key": "declare laws unconstitutional",
        "topic": "Checks & Balances",
        "hint": "This power — nowhere explicitly written in the Constitution — was claimed by the Supreme Court for itself in 1803, and has made the judiciary arguably the most powerful check on both Congress and the President."
    },
    {
        "q": "Which branch has the power to impeach the President?",
        "a": "Legislative branch (House)",
        "key": "power to impeach the President",
        "topic": "Checks & Balances",
        "hint": "This chamber acts as the nation's grand jury for presidential misconduct — it investigates, draws up articles of impeachment, and votes with a simple majority to send the President to trial before the other chamber."
    },
    {
        "q": "Which branch conducts impeachment trials?",
        "a": "Legislative branch (Senate)",
        "key": "conducts impeachment trials",
        "topic": "Checks & Balances",
        "hint": "When the President is on trial here, the Chief Justice presides rather than the Vice President — who has an obvious conflict of interest, being next in line for the presidency if the President is removed."
    },
    {
        "q": "Which branch appoints federal judges?",
        "a": "Executive branch",
        "key": "appoints federal judges",
        "topic": "Checks & Balances",
        "hint": "This appointment power creates a lasting legacy — a President who serves four years can shape the federal courts for decades through judicial appointments, since those judges serve for life."
    },

    # ── Federalism & Structure ─────────────────────────────────────────
    {
        "q": "Which system of government divides power between national and state governments?",
        "a": "Federalism",
        "key": "divides power between national and state governments",
        "topic": "Federalism",
        "hint": "The United States invented this system at the Constitutional Convention — unlike a unitary government where one central authority rules everything, or a confederation where states hold all power, this middle path shares sovereignty between two levels."
    },
    {
        "q": "What are reserved powers?",
        "a": "Powers kept by the states",
        "key": "reserved powers",
        "topic": "Federalism",
        "hint": "The 10th Amendment was added specifically to protect these powers — anything not given to the federal government and not prohibited to the states stays with the states or the people, covering things like education, marriage laws, and driver's licenses."
    },
    {
        "q": "Which amendment reinforces reserved powers?",
        "a": "Tenth Amendment",
        "key": "amendment reinforces reserved powers",
        "topic": "Federalism",
        "hint": "Added as part of the Bill of Rights to calm Anti-Federalist fears, this amendment was a promise that the new national government would not swallow up the states — any power not explicitly given to Washington stays with the states."
    },
    {
        "q": "What are delegated powers?",
        "a": "Powers given to the national government",
        "key": "delegated powers",
        "topic": "Federalism",
        "hint": "These are the powers the states handed over to the new central government when they ratified the Constitution — things like coining money, declaring war, and regulating interstate commerce that make more sense at a national level."
    },
    {
        "q": "What is the main purpose of separation of powers?",
        "a": "To prevent concentration of power",
        "key": "main purpose of separation of powers",
        "topic": "Federalism",
        "hint": "James Madison wrote that if all legislative, executive, and judicial power were in one set of hands, the result would be the very definition of tyranny — so the Constitution places each power in a different branch as a structural safeguard against abuse."
    },
    {
        "q": "What is the main purpose of checks and balances?",
        "a": "To ensure no branch becomes too powerful",
        "key": "main purpose of checks and balances",
        "topic": "Federalism",
        "hint": "Each branch was given tools to restrain the others — the President vetoes Congress, Congress overrides vetoes and confirms judges, and courts strike down laws — creating a system where ambition, as Madison said, 'must be made to counteract ambition.'"
    },

    # ── Articles of Confederation — Scenario ──────────────────────────
    {
        "q": "A national economic crisis hits, but Congress can only ask states for money and many refuse. Which weakness of the Articles of Confederation is shown?",
        "a": "Congress could not tax (it could only request money from states)",
        "key": "Congress can only ask states for money",
        "topic": "Articles of Confederation",
        "hint": "The Continental Congress owed millions to war veterans and foreign creditors, but without the power to tax, it could only send begging letters to states that routinely ignored them — making national bankruptcy almost inevitable."
    },
    {
        "q": "Two states begin charging taxes on each other's goods at the border, hurting trade. Under the Articles of Confederation, what power did Congress lack that would fix this?",
        "a": "The power to regulate interstate commerce",
        "key": "charging taxes on each other's goods at the border",
        "topic": "Articles of Confederation",
        "hint": "New York taxed New Jersey firewood and Connecticut butter, states erected trade barriers like rival countries — and Congress could only watch helplessly, having no authority to stop states from waging economic war on each other."
    },
    {
        "q": "Congress wants to build a national army quickly, but states ignore requests for soldiers. Under the Articles of Confederation, why can Congress not force compliance?",
        "a": "There was no strong national executive/enforcement power (states could ignore Congress)",
        "key": "states ignore requests for soldiers",
        "topic": "Articles of Confederation",
        "hint": "During the Revolutionary War itself, Washington's army nearly starved at Valley Forge because Congress could not compel states to send food or men — the government had to rely on the goodwill of 13 independent-minded states."
    },
    {
        "q": "A small uprising of farmers threatens state courts and the national government cannot respond effectively. Which event best illustrates this problem and helped lead to the Constitution?",
        "a": "Shays' Rebellion",
        "key": "uprising of farmers threatens state courts",
        "topic": "Articles of Confederation",
        "hint": "When debt-ridden farmers in western Massachusetts closed down courts by force in 1786, George Washington wrote in alarm that the country was heading toward anarchy — their leader's name became synonymous with the failure of the Articles."
    },
    {
        "q": "Thirteen states must all agree to fix a major problem in the national government, but one state refuses. What Articles of Confederation rule is causing the failure?",
        "a": "Unanimous consent was required to amend the Articles",
        "key": "Thirteen states must all agree",
        "topic": "Articles of Confederation",
        "hint": "Rhode Island single-handedly blocked a national import tax in 1781 and 1782 that could have solved the government's financial crisis — one small state's refusal was all it took to paralyze the entire nation."
    },

    # ── Article I — Scenario ──────────────────────────────────────────
    {
        "q": "Congress passes a law raising income taxes. Which Article gives Congress the power to levy taxes?",
        "a": "Article I (Taxing and Spending power)",
        "key": "power to levy taxes",
        "topic": "Article I – Legislative",
        "hint": "Article I, Section 8 lists the power to 'lay and collect Taxes' as the very first enumerated power of Congress — the framers knew that without revenue, government is just words on paper."
    },
    {
        "q": "Congress creates a new agency to enforce consumer-safety rules even though the agency is not named in the Constitution. Which clause best supports Congress creating the agency?",
        "a": "Necessary and Proper Clause (Elastic Clause)",
        "key": "agency is not named in the Constitution",
        "topic": "Article I – Legislative",
        "hint": "The FDA, EPA, FCC, and hundreds of other federal agencies exist because of this clause — none are in the Constitution by name, but Congress created them as tools 'necessary and proper' to carry out its listed powers."
    },
    {
        "q": "Congress passes a law regulating activity that occurs only within one state, arguing it affects national markets. Which constitutional power is Congress using?",
        "a": "Commerce Clause",
        "key": "activity that occurs only within one state",
        "topic": "Article I – Legislative",
        "hint": "The Supreme Court upheld this expansive reading in 1942, ruling that a farmer growing wheat only for his own family still affected interstate commerce because millions of farmers doing the same thing collectively could move national wheat prices."
    },
    {
        "q": "A bill passes the House but fails in the Senate. What constitutional principle explains why passage requires approval by both chambers?",
        "a": "Bicameralism (two-house legislature)",
        "key": "passage requires approval by both chambers",
        "topic": "Article I – Legislative",
        "hint": "The framers required both chambers to agree because they wanted legislation to survive two very different political tests — the democratic passions of the House and the calmer, state-representing deliberation of the Senate."
    },
    {
        "q": "The House investigates a cabinet secretary for corruption and votes to impeach. What is the Senate's next constitutional role?",
        "a": "Hold an impeachment trial and vote to convict or acquit",
        "key": "Senate's next constitutional role",
        "topic": "Article I – Legislative",
        "hint": "The House's impeachment vote is only an accusation — the Senate then becomes a courtroom where evidence is presented, the accused can mount a defense, and senators act as jurors deciding guilt or innocence."
    },
    {
        "q": "A member of Congress proposes a law, but the Constitution does not list that exact power. Supporters argue the law is needed to carry out listed powers. What type of power is being claimed?",
        "a": "Implied power",
        "key": "Constitution does not list that exact power",
        "topic": "Article I – Legislative",
        "hint": "McCulloch v. Madison established that Congress does not need explicit permission for every act — if the action is a reasonable means to achieve a constitutionally listed end, the Elastic Clause provides the authority."
    },
    {
        "q": "Congress passes a law and the President signs it. Later, Congress tries to punish a specific person without a trial using a law. What constitutional restriction is being violated?",
        "a": "It violates constitutional limits on Congress (due process protections)",
        "key": "punish a specific person without a trial",
        "topic": "Article I – Legislative",
        "hint": "The Constitution specifically bans Congress from passing bills that target and punish named individuals — that power belongs to courts, not legislatures, and blurring that line was a tool of tyranny the framers knew well from English history."
    },
    {
        "q": "Congress passes a law applying only to one individual, declaring them guilty of a crime without court proceedings. What is this called?",
        "a": "Bill of attainder",
        "key": "guilty of a crime without court proceedings",
        "topic": "Article I – Legislative",
        "hint": "English kings used these legislative punishments to destroy political enemies without the inconvenience of a trial — the framers banned them in Article I because they were one of the most infamous tools of tyranny in the history of governance."
    },
    {
        "q": "Congress passes a law requiring people to be punished for actions that were legal when committed. What constitutional restriction is violated?",
        "a": "Ex post facto law",
        "key": "punished for actions that were legal when committed",
        "topic": "Article I – Legislative",
        "hint": "From the Latin meaning 'after the fact,' this ban means Congress cannot criminalize behavior retroactively — you can only be punished for breaking a rule that existed at the time you broke it, a bedrock principle of fair law."
    },
    {
        "q": "A representative is elected from a large state and a senator is elected from the same state. Which constitutional idea explains why their constituencies are represented differently?",
        "a": "Great Compromise (House by population, Senate equal)",
        "key": "constituencies are represented differently",
        "topic": "Article I – Legislative",
        "hint": "Roger Sherman of Connecticut proposed the solution that saved the Constitutional Convention — large states get proportional representation in the House, small states get equal representation in the Senate, and everyone goes home happy."
    },

    # ── Article II — Scenario ─────────────────────────────────────────
    {
        "q": "Congress passes a bill, but the President returns it unsigned with objections. What formal power is the President using?",
        "a": "Veto",
        "key": "returns it unsigned with objections",
        "topic": "Article II – Executive",
        "hint": "When a President sends a bill back to Congress with written objections, it triggers a constitutional showdown — Congress must now assemble a rare two-thirds supermajority in both chambers to override the rejection."
    },
    {
        "q": "The President signs a treaty with another country. What must happen next for the treaty to take effect under the Constitution?",
        "a": "Senate must approve by a two-thirds vote",
        "key": "treaty to take effect under the Constitution",
        "topic": "Article II – Executive",
        "hint": "Woodrow Wilson negotiated the Treaty of Versailles and the League of Nations after WWI, but the Senate refused to ratify it — demonstrating that a presidential signature on an international agreement means nothing without Senate consent."
    },
    {
        "q": "The President nominates a Supreme Court justice. Which body must confirm the nominee?",
        "a": "U.S. Senate",
        "key": "nominates a Supreme Court justice",
        "topic": "Article II – Executive",
        "hint": "This confirmation process — now televised and contested — was designed so that a President could not simply install a loyalist for life on the nation's highest court without the consent of the chamber representing all the states."
    },
    {
        "q": "During a military conflict, the President orders troops into action. Which constitutional role supports the President's authority in this situation?",
        "a": "Commander in Chief",
        "key": "orders troops into action",
        "topic": "Article II – Executive",
        "hint": "Article II gives the President direct command of the military — but Congress holds the formal power to declare war, creating a constitutional tension that has never been fully resolved and that every wartime President has navigated differently."
    },
    {
        "q": "A President directs executive agencies to enforce environmental laws. Which constitutional duty is being carried out?",
        "a": "Take Care Clause (faithfully execute the laws)",
        "key": "directs executive agencies to enforce environmental laws",
        "topic": "Article II – Executive",
        "hint": "This clause makes the President constitutionally responsible for ensuring all laws are enforced — even laws the President personally opposes — because the executive branch exists to carry out the will of Congress, not to substitute its own judgment."
    },
    {
        "q": "A President issues an executive order that critics claim goes beyond the Constitution and laws passed by Congress. Which branch has the power to review and possibly invalidate the action?",
        "a": "Judicial branch (courts can review constitutionality)",
        "key": "goes beyond the Constitution and laws passed by Congress",
        "topic": "Article II – Executive",
        "hint": "President Truman learned this lesson in 1952 when the Supreme Court struck down his executive order seizing steel mills during the Korean War — even wartime emergency does not give a President unlimited legislative power."
    },
    {
        "q": "A President wants to remove a top executive official who opposes the President's policy. Which constitutional principle supports the President's control over the executive branch?",
        "a": "Executive control / unitary executive principle (presidential removal power concept)",
        "key": "President's control over the executive branch",
        "topic": "Article II – Executive",
        "hint": "The Supreme Court ruled in 1926 that since the President is responsible for executing the laws, the President must be able to fire executive officers who refuse to carry out that mission — otherwise accountability becomes impossible."
    },
    {
        "q": "The President is accused of using official power for personal gain. Which constitutional process can remove the President from office?",
        "a": "Impeachment (House impeaches, Senate convicts)",
        "key": "remove the President from office",
        "topic": "Article II – Executive",
        "hint": "The Constitution requires 'high crimes and misdemeanors' for this process — a deliberately vague standard that the framers left flexible, knowing that the worst abuses of executive power might be political and moral, not necessarily criminal."
    },
    {
        "q": "A President refuses to follow a law passed by Congress that is constitutional. Which constitutional duty is being violated?",
        "a": "Take Care Clause duty is violated (failure to enforce the law)",
        "key": "refuses to follow a law passed by Congress",
        "topic": "Article II – Executive",
        "hint": "A President has no constitutional authority to simply ignore a law the President dislikes — the Take Care Clause makes faithfully executing valid law a presidential duty, not an optional preference."
    },
    {
        "q": "A President pardons someone convicted of a federal crime. Which type of presidential power is being used?",
        "a": "Pardon power (executive clemency)",
        "key": "pardons someone convicted of a federal crime",
        "topic": "Article II – Executive",
        "hint": "This power is almost unlimited — a President can pardon anyone for any federal offense, before or after conviction, and the pardon cannot be overridden by Congress or reviewed by courts, making it one of the few truly unchecked presidential powers."
    },

    # ── Article III — Scenario ────────────────────────────────────────
    {
        "q": "A federal court rules that a state law violates the U.S. Constitution. Which principle allows courts to strike down unconstitutional laws?",
        "a": "Judicial review",
        "key": "courts to strike down unconstitutional laws",
        "topic": "Article III – Judicial",
        "hint": "Chief Justice John Marshall invented this power for the Court in 1803, and it was controversial from the start — nowhere does the Constitution say courts can void laws, but Marshall argued that if courts cannot enforce the Constitution, it is not truly supreme."
    },
    {
        "q": "A person argues that their First Amendment rights were violated by a state law. Why can the case be heard in federal court?",
        "a": "It involves a constitutional issue/federal question (federal law)",
        "key": "First Amendment rights were violated",
        "topic": "Article III – Judicial",
        "hint": "Federal courts have jurisdiction over any case that turns on the meaning of the Constitution or federal law — so any time someone claims their constitutional rights were violated, federal courts can hear the dispute regardless of whether a state is involved."
    },
    {
        "q": "Congress passes a law, and soon after, the Supreme Court declares it unconstitutional. What power is the Court using?",
        "a": "Judicial review",
        "key": "Supreme Court declares it unconstitutional",
        "topic": "Article III – Judicial",
        "hint": "When nine unelected justices can permanently invalidate a law passed by 535 elected representatives and signed by the President, it raises profound questions about democracy — questions that have been debated ever since Marbury v. Madison."
    },
    {
        "q": "A federal judge makes unpopular rulings, but cannot easily be removed from office. What constitutional feature explains this independence?",
        "a": "Life tenure during good behavior",
        "key": "cannot easily be removed from office",
        "topic": "Article III – Judicial",
        "hint": "Alexander Hamilton argued in Federalist No. 78 that judges need lifetime appointments to be truly independent — a judge who fears being fired for an unpopular ruling will decide cases based on politics, not law."
    },
    {
        "q": "Two states dispute the location of their border. Which court is most likely to have original jurisdiction?",
        "a": "The U.S. Supreme Court",
        "key": "Two states dispute the location of their border",
        "topic": "Article III – Judicial",
        "hint": "Article III gives the Supreme Court original jurisdiction — meaning it is the first and only court to hear the case — in disputes between states, because no state court could fairly hear a case in which its own state is a party."
    },
    {
        "q": "A citizen is charged with treason for helping an enemy during war. Which Article defines treason and sets rules for convicting someone of it?",
        "a": "Article III",
        "key": "defines treason and sets rules for convicting",
        "topic": "Article III – Judicial",
        "hint": "The framers put the definition of treason directly in the Constitution — rather than leaving it to Congress — because they had seen treason charges used by British kings to silence political opposition and did not want the same weapon in American hands."
    },
    {
        "q": "A defendant argues their confession was forced by police threats. Which general constitutional principle protects against coerced confessions (due process)?",
        "a": "Due process (Fifth/Fourteenth Amendment principles)",
        "key": "confession was forced by police threats",
        "topic": "Article III – Judicial",
        "hint": "The Supreme Court ruled in 1936 that a confession beaten out of a suspect by Mississippi deputies was so fundamentally unfair that it violated the Constitution — establishing that the method of obtaining evidence matters as much as the evidence itself."
    },
    {
        "q": "A state passes a law that conflicts with a federal court ruling interpreting the Constitution. Which branch's interpretation prevails, and why?",
        "a": "Judicial branch interpretation prevails (courts interpret the Constitution)",
        "key": "state passes a law that conflicts with a federal court ruling",
        "topic": "Article III – Judicial",
        "hint": "When Arkansas tried to pass a law overriding the Supreme Court's school desegregation ruling, all nine justices signed a single opinion declaring that state officials are bound by the Court's constitutional interpretations — period."
    },

    # ── Article IV — Scenario ─────────────────────────────────────────
    {
        "q": "A couple legally marries in State A and moves to State B. State B must recognize the marriage license from State A. Which clause requires this?",
        "a": "Full Faith and Credit Clause",
        "key": "State B must recognize the marriage license",
        "topic": "Article IV – States",
        "hint": "Without this clause, a couple married in one state would legally become strangers the moment they crossed a state line — making interstate life unworkable and turning state borders into legal barriers to ordinary life."
    },
    {
        "q": "A person commits a felony in State X, then flees to State Y. State X requests the person be returned to face trial. Which clause applies?",
        "a": "Extradition Clause",
        "key": "flees to State Y",
        "topic": "Article IV – States",
        "hint": "The word 'extradition' means handing someone over to another jurisdiction for trial — and this clause ensures that criminals cannot use state borders as an escape hatch from the justice system."
    },
    {
        "q": "A state denies citizens from other states access to its courts for the same protections its own citizens receive. Which clause is being violated?",
        "a": "Privileges and Immunities Clause",
        "key": "citizens from other states access to its courts",
        "topic": "Article IV – States",
        "hint": "This clause prevents states from treating out-of-staters as second-class visitors — it was designed to create genuine national unity by ensuring that an American's basic rights travel with them across every state border."
    },
    {
        "q": "State A's court issues a custody order. The parent moves to State B, and State B must enforce the order. Which clause requires this?",
        "a": "Full Faith and Credit Clause",
        "key": "State B must enforce the order",
        "topic": "Article IV – States",
        "hint": "This clause turns every state's court system into a 50-state enforcement network — a child custody ruling, a civil judgment, or a legal document from any state carries full legal weight in every other state."
    },
    {
        "q": "Congress votes to admit a new state into the United States. Which Article describes the process for admitting new states?",
        "a": "Article IV",
        "key": "process for admitting new states",
        "topic": "Article IV – States",
        "hint": "Under Article IV, Congress has sole power to admit new states — and the process was used 37 times after the original 13, most recently when Hawaii and Alaska joined in 1959 after decades of petitioning for statehood."
    },
    {
        "q": "A state tries to replace its elected legislature with a monarchy-style ruler. Which constitutional guarantee would be violated?",
        "a": "Guarantee Clause (republican form of government)",
        "key": "replace its elected legislature with a monarchy-style ruler",
        "topic": "Article IV – States",
        "hint": "The framers guaranteed every state a 'republican form of government' — meaning an elected representative system — because they feared that a state captured by a demagogue or monarch could undermine the entire democratic experiment."
    },
    {
        "q": "A hurricane devastates one state, and the national government provides aid and protection. Which Article's ideas support cooperation among states and the federal government?",
        "a": "Article IV (states' relations/cooperation concepts)",
        "key": "national government provides aid and protection",
        "topic": "Article IV – States",
        "hint": "Article IV's guarantee of federal protection to every state was designed precisely for moments of crisis — the framers envisioned an active federal role in defending states against invasion, domestic violence, and disasters."
    },

    # ── Article V — Scenario ──────────────────────────────────────────
    {
        "q": "A proposed amendment passes both the House and Senate by a two-thirds vote. What must happen next for it to become part of the Constitution?",
        "a": "Ratification by three-fourths of the states",
        "key": "What must happen next for it to become part of the Constitution",
        "topic": "Article V – Amendments",
        "hint": "Congressional approval is only the beginning — 38 states must then independently agree, a process that took 202 years for the 27th Amendment (proposed in 1789, ratified in 1992) to complete."
    },
    {
        "q": "A proposed amendment is supported by many states, and two-thirds of state legislatures demand a convention. What is this step called?",
        "a": "A national convention to propose amendments (constitutional convention method)",
        "key": "two-thirds of state legislatures demand a convention",
        "topic": "Article V – Amendments",
        "hint": "This method — written into Article V as a safety valve if Congress refuses to propose needed amendments — has never been used in American history, and many constitutional scholars fear it could open the entire Constitution to wholesale revision."
    },
    {
        "q": "Thirty-eight states approve an amendment. Why is this number significant?",
        "a": "It equals three-fourths of the states (required for ratification)",
        "key": "Thirty-eight states approve an amendment",
        "topic": "Article V – Amendments",
        "hint": "38 out of 50 is exactly three-quarters — the constitutional threshold the framers set for ratification, a number chosen to ensure amendments reflect a true national consensus rather than a bare or regional majority."
    },
    {
        "q": "Congress proposes an amendment, but only a simple majority of states approve it. What happens to the amendment?",
        "a": "It fails (does not become part of the Constitution)",
        "key": "only a simple majority of states approve it",
        "topic": "Article V – Amendments",
        "hint": "The Equal Rights Amendment is the most famous example — it passed Congress and was ratified by many states but ultimately fell short of the three-fourths threshold, leaving it in constitutional limbo for decades."
    },
    {
        "q": "A citizen argues the Constitution should be easy to change like a regular law. Which Article shows the Constitution was designed to be harder to change, and how?",
        "a": "Article V; it requires supermajorities to propose and ratify amendments",
        "key": "harder to change",
        "topic": "Article V – Amendments",
        "hint": "In 230+ years, thousands of amendments have been proposed in Congress — only 27 have ever made it through the gauntlet of supermajority approval in Congress AND ratification by three-fourths of the states."
    },

    # ── Article VI — Scenario ─────────────────────────────────────────
    {
        "q": "A state law allows something that federal law prohibits. A court must decide which law controls. Which clause resolves this conflict?",
        "a": "Supremacy Clause",
        "key": "state law allows something that federal law prohibits",
        "topic": "Article VI – Supremacy",
        "hint": "When Arizona passed an immigration enforcement law that conflicted with federal immigration policy, the Supreme Court invoked this clause — the Constitution's explicit declaration that federal law is 'the supreme Law of the Land.'"
    },
    {
        "q": "A state judge refuses to enforce a federal law because they personally disagree with it. Which constitutional requirement is being ignored?",
        "a": "Oath of office requirement to support the Constitution",
        "key": "refuses to enforce a federal law",
        "topic": "Article VI – Supremacy",
        "hint": "Article VI binds state judges — not just federal ones — to follow the Constitution and federal law, and every judge swears an oath to that effect before taking the bench, making personal disagreement constitutionally irrelevant."
    },
    {
        "q": "A state requires all elected officials to pass a test proving they follow a specific religion. Which constitutional rule is violated?",
        "a": "No religious test clause",
        "key": "pass a test proving they follow a specific religion",
        "topic": "Article VI – Supremacy",
        "hint": "At the founding, several states had official Protestant Christianity requirements for officeholders — Article VI broke sharply with that tradition, making the United States one of the first governments in history to separate religion from political eligibility."
    },
    {
        "q": "A state constitution conflicts with the U.S. Constitution. Which legal authority is highest and must be followed?",
        "a": "The U.S. Constitution is supreme",
        "key": "state constitution conflicts with the U.S. Constitution",
        "topic": "Article VI – Supremacy",
        "hint": "The Supremacy Clause creates a clear legal hierarchy — the U.S. Constitution sits at the top, followed by federal laws and treaties, and state constitutions and laws must yield whenever they conflict with any of these higher authorities."
    },
    {
        "q": "A state passes a law that contradicts a treaty ratified by the United States. Under the Constitution, what is the correct outcome?",
        "a": "Federal treaty prevails over conflicting state law (Supremacy Clause)",
        "key": "contradicts a treaty ratified by the United States",
        "topic": "Article VI – Supremacy",
        "hint": "The Supremacy Clause lists treaties alongside the Constitution and federal laws as part of 'the supreme Law of the Land' — meaning a state cannot opt out of an international agreement the nation has legally committed to."
    },

    # ── Article VII — Scenario ────────────────────────────────────────
    {
        "q": "After the Constitution was written, it did not require all 13 states to approve it before taking effect. What did it require instead?",
        "a": "Ratification by 9 states",
        "key": "did not require all 13 states to approve",
        "topic": "Article VII – Ratification",
        "hint": "The framers deliberately avoided the Articles of Confederation's fatal unanimity rule — they knew Rhode Island (which refused to even send delegates to the Convention) would never ratify, so they set nine states as enough to launch the new government."
    },
    {
        "q": "A state holds a special meeting where citizens vote on whether to approve the Constitution. What is this type of meeting called?",
        "a": "State ratifying convention",
        "key": "special meeting where citizens vote on whether to approve the Constitution",
        "topic": "Article VII – Ratification",
        "hint": "By using elected conventions rather than state legislatures, the framers gave the Constitution an extra layer of democratic legitimacy — the people themselves were approving it, not just their established politicians who might resist losing power."
    },
    {
        "q": "Supporters argued the Constitution should take effect once 9 states approved it. Which Article describes this rule?",
        "a": "Article VII",
        "key": "take effect once 9 states approved it",
        "topic": "Article VII – Ratification",
        "hint": "New Hampshire was the crucial ninth state — when it ratified on June 21, 1788, the Constitution technically took effect, though everyone knew the new government couldn't really work without the large states of Virginia and New York."
    },

    # ── Checks & Balances / Separation of Powers — Scenario ──────────
    {
        "q": "Congress passes a bill, the President vetoes it, and Congress votes again and the bill becomes law anyway. What happened?",
        "a": "Congress overrode the veto with a two-thirds vote in both houses",
        "key": "becomes law anyway",
        "topic": "Checks & Balances",
        "hint": "This is one of the rarest events in American government — mustering two-thirds of the House and two-thirds of the Senate against a sitting President requires a bipartisan supermajority that is almost impossible to assemble."
    },
    {
        "q": "The President appoints an ambassador, but the Senate refuses to approve the appointment. What principle is being demonstrated?",
        "a": "Checks and balances (Senate advice and consent)",
        "key": "Senate refuses to approve the appointment",
        "topic": "Checks & Balances",
        "hint": "The Senate's role in confirming presidential appointments was designed so that no President could staff the government, courts, and diplomatic corps entirely with unqualified loyalists — the other elected branch must agree."
    },
    {
        "q": "The Supreme Court rules that a law violates the Constitution, even though the law was popular. What principle is shown?",
        "a": "Judicial review / checks and balances",
        "key": "Supreme Court rules that a law violates the Constitution",
        "topic": "Checks & Balances",
        "hint": "This is the defining feature of constitutional government — the idea that certain rights and limits are beyond the reach of popular majorities, and that unelected judges serve as the ultimate guardians of those limits."
    },
    {
        "q": "Congress threatens to remove Supreme Court justices because it dislikes a decision. What constitutional idea protects judicial independence?",
        "a": "Life tenure and separation of powers protect independence",
        "key": "remove Supreme Court justices because it dislikes a decision",
        "topic": "Checks & Balances",
        "hint": "Federal judges can only be removed through impeachment for misconduct — never for unpopular rulings — so Congress cannot punish the Court for decisions it dislikes, a protection Alexander Hamilton called essential to the rule of law."
    },
    {
        "q": "A President tries to make laws without Congress by issuing executive orders that function like statutes. Which constitutional principle limits this?",
        "a": "Separation of powers (lawmaking is mainly legislative)",
        "key": "make laws without Congress",
        "topic": "Checks & Balances",
        "hint": "The very first sentence of Article I declares that 'All legislative Powers herein granted shall be vested in a Congress' — not in a President — making unilateral executive lawmaking a direct violation of the Constitution's fundamental structure."
    },
    {
        "q": "The House impeaches a President, but the Senate fails to reach the required vote to convict. What is the result?",
        "a": "The President is acquitted and stays in office",
        "key": "Senate fails to reach the required vote to convict",
        "topic": "Checks & Balances",
        "hint": "Andrew Johnson, Bill Clinton, and Donald Trump (twice) were all impeached by the House but acquitted by the Senate — demonstrating that impeachment is a political process, and two-thirds of the Senate is an enormously high bar to reach."
    },
    {
        "q": "Congress creates a law enforcing its own interpretation of the Constitution, but the Supreme Court issues a different interpretation in a case. Which interpretation controls in that case?",
        "a": "The Supreme Court's interpretation controls in the case (judicial review)",
        "key": "Supreme Court issues a different interpretation",
        "topic": "Checks & Balances",
        "hint": "Since Marbury v. Madison, it has been settled that the Supreme Court has the final word on what the Constitution means in actual legal cases — Congress can pass laws all it wants, but the Court decides whether those laws comply with the Constitution."
    },

    # ── Federalism — Scenario ──────────────────────────────────────────
    {
        "q": "The federal government sets a nationwide minimum age to vote in federal elections. States must follow it. Which power relationship is this?",
        "a": "Federal supremacy / delegated national authority in elections (federal law prevails)",
        "key": "States must follow it",
        "topic": "Federalism",
        "hint": "The 26th Amendment set the voting age at 18 nationwide — and while states can set other election rules, they cannot override a constitutional provision or a valid federal law governing federal elections."
    },
    {
        "q": "A state sets speed limits and requires driver's licenses. The federal government generally allows states to do this. What kind of power is this?",
        "a": "Reserved power (state police power)",
        "key": "speed limits and requires driver's licenses",
        "topic": "Federalism",
        "hint": "Traffic laws, marriage licenses, education standards, and most criminal law are all examples of this type of power — authority that the 10th Amendment reserves to states for the day-to-day governance of their citizens' lives."
    },
    {
        "q": "Both the state and federal government can tax income. What kind of power is this?",
        "a": "Concurrent power",
        "key": "Both the state and federal government can tax",
        "topic": "Federalism",
        "hint": "Your paycheck can be taxed by Washington and by your state capital at the same time — this is one of the clearest examples of a power that both levels of government legitimately share under the constitutional design."
    },
    {
        "q": "The national government declares war, but states also maintain National Guard units. Which constitutional system is being shown?",
        "a": "Federalism",
        "key": "national government declares war, but states also maintain National Guard units",
        "topic": "Federalism",
        "hint": "Under the constitutional design, the President commands the military as Commander in Chief, but each state maintains its own Guard units that can be called up for state emergencies or federalized by the President — a uniquely American military federalism."
    },
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
        self.dialog.title("Quiz Setup – Articles (Origins & Purposes of Law and Government)")
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
        self.root.title('FCLE – Origins & Purposes of Law and Government: "Articles"')
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
