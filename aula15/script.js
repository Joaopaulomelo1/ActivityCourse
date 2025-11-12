const loadButton = document.getElementById('loadButton');
const userList = document.getElementById('userList');
const errorMessage = document.getElementById('errorMessage');

loadButton.addEventListener('click', async () => {
  userList.innerHTML = '';
  errorMessage.textContent = '';

  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!response.ok) {
      throw new Error('Erro na requisição');
    }

    const users = await response.json();

    users.forEach(user => {
      const li = document.createElement('li');
      li.textContent = `${user.name} - ${user.email}`;
      userList.appendChild(li);
    });

  } catch (error) {
    errorMessage.textContent = 'Erro ao carregar os usuários, tente novamente mais tarde.';
  }
});
