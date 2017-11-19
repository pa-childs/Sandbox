var game_started = false;
var questions_asked = 0;
var start_button = document.querySelector("#start_button");
var question_div = document.querySelector("#question");

start_button.addEventListener("click", function(){

    game_started = true;
    start_button.style.visibility = 'hidden';
    question_div.style.visibility = 'visible';

    console.log("Game has started: " + game_started);

})