const btn = document.getElementById("optimizeBtn");
const resultDiv = document.getElementById("result");

btn.addEventListener("click", () => {
  resultDiv.innerText = "Testing connection...";

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    let url = tabs[0].url || "";
    let domain = "unknown";

    try {
      domain = new URL(url).hostname;
    } catch (e) {}

    fetch("http://127.0.0.1:4545/optimize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ domain: domain })
    })
      .then(res => res.json())
      .then(data => {
        if (data.status === "ok") {
          resultDiv.innerHTML =
            "Domain: " + data.domain + "<br>" +
            "DNS: " + data.dns + "<br>" +
            "Ping: " + data.ping + " ms";
        } else {
          resultDiv.innerText = "Connection error";
        }
      })
      .catch(() => {
        resultDiv.innerText = "Mordad Connect app is not running";
      });
  });
});
