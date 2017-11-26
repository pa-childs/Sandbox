var current_vocabulary_word;
var questions_asked = 0;
var used_vocabulary_words = [];
var vocabulary_words = [
    ["Outward Block", "Bah-guh-roh Mahk-gee", "Blocks"],
    ["Inward Block", "Ahn-uh-roh Mahk-gee", "Blocks"],
    ["Low Block", "Ah-reh Mahk-gee", "Blocks"],
    ["Dodge", "Pee-heh-gee", "Blocks"],

    ["Attention", "Chah-ryut", "Commands"],
    ["Bow", "Gyung-yeh", "Commands"],
    ["Ready", "Joon-bee", "Commands"],
    ["Begin", "See-jahk", "Commands"],
    ["Back To Ready", "Bah-roh", "Commands"],
    ["Stop", "Guh-mahn", "Commands"],
    ["At Ease", "Shee-uh", "Commands"],
    ["In Your Own Time", "Goo-ryung Uhp-see", "Commands"],
    ["By The Count", "Goo-ryung Aeh Mah-choo-uh", "Commands"],
    ["About Turn", "Dwee-roh Doh-rah", "Commands"],
    ["Dismiss", "Heh-sahn", "Commands"],
    ["Move Forward", "Ahp-uh-roh Gah-myuh", "Commands"],
    ["Move Backward", "Ahp-uh-roh Gah-myuh", "Commands"],
    ["Switch Stance", "Bahl Bah-gwah", "Commands"],

    ["One", "Hah-nah", "Counting"],
    ["Two", "Dool", "Counting"],
    ["Three", "Set", "Counting"],
    ["Four", "Neht", "Counting"],
    ["Five", "Dah-suht", "Counting"],
    ["Six", "Yuh-suht", "Counting"],
    ["Seven", "Il-gohp", "Counting"],
    ["Eight", "Yuh-duhlp", "Counting"],
    ["Nine", "Ah-hohp", "Counting"],
    ["Ten", "Yuhl", "Counting"],

    ["Front", "Ahp", "Directions"],
    ["Rear", "Bahl", "Directions"],
    ["Side", "Yuhp", "Directions"],
    ["Right", "Woo", "Directions"],
    ["Left", "Jwah", "Directions"],
    ["Reverse", "Bahn-deh", "Directions"],
    ["Outer", "Bahk Un-roh", "Directions"],
    ["Inward", "Ahn Uh-roh", "Directions"],
    ["About Turn", "Dwee-roh Do-rah", "Directions"],

    ["Front Foot", "Ahp Bahl", "Kicks"],
    ["Rear Foot", "Dwee Bahl", "Kicks"],
    ["Front Foot Front Kick", "Ahp Bahl Ahp Chah-gee", "Kicks"],
    ["Rear Foot Front Kick", "Dwee Bahl Ahp Chah-gee", "Kicks"],
    ["Knee Strike", "Moo-reup Chee-gee", "Kicks"],
    ["Front Foot Side Kick", "Ahp Bahl Yup Cha-gee", "Kicks"],
    ["Rear Foot Side Kick", "Dwee Bahl Yup Cha-gee", "Kicks"],
    ["Front Foot Swing Kick", "Ahp Bahl Hoo-lyuh Cha-gee", "Kicks"],
    ["Rear Foot Swing Kick", "Dwee Bahl Hoo-lyuh Cha-gee", "Kicks"],
    ["Front Foot Reverse Swing Kick", "Ahp Bahl Bahn-deh Hoo-lyuh Cha-gee", "Kicks"],
    ["Rear Foot Reverse Swing Kick", "Dwee Bahl bahn-deh Hoo-lyuh Cha-gee", "Kicks"],
    ["Front Foot Heel Front Kick", "Ahp Bahl Dwee-goom-chee Ahp Cha-gee", "Kicks"],
    ["Rear Foot Heel Front Kick", "Dwee Bahl Dwee-goom-chee Ahp Cha-gee", "Kicks"],
    ["Front Foot Downward Kick", "Ahp Bahl Neh-ryuh Cha-gee", "Kicks"],
    ["Rear Foot Downward Kick", "Dwee Bahl Neh-ryuh Cha-gee", "Kicks"],
    ["Front Foot Crescent Kick", "Ahp Bahl Bahn-dahl Cha-gee", "Kicks"],
    ["Rear Foot Crescent Kick", "Dwee Bahl Bahn-dahl Cha-gee", "Kicks"],
    ["Front Foot Twisting Kick", "Ahp Bahl Bee-tuhl-uh Cha-gee", "Kicks"],
    ["Rear Foot Twisting Kick", "Dwee Bahl Bee-tuhl-uh Cha-gee", "Kicks"],

    ["White Belt Pattern", "Gyum-sohn Il Juhl", "Pattern"],
    ["White Belt Senior Pattern", "Gyum-sohn Il Jahng", "Pattern"],
    ["Yellow Belt Pattern", "Gyum-sohn Ee Juhl", "Pattern"],
    ["Yellow Belt Senior Pattern", "Gyum-sohn Ee Jahng", "Pattern"],
    ["Gold Belt Pattern", "Gyum-sohn Sahm Juhl", "Pattern"],
    ["Gold Belt Senior Pattern", "Gyum-sohn Sahm Jahng", "Pattern"],
    ["Orange Belt Pattern", "Gyum-sohn Sah Juhl", "Pattern"],
    ["Orange Belt Senior Pattern", "Gyum-sohn Sah Jahng", "Pattern"],
    ["Green Belt Pattern", "Gyum-sohn Oh Juhl", "Pattern"],
    ["Green Belt Senior Pattern", "Gyum-sohn Oh Jahng", "Pattern"],
    ["Blue Belt Pattern", "Gyum-sohn Yook Juhl", "Pattern"],
    ["Blue Belt Senior Pattern", "Gyum-sohn Yook Jahng", "Pattern"],
    ["Purple Belt Pattern", "Gyum-sohn Chil Juhl", "Pattern"],
    ["Purple Belt Senior Pattern", "Gyum-sohn Chil Jahng", "Pattern"],
    ["Red Belt Pattern", "Gyum-sohn Pahl Juhl", "Pattern"],
    ["Red Belt Senior Pattern", "Gyum-sohn Pahl Jahng", "Pattern"],
    ["Brown Belt Pattern", "Gyum-sohn Goo Juhl", "Pattern"],
    ["Brown Belt Senior Pattern", "Gyum-sohn Goo Jahng", "Pattern"],

    ["Humility", "Gyum-sohn", "Principles"],
    ["Honesty", "Jung-jik", "Principles"],
    ["Gentleness", "On-yu", "Principles"],
    ["Perseverance", "In-Nae", "Principles"],
    ["Self-Control", "Geuk-gee", "Principles"],
    ["Unbreakable Spirit", "Bool-gool", "Principles"],

    ["Punch", "Gee-reuh-gee", "Punches"],
    ["Fist", "Joo-muhk", "Punches"],
    ["Front Fist", "Ahp Joo-muhk", "Punches"],
    ["Rear Fist", "Dwee Joo-muhk", "Punches"],
    ["Side Fist", "Yuhp Joo-muhk", "Punches"],
    ["Back Fist", "Deung Joo-muhk", "Punches"],
    ["Knife Hand", "Sohn-kahl", "Punches"],
    ["Forward Dynamic Stance", "Ahp Dong-juhk Suh", "Punches"],
    ["Rear Dynamic Stance", "Dwee Dong-juhk Suh", "Punches"],
    ["Front Fist Inward Punch", "Ahp Joo-muhk Ahn-uh-ro Gee-reuh-gee", "Punches"],
    ["Rear Fist Inward Punch", "Dwee Joo-muhk Ahn-uh-ro Gee-reuh-gee", "Punches"],
    ["Front Fist Round Punch", "Ahp Joo-muhk Dol-lyuh Gee-reuh-gee", "Punches"],
    ["Rear Fist Round Punch", "Dwee Joo-muhk Dol-lyuh Gee-reuh-gee", "Punches"],
    ["Front Fist Upward Punch", "Ahp Joo-muhk Ohl-lyuh Gee-reuh-gee", "Punches"],
    ["Rear Fist Upward Punch", "Dwee Joo-muhk Ohl-lyuh Gee-reuh-gee", "Punches"],
    ["Front Inward Palm Strike", "Ahp Sohn-bah-dahk Ahn-un-ro Chee-gee", "Punches"],
    ["Rear Inward Palm Strike", "Dwee Sohn-bah-dahk Ahn-un-ro Chee-gee", "Punches"],
    ["Front Palm Diagonal Strike", "Ahp Sohn-bah-dahk Sah-suhn Chee-gee", "Punches"],
    ["Rear Palm Diagonal Strike", "Dwee Sohn-bah-dahk Sah-suhn Chee-gee", "Punches"],
    ["Front Round Elbow Strike", "Ahp Pahl-goop Dol-lyuh Chee-gee", "Punches"],
    ["Rear Round Elbow Strike", "Dwee Pahl-goop Dol-lyuh Chee-gee", "Punches"],
    ["Front Reverse Knife Hand Strike", "Ahp Sohn-kahl-dung Chee-gee", "Punches"],
    ["Rear Reverse Knife Hand Strike", "Dwee Sohn-kahl-dung Chee-gee", "Punches"],
    ["Front Claw Finger Strike", "Ahp Sohn-geut Chee-gee", "Punches"],
    ["Rear Claw Finger Strike", "Dwee Sohn-geut Chee-gee", "Punches"],

    ["Grade", "Guhp", "Rank"],
    ["Degree", "Dan", "Rank"],

    ["Certain Victory", "Pil Seung", "Terms"],
    ["House of Discipline", "Dojahng", "Terms"],
    ["Uniform", "Doh Bohk", "Terms"],
    ["Pattern", "Hyuhng", "Terms"],
    ["Self Defense", "Jah-gee Bahng-uh", "Terms"],
    ["Loud Yell", "Ki Hap", "Terms"]

];

var answer_input = document.querySelector("#answer");
var question_label = document.querySelector("#question");
var quiz_div = document.querySelector("#quiz");
var result_header = document.querySelector("#result");

function determine_vocabulary_word(){
    var number_chosen = false;
    var total_vocabulary_words = vocabulary_words.length;
    var vocabulary_word = [];

    // Don't run if all words have been used
    if (used_vocabulary_words.length === vocabulary_words.length){

        console.log("There are no words left to use.");
        return -1;

    }

    while (!number_chosen){

        // Pick random number based on length of vocabulary_words
        random_number = Math.floor(Math.random() * (total_vocabulary_words - 0)) + 0;

        // Only do if vocabulary word number has not been chosen
        if (!used_vocabulary_words.includes(random_number)){

            // Grab Vocabulary Word and Translation
            vocabulary_word.push(vocabulary_words[random_number][0]); // English
            vocabulary_word.push(vocabulary_words[random_number][1]); // Korean
            vocabulary_word.push(vocabulary_words[random_number][2]); // Category Hint

            // Add word to used_vocabulary_words
            used_vocabulary_words.push(random_number);

            return vocabulary_word;

        }
    }
}

function next_word(){

    console.log("Displaying next word")

    // Prepare for next word
    current_vocabulary_word = determine_vocabulary_word();

    // Hide elements that are needed
    result_header.style.display = "none";
    result_header.innerHTML = "";
    result_header.classList.remove("correct")
    result_header.classList.remove("incorrect")
    next_word_button.style.display = "none";

    // Show elements that are needed
    question_label.style.display = "block";
    answer_input.style.display = "block";
    check_button.style.display = "block";

    // Set text for new word
    question_header.innerHTML = "Vocabulary word " + (questions_asked + 1) + " of 10.";
    question_label.innerHTML = "What is the meaning of <em>" + current_vocabulary_word[1] + "</em>?";
    answer_input.value = "";
    console.log("Vocabulary presented: " + current_vocabulary_word[1]);

}

function try_again(hint){

    console.log("Trying " + current_vocabulary_word[1] + " again");

    // Hide elements that are not needed
    result_header.style.display = "none";
    result_header.innerHTML = ""
    result_header.classList.remove("incorrect")
    try_again_button.style.display = "none";
    need_hint_button.style.display = "none";
    pass_button.style.display = "none";

    // Show elements that are needed
    question_label.style.display = "block";
    answer_input.style.display = "block";
    check_button.style.display = "block";

    if (hint){

        console.log("Getting a hint")
        question_label.innerHTML = "What is the meaning of <em>" + current_vocabulary_word[1] + "</em>? (Hint: <strong>" + current_vocabulary_word[2] + "</strong>)";

    }

    // Clear input box
    answer_input.value = ""

}

answer_input.addEventListener("keyup", function(event){

    event.preventDefault();
    if (event.keyCode === 13) {

        check_button.click()

    }

})

check_button.addEventListener("click", function(){

    answer = document.querySelector("input").value;

    if (answer.toLowerCase() == current_vocabulary_word[0].toLowerCase()){

        console.log("Answer was correct")

        questions_asked++;

        // Hide elements that are not needed
        question_label.style.display = "none";
        answer_input.style.display = "none";
        check_button.style.display = "none";

        // Show elements that are needed
        if (questions_asked < 10) {

            result_header.style.display = "block";
            result_header.innerHTML = "Correct! <em>" + current_vocabulary_word[1] + "</em> means " + current_vocabulary_word[0] + "."
            result_header.className += " correct"
            next_word_button.style.display = "block";

        } else {

            result_header.style.display = "block";
            result_header.innerHTML = "Correct! <em>" + current_vocabulary_word[1] + "</em> means " + current_vocabulary_word[0] + ". <br> Would you like to try some more words?"
            result_header.className += " correct"
            start_again_button.style.display = "block";

        }

    } else {

        console.log("Answer was incorrect")

        // Hide elements that are not needed
        question_label.style.display = "none";
        answer_input.style.display = "none";
        check_button.style.display = "none";

        // Show elements that are needed
        result_header.style.display = "block";
        result_header.innerHTML = "That was not correct. Try again?"
        result_header.className += " incorrect"
        try_again_button.style.display = "inline";
        need_hint_button.style.display = "inline";
        pass_button.style.display = "inline";
    }

})

need_hint_button.addEventListener("click", function(){

    try_again(true);

})

next_word_button.addEventListener("click", function(){

    next_word();

})

start_button.addEventListener("click", function(){

    current_vocabulary_word = determine_vocabulary_word();

    start_button.style.display = "none";
    console.log("Game has begun");

    question_header.innerHTML = "Vocabulary question " + (questions_asked + 1) + " of 10.";
    question_label.innerHTML = "What is the meaning of <em>" + current_vocabulary_word[1] + "</em>?";
    quiz_div.style.visibility = "visible";
    console.log("Vocabulary presented: " + current_vocabulary_word[1]);

})

start_again_button.addEventListener("click", function(){

    // Reset game variables
    questions_asked = 0;
    used_vocabulary_words = [];
    result_header.style.display = "none";
    result_header.innerHTML = "";
    start_again_button.style.display = "none";

    console.log("Game has begun again");
    next_word();

})

try_again_button.addEventListener("click", function(){

    try_again(false);

})

pass_button.addEventListener("click", function(){

    try_again_button.style.display = "none";
    need_hint_button.style.display = "none";
    pass_button.style.display = "none";
    next_word();

})