document.getElementById("riskForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value,
    average_score: parseFloat(document.getElementById("score").value),
    attendance_rate: parseFloat(document.getElementById("attendance").value),
    behavior_score: parseFloat(document.getElementById("behavior").value)
  };

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(result => {
      if (result.status === "success") {
        document.getElementById("result").innerText = 
          `${result.student_name} is ` + 
          (result.risk === 1 ? "AT RISK." : "NOT at risk.");
      } else {
        document.getElementById("result").innerText = 
          "Error: " + result.message;
      }
    })
    .catch(error => {
      document.getElementById("result").innerText = 
        "Request failed: " + error;
    });
});
