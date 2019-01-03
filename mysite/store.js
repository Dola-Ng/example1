// Get the elements with class="column"
var elements = document.getElementsByClassName("column");
var header = document.getElementById("myHeader");
var btns = header.getElementsByClassName("btn");
var btnone = document.getElementById("one");
var btntwo = document.getElementById("two");
var btnfour = document.getElementById("four");
var i;

btnone.addEventListener("click", ones);
btntwo.addEventListener("click", twos);
btnfour.addEventListener("click", fours);

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}


// Full-width images
function ones() {
    for (i = 0; i < elements.length; i++) {
    elements[i].style.msFlex = "100%";  // IE10
    elements[i].style.flex = "100%";
  }
}

// Two images side by side
function twos() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.msFlex = "50%";  // IE10
    elements[i].style.flex = "50%";
  }
}

// Four images side by side
function fours() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.msFlex = "25%";  // IE10
    elements[i].style.flex = "25%";
  }
}


