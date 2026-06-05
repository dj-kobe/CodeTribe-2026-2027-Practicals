//calculate a banking fee for each transaction 

  var feeAmount = 0.02;
    var latestTrans = 8000;
    var totalfee = feeAmount * latestTrans;
function calculatefee(){
if (latestTrans < 5000) {
   console.log("The fee for this transaction is : R 0.00");
}else if (latestTrans >= 5000) {
    console.log("The fee for this transaction is : R 10.00");
}
}

calculatefee(8000 + totalfee);