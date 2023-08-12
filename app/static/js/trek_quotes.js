// // Sample quote list (replace with your actual data)



// console.log("Hello from inside the trek_quotes.js file")



const quoteList = [
	["Well Bones, do the new medical facilities meet with your approval?", "Kirk", 'Star Trek: The Motion Picture'],
	["They do not. It's like working in a damn computer center.", 'McCoy', 'Star Trek: The Motion Picture'],
	["Spock, will you please sit down!", 'Kirk', 'Star Trek: The Motion Picture'],
	["Just a moment, Captain, sir. I'll explain what happened. Your revered Admiral Nogura invoked a little known, seldom used, reserve activation clause. In simpler language, Captain, they drafted me!", 'McCoy', 'Star Trek: The Motion Picture'],
    	["Spock. This child is about to wipe out every living thing on Earth. Now, what do you suggest we do....spank it?", 'McCoy', 'Star Trek: The Motion Picture'],
        ["Your child is having a tantrum, Mr. Spock.", 'McCoy', 'Star Trek: The Motion Picture'],
        ["(McCoy) Spock, you haven't changed a bit. You're just as warm and friendly as ever.<br><br>Nor have you, Doctor, as your continued predilection for irrelevancy demonstrates.", 'Spock', 'Star Trek: The Motion Picture'],
        [" (Kirk) It was the best of times, it was the worst of times...Message, Spock?<br><br>None that I am concious of... except, of course, Happy Birthday. Surely the best of times.", 'Spock', 'Star Trek II'],
        ["Humour. It is a difficult concept.", 'Saavik', 'Star Trek II'],
        ["Who's been holding up the damn elevator?", 'McCoy', 'Star Trek II'],
        ["(Spock) It has always been easier to destroy that to create.<br><br>Not anymore! Now we can do both at the same time. According to myth, the Earth was created in six days. Now watch out! Here comes Genesis, we'll do it for ya in six minutes.", 'McCoy', 'Star Trek II '],
        ["(McCoy) Where are we going?<br><br>(Kirk) Where they went.<br><br>(McCoy) What if they went nowhere?<br><br>Then this will be your big chance to get away from it all.", 'Kirk', 'Star Trek II'],
        [" (Sulu) I’ m delighted. Any chance to go aboard the Enterprise. /nWell, I for one am glad to have you at the helm for three weeks.I don 't think these kids can steer.", 'Kirk', 'Star Trek II '],
        ["(Spock) In any case, were I to invoke logic, logic clearly dictates that the needs of the many outweigh the needs of the few.<br><br>Or the one.", 'Kirk', 'Star Trek II'],
        ["I have been, and ever shall be, your friend. Live long, and prosper.", 'Spock', 'Star Trek II'],
        ["How many fingers am I holding up?", 'Kirk', 'Star Trek III'],
        ["That's not very damn funny.", 'McCoy', 'Star Trek III'],
        ["Don’t call me Tiny.", 'Sulu', 'Star Trek III'],
        ["(Kirk) You’re suffering from a Vulcan Mind Meld, Doctor.<br><br>That green - blooded Son of a Bitch. It's his revenge for all those arguments he lost to me.", 'McCoy', 'Star Trek III'],
        ["(Kirk) My God, what have I done?<br><br>What you always do. Turn death into a fighting chance to live.", 'McCoy', 'Star Trek III'],
        [" (Kirk) You’re not exactly catching us at our best.<br><br>That much is certain.", 'Spock', 'Star Trek IV'],
        ["No, I'm from Iowa. I only work in outer space.", 'Kirk', 'Star Trek IV'],
        ['Avoid the planet Earth at all costs. Farewell.', 'Federation President', 'Star Trek IV'],
        ["(Kirk) Spock, where the hell's the power you promised?<br><br>One damn minute, admiral.", 'Spock', 'Star Trek IV'],
        ["(Kirk) Him? He's harmless. Back in the 60's he was part of the peace movement at Berkeley. I think he did a little too much LDS.<br><br>(Dr.Taylor) LDS?<br><br>Umm-huh.", 'Kirk', 'Star Trek IV'],
        ["Damn medievalism!", 'McCoy', 'Star Trek IV'],
        ["(Kirk) Nobody understands you in this century unless you swear every other word. You'll find it in all the literature of the era: Jackelyn Susann, the novels of Harrold Robbins.<br><br>Ah, the giants.", 'Spock', 'Star Trek IV'],
        ["Sounds more like the goddam Spanish Inquisition.", 'McCoy', 'Star Trek IV'],
        ["(Naval Commander) Don’t mess around with me or you're through!<br><br>Really? Can I go now?", 'Chekov', 'Star Trek IV'],
        ["(Spock) Captain, I do not believe you realize the gravity of your situation.<br><br>On the contrary, gravity is the foremost thing on my mind.", 'Kirk', 'Star Trek V'],
        ["Jim, you don't go around asking the Almighty for his I.D.!", 'McCoy', 'Star Trek V'],
        ["Captain, life is not a dream.", 'Spock', 'Star Trek V'],
        ["(Spock) I was attempting to ascertain the meaning of the lyrics.<br><br>(McCoy) It's a song, you green-blooded...Vulcan. You don't analyse it. The point is you have a good time singing it.<br><br>Oh, I am sorry, Doctor. Were we having a good time?", 'Spock', 'Star Trek V'],
        ["(McCoy) Beans. My great grand daddy's recipe. With a secret ingredient.<br><br>Beans and bourbon. An explosive combination.", 'Kirk', 'Star Trek V'],
        ["I need a shower.", 'Kirk', 'Star Trek V'],
        ["Please Captain, not in front of the Klingons.", 'Spock', 'Star Trek V'],
        ["To be... or not to be... that is the question which troubles my people.", 'General Chang', 'Star Trek VI'],
        ["Guess who's coming to dinner?", 'Chekov', 'Star Trek VI'],
        ["Where's that damn torpedo?", 'Kirk', 'Star Trek VI'],
        ["(Kirk) Uhura, signal our surrender.<br><br>(Uhura) Captain?!<br><br>We surrender!", 'Kirk', 'Star Trek VI'],
        ["(Spock) Ahh, Mr.Scott, I understand you're having difficulty with the warp drive. How much time do you require for repair?<br><br>(Scotty) There’ s nothing wrong with the bloody thing!<br><br>(Spock) Mr.Scott, if we return to Spacedock, the assassins will surely find a way to dispose of their incriminating footwear, and we will never see the captain, or Dr.McCoy, alive again.<br><br>(Scotty) Could take weeks, sir.<br><br>Thank you, Mr.Scott.", 'Spock', 'Star Trek VI'],
        ["If I were human, I believe the correct response would be 'Go to Hell.'", 'Spock', 'Star Trek VI'],
        ["(Chang) I am constant as the Northern Star.<br><br>I'd give real money if he'd shut up.", 'McCoy', 'Star Trek VI'],
        ["You can't appreciate Shakespeare until you've read him in the original Klingon.", 'General Chang', 'Star Trek VI'],
        ["Logic is the beginning of wisdom; not the end.", 'Spock', 'Star Trek VI'],
        ["Oh, shit!!!", 'Data', 'Star Trek Generations'],
        ["I was out saving the galaxy when your grandfather was in diapers.", 'Kirk', 'Star Trek Generations'],
        ["You will excuse me now, Captain. I have an appointment with eternity and I don't want to be late.", 'Dr. Soran', 'Star Trek Generations'],
        ["Yes!!!!!!!", 'Data', 'Star Trek Generations'],
     
	["Time is the fire in which we burn...", 'Dr. Soran', 'Star Trek Generations'],
	["Normal is what everyone else is and you are not.", 'Dr. Soran', 'Star Trek Generations'],
	["Seize the time, Meribor. Live now; make now always the most precious time. Now will never come again.", 'Captain Picard', 'The Inner Light (TNG)'],
	["Shields up! Rrrrred alert!", 'Riker'],
	["Eaten any good books lately?", 'Q', 'Deja-Q'],
	["You're so stolid. You weren't like that before the beard.", 'Q', 'Deja-Q (TNG)'],
	["‘With the first link, the chain is forged. The first speech censored, the first thought forbidden, the first freedom denied, chains us all irrevocably.’", 'Captain Picard', 'The Drumhead (TNG)'],
	["Fate protects fools, little children and ships named Enterprise.", 'Riker', 'Contagion (TNG)'],
	["Let's make sure that history never forgets the name... Enterprise.", 'Captain Picard', "Yesterday's Enterprise (TNG)"],
	["If you prick me, do I not... leak?", 'Data', 'The Naked Now'],
	["If there's nothing wrong with me... maybe there's something wrong with the universe!", 'Dr. Crusher', 'Remember Me (TNG)'],
	["The universe is a spheroid region, 705 metres in diameter.", 'The Computer', 'Remember Me'],
	["Nice Legs... for a human.", 'Worf', 'Qpid (TNG)'],
	["Jean-Luc! It's so good to see you again. How about a big hug?", 'Q', 'Qpid (TNG)'],
	["I am not a merry man!", 'Worf', 'Qpid (TNG)'],
	["If you can't take a little bloody nose, maybe you oughtta go back home and crawl under your bed. It's not safe out here. It's wondrous, with treasures to satiate desires both subtle and gross; but it's not for the timid.", 'Q', 'Q Who? (TNG)'],
	["Spot. This is down. Down is good.", 'Data', 'Force of Nature (TNG)'],
	["Please Mrs. Troi! ... and it's Worf, not Woof.", 'Worf', 'Half a Life (TNG)'],
	["All good things must come to an end...", 'Q', 'All Good Things... (TNG)'],
	["Besides, you look good in a dress.", 'Riker', 'Liasons (TNG)'],
	["Sometimes a cigar is just a cigar!", 'Sigmund Freud', 'Phantasms (TNG)'],
	["(Data)You must talk to him; tell him that he is a good cat, and a pretty cat, and…<br><br>I will feed him.", 'Worf', 'Phantasms (TNG)'],
	["Some of the colonists objected to having an anatomically correct android running around without any clothes on.", 'Juliana Soong', 'Inheritance (TNG)'],
	["Captain, we're receiving two hundred and eighty-five thousand hails.", 'Lt. Wesley Crusher', 'Parallels (TNG)'],
	["Synthetic Scotch, synthetic Commanders...", 'Scotty', 'Relics (TNG)'],
	["… and get that fish out of my ready room.", 'Captain Jellico', 'Chain of Command, Part I (TNG)'],
	["Policemen, I'd recognize them in any century.", 'Professor Moriarty', 'Ship in a Bottle (TNG)'],
	["You're dead, this is the afterlife, and I'm God.", 'Q', 'Tapestry (TNG)'],
	["Yes, absolutely, I do indeed concur, wholeheartedly!", 'Riker', 'Where Silence has Lease (TNG)'],
	["Well, he did make a pass at me... and it was a good one!", 'Troi', 'The Nth Degree (TNG)'],
	["The Federation's gone; the Borg is everywhere!", 'Riker', 'Parallels (TNG)'],
	["Captain's Personal Log, supplemental. I have just witnessed the total destruction of the U.S.S. Enterprise with the loss of all hands. Save one. Me.", 'Captain Picard', 'Time Squared (TNG)'],
	["(Locutus) I will continue, aboard this ship, to speak for the Borg. While they continue, without further diversion, to Sector 001, where they will force your unconditional surrender.", 'The Borg', 'The Best of Both Worlds II (TNG)'],
	["I’m not suppsed to be here, sir. I'm.....supposed to be dead!", 'Tasha Yar', "Yesterday's Enterprise (TNG)"],
	["Starfleet reports it has engaged the Borg at Wolf 359, sir.", 'Data', 'The Best of Both Worlds II (TNG)'],
	["Mr. Crusher, ready a collision course with the Borg ship.", 'Riker', 'The Best of Both Worlds II (TNG)'],
	["And how do I know that someone I might save down there might not be the next Adolf Hitler? Or Khan Singh? I'm willing to take that chance.", 'Captain Picard', "A Matter of Time (TNG)"],
	["Who knows if we're even dead or alive?", 'LaForge', "Yesterday's Enterprise (TNG)"],
	["We have engaged...the Borg.", 'Captain Picard', 'The Best of Both Worlds I (TNG)'],
	["Legends...are the spice of the universe, Mr. Data, because they have a way of sometimes coming true.", 'Captain Picard', 'Haven'],
	["Baby needs a new pair of shoes.", 'Data', 'The Royale (TNG)'],
	["One thing is clear - you'll never look at your hairline again in the same way.", 'Captain Picard', 'Bloodines (TNG)'],
	["It's time to put an end to your trek through the stars.", 'Q', 'All Good Things... (TNG)'],
	["Five card stud, nothing wild. And the sky's the limit.", 'Captain Picard', 'All Good Things... (TNG)'],
	["We will add your biological and technological distinctiveness to our own. Your culture will adapt to service us. Resistance is futile. We are the Borg.", 'The Borg', 'The Best of Both Worlds, Part I (TNG)'],
	["Good tea. Nice house.", 'Worf', 'The Survivors'],
	["We do exactly what we would do if this Q never existed. If we're going to be damned, let's be damned for who we really are.", 'Captain Picard', 'Encounter At Farpoint (TNG)'],
	["Q might have done the right thing for the wrong reason, perhaps we need a good kick in our complacency to get us ready for what's ahead.", 'Captain Picard', 'Q Who? (TNG)'],
	["Did the table do something wrong?", 'Troi', 'Birthright Part I (TNG)'],
	["Sir, you have no sense of fair play?", 'Captain Picard', 'Hollow Pursuits (TNG)'],
	["Your head is not an artifact!", 'Riker', "Time's Arrow, Part 1 (TNG)"],
	["Ah. I understand the source of your misperception, but this is not sleepwear, and I do not have a 'missus.'", 'Data', "Time's Arrow (TNG)"],
	["Thank you for the advice, but I am trying to find two individuals with a snake.", 'Data', "Time's Arrow  (TNG)"],
	["There are four lights!", 'Captain Picard', 'Chain of Command, Part 2 (TNG)'],
	["... a dream that became a reality and spread throughout the stars.", "Kirk", "Whom Gods Destroy (TOS)"],
	["Just before they went into warp, I beamed the whole kit and kaboodle into their engine room, where they'll be no tribble at all.", "Scotty", "The Trouble With Tribbles (TOS)"],
	["Right out of hell, I saw it!", "Commodore Decker", "The Doomsday Machine (TOS)"],
	["You will die of suffocation, in the icy cold of space.", "Kang", "Day of the Dove (TOS)"],
	["The mid-1990s was the era of your so-called Third World War.", "Spock", "Space Seed (TOS)"],
	["We simply must accept the fact that Captain Kirk is no longer alive.", "Spock", "The Tholian Web (TOS)"],
	["They seemed to have been spared the agony of your first three World Wars, doctor.", "Spock", "Bread and Circuses (TOS)"],
	["You are authorized to use all measures available to destroy the Enterpise.", "Starfleet Command Representative", "The Ultimate Computer (TOS)"],
	["I didn't mean to say that the Enterprise should be hauling garbage. I meant to say that it should be hauled away AS garbage.", "Korax", "The Trouble With Tribbles (TOS)"],
	["You look quite well for a man that's been 'utterly destroyed', Mr. Spock.", "Kirk", "Patterns of Force (TOS)"],
	["In four hours the ship blows up.", "Scotty", "The Savage Curtain (TOS)"],
	["Computer, compute to the last digit the value of pi.", "Spock", "Wolf in the Fold (TOS)"],
	["Mr. Spock, the women on your planet are logical. That's the only planet in the galaxy that can make that claim.", "Kirk", "Elaan of Troyius (TOS)"],
	["Ston, she is yours. You may find that having is not so pleasing a thing as wanting. This is not logical, but it is often true.", "Spock", "Amok Time (TOS)"],
	["The best diplomat that I know is a fully-loaded phaser bank.", "Scotty", "A Taste of Armageddon (TOS)"],
	["I signed aboard this ship to practice medicine, not to have my atoms scattered back and forth across space by this gadget.", "McCoy", "Space Seed (TOS)"],
	["By golly, Jim... I'm beginning to think I can cure a rainy day!", "McCoy", "The Devil in the Dark (TOS)"],
	["I find myself growing fatigued, Doctor. May we continue this questioning at some other time?", "Khan", "Space Seed (TOS)"],
	["(Locutus) Resistance is futile. You will disarm your weapons, and escort us to Sector 001. If you attempt to intervene, we will destroy you.", "Captain Picard", "Emissary (TOS)"],
	["Picard would never have hit me...", "Q", "Q-less (DS9)"],
	["Die with honour.", "Tosk", "Tosk (DS9)"],
	["I'm a doctor, not a botanist.", "Dr. Bashir", "The Wire (DS9)"],
	["In my expert medical opinion, I'd say... it's sick.", "Dr. Bashir", "The Wire (DS9)"],
	["(Kira) If your lies are going to be this transparent, this is going to be a very short interrogation.<br><br>Then I'll try to make my lies more opaque...", "Gul Darhe'el", "Duet (DS9)"],
	["I'm sorry, Commander, but I've learned we can't afford to die here, not even once.", "Dr. Bashir ", "Battlelines(DS9)"],
	["Do I annoy you ? ", "Dr. Bashir ", "The Storyteller(DS9)"],
	["He's still dead, if that's what you mean.", "Dr. Bashir", "Dramatis Personae (DS9)"],
	["Whoah! What's that? Is that a spider or a dog?", "Jadzia Dax", "The Siege (DS9)"],
	["The Provisional Government is going to fall, and when governments fall people like me are the first ones shot.", "Quark", "Emissary (DS9)"],
	["Cardassian rule may have been oppressive, but at least it was simple.", "Odo", "Past Prologue (DS9)"],
	["Laws change depending on who's making them, but justice is justice.", "Odo", "A Man Alone (DS9)"],
	["Rom's an idiot. He couldn't fix a straw if it was bent.", "Odo", "Babel (DS9)"],
	["I am sorry I have no vices for you to exploit.", "Tosk", "Captive Pursuit (DS9)"],
	["I don't get out often.", "Kai Opaka", "Battle Lines (DS9)"],
	["Nothing makes them happy! They are dedicated to being unhappy, and to spreading that unhappiness to others! They are the Ambassadors of Unhappy!", "Dr. Bashir", "The Forsaken (DS9)"],
	["(Bashir) A bite on the hand is certainly worth saving a boy's life, wouldn't you say?<br><br>I suppose it depends on whose hand.... just joking, Doctor.", "Garak", "Cardassians (DS9)"],
	["We can't have these Bajorans going around killing each other.", "Dukat", "Necessary Evil (DS9)"],
	["The truth is usually just an excuse for a lack of imagination.", "Garak", "Improbable Cause (DS9)"],
	["This is not a synthale kind of night.", "Dr. Bashir", "Explorers (DS9)"],
	["Captain, are you aware there's a Klingon on your bridge?", "Dukat", "The Way of the Warrior (DS9)"],
	["All I ask is a tall ship, and a load of contraband to fill her with...", "Quark", "Little Green Men (DS9)"],
	["I'm a much more complicated man than you give me credit for, Major.", "Dukat", "Return to Grace (DS9)"],
	["I'm sorry if I made you feel... unwelcome. It's just my way.", "Odo", "Muse (DS9)"],
	["You've got a good start on a novel here, Jake. The dialog is sharp, the story is interesting, the characters are real... the spelling is terrible.", "Sisko", "Muse (DS9)"],
	["I hate prototypes.", "O'Brien", "Apocalypse Rising (DS9)"],
	["(Odo) I see I'm going to have to add the word pickpocket to your resume.<br><br>It's only a hobby.", "Garak", "Things Past (DS9)"],
	["Constable, why are you talking to your beverage?", "Worf", "The Begotten (DS9)"],
	["There's an old saying, Fortune favors the bold. Well, I guess we're about to find out.", "Sisko", "Sacrifice of Angels (DS9)"],
	["Why pretend we're going home at all when all we're really going to do is investigate every cubic millimter of this quadrant, aren't we?", "The Doctor", "The Cloud (VOY)"],
	["I don't like threats, I don't like bullies, and I don't like you!", "Captain Janeway ", "State of Flux (VOY)"],
	["Get the cheese to sickbay!", "B'Elanna Torres", "Learning Curve (VOY)"],
	["It appears we have lost our sex appeal, Captain.", "Tuvok", "Elogium (VOY)"],
	["Now's as good a time as any to tell you. Your ceiling is hideous.", "Neelix", "Phage (VOY)"],
	["The procedure is quite simple. I'll drill an opening into your skull percisely two milimeters in diameter and then use a neuralyte probe to extract a sample of your parietal lobe weighing approximately one gram.", "The Doctor", "Lifesigns (VOY)"],
	["(Q) Trouble sleeping, Captain?<br><br>...Get out.", "Captain Janeway", "Deathwish (VOY)"],
	["Your voice says to go away, but your heart wants me to make you smile!", "Neelix", "Meld (VOY)"],
	["You're on your way to being normal, although I 'm not sure how normal applies to a species who suppress all their emotions.", "The Doctor", "Meld (VOY)"],
	["(Janeway) Doctor, I forgot all about you!<br><br>How flattering.", "The Doctor", "Dreadnought (VOY)"],
	["Well, isn't this just fine! Humans aren't supposed to be in this quadrant for 100 years!", "Q", "Death Wish (VOY)"],
	["Facial art... ooh, how... wilderness of you!", "Q", "Death Wish (VOY)"],
	["This ship will not survive the formation of the cosmos!", "B'Elanna Torres", "Death Wish (VOY)"],
	["(Janeway) Where are we now?<br><br>We seem to be tethered to some sort of... plant.", "Tom Paris", "Death Wish (VOY)"],
	["Can't you see, Captain? For us, the disease is immortality.", "Q", "Death Wish (VOY)"],
	["Fear exists for one purpose: to be conquered.", "Captain Janeway", "The Thaw (VOY)"],
	["Oh, I see! This is one of those silly human rituals. You're playing hard to get!", "Q", "The Q and the Grey (VOY)"],
	["Captain ... I believe I speak for everyone here, sir, when I say, 'To Hell with our orders.'", "Data", "Star Trek First Contact"],
	["Believing oneself to be perfect is often the sign of a delusional mind.", "Data", "Star Trek First Contact"],
	["They invade our space, and we fall back. They assimilate countless worlds, and we fall back. Not again. Not this time. The line must be drawn here! This far, no farther! And I will make them pay for what they have done!", "Captain Picard", "Star Trek First Contact"],
	["Smooth as an android's bottom, eh, Data?", "Riker", "Star Trek Insurrection"],
	["We're through running from these bastards.", "Riker", "Star Trek Insurrection"],
	["Definitely feeling agressive tendencies, sir.", "Worf", "Star Trek Insurrection"],
	["Does anyone remember when we were explorers?", "Captain Picard", "Star Trek Insurrection"],
	["In the event of a water landing, I have been designed to act as a floatation device.", "Data", "Star Trek Insurrection"],
	["The Son'a wish to negotiate a cease-fire. It may have something to do with the fact that we only have three minutes of air left.", "Worf", "Star Trek Insurrection"]
]

// // make a function to loop over each quote 
// // quote[0] = quote
// //quote[1] = person
// // //quote[2] = source
// const quoteList = [
//     ["To be or not to be.", "William Shakespeare", "Hamlet"],
//     ["The only thing we have to fear is fear itself.", "Franklin D. Roosevelt", "Inaugural Address"],
//     // ... more quotes
// ];


const formatQuote = (quoteList) => {
    let formattedQuotes = quoteList.map((q) => {
        return {
            quote: q[0],
            person: q[1],
            source: q[2]
        };
    });
    return formattedQuotes;
};

function showRandomQuote(formattedQuotes) {
    // Randomly select an index from the array
    const randomIndex = Math.floor(Math.random() * formattedQuotes.length);

    // Get the randomly selected quote
    const randomQuote = formattedQuotes[randomIndex];

    // Display the random quote
	$('.quotes').html('');
    let $quoteCard = `
    <div class="quote-card">
    <div class="quote-text"><strong>${randomQuote.quote}</strong></div>
    <div class="quote-person"><em> -${randomQuote.person}</em></div>
    <div class="quote-source"><u>${randomQuote.source}</u></div>
</div>
    `;

    $('.quotes').html($quoteCard);
}

function displayRandomQuotes(formattedQuotes) {
    formattedQuotes = formatQuote(quoteList)
    // Display a random quote immediately
    showRandomQuote(formattedQuotes);

    // Show a new random quote every 10 seconds
    setInterval(function() {
        showRandomQuote(formattedQuotes);
    }, 10000);
}

$(document).ready(function() {
	displayRandomQuotes();
});