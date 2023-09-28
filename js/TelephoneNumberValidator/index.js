function telephoneCheck(str) {
    // Regular expression for valid US phone numbers
    const phoneRegex = /^(1\s?)?(\(\d{3}\)|\d{3})([\s\-]?)\d{3}([\s\-]?)\d{4}$/;
  
    return phoneRegex.test(str);
}
  
const check = telephoneCheck("555-555-5555");
console.log(check);