let lista = [];

while (true) {
  let opcao = prompt(
    "Escolha uma opção:\n1 - Adicionar item\n2 - Remover item\n3 - Exibir lista\n4 - Atualizar item\n5 - Sair"
  );

  if (opcao === "1") {
    let item = prompt("Digite o item que deseja adicionar:");
    lista.push(item);
    alert(`"${item}" foi adicionado à lista.`);
  } 
  else if (opcao === "2") {
    let indice = prompt("Digite o índice do item que deseja remover:");
    indice = Number(indice);
    if (indice >= 0 && indice < lista.length) {
      let removido = lista.splice(indice, 1);
      alert(`"${removido}" foi removido da lista.`);
    } else {
      alert("Índice inválido.");
    }
  } 
  else if (opcao === "3") {
    let resultado = "Lista de Compras:\n";
    let i = 0;
    for (let item of lista) {
      resultado += `${i}: ${item}\n`;
      i++;
    }
    alert(resultado);
  } 
  else if (opcao === "4") {
    let indice = prompt("Digite o índice do item que deseja atualizar:");
    indice = Number(indice);
    if (indice >= 0 && indice < lista.length) {
      let novoValor = prompt("Digite o novo valor para o item:");
      lista[indice] = novoValor;
      alert("Item atualizado com sucesso!");
    } else {
      alert("Índice inválido.");
    }
  } 
  else if (opcao === "5") {
    alert("Encerrando o programa...");
    break;
  } 
  else {
    alert("Opção inválida.");
  }
}
