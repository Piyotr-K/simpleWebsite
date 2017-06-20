/*
 * My test script
 */

function myfunc() {
  var doc = document
  var container = doc.getElementsByClassName("container")[0]
  var newP = doc.createElement("p")
  container.appendChild(newP)
  newP.innerHTML = "Die"
}

myfunc()
