document.getElementById("riskForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const data = {
    average_score: parseFloat(document.getElementById("score").value),
    attendance_rate: parseFloat(document.getElementById("attendance").value),
    behavior_score: parseFloat(document.getElementById("behavior").value)
  };

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText =
      data.risk === 1 ? "Student is AT RISK" : "Student is NOT at risk";
  });
});
