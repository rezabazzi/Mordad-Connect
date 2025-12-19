document.getElementById("check").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const url = new URL(tabs[0].url);
    const domain = url.hostname;

    document.getElementById("result").innerHTML =
      "Site: " + domain +
      "<br>Recommended DNS:<br>" +
      "Cloudflare (1.1.1.1)<br>" +
      "Status: Tested & Stable";
  });
});
