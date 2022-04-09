console.log("javascript is connected");

let buttonClick = document.querySelector("#buttonClick");

if (buttonClick) {
	buttonClick.addEventListener("click", function () {
		console.log("button clicked");
	});
}

//display message to none after 3 seconds
let message = document.querySelector(".messages");
if (message) {
	console.log("message is connected");
	setTimeout(function () {
		message.style.display = "none";
	}, 3000);
}
