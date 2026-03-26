## Written by Scott Johnson       2026/02/09
## For the Youtube Channel: Software Nuggets
## https://www.youtube.com/c/softwareNuggets
## Version 3  — Smart engine from supreme_court_cases_v3.py merged into
##              american_democracy_v3.py
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
        "q": "What is democracy?",
        "a": "A system of government in which power comes from the people",
        "key": "define democracy",
        "topic": "Democracy Basics",
        "hint": "Key words: power comes from the people. Democracy means the citizens have a say in how they are governed. The word comes from the Greek words 'demos' (people) and 'kratos' (rule). The United States is a representative democracy, meaning voters choose leaders to govern on their behalf."
    },
    {
        "q": "What is the difference between a direct democracy and a representative democracy?",
        "a": "In a direct democracy citizens vote on laws themselves; in a representative democracy citizens elect leaders to vote on laws for them",
        "key": "direct vs representative democracy",
        "topic": "Types of Democracy",
        "hint": "Key words: direct democracy, representative democracy. In ancient Athens, citizens voted directly on laws. The United States uses a representative democracy, also called a republic, because the country is too large for every citizen to vote on every issue."
    },
    {
        "q": "What type of government does the United States have?",
        "a": "A constitutional federal republic",
        "key": "type of U.S. government",
        "topic": "U.S. Government Type",
        "hint": "Key words: constitutional, federal, republic. The U.S. is a republic because citizens elect representatives. It is federal because power is shared between national and state governments. It is constitutional because government power is limited by the Constitution."
    },
    {
        "q": "What is the supreme law of the United States?",
        "a": "The Constitution",
        "key": "supreme law",
        "topic": "The Constitution",
        "hint": "Key words: supreme law of the land. The Constitution, written in 1787 and effective in 1789, is the highest law in the country. No federal or state law can legally conflict with it."
    },
    {
        "q": "What is the purpose of government according to the Declaration of Independence?",
        "a": "To protect the natural rights of its citizens",
        "key": "purpose of government Declaration",
        "topic": "Declaration of Independence",
        "hint": "Key words: purpose of government, natural rights. The Declaration of Independence, written by Thomas Jefferson in 1776, states that governments are created to protect people's rights to life, liberty, and the pursuit of happiness. If a government fails to do this, the people have the right to change it."
    },
    {
        "q": "What three natural rights does the Declaration of Independence identify?",
        "a": "Life, liberty, and the pursuit of happiness",
        "key": "three natural rights Declaration",
        "topic": "Declaration of Independence",
        "hint": "Key words: natural rights, Declaration of Independence. Thomas Jefferson wrote in 1776 that all people are 'endowed by their Creator with certain unalienable Rights,' which he listed as life, liberty, and the pursuit of happiness. These ideas came from philosopher John Locke."
    },
    {
        "q": "What political philosopher most influenced the idea that government must protect natural rights?",
        "a": "John Locke",
        "key": "philosopher natural rights",
        "topic": "Enlightenment Influences",
        "hint": "Key words: philosopher, natural rights, government protection. John Locke, an English philosopher from the 1600s, wrote that people have natural rights to life, liberty, and property. Thomas Jefferson drew heavily on Locke's ideas when writing the Declaration of Independence."
    },
    {
        "q": "What is the social contract theory?",
        "a": "The idea that people agree to give up some freedoms to government in exchange for the protection of their remaining rights",
        "key": "social contract",
        "topic": "Social Contract",
        "hint": "Key words: agree to give up freedoms in exchange for protection. The social contract theory, associated with John Locke and Jean-Jacques Rousseau, says citizens and government have a mutual agreement. Citizens obey government, and government protects their rights."
    },
    {
        "q": "What does the phrase 'consent of the governed' mean?",
        "a": "Government authority comes from the agreement and approval of the people being governed",
        "key": "consent of the governed",
        "topic": "Consent of the Governed",
        "hint": "Key words: consent of the governed. This phrase from the Declaration of Independence means a government's power is only legitimate if the people agree to it. It is why Americans hold elections to give the people a voice in who governs them."
    },
    {
        "q": "What is a citizen?",
        "a": "A person who owes loyalty to and is entitled to the protection of a nation",
        "key": "define citizen",
        "topic": "Citizenship",
        "hint": "Key words: loyalty, entitled to protection. A citizen has both rights and responsibilities within a country. In the United States, citizenship can be gained by birth on U.S. soil, birth to a U.S. parent, or through a legal process called naturalization."
    },
    {
        "q": "What are the two ways a person can become a U.S. citizen?",
        "a": "By birth or through naturalization",
        "key": "two ways become citizen",
        "topic": "Citizenship",
        "hint": "Key words: birth, naturalization. A person born on U.S. soil or born to a U.S. citizen parent is automatically a citizen. A foreign-born person can become a citizen through naturalization, a legal process that includes a civics test and oath of allegiance."
    },
    {
        "q": "What is naturalization?",
        "a": "The legal process by which a foreign-born person becomes a U.S. citizen",
        "key": "define naturalization",
        "topic": "Naturalization",
        "hint": "Key words: legal process, foreign-born, becomes a citizen. To become a naturalized citizen, a person must live in the U.S. for a required time, pass a background check, demonstrate basic English, and pass a civics test. The Fourteenth Amendment and federal law govern this process."
    },
    {
        "q": "What is the right to vote called?",
        "a": "Suffrage",
        "key": "right to vote",
        "topic": "Suffrage",
        "hint": "Key words: right to vote. Suffrage means the legal right to vote in public elections. In early America, only white male property owners could vote. Over time, amendments and laws expanded suffrage to Black men, women, and citizens 18 and older."
    },
    {
        "q": "What is civic participation?",
        "a": "Taking part in activities that help govern the community and nation, such as voting, running for office, or volunteering",
        "key": "civic participation",
        "topic": "Civic Responsibility",
        "hint": "Key words: taking part in governing the community. Civic participation includes voting, contacting elected officials, serving on juries, attending public meetings, and volunteering. Democracy depends on citizens staying involved in their government."
    },
    {
        "q": "What is the most important civic duty in a democracy?",
        "a": "Voting",
        "key": "most important civic duty",
        "topic": "Voting",
        "hint": "Key words: most important civic duty in a democracy. Voting allows citizens to choose their leaders and influence government policy. Many Americans have fought and died to secure the right to vote for all citizens, and casting a ballot is considered the foundation of democratic participation."
    },
    {
        "q": "What is a political party?",
        "a": "An organized group of people with shared political views who work together to win elections and control government",
        "key": "define political party",
        "topic": "Political Parties",
        "hint": "Key words: organized group, shared views, win elections. Political parties help voters understand candidates' positions and help elected officials work together. The United States has a two-party system dominated by the Democratic and Republican parties, though third parties also exist."
    },
    {
        "q": "What are the two major political parties in the United States today?",
        "a": "The Democratic Party and the Republican Party",
        "key": "two major parties",
        "topic": "Political Parties",
        "hint": "Key words: two major political parties. The Democratic Party and the Republican Party have dominated U.S. politics since the Civil War era. Democrats generally favor a more active government, while Republicans generally favor less government intervention."
    },
    {
        "q": "What is an election?",
        "a": "A formal process by which citizens vote to choose government officials or decide on public issues",
        "key": "define election",
        "topic": "Elections",
        "hint": "Key words: citizens vote, choose officials. Elections are the main mechanism through which democracy operates. In the United States, elections are held at local, state, and national levels to fill offices and sometimes to vote on ballot measures."
    },
    {
        "q": "How often are presidential elections held in the United States?",
        "a": "Every four years",
        "key": "presidential election frequency",
        "topic": "Presidential Elections",
        "hint": "Key words: how often are presidential elections held. Presidential elections occur every four years on the first Tuesday after the first Monday in November. This schedule has been followed since 1792."
    },
    {
        "q": "What is the Electoral College?",
        "a": "The body of electors chosen by each state to formally elect the president and vice president",
        "key": "Electoral College",
        "topic": "Electoral College",
        "hint": "Key words: body of electors, elect the president. The Electoral College was created by the Constitution in 1787 as a compromise. Each state gets a number of electors equal to its total number of senators and representatives. A candidate needs 270 electoral votes to win the presidency."
    },
    {
        "q": "How many electoral votes are needed to win the presidency?",
        "a": "270",
        "key": "electoral votes needed",
        "topic": "Electoral College",
        "hint": "Key words: 270 electoral votes to win. There are 538 total electoral votes. A majority, which is 270, is needed to win the presidency. If no candidate reaches 270, the House of Representatives chooses the president."
    },
    {
        "q": "What happens if no presidential candidate wins a majority in the Electoral College?",
        "a": "The House of Representatives chooses the president",
        "key": "no Electoral College majority",
        "topic": "Electoral College",
        "hint": "Key words: no Electoral College majority, House chooses president. If no candidate gets 270 electoral votes, the Constitution sends the decision to the House of Representatives. This happened in 1824 when the House chose John Quincy Adams."
    },
    {
        "q": "What is a primary election?",
        "a": "An election in which members of a political party vote to choose their candidate for a general election",
        "key": "define primary election",
        "topic": "Primary Elections",
        "hint": "Key words: party members vote to choose a candidate. In a primary, voters within a party pick who will represent them in the general election. Presidential primaries, held state by state, determine which candidate a party will nominate for president."
    },
    {
        "q": "What is a general election?",
        "a": "The main election in which voters choose between candidates from different parties to fill a government office",
        "key": "define general election",
        "topic": "General Elections",
        "hint": "Key words: main election, voters choose between parties. The general election is where the actual officeholders are decided. In the United States, the major general elections are held every two years in November."
    },
    {
        "q": "What is the purpose of the Census?",
        "a": "To count the population of the United States every ten years to distribute congressional seats and federal funding",
        "key": "purpose of Census",
        "topic": "Census",
        "hint": "Key words: count population, distribute seats, federal funding. The Census is required by Article I of the Constitution and is conducted every ten years. Its results determine how many House seats each state gets, a process called apportionment."
    },
    {
        "q": "What is apportionment?",
        "a": "The process of distributing House seats among the states based on population",
        "key": "define apportionment",
        "topic": "Apportionment",
        "hint": "Key words: distributing House seats based on population. After each Census, Congress reapportions the 435 House seats among the 50 states. States that grow in population may gain seats, and states that shrink may lose them."
    },
    {
        "q": "What is gerrymandering?",
        "a": "Drawing voting district boundaries in a way that gives one political party an unfair advantage",
        "key": "define gerrymandering",
        "topic": "Gerrymandering",
        "hint": "Key words: drawing voting districts unfairly. Gerrymandering is when a political party in power redraws district lines to concentrate or spread out opposing voters to win more seats. The term comes from Governor Elbridge Gerry, who signed an oddly shaped district into law in 1812."
    },
    {
        "q": "What is free speech?",
        "a": "The right of citizens to express opinions without government censorship or punishment",
        "key": "define free speech",
        "topic": "Free Speech",
        "hint": "Key words: express opinions, no government censorship. Free speech is protected by the First Amendment, added in 1791. It allows citizens to criticize the government, discuss political ideas, and express themselves freely, which is considered essential to a functioning democracy."
    },
    {
        "q": "Does the First Amendment protect all forms of speech absolutely?",
        "a": "No, some forms of speech such as incitement to violence or true threats can be restricted",
        "key": "limits on free speech",
        "topic": "Free Speech",
        "hint": "Key words: not all speech is absolutely protected. The Supreme Court has ruled that certain speech is not protected, including direct incitement to imminent lawless action, true threats, and defamation. The government still cannot broadly restrict political or social speech."
    },
    {
        "q": "What is freedom of the press?",
        "a": "The right of news organizations and journalists to report and publish information without government control",
        "key": "freedom of the press",
        "topic": "Free Press",
        "hint": "Key words: journalists report without government control. Freedom of the press is protected by the First Amendment and is considered a watchdog function in a democracy. A free press can investigate government wrongdoing and keep citizens informed."
    },
    {
        "q": "Why is a free press important in a democracy?",
        "a": "It keeps citizens informed and holds government accountable",
        "key": "why free press important",
        "topic": "Free Press",
        "hint": "Key words: informed citizens, hold government accountable. A free press is sometimes called the Fourth Estate because it acts as a check on government power alongside the three branches. Without a free press, citizens cannot make informed decisions about their leaders."
    },
    {
        "q": "What is the right to petition?",
        "a": "The right to ask the government to take action or correct a wrong",
        "key": "right to petition",
        "topic": "First Amendment Rights",
        "hint": "Key words: ask government to take action. The right to petition is protected by the First Amendment. It means citizens can sign petitions, contact elected officials, or even sue the government to address grievances."
    },
    {
        "q": "What is freedom of assembly?",
        "a": "The right to gather peacefully in groups for any lawful purpose",
        "key": "freedom of assembly",
        "topic": "First Amendment Rights",
        "hint": "Key words: gather peacefully in groups. Freedom of assembly, protected by the First Amendment, allows citizens to hold protests, parades, rallies, and public meetings. The government cannot ban peaceful gatherings simply because it dislikes the message."
    },
    {
        "q": "What is majority rule?",
        "a": "The principle that the decision supported by more than half of the voters or legislators is adopted",
        "key": "majority rule",
        "topic": "Democratic Principles",
        "hint": "Key words: decision supported by more than half. Majority rule is a basic principle of democracy meaning more votes wins. However, in the United States, majority rule is balanced with minority rights, so a majority cannot vote to take away the rights of a smaller group."
    },
    {
        "q": "What are minority rights in a democracy?",
        "a": "Protections that ensure the majority cannot violate the basic rights of individuals or smaller groups",
        "key": "minority rights",
        "topic": "Minority Rights",
        "hint": "Key words: majority cannot violate rights of smaller groups. In a democracy, the majority makes decisions, but cannot strip away the fundamental rights of individuals or minorities. This balance is enforced through the Constitution and the courts."
    },
    {
        "q": "What is limited government?",
        "a": "A government whose powers are restricted by law, especially by a constitution",
        "key": "define limited government",
        "topic": "Limited Government",
        "hint": "Key words: government power restricted by law. Limited government means the government cannot do whatever it wants. The Constitution, the Bill of Rights, and separation of powers all work together to prevent any branch or official from having unlimited authority."
    },
    {
        "q": "What is the importance of the rule of law in a democracy?",
        "a": "It ensures that everyone, including government officials, is subject to the law and no one is above it",
        "key": "importance rule of law",
        "topic": "Rule of Law",
        "hint": "Key words: everyone subject to the law, no one above it. The rule of law is what prevents tyranny. If leaders could ignore the law, rights would not be safe. In the United States, even the president can be prosecuted for crimes."
    },
    {
        "q": "What is an independent judiciary?",
        "a": "A court system that makes decisions based on law, not on pressure from other branches or political groups",
        "key": "independent judiciary",
        "topic": "Judicial Independence",
        "hint": "Key words: courts decide based on law, not political pressure. An independent judiciary protects individual rights and the Constitution. In the United States, federal judges serve during good behavior, which in practice means for life, so they cannot easily be pressured by politicians."
    },
    {
        "q": "What is civil society?",
        "a": "The network of private organizations, community groups, and institutions that exist between government and individuals",
        "key": "define civil society",
        "topic": "Civil Society",
        "hint": "Key words: private organizations between government and citizens. Civil society includes churches, unions, civic clubs, charities, and advocacy groups. These organizations give citizens ways to participate in public life beyond just voting."
    },
    {
        "q": "What is the role of interest groups in American democracy?",
        "a": "They try to influence government policy on behalf of their members",
        "key": "role of interest groups",
        "topic": "Interest Groups",
        "hint": "Key words: influence government policy. Interest groups represent people with shared goals, such as environmental groups, business associations, and labor unions. They lobby Congress, make campaign contributions, and try to shape laws to benefit their members."
    },
    {
        "q": "What is lobbying?",
        "a": "The practice of attempting to influence government officials or legislators to support particular policies",
        "key": "define lobbying",
        "topic": "Lobbying",
        "hint": "Key words: influence government officials, support policies. Lobbying is a form of petition protected by the First Amendment. Lobbyists meet with lawmakers, provide research, and advocate for their clients' interests. Federal lobbyists must register with the government."
    },
    {
        "q": "What is public opinion?",
        "a": "The collective views and attitudes of citizens on political issues and government",
        "key": "define public opinion",
        "topic": "Public Opinion",
        "hint": "Key words: collective views of citizens. Public opinion refers to what the general population thinks about issues. Politicians pay attention to public opinion polls when making decisions, and public opinion can drive changes in law and policy."
    },
    {
        "q": "What role do elections play in a representative democracy?",
        "a": "They give citizens the power to choose their leaders and hold them accountable",
        "key": "role of elections",
        "topic": "Elections",
        "hint": "Key words: choose leaders, hold accountable. Elections are the primary mechanism of democratic accountability. If citizens are unhappy with elected officials, they can vote them out of office. This keeps leaders responsive to the people they represent."
    },
    {
        "q": "What is civic education?",
        "a": "Learning about the rights, responsibilities, and workings of government so citizens can participate effectively",
        "key": "civic education",
        "topic": "Civic Education",
        "hint": "Key words: learning rights, responsibilities, workings of government. Civic education teaches people how government works, what their rights are, and how to participate in democracy. Informed citizens are essential to a healthy democratic system."
    },
    {
        "q": "What does it mean to be an informed voter?",
        "a": "To understand the candidates, issues, and how government works before casting a ballot",
        "key": "informed voter",
        "topic": "Voting and Civic Duty",
        "hint": "Key words: understand candidates and issues before voting. An informed voter researches the candidates and issues before Election Day. Democracy works better when citizens vote based on knowledge rather than habit, appearance, or party alone."
    },
    {
        "q": "What is the separation of church and state?",
        "a": "The principle that government and religion operate independently and government cannot promote or favor any religion",
        "key": "separation church and state",
        "topic": "Church and State",
        "hint": "Key words: government and religion independent, no favoring religion. The First Amendment's Establishment Clause prevents the government from creating an official religion or favoring one faith over others. The phrase 'wall of separation between church and state' was used by Thomas Jefferson."
    },
    {
        "q": "What is equal protection under the law?",
        "a": "The guarantee that government must treat all people equally and cannot discriminate without just cause",
        "key": "equal protection",
        "topic": "Equal Protection",
        "hint": "Key words: government must treat all people equally. Equal protection is guaranteed by the Fourteenth Amendment, ratified in 1868. It means the government cannot discriminate against people based on race, national origin, or other protected characteristics without a legitimate reason."
    },
    {
        "q": "What landmark Supreme Court case ruled that racial segregation in public schools was unconstitutional?",
        "a": "Brown v. Board of Education",
        "key": "segregation unconstitutional schools",
        "topic": "Civil Rights",
        "hint": "Key words: racial segregation in schools unconstitutional. In 1954, the Supreme Court ruled in Brown v. Board of Education that segregating students by race in public schools violated the Fourteenth Amendment's equal protection guarantee. It overturned Plessy v. Ferguson's 'separate but equal' doctrine."
    },
    {
        "q": "What Supreme Court case established the 'separate but equal' doctrine that justified racial segregation?",
        "a": "Plessy v. Ferguson",
        "key": "separate but equal",
        "topic": "Civil Rights",
        "hint": "Key words: separate but equal. In 1896, the Supreme Court ruled in Plessy v. Ferguson that racial segregation was constitutional as long as facilities were 'separate but equal.' This doctrine was used to justify Jim Crow laws until it was overturned by Brown v. Board of Education in 1954."
    },
    {
        "q": "What is the Civil Rights Act of 1964?",
        "a": "A federal law that banned discrimination based on race, color, religion, sex, or national origin",
        "key": "Civil Rights Act 1964",
        "topic": "Civil Rights",
        "hint": "Key words: ban discrimination, race, sex, national origin. The Civil Rights Act of 1964, signed by President Lyndon B. Johnson, was a landmark law that made discrimination illegal in public places, employment, and any program receiving federal funding. It grew out of the Civil Rights Movement led by Dr. Martin Luther King Jr."
    },
    {
        "q": "What is the Voting Rights Act of 1965?",
        "a": "A federal law that banned discriminatory practices like literacy tests that had been used to prevent Black Americans from voting",
        "key": "Voting Rights Act 1965",
        "topic": "Voting Rights",
        "hint": "Key words: banned discriminatory voting practices, literacy tests. The Voting Rights Act of 1965, signed by President Lyndon B. Johnson, enforced the Fifteenth Amendment. It responded directly to violent attacks on peaceful marchers at Selma, Alabama, and dramatically expanded Black voter registration in the South."
    },
    {
        "q": "Who was the primary leader of the Civil Rights Movement?",
        "a": "Dr. Martin Luther King Jr.",
        "key": "Civil Rights Movement leader",
        "topic": "Civil Rights Movement",
        "hint": "Key words: leader of the Civil Rights Movement. Dr. Martin Luther King Jr. led the Civil Rights Movement in the 1950s and 1960s using nonviolent protest. He organized marches, delivered speeches including the famous 'I Have a Dream' speech in 1963, and helped win passage of the Civil Rights Act and Voting Rights Act."
    },
    {
        "q": "What is civil disobedience?",
        "a": "The deliberate, peaceful refusal to obey an unjust law to bring about change",
        "key": "define civil disobedience",
        "topic": "Civil Disobedience",
        "hint": "Key words: peaceful refusal to obey unjust law. Civil disobedience, practiced by leaders like Mahatma Gandhi and Dr. Martin Luther King Jr., means breaking unjust laws openly and nonviolently to draw attention to injustice and pressure the government to make changes."
    },
    {
        "q": "What is the significance of the Declaration of Independence to American democracy?",
        "a": "It declared independence from Britain and established the principles of equality, natural rights, and government by consent",
        "key": "significance Declaration of Independence",
        "topic": "Declaration of Independence",
        "hint": "Key words: declared independence, equality, natural rights, consent. The Declaration of Independence, written by Thomas Jefferson and adopted on July 4, 1776, is the founding statement of American democracy. It laid out the philosophical basis for the new nation: that all people are equal and government must protect their rights."
    },
    {
        "q": "What does 'all men are created equal' mean in the context of American democracy?",
        "a": "All people possess the same basic rights and dignity under the law regardless of birth or status",
        "key": "all men created equal meaning",
        "topic": "Equality",
        "hint": "Key words: same basic rights and dignity. This phrase from the Declaration of Independence, written in 1776, was radical at the time. It set an ideal the country has worked toward ever since, including through amendments that abolished slavery, guaranteed equal protection, and expanded voting rights."
    },
    {
        "q": "What is a constitutional amendment?",
        "a": "A formal change to the Constitution approved by Congress and ratified by three-fourths of the states",
        "key": "what is constitutional amendment",
        "topic": "Amendment Process",
        "hint": "Key words: formal change, approved by Congress, ratified by states. Amending the Constitution is intentionally difficult. An amendment must be proposed by a two-thirds vote in both houses of Congress, then ratified by three-fourths (38) of the 50 states."
    },
    {
        "q": "What does transparency in government mean?",
        "a": "Government operates openly so that citizens can see and understand what their officials are doing",
        "key": "government transparency",
        "topic": "Transparency",
        "hint": "Key words: government operates openly. Transparency means citizens can access information about government decisions. The Freedom of Information Act (FOIA) allows Americans to request government documents. Open government is essential for accountability in a democracy."
    },
    {
        "q": "What is the Freedom of Information Act (FOIA)?",
        "a": "A federal law that allows citizens to request access to government records",
        "key": "FOIA",
        "topic": "Government Transparency",
        "hint": "Key words: citizens request government records. The Freedom of Information Act, enacted in 1966, gives citizens the legal right to request documents from federal agencies. It promotes government transparency and is frequently used by journalists and researchers."
    },
    {
        "q": "What is the role of the citizen in a democracy?",
        "a": "To participate in government through voting, staying informed, obeying laws, paying taxes, and serving on juries",
        "key": "role of citizen in democracy",
        "topic": "Civic Responsibility",
        "hint": "Key words: participate in government. Democracy requires active citizens. Key responsibilities include voting, following the law, paying taxes, serving on juries when called, and staying informed about issues. Without engaged citizens, democratic government cannot function well."
    },
    {
        "q": "What does serving on a jury mean?",
        "a": "Being selected to hear the evidence in a trial and decide whether a defendant is guilty or not guilty",
        "key": "serve on jury",
        "topic": "Jury Duty",
        "hint": "Key words: hear evidence, decide guilt in a trial. Jury service is both a right and a civic duty. The Sixth Amendment guarantees the right to a jury trial. Citizens summoned for jury duty help ensure that defendants are judged by their fellow citizens, not just by government officials."
    },
    {
        "q": "What is a civil right?",
        "a": "A right guaranteed by the government that protects individuals from unfair treatment",
        "key": "define civil right",
        "topic": "Civil Rights",
        "hint": "Key words: government-guaranteed right, protects from unfair treatment. Civil rights are protections given by laws and the Constitution that prevent discrimination. Examples include the right to vote, equal treatment in public accommodations, and equal protection under law."
    },
    {
        "q": "What is a civil liberty?",
        "a": "A freedom that protects an individual from government interference, such as free speech or freedom of religion",
        "key": "define civil liberty",
        "topic": "Civil Liberties",
        "hint": "Key words: freedom, protects from government interference. Civil liberties are protections against government overreach and are mostly found in the Bill of Rights. Examples include freedom of speech, freedom of religion, and the right against unreasonable searches."
    },
    {
        "q": "What is due process?",
        "a": "The requirement that the government follow fair legal procedures before taking away a person's life, liberty, or property",
        "key": "define due process democracy",
        "topic": "Due Process",
        "hint": "Key words: fair legal procedures, life liberty property. Due process, protected by the Fifth and Fourteenth Amendments, means the government cannot punish, jail, or take from someone without following proper legal steps. It is a cornerstone of fair government."
    },
    {
        "q": "What is the principle of individual rights in American democracy?",
        "a": "The idea that every person has basic rights that cannot be taken away by the government without good cause",
        "key": "individual rights principle",
        "topic": "Individual Rights",
        "hint": "Key words: every person has basic rights, cannot be taken away. The Bill of Rights was added in 1791 specifically to protect individual rights from government abuse. These rights include speech, religion, due process, and others that exist to protect every person."
    },
    {
        "q": "What is the common good?",
        "a": "The overall well-being of all members of society, not just individuals or certain groups",
        "key": "define common good",
        "topic": "Common Good",
        "hint": "Key words: overall well-being of all members of society. Democratic governments must balance individual rights with the needs of the community. Policies like public education, highways, and public health programs exist to promote the common good even when they require all citizens to contribute."
    },
    {
        "q": "What is patriotism?",
        "a": "Love of and devotion to one's country, including supporting its values and institutions",
        "key": "define patriotism",
        "topic": "Patriotism",
        "hint": "Key words: love and devotion to one's country. Patriotism in a democracy does not just mean pride in the country, but also commitment to its founding ideals such as freedom, equality, and the rule of law. Voting, serving in the military, and obeying laws are all expressions of patriotism."
    },
    {
        "q": "What is the significance of the Gettysburg Address to American democracy?",
        "a": "President Lincoln redefined the Civil War as a struggle for equality and self-government, and honored those who died to preserve the Union",
        "key": "Gettysburg Address significance",
        "topic": "Gettysburg Address",
        "hint": "Key words: Lincoln, Civil War, equality, self-government. The Gettysburg Address was a short speech delivered by President Abraham Lincoln in November 1863 at the dedication of a military cemetery in Pennsylvania. Lincoln said the nation was dedicated to the proposition that all men are created equal and called on citizens to ensure that government of, by, and for the people shall not perish."
    },
    {
        "q": "What famous phrase from the Gettysburg Address describes democratic government?",
        "a": "Government of the people, by the people, for the people",
        "key": "Gettysburg phrase democracy",
        "topic": "Gettysburg Address",
        "hint": "Key words: government of by for the people. President Lincoln's phrase from 1863 summarizes the essence of American democracy: the government comes from the people, is run by the people, and serves the people. It remains one of the most famous descriptions of democracy."
    },
    {
        "q": "What is the significance of the Pledge of Allegiance?",
        "a": "It is a public declaration of loyalty to the United States and to the values of the republic",
        "key": "significance Pledge of Allegiance",
        "topic": "Pledge of Allegiance",
        "hint": "Key words: loyalty to the United States, values of the republic. The Pledge of Allegiance was written in 1892 and is recited in schools and public ceremonies. The phrase 'one nation, under God, indivisible, with liberty and justice for all' highlights unity and the democratic values of freedom and equal justice."
    },
    {
        "q": "What is federalism in the context of American democracy?",
        "a": "A system in which power is divided between the national government and state governments",
        "key": "federalism in democracy",
        "topic": "Federalism",
        "hint": "Key words: power divided, national and state governments. Federalism protects democracy by preventing any single government from holding all power. States can experiment with different policies, and the national government handles issues affecting the whole country."
    },
    {
        "q": "Why is free and fair elections considered the foundation of American democracy?",
        "a": "Because elections allow citizens to choose their leaders, hold officials accountable, and peacefully transfer power",
        "key": "free fair elections foundation",
        "topic": "Elections",
        "hint": "Key words: choose leaders, hold accountable, peaceful transfer of power. Free and fair elections ensure that government power comes from the people. Peaceful transfers of power after elections are a hallmark of stable democracy and have happened in the United States since 1797."
    },
    {
        "q": "What is the peaceful transfer of power?",
        "a": "When a newly elected government takes office without violence or forceful resistance from the outgoing government",
        "key": "peaceful transfer of power",
        "topic": "Democratic Stability",
        "hint": "Key words: new government takes office without violence. The peaceful transfer of power has been a cornerstone of American democracy since George Washington voluntarily stepped down after two terms in 1797. It symbolizes that no individual is above the democratic process."
    },
    {
        "q": "What is the significance of George Washington's decision to step down after two terms?",
        "a": "It established the tradition of peaceful transfer of power and showed that leaders serve the people, not themselves",
        "key": "Washington stepping down significance",
        "topic": "Democratic Traditions",
        "hint": "Key words: Washington, stepped down, tradition, peaceful transfer. When Washington voluntarily left office in 1797, he set the example that American presidents serve the people and do not cling to power. This tradition was later formalized by the Twenty-Second Amendment in 1951, limiting presidents to two terms."
    },
    {
        "q": "What does a constitutional democracy protect against?",
        "a": "Tyranny, abuse of power, and the violation of citizens' rights",
        "key": "constitutional democracy protects against",
        "topic": "Constitutional Democracy",
        "hint": "Key words: protects against tyranny, abuse of power. A constitutional democracy uses a constitution, separation of powers, checks and balances, and individual rights protections to prevent any person or group from abusing government power. This is why the framers designed the system with so many safeguards."
    },
    {
        "q": "What is a republic?",
        "a": "A form of government in which citizens elect representatives to make laws and run the government",
        "key": "define republic",
        "topic": "Republic",
        "hint": "Key words: citizens elect representatives to govern. A republic is a form of representative government. The United States is a republic, not a direct democracy, because citizens choose leaders to represent them rather than voting directly on every issue."
    },
    {
        "q": "What does 'checks and balances' mean in the context of American democracy?",
        "a": "Each branch of government has powers that can limit the other branches to prevent any one branch from becoming too powerful",
        "key": "checks balances democracy",
        "topic": "Checks and Balances",
        "hint": "Key words: each branch limits others, prevent too much power. Checks and balances make American democracy more stable. For example, the president can veto laws, Congress can override vetoes, and the Supreme Court can strike down unconstitutional laws."
    },
    {
        "q": "What is the right to a jury trial?",
        "a": "The constitutional guarantee that a person accused of a crime has the right to have their case decided by a group of fellow citizens",
        "key": "right jury trial",
        "topic": "Sixth Amendment",
        "hint": "Key words: accused person, decided by fellow citizens. The Sixth Amendment guarantees the right to a jury trial in criminal cases. This protects citizens from being convicted solely by government officials and ensures ordinary people have a role in the justice system."
    },
    {
        "q": "What is the significance of the Emancipation Proclamation?",
        "a": "It was President Lincoln's 1863 executive order declaring that enslaved people in Confederate states were free",
        "key": "Emancipation Proclamation significance",
        "topic": "Civil War and Democracy",
        "hint": "Key words: Lincoln, 1863, enslaved people declared free. The Emancipation Proclamation, issued on January 1, 1863, was a wartime measure that declared enslaved people in Confederate states to be free. While limited in scope, it transformed the Civil War into a war for freedom and paved the way for the Thirteenth Amendment."
    },
    {
        "q": "What was the significance of the Reconstruction Amendments (13th, 14th, and 15th) to American democracy?",
        "a": "They abolished slavery, guaranteed equal protection and citizenship, and prohibited denying the vote based on race",
        "key": "Reconstruction Amendments significance",
        "topic": "Reconstruction Amendments",
        "hint": "Key words: abolished slavery, equal protection, voting rights by race. The three Reconstruction Amendments, passed after the Civil War between 1865 and 1870, expanded democracy by formally ending slavery, granting equal citizenship to Black Americans, and protecting voting rights based on race."
    },
    {
        "q": "What was Jim Crow?",
        "a": "A system of state and local laws in the South that enforced racial segregation after the Civil War",
        "key": "Jim Crow laws",
        "topic": "Segregation and Civil Rights",
        "hint": "Key words: state and local laws, racial segregation, South. Jim Crow laws were enacted mainly in Southern states after Reconstruction ended in 1877. They forced Black and white Americans to use separate public facilities and suppressed Black voting through literacy tests, poll taxes, and intimidation. They lasted until the Civil Rights Act of 1964."
    },
    {
        "q": "What was the women's suffrage movement?",
        "a": "A campaign by women to gain the right to vote, which succeeded with the Nineteenth Amendment in 1920",
        "key": "women's suffrage movement",
        "topic": "Women's Rights",
        "hint": "Key words: women's right to vote, Nineteenth Amendment 1920. The women's suffrage movement began in earnest at the Seneca Falls Convention in 1848 and lasted over 70 years. Key leaders included Susan B. Anthony and Elizabeth Cady Stanton. The movement succeeded when the Nineteenth Amendment was ratified in 1920."
    },
    {
        "q": "What is the Equal Protection Clause?",
        "a": "A part of the Fourteenth Amendment requiring states to apply laws equally to all persons",
        "key": "Equal Protection Clause",
        "topic": "Fourteenth Amendment",
        "hint": "Key words: states must apply laws equally. The Equal Protection Clause in the Fourteenth Amendment, ratified in 1868, says no state can deny any person equal protection of the laws. It has been used to fight racial segregation, sex discrimination, and other forms of unequal treatment."
    },
    {
        "q": "What is democracy's greatest strength according to most political thinkers?",
        "a": "Its ability to peacefully correct government mistakes through elections, free speech, and the rule of law",
        "key": "democracy greatest strength",
        "topic": "Democracy Strengths",
        "hint": "Key words: peacefully correct mistakes, elections, free speech. Unlike dictatorships, democracies have built-in mechanisms for change: elections remove bad leaders, free speech allows criticism, courts check abuse, and laws can be revised. This makes democratic systems self-correcting over time."
    },
    {
        "q": "What is a dictatorship?",
        "a": "A form of government in which one leader or group holds absolute power without constitutional limits",
        "key": "define dictatorship",
        "topic": "Government Comparisons",
        "hint": "Key words: one leader, absolute power, no constitutional limits. A dictatorship is the opposite of a constitutional democracy. The leader controls the government, the courts, and often the press. Citizens have no meaningful vote or legal protections against the government's actions."
    },
    {
        "q": "Why is an independent Supreme Court important to American democracy?",
        "a": "It can strike down laws that violate the Constitution, protecting rights even when the majority disagrees",
        "key": "independent Supreme Court importance",
        "topic": "Supreme Court and Democracy",
        "hint": "Key words: strike down unconstitutional laws, protect rights. The Supreme Court's independence means it can protect the Constitution even against popular opinion. For example, in Brown v. Board of Education, the Court struck down school segregation even though many Americans supported it at the time."
    },
    {
        "q": "What is the relationship between liberty and law in American democracy?",
        "a": "Liberty is not unlimited freedom; it is freedom protected and regulated by law so everyone's rights are respected",
        "key": "liberty and law relationship",
        "topic": "Liberty and Law",
        "hint": "Key words: freedom protected and regulated by law. In a democracy, personal freedom must be balanced with the rights of others and the needs of society. Laws set the boundaries within which people are free to live their lives without harming others."
    },
    {
        "q": "What is political equality?",
        "a": "The principle that every citizen's vote counts equally and that all citizens have the same political rights",
        "key": "political equality",
        "topic": "Equality in Democracy",
        "hint": "Key words: every vote counts equally, same political rights. Political equality means one person, one vote. In a democracy, a poor person's vote is worth the same as a wealthy person's vote, and all citizens have the same right to run for office and participate in government."
    },
    {
        "q": "What is the difference between rights and responsibilities in a democracy?",
        "a": "Rights are protections citizens have; responsibilities are duties citizens owe to their community and government",
        "key": "rights vs responsibilities",
        "topic": "Rights and Responsibilities",
        "hint": "Key words: rights are protections, responsibilities are duties. Democracy works when citizens exercise their rights, such as voting and free speech, while also fulfilling responsibilities like obeying laws, paying taxes, and participating in public life."
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
        self.dialog.title("Quiz Setup – American Democracy")
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
        self.root.title('FCLE – American Democracy')
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
