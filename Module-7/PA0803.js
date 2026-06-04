var Balance = 100;
var latestBalance;
var latestTrans;
var debited = 150;

function deposit(debited) {
  Balance += debited;
  latestTrans = debited;
  console.log("Balance after deposit: R " + Balance + ".00");
}

function statement(totalAmt) {
  console.log("Total available balance is: R " + Balance + ".00");
  console.log("Latest Transaction is: R " + latestTrans + ".00");
}

