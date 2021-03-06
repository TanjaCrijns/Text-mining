### Assignment week 4  Text mining - Tanja Crijns s4204999

I have included the timeline of Obama's life last because this is a table of six pages. I will answer the other questions first.

##### *1. Report	the	precision	of	your	date	expression	extractor.*
Number of retrieved dates:109<br />
Number of correctly retrieved dates: 109<br />
`Precision = 109/109 = 1`<br />

The dates are all retrieved in the correct format. However, it is questionable wether the retrieved sentences are always useful. An example would be the following result, the event *moving to kenwood* did not happen in 1998 however the dates are extracted correctly:
- *1998 - They moved to Kenwood, on Chicago's South Side, and welcomed two daughters several years later: Malia (born 1998) and Sasha (born 2001).*

<br />
Other examples are paragraph headers:
- *2004 - Senate in 2004.* <br />
- *2014 - Presidency After 2014 Elections* <br />

##### 2. Difficulties
My script from the first week didn't work so well on this text. The regular expression I used for finding end of lines didn't work so I made another regular expression that did work. A lot of other things were quite useless like identifying the titles, footnotes and pagenumbers so I removed this. <br />
It was challenging to retrieve all the dates from the text because dates can be formatted differently. I wrote down the possible formats and decided to construct regular expression to find them in the text. The formats I used were:
- *MM, YYYY, DD*
- *MM, DD, YYYY*
- *MM, YYYY*
- *YYYY*<br/>

The formats that I did not include were *MM* or *MM, DD* or *DD, MM* because there was no year present. However, this could be solved by remembering the last mentioned year although this might not always be correct. This is something that I could improve. <br/>
In order to get the dates in the correct ISO 8601 format I parsed the string values of the dates with three regular expressions for *year*, *month* and *day* and returned them in the corrrect order.<br/>
<br/><br/>
##### *Timeline of Obama's life*


| Date | Event sentence |
|---|---|
| 1928 | The first sitting American president to visit the island nation since 1928, Obama made the three-day visit—accompanied by First Lady Michelle Obama and their daughters Malia and Sasha. |
| 1961 | Obama's visit was part of a larger program to establish greater cooperation between the two countries, the foundations of which were laid in late 2014, when Obama and Cuban president Raul Castro announced the normalizing of diplomatic relations for the first time since 1961.|
| 1961-02-02 | While studying at the University of Hawaii at Manoa, Obama Sr. met fellow student Ann Dunham, and they married on February 2, 1961.|
| 1961-08-04 | Born on August 4, 1961, in Honolulu, Hawaii, Barack Obama is the 44th and current president of the United States.|
| 1961-08-04 | Barack Hussein Obama II was born on August 4, 1961, in Honolulu, Hawaii.|
| 1964-03 | Obama's parents officially separated several months later and ultimately divorced in March 1964, when their son was two.|
| 1965 | In 1965, Dunham married Lolo Soetoro, a University of Hawaii student from Indonesia.|
| 1970 | A year later, the family moved to Jakarta, Indonesia, where Obama's half-sister, Maya Soetoro Ng, was born in 1970.|
| 1971 | Obama also struggled with the absence of his father, who he saw only once more after his parents divorced, when Obama Sr. visited Hawaii for a short time in 1971.|
| 1979 | While living with his grandparents, Obama enrolled in the esteemed Punahou Academy, He excelled in basketball and graduated with academic honors in 1979.|
| 1981 | Ten years later, in 1981, tragedy struck Obama Sr. when he lost both of his legs in a serious car accident.|
| 1982 | In 1982, Obama Sr. was involved in yet another car accident while traveling in Nairobi.|
| 1982-11-24 | Obama Sr. died on November 24, 1982, when Obama was 21 years old.|
| 1983 | He then transferred to Columbia University in New York City, graduating in 1983 with a degree in political science.|
| 1985 | After working in the business sector for two years, Obama moved to Chicago in 1985.|
| 1988 | Returning from Kenya with a sense of renewal, Obama entered Harvard Law School in 1988.|
| 1990-02 | In February 1990, Obama was elected the first African-American editor of the Harvard Law Review.|
| 1991 | He graduated magna cum laude from Harvard Law in 1991.|
| 1992 | He also taught constitutional law part-time at the University of Chicago Law School between 1992 and 2004—first as a lecturer and then as a professor—and helped organize voter registration drives during Bill Clinton's 1992 presidential campaign.|
| 1992 | He also taught constitutional law part-time at the University of Chicago Law School between 1992 and 2004—first as a lecturer and then as a professor—and helped organize voter registration drives during Bill Clinton's 1992 presidential campaign.|
| 1992-10-03 | On October 3, 1992, he and Michelle were married.|
| 1995 | Obama published an autobiography, Dreams from My Father: A Story of Race and Inheritance, in 1995.|
| 1996 | He was elected to the Illinois State Senate in 1996 and to the U.S.|
| 1996 | He ran as a Democrat and won election in 1996.|
| 1998 | They moved to Kenwood, on Chicago's South Side, and welcomed two daughters several years later: Malia (born 1998) and Sasha (born 2001).|
| 2000 | In 2000, Obama made an unsuccessful Democratic primary run for the U.S.|
| 2001 | They moved to Kenwood, on Chicago's South Side, and welcomed two daughters several years later: Malia (born 1998) and Sasha (born 2001).|
| 2001 | Following the 9/11 attacks in 2001, Obama was an early opponent of President George W. Bush's push to go to war with Iraq.|
| 2002 | Undeterred, he created a campaign committee in 2002 and began raising funds to run for a seat in the U.S.|
| 2002-10 | Obama was still a state senator when he spoke against a resolution authorizing the use of force against Iraq during a rally at Chicago's Federal Plaza in October 2002.|
| 2003 | " Despite his protests, the Iraq War began in 2003.|
| 2004 | Senate in 2004.|
| 2004 | He also taught constitutional law part-time at the University of Chicago Law School between 1992 and 2004—first as a lecturer and then as a professor—and helped organize voter registration drives during Bill Clinton's 1992 presidential campaign.|
| 2004 | The book had a second printing in 2004 and was adapted for a children's version.|
| 2004 | Senate in 2004.|
| 2004 | In the 2004 Democratic primary, he defeated multimillionaire businessman Blair Hull and Illinois Comptroller Daniel Hynes with 52 percent of the vote.|
| 2004 | That summer, he was invited to deliver the keynote speech in support of John Kerry at the 2004 Democratic National Convention in Boston.|
| 2004-08 | In August 2004, diplomat and former presidential candidate Alan Keyes accepted the Republican nomination to replace Ryan.|
| 2004-06 | However, Ryan withdrew from the race in June 2004 following public disclosure of unsubstantiated sexual deviancy allegations by his ex-wife, actress Jeri Ryan.|
| 2004-11 | In the November 2004 general election, Obama received 70 percent of the vote to Keyes' 27 percent, the largest electoral victory in Illinois history.|
| 2005 | The plan calls for aggressive Environmental Protection Agency regulations including requiring existing power plants to cut carbon dioxide emissions 32 percent from 2005 levels by 2030 and use more renewable energy sources like wind and solar power.|
| 2005-01-03 | Sworn into office on January 3, 2005, Obama partnered with Republican Senator Richard Lugar of Indiana on a bill that expanded efforts to destroy weapons of mass destruction in Eastern Europe and Russia.|
| 2006 | The audiobook version of Dreams, narrated by Obama, received a Grammy Award for best spoken word album in 2006.|
| 2006-10 | His second book, The Audacity of Hope: Thoughts on Reclaiming the American Dream, was published in October 2006.|
| 2007-02 | In February 2007, Obama made headlines when he announced his candidacy for the 2008 Democratic presidential nomination.|
| 2008 | First elected to the presidency in 2008, he won a second term in 2012.|
| 2008 | presidency in 2008, and won re-election in 2012 against Republican challenger Mitt Romney.|
| 2008 | 2008 Presidential Election|
| 2008 | In February 2007, Obama made headlines when he announced his candidacy for the 2008 Democratic presidential nomination.|
| 2008 | As he did in 2008, during his campaign for a second presidential term, Obama focused on grassroots initiatives.|
| 2008-06-03 | On June 3, 2008, Obama became the Democratic Party's presumptive nominee after winning a sufficient number of pledged delegates during the primaries, and Clinton delivered her full support to Obama for the duration of his campaign.|
| 2008-11-04 | On November 4, 2008, Barack Obama defeated Republican presidential nominee John McCain, 52.9 percent to 45.7 percent, to win election as the 44th president of the United States—and the first African-American to hold this office.|
| 2009 | For his efforts, the Nobel Committee in Norway awarded Obama the 2009 Nobel Peace Prize.|
| 2009 | Voting with the majority were two associate justices appointed by Obama—Sonia Sotomayor (confirmed in 2009) and Elena Kagan (confirmed in 2010).|
| 2009-01-20 | Obama's inauguration took place on January 20, 2009.|
| 2009-04-29 | Between Inauguration Day and April 29, 2009, the Obama administration took action on many fronts.|
| 2010 | 2010 State of the Union|
| 2010 | House of Representatives in the 2010 mid-term elections, he signed the Budget Control Act of 2011 in an effort to rein in government spending and prevent the government from defaulting on its financial obligations.|
| 2010 | Voting with the majority were two associate justices appointed by Obama—Sonia Sotomayor (confirmed in 2009) and Elena Kagan (confirmed in 2010).|
| 2010-01-27 | On January 27, 2010, President Obama delivered his first State of the Union speech.|
| 2010-08 | He committed an additional 21,000 troops to Afghanistan and set an August 2010 date for withdrawal of nearly all U.S.|
| 2010-03 | In spite of opposition from Congressional Republicans and the populist Tea Party movement, Obama signed his health care reform plan, known as the Affordable Care Act, into law in March 2010.|
| 2011 | House of Representatives in the 2010 mid-term elections, he signed the Budget Control Act of 2011 in an effort to rein in government spending and prevent the government from defaulting on its financial obligations.|
| 2011 | Also in 2011, Obama signed a repeal of the military policy known as "Don't Ask, Don't Tell," which prevented openly gay troops from serving in the U.S.|
| 2011-03 | In March 2011, he approved U.S.|
| 2012 | First elected to the presidency in 2008, he won a second term in 2012.|
| 2012 | presidency in 2008, and won re-election in 2012 against Republican challenger Mitt Romney.|
| 2012 | “The better he did at Harvard Law School and the more he impressed people, the more obvious it became that he could have had anything, said Professor Tribe in a 2012 interview with Frontline, “but it was clear that he wanted to make a difference to people, to communities.|
| 2012 | 2012 Re-Election|
| 2012 | In the 2012 election, Obama faced Republican opponent Mitt Romney and Romney's vice-presidential running mate, U.S.|
| 2012 | Prior to the bill's passage, in late 2012, tense negotiations between Republicans and Democrats over spending cuts and tax increases became a bitter political battle until Vice President Joe Biden managed to hammer out a deal with Republican Senate Minority Leader Mitch McConnell.|
| 2012 | Citing examples such as the 2012 mass shooting at Sandy Hook elementary school, the president shed tears as he called on Congress and the gun lobby to work with him to make the country safer.|
| 2012 | Citing examples such as the 2012 mass shooting at Sandy Hook elementary school in Connecticut, the president shed tears as he called on Congress and the gun lobby to work with him to make the country safer.|
| 2012-11-06 | On November 6, 2012, Obama won a second four-year term as president by receiving nearly five million more votes than Romney and capturing more than 60 percent of the Electoral College.|
| 2012-12-14 | Nearly one month after President Obama's re-election, the nation endured one of its most tragic school shootings to date when 20 children and six adults were shot to death at the Sandy Hook Elementary School in Newtown, Connecticut, on December 14, 2012.|
| 2012-06 | Obama gained a legal victory in June 2012 when the U.S.|
| 2012-06 | "I guarantee you, we will move this country forward," Obama stated in June 2012, at a campaign event in Maryland.|
| 2012-05 | President Obama, who became the first president to voice support for same-sex marriage in May 2012, praised the court for affirming "that the Constitution guarantees marriage equality.|
| 2013 | The fall of 2013 brought Obama additional challenges in the area of foreign relations.|
| 2013-01-01 | Obama achieved a major legislative victory on January 1, 2013, when the Republican-controlled House of Representatives approved a bipartisan agreement on tax increases and spending cuts, in an effort to avoid the looming fiscal cliff crisis (the Senate voted in favor of the bill earlier that day).|
| 2013-01-21 | Barack Obama officially began his second term on January 21, 2013, when U.S.|
| 2013-04-15 | After the inauguration, Obama led the nation through many challenges—none more difficult, perhaps, than the terrorist bombings of the Boston Marathon on April 15, 2013, which killed three people and left more than 200 injured.|
| 2013-09-10 | Obama then announced an alternative solution on September 10, 2013, by stating that if al-Assad agreed with the stipulations outlined in a proposal made by Russia to give up its chemical weapons, then a direct strike against the nation could be avoided.|
| 2013-07 | In early July 2013, President Obama made history when he joined former President George W. Bush in Africa to commemorate the 15th anniversary of al-Qaeda’s first attack on American targets, the U.S.|
| 2013-11 | In the wake of these controversies, Obama saw his approval rating drop to a new low in November 2013.|
| 2013-10 | Obama found himself struggling on the domestic front in October 2013.|
| 2013-10 | In October 2013, German Chancellor Angela Merkel revealed that the NSA had been listening in to her cell phone calls.|
| 2013-09 | Obama found himself grappling with an international crisis in late August and September 2013 when it was discovered that Syrian leader Bashar al-Assad had used chemical weapons against civilians.|
| 2014 | "In 2014 we are well beyond the days when borders can be redrawn over the heads of democratic leaders," Obama stated.|
| 2014 | In addition to the ongoing troubles in Ukraine, tensions between Israelis and Palestinians erupted into violence in Gaza during the summer of 2014.|
| 2014 | Presidency After 2014 Elections|
| 2014 | Obama's visit was part of a larger program to establish greater cooperation between the two countries, the foundations of which were laid in late 2014, when Obama and Cuban president Raul Castro announced the normalizing of diplomatic relations for the first time since 1961.|
| 2014-08 | In August 2014, Obama ordered the first airstrikes against the self-proclaimed Islamic State, also known as ISIS or ISIL, which had seized large swathes of Iraq and Syria and conducted high-profile beheadings of foreign hostages.|
| 2014-02 | Echoes of the Cold War also returned after civil unrest and protests in the capital city of Kiev led to the downfall of Ukrainian President Viktor Yanukovych's administration in February 2014.|
| 2015 | In his 2015 State of the Union address, Obama declared that the nation was out of recession.|
| 2015 | The summer of 2015 brought two major U.S.|
| 2015 | 2015 Paris Climate Conference|
| 2015 | According to a 2015 Gallup poll, most Americans favor some kind of stricter regulations of gun sales.|
| 2015 | According to a 2015 Gallup poll, most Americans favor some kind of stricter regulations of gun sales. |
| 2015-08 | In August 2015, the Obama administration announced The Clean Power Plan, a major climate change plan aimed at reducing greenhouse gas emissions, the first-ever national standards to limit carbon pollution from coal-burning power plants in the United States.|
| 2015-11 | In November 2015, Obama further demonstrated his commitment to environmental issues as a primary player in the international COP21 summit held outside of Paris, France.|
| 2015-07 | In July 2015, Obama announced that, after lengthy negotiations, the United States and five world powers had reached an agreement with Iran over its nuclear program.|
| 2016 | Under the regulations, states will be allowed to create their own plans to reduce emissions and are required to submit initial plans by 2016 and final versions by 2018.|
| 2016-01-12 | Shortly after the press conference, on January 12, 2016, Barack Obama delivered what would be his final State of the Union address.|
| 2016-01 | Entering his final year as President of the United States, in early January 2016 Obama held a press conference to announce a new series of executive orders related to gun control.|
| 2016-01 | Entering his final year as President of the United States, in early January 2016 Obama held a press conference to announce a new series of executive orders related to gun control.|
| 2018 | Under the regulations, states will be allowed to create their own plans to reduce emissions and are required to submit initial plans by 2016 and final versions by 2018.|
| 2030 | The plan calls for aggressive Environmental Protection Agency regulations including requiring existing power plants to cut carbon dioxide emissions 32 percent from 2005 levels by 2030 and use more renewable energy sources like wind and solar power.|
| 2030 | President Obama praised the agreement for establishing the “enduring framework the world needs to solve the climate crisis” and pledged that the United States would cut its emissions more than 25 percent by 2030. |
