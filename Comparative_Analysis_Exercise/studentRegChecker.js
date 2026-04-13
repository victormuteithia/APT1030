// Student Registration Status Checker in JS

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Enter student name: ", (studentName) => {
    readline.question("Enter number of registered units: ", (unitsInput) => {
        const units = unitsInput;
        
        // Determine registration status
        const status = units > 7 ? "Overload - Approval Required" : "Registration Accepted";
        
        // Print final summary
        console.log("\n========== REGISTRATION SUMMARY ==========");
        console.log(`Student Name: ${studentName}`);
        console.log(`Registered Units: ${units}`);
        console.log(`Status: ${status}`);
        console.log("==========================================\n");
        
        readline.close();
    });
});