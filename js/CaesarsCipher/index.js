function rot13(str) {
    return str.replace(/[A-Z]/g, (char) => {
    const code = char.charCodeAt(0);
    if (code >= 65 && code <= 77) {
      // Shift letters A-M by 13 positions
      return String.fromCharCode(code + 13);
    } else if (code >= 78 && code <= 90) {
      // Shift letters N-Z by 13 positions
      return String.fromCharCode(code - 13);
    }
    return char;
    });
}
 
console.log(rot13("SERR PBQR PNZC"));