//pass balance and latest transaction to statement function to print the statement
function withdrawal(debited) {
  if (debited > Balance) {
    console.log(
      "user not allowed to withdraw this amount. Please enter lower amount",
    );
  } else {
    Balance -= debited;
    latestTrans = debited;
    console.log("Balance after withdrawal: R", +Balance + ".00");
  }
}

function statement(totalAmt) {
  console.log("Total available balance is: R " + Balance + ".00");
  console.log("Latest Transaction is: R " + latestTrans + ".00");
}
