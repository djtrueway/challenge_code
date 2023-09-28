function checkCashRegister(price, cash, cid) {
    // Define the currency units and their values in cents
    const currencyUnits = {
      "PENNY": 1,
      "NICKEL": 5,
      "DIME": 10,
      "QUARTER": 25,
      "ONE": 100,
      "FIVE": 500,
      "TEN": 1000,
      "TWENTY": 2000,
      "ONE HUNDRED": 10000
    };
  
    let changeDue = Math.round((cash - price) * 100); // Convert to cents
    const totalCID = cid.reduce((acc, item) => acc + Math.round(item[1] * 100), 0); // Convert to cents
  
    if (totalCID === changeDue) {
      return { status: "CLOSED", change: cid };
    }
  
    const change = [];
    for (let i = cid.length - 1; i >= 0; i--) {
      const [unitName, availableAmount] = cid[i];
      const unitValue = currencyUnits[unitName];
      const availableCents = Math.round(availableAmount * 100); // Convert to cents
  
      const unitCount = Math.floor(availableCents / unitValue);
      const maxToReturn = Math.floor(changeDue / unitValue);
      const toReturn = Math.min(unitCount, maxToReturn);
  
      if (toReturn > 0) {
        const returnedCents = toReturn * unitValue;
        change.push([unitName, returnedCents / 100]); // Convert back to dollars
        changeDue -= returnedCents;
      }
    }
  
    if (changeDue === 0) {
      if (totalCID === change.reduce((acc, item) => acc + Math.round(item[1] * 100), 0)) { // Convert to cents
        return { status: "CLOSED", change: cid };
      }
  
      return { status: "OPEN", change: change };
    } else {
      return { status: "INSUFFICIENT_FUNDS", change: [] };
    }
}
  
const check = checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);

console.log(check);