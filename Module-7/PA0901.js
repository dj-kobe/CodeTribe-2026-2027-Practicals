//Marks checker
//pass or fail system

var marks = 48;

function checkMarks(marks) {
  if (marks >= 50) {
    console.log("Congratulations! You have passed.");
  } else {
    console.log("Sorry, you have failed. Please try again.");
  }

  function checkMarks(marks) {
    if (marks >= 50) {
      console.log("Your grade is 7.");
    } else if (marks >= 70) {
      console.log("Your grade is 6.");
    } else if (marks >= 60) {
      console.log("Your grade is 5.");
    } else if (marks >= 50) {
      console.log("Your grade is 4.");
    } else {
      console.log("Your grade is F.");
    }
  }
}

checkMarks();
