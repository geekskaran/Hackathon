const signupBtn = document.getElementById("signup-btn");
const closeBtn = document.getElementById("close-btn");
const signupModal = document.getElementById("signup-modal");
const signupForm = document.querySelector("#signup-modal form");

signupBtn.addEventListener("click", function() {
  signupModal.classList.add("show");
});

closeBtn.addEventListener("click", function() {
  signupModal.classList.remove("show");
});

window.addEventListener("click", function(event) {
  if (event.target == signupModal) {
    signupModal.classList.remove("show");
  }
});

signupForm.addEventListener("submit", function(event) {
  event.preventDefault();
  // add code here to submit the form data to the server
});
