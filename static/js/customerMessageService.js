async function sendCustomers() {
  
}

async function getExampleCustomersMessages() {
  const resultParagraph = document.getElementById("resultParagraph");

  resultParagraph.innerHTML = "Carregando...";

  try {
    const response = await fetch('/get_clients');
    const data = await response.text();

    resultParagraph.innerHTML = data;
  } catch (e) {
    resultParagraph.innerHTML = "Erro ao carregar mensagem dos clientes";
    console.log(e);
  }
}

function clearResult() {
  const resultParagraph = document.getElementById("resultParagraph");
  resultParagraph.innerHTML = "";
}
