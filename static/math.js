start = document.getElementsByClassName("start")
add = document.getElementsByClassName("add")

modal = document.getElementsByClassName("modal")
start[0].addEventListener('click',() => {
    console.log("clicked start")
    start[0].style.visibility = "hidden"
    add[0].style.visibility = "hidden"
    modal[0].style.visibility = "visible"

})


