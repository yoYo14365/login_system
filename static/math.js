start = document.getElementsByClassName("start")
add = document.getElementsByClassName("add")

modal_start = document.getElementsByClassName("modal_start")
modal_add = document.getElementsByClassName("modal_add")
question = document.getElementsByClassName("question")[0]
answer = document.getElementsByClassName("answer-input")[0].textContent
submit_answer = document.getElementsByClassName("submit-answer")[0]

start[0].addEventListener('click',() => {
    getQuestion()
    console.log("clicked start")
    start[0].style.visibility = "hidden"
    add[0].style.visibility = "hidden"
    modal_start[0].style.visibility = "visible"

})
add[0].addEventListener('click',() => {
    console.log("clicked add")
    start[0].style.visibility = "hidden"
    add[0].style.visibility = "hidden"
    modal_add[0].style.visibility = "visible"
    
})
submit_answer.addEventListener('click', () => {
    console.log("clicked submit answer")
    $.ajax({
        url: 'math',
        method: 'POST',
        contentType: "application/json",
        data: JSON.stringify({
            command: "submit_answer",
            answer: answer
        }),
        success: (response) => {
            console.log("Answer submitted successfully:", response);
        },
        error: (error) => {
            console.error("Error submitting answer:", error);
        }
    });
})

add_Submit = document.getElementsByClassName("submit-question")
add_Submit[0].addEventListener('click', () => {
    console.log("clicked submit question")

    $.ajax({
        url: 'math',
        method: 'POST',
        contentType: "application/json",
        data: JSON.stringify({
            command: "add_question",
            question: document.getElementsByClassName("question-input")[0].value,
            answer: document.getElementsByClassName("answer-input")[0].value,
            difficulty: document.getElementsByClassName("difficulty-select")[0].value
        }),
        success: (response) => {
            console.log("Question added successfully:", response);
        },
        error: (error) => {
            console.error("Error adding question:", error);
        }
    });
})
getQuestion = () => {
    $.ajax({
        url: 'math',
        method: 'POST',
        contentType: "application/json",
        data: JSON.stringify({
            command: "get_question"
        }),
        success: (response) => {
            console.log("Question retrieved successfully:", response);
            question.innerText = response.question;

        },
        error: (error) => {
            console.error("Error retrieving question:", error);
        }
    });
}