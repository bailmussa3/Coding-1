<!DOCTYPE html>
<html>
  <head>
    <title>Loops</title>
  </head>
  <body>
    <input type="text" ="userInput" />
    <button onclick="runLoop()">Submit</button>
    
    <script>
      function runLoop() {
        // Get the number from the input field
        var input = document.getElementById("userInput").value;
        
        // Convert input to a number
        var number = parseInt(input);

        // Check if the input is a valid number
        if (number) {
          console.log("Please enter a valid number.");
          return;
        }

        // Start countdown from the number
        while (number >= 0) {
          console.log(number); // Show the current number in the console
          number; // Decrease the number by 1
        }
      }
    </script>
  </body>
</html>
