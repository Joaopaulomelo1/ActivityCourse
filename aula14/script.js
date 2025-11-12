const button = document.getElementById('fetchButton');
const resultsContainer = document.getElementById('results');

button.addEventListener('click', async () => {
  resultsContainer.innerHTML = '';

  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!response.ok) {
      throw new Error('API não está respondendo corretamente');
    }

    const data = await response.json();

    data.forEach(user => {
      const userDiv = document.createElement('div');
      userDiv.classList.add('result-item');
      userDiv.innerHTML = `
        <strong>Nome:</strong> ${user.name} <br>
        <strong>Email:</strong> ${user.email} <br>
        <strong>Empresa:</strong> ${user.company.name}
      `;
      resultsContainer.appendChild(userDiv);
    });

  } catch (error) {
    const errorDiv = document.createElement('div');
    errorDiv.classList.add('error');
    errorDiv.textContent = 'Erro ao buscar os dados: ' + error.message;
    resultsContainer.appendChild(errorDiv);
  }
});
