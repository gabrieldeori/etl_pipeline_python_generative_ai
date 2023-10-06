async function getExampleCustomersMessages() {
  const resultParagraph = document.getElementById("resultParagraph");
  try {
    const response = await fetch('/run_script');
    const data = await response.text();

    resultParagraph.innerHTML = data;
  } catch (e) {
    console.log(e);
  }
}

function clearResult() {
  const resultParagraph = document.getElementById("resultParagraph");
  resultParagraph.innerHTML = "";
}
