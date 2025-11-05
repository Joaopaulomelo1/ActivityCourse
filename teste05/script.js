let tarefas = [];
let opcao = "";

while (opcao !== "5") {
  opcao = prompt(
    "O que deseja fazer?\n" +
      "1 - Adicionar tarefa\n" +
      "2 - Listar tarefas\n" +
      "3 - Remover tarefa\n" +
      "4 - Concluir tarefa\n" +
      "5 - Sair"
  );

  switch (opcao) {
    case "1":
      let novaTarefa = prompt("Digite o nome da tarefa:");
      if (novaTarefa) {
        tarefas.push(novaTarefa);
        alert(`Tarefa adicionada: ${novaTarefa}`);
      } else {
        alert("Nenhuma tarefa adicionada!");
      }
      break;

    case "2":
      if (tarefas.length === 0) {
        alert("Nenhuma tarefa na lista.");
      } else {
        let lista = "📋 Lista de Tarefas:\n";
        for (let i = 0; i < tarefas.length; i++) {
          lista += `${i} - ${tarefas[i]}\n`;
        }
        alert(lista);
      }
      break;

    case "3":
      if (tarefas.length === 0) {
        alert("Não há tarefas para remover.");
      } else {
        let indiceRemover = parseInt(
          prompt("Digite o índice da tarefa que deseja remover:")
        );
        if (
          !isNaN(indiceRemover) &&
          indiceRemover >= 0 &&
          indiceRemover < tarefas.length
        ) {
          let removida = tarefas.splice(indiceRemover, 1);
          alert(`Tarefa removida: ${removida}`);
        } else {
          alert("Índice inválido!");
        }
      }
      break;

    case "4":
      if (tarefas.length === 0) {
        alert("Não há tarefas para concluir.");
      } else {
        let indiceConcluir = parseInt(
          prompt("Digite o índice da tarefa concluída:")
        );
        if (
          !isNaN(indiceConcluir) &&
          indiceConcluir >= 0 &&
          indiceConcluir < tarefas.length
        ) {
          tarefas[indiceConcluir] = "✅ " + tarefas[indiceConcluir];
          alert("Tarefa marcada como concluída!");
        } else {
          alert("Índice inválido!");
        }
      }
      break;

    case "5":
      alert("Saindo do programa...");
      break;

    default:
      alert("Opção inválida! Escolha entre 1 e 5.");
  }
}
