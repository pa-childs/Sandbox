var game_started = false;
var questions_asked = 0;
var vocabulary_words = [
    ["Loud Yell", "Ki Hap"],
    ["Front", "Ahp"],
    ["Rear", "Bahl"],
    ["Side", "Yuhp"],
    ["Right", "Woo"],
    ["Left", "Jwah"],
    ["Reverse", "Bahn-deh"],
    ["Inner", "Ahn Uh-roh"],
    ["Outer", "Bahk Un-roh"],
    ["About Turn", "Dwee-roh Do-rah"]
];
var used_vocabulary_words = [];
var current_vocabulary_word;

var start_button = document.querySelector("#start_button");
var check_button = document.querySelector("#check_button");
var next_button = document.querySelector("#next_button");
var quiz_div = document.querySelector("#quiz");
var question_header = document.querySelector("#question_header");
var question_label = document.querySelector("#question");
var answer_input = document.querySelector("#answer");
var result_header = document.querySelector("#result");


function random_test(min, max){
    random_number = Math.floor(Math.random() * (max - min)) + min;
    console.log("random_number: " + random_number);
}

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

            // Add word to used_vocabulary_words
            used_vocabulary_words.push(random_number);

            number_chosen = true;
            return vocabulary_word;

        }
    }
}

start_button.addEventListener("click", function(){

    current_vocabulary_word = determine_vocabulary_word();

    game_started = true;
    start_button.style.display = "none";
    console.log("Game has started: " + game_started);

    question_header.innerHTML = "Vocabulary question " + (questions_asked + 1) + " of 10.";
    question_label.innerHTML = "What is the meaning of " + current_vocabulary_word[1] + "?";
    quiz_div.style.visibility = "visible";
    console.log("Vocabulary presented: " + current_vocabulary_word[1]);

})

check_button.addEventListener("click", function(){

    answer = document.querySelector("input").value;

    if (answer.toLowerCase() == current_vocabulary_word[0].toLowerCase()){

        console.log("Answer was correct")

        // Hide elements that are not needed
        question_label.style.display = "none";
        answer_input.style.display = "none";
        check_button.style.display = "none";

        // Show elements that are needed
        result_header.style.display = "block";
        result_header.innerHTML = "Correct! " + current_vocabulary_word[1] + " means " + current_vocabulary_word[0] + "."
        next_button.style.display = "block";
        questions_asked++;

    } else {

        console.log("Answer was incorrect")

        // Hide elements that are not needed
        question_label.style.display = "none";
        answer_input.style.display = "none";
        check_button.style.display = "none";

        // Show elements that are needed
        result_header.style.display = "block";
        result_header.innerHTML = "That was not correct. Try again?"
        try_again_button.style.display = "inline";
        pass_button.style.display = "inline";
    }

})