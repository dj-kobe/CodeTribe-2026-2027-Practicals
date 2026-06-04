//calculate a banking fee for each transaction 

function caluculatefee(){
    var fee = 0.05;
    var latestTrans = 8000;
    var totalfee = fee * latestTrans;
    console.log("The fee for this transaction is : R " + totalfee + ".00");
}

caluculatefee(8000)